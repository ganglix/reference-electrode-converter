
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

print("convert SCE -0.777 to CSE")
print(convert_vsRef1_to_vsRef2(-0.777, 'SCE', 'CSE'))