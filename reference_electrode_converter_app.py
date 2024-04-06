import streamlit as st
import matplotlib.pyplot as plt


def ref_temp_corrected(pot, thermal_coeff, T):
    """
    potential+ thermal temp coeff * (T-25): 
    """
    return pot + thermal_coeff * (T-25)
    
# end def
def convert_to_vsSHE(pot_vsRef, ref, T):
    # convert to SHE @ 25 degC
    pot_vsSHE = pot_vsRef + ref_temp_corrected(*REF_POT_SHE[ref], T)
    return pot_vsSHE

def convert_to_vsRef(pot_vsSHE, ref, T):
    # convert from SHE @ 25 degC
    pot_vsRef = pot_vsSHE - ref_temp_corrected(*REF_POT_SHE[ref], T)
    return pot_vsRef

def convert_vsRef1_to_vsRef2(pot_vsRef1, ref1, ref2, T1, T2):
    pot_vsSHE = convert_to_vsSHE(pot_vsRef1, ref1, T1)
    pot_vsRef2 = convert_to_vsRef(pot_vsSHE, ref2, T2)
    return pot_vsRef2

def plot_reference_electrodes(pot_vsRef2, ref2, T2):
    categories = list(REF_POT_SHE.keys())
    offsets = [v[0] for v in REF_POT_SHE.values()]  # all 25 degC

    x_positions = range(len(categories))
    category_x_dict = {cat: x_pos for cat, x_pos in zip(categories, x_positions)}
    
    # update offset for ref2 at T2
    offsets[category_x_dict[ref2]] = ref_temp_corrected(*REF_POT_SHE[ref2], T2)

    fig, ax = plt.subplots(figsize=(5, 6))

    for x, offset in zip(x_positions, offsets):
        ax.plot([x, x, x], [-1 + offset, 0 + offset, 1 + offset], 'k',marker='+', alpha = (categories[x]==ref2)*0.8+0.2)
        # Annotate the offset next to each line
        ax.text(x, offset-0.03, f'  0 vs. {categories[x]}', horizontalalignment='left')
    
    # Plot a horizontal line to represent the converted potential
    pot_vsSHE = convert_to_vsSHE(pot_vsRef2, ref2, T2)
    ax.plot([x_positions[0], x_positions[-1]], [pot_vsSHE, pot_vsSHE], 'r--', linewidth=0.5)
    # add arrow
    # Plot a red arrowed line from start_point to end_point
    end_point = (category_x_dict[ref2]+0.05, pot_vsSHE)
    start_point = (category_x_dict[ref2]+0.05, offsets[category_x_dict[ref2]])
    ax.annotate("", xy= end_point, xycoords='data',
            xytext= start_point, textcoords='data',
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="red"))

    ax.text(category_x_dict[ref2], pot_vsSHE, f'  {pot_vsRef2:.3f} vs. {ref2}', horizontalalignment='left', color='r')

    ax.set_xticks(x_positions)
    xticks_list = [c + '\n25°C' for c in categories]
    xticks_list[category_x_dict[ref2]] = xticks_list[category_x_dict[ref2]].split('\n')[0] + f'\n{T2}°C'
    ax.set_xticklabels(xticks_list)
    ax.set_ylabel("V vs. SHE at 25°C")

    # Turn off the top, right, and bottom spines (borders)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    ax.spines['left'].set_visible(True)

    # To further clean up the plot, you can turn off x-axis ticks as well
    ax.tick_params(axis='x', which='both', bottom=False, top=False)
    return fig

# Streamlit app starts here
st.title('Electrode Potential Converter')
st.write('This app allows you to convert potential readings from one reference electrode to another. Simply select the reference electrodes and enter the potential to convert.')


# dictionary and functions

thermal_handling= st.radio(
    "Select Temperature Dependence",
    ["Thermal", "Isothermal"],
    captions=["Referenced to Standard Hydrogen Electrode (SHE) at 25 °C [Default]",
                "Referenced to SHE at the operation temperature of the other electrode"])

if thermal_handling == "Thermal":
    REF_POT_SHE = {
    #name: (potential vs SHE, Thermal temperature coefficient V/degC)
    "SHE": (0.000, 0.87e-3),
    "SCE": (0.241, 0.22e-3),
    "CSE": (0.314, 0.9e-3),
    "Ag/AgCl (sat'd KCl)": (0.196, 0) # Thermal temperature coefficient not available
    }

else:
    DIFF = 0.87e-3 #V/degC
    REF_POT_SHE = {
    #name: (potential vs SHE, Thermal temperature coefficient V/degC)
    "SHE": (0.000, 0.87e-3 - DIFF),
    "SCE": (0.241, 0.22e-3 - DIFF),
    "CSE": (0.314, 0.9e-3 - DIFF),
    "Ag/AgCl (sat'd KCl)": (0.196, 0) # Thermal temperature coefficient not available
}



# Use Streamlit's columns function to create two columns
col1, col2 = st.columns(2)

# First column for selecting the original reference electrode and entering the potential
with col1:
    ref1 = st.selectbox('Select the original reference electrode:', list(REF_POT_SHE.keys()), index=0, key='original_ref')
    T1 = st.number_input('Operating at T1 [°C]:', value=25.0, step=1.0, format="%.1f")
    pot_vsRef1 = st.number_input('Enter the potential vs. the original reference electrode (in volts):', format="%.3f")

# Second column for selecting the target reference electrode
with col2:
    ref2 = st.selectbox('Select the target reference electrode:', list(REF_POT_SHE.keys()), key='ref2')
    if ref2 == "Ag/AgCl (sat'd KCl)":
        T2 = 25.0
        st.write(f'Temperature input is disabled due to lack of literature data. T2 is set at 25 [°C]')
    else:
        T2 = st.number_input('Operating at T2 [°C]:', value=25.0, step=1.0, format="%.1f")
    result_container = st.container(border=True)
    result_container.write(f'The converted potential vs. {ref2} is:')


# Button for performing the conversion
# Placed outside columns so it spans the entire width

display_plot = st.checkbox('Display the potential scales', value=True)

if st.button('Convert Potential'):
    result = convert_vsRef1_to_vsRef2(pot_vsRef1, ref1, ref2, T1, T2)
    result_container.write(f'{result:.3f} V')

    if display_plot:
        # display the plot
        fig = plot_reference_electrodes(result, ref2, T2)
        st.pyplot(fig)


# Divider
st.markdown("---")

with st.expander("Notes"):
    # Display REF_POT_SHE information below the columns
    st.write('Note: Reference Electrode Potentials vs. SHE')
    for ref, pot in REF_POT_SHE.items():
        st.write(f"{ref}: {pot} V")
