import streamlit as st
import matplotlib.pyplot as plt

# dictionary and functions
REF_POT_SHE = {
    "SHE": 0.000, 
    "SCE": 0.241,
    "CSE": 0.314,
    "Ag/AgCl (saturated KCl)": 0.197,
}

def convert_to_vsSHE(pot_vsRef, ref):
    pot_vsSHE = pot_vsRef + REF_POT_SHE[ref]
    return pot_vsSHE

def convert_to_vsRef(pot_vsSHE, ref):
    pot_vsRef = pot_vsSHE - REF_POT_SHE[ref]
    return pot_vsRef

def convert_vsRef1_to_vsRef2(pot_vsRef1, ref1, ref2):
    pot_vsSHE = convert_to_vsSHE(pot_vsRef1, ref1)
    pot_vsRef2 = convert_to_vsRef(pot_vsSHE, ref2)
    return pot_vsRef2

def plot_reference_electrodes(pot_vsRef2, ref2):
    categories = list(REF_POT_SHE.keys())
    offsets = list(REF_POT_SHE.values())

    fig, ax = plt.subplots(figsize=(5, 6))
    x_positions = range(len(categories))

    for x, offset in zip(x_positions, offsets):
        ax.plot([x, x, x], [-1 + offset, 0 + offset, 1 + offset], 'k',marker='+', alpha = (categories[x]==ref2)*0.8+0.2)
        # Annotate the offset next to each line
        ax.text(x, offset, f'  0 vs. {categories[x]}', horizontalalignment='left')
    
    # Plot a horizontal line to represent the converted potential
    converted_potential = convert_to_vsSHE(pot_vsRef2, ref2)
    ax.plot([x_positions[0], x_positions[-1]], [converted_potential, converted_potential], 'r--', linewidth=1)

    ax.set_xticks(x_positions)
    ax.set_xticklabels(categories)
    ax.set_ylabel("V vs. SHE")
    # Turn off the top, right, and bottom spines (borders)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    ax.spines['left'].set_visible(True)

    # To further clean up the plot, you can turn off x-axis ticks as well
    ax.tick_params(axis='x', which='both', bottom=False, top=False)


    return fig

# Streamlit app starts here
st.title('Electrode Potential Converter at 25°C')
st.write('This app allows you to convert potential readings from one reference electrode to another. Simply select the reference electrodes and enter the potential to convert.')

# Use Streamlit's columns function to create two columns
col1, col2 = st.columns(2)

# First column for selecting the original reference electrode and entering the potential
with col1:
    ref1 = st.selectbox('Select the original reference electrode:', list(REF_POT_SHE.keys()), index=0, key='original_ref')
    # Create a sub-column layout within col1 to place the input field and the unit label ("V")
    pot_vsRef1 = st.number_input('Enter the potential vs. the original reference electrode (in volts):', format="%.3f")

# Second column for selecting the target reference electrode
with col2:
    ref2 = st.selectbox('Select the target reference electrode:', list(REF_POT_SHE.keys()), key='ref2')
    result_container = st.container(border=True)
    result_container.write(f'The converted potential vs. {ref2} is:')


# Button for performing the conversion
# Placed outside columns so it spans the entire width

if st.button('Convert Potential'):
    result = convert_vsRef1_to_vsRef2(pot_vsRef1, ref1, ref2)
    # Store the result in session state
    st.session_state['result'] = result
    # Update the result in the second column
    result_container.write(f'{result:.3f} V')


    # display the plot
    fig = plot_reference_electrodes(result, ref2)
    st.pyplot(fig)



# Divider
st.markdown("---")

# Display REF_POT_SHE information below the columns
st.write('Note: Reference Electrode Potentials vs. SHE')
for ref, pot in REF_POT_SHE.items():
    st.write(f"{ref}: {pot} V")
