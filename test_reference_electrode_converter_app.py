import unittest
from reference_electrode_converter_app import convert_vsRef1_to_vsRef2, REF_POT_SHE

class TestElectrodePotentials(unittest.TestCase):

    def test_convert_SCE_to_CSE(self):
        """Test conversion from SCE to CSE."""
        result = convert_vsRef1_to_vsRef2(-0.777, "SCE", "CSE")
        self.assertAlmostEqual(result, -0.850, places=3)

    def test_convert_SHE_to_SCE(self):
        """Test conversion from SHE to SCE."""
        result = convert_vsRef1_to_vsRef2(1.229, "SHE", "SCE")
        self.assertAlmostEqual(result, 0.988, places=3)

    def test_convert_AgAgCl_to_CSE(self):
        """Test conversion from Ag/AgCl (saturated KCl) to CSE."""
        result = convert_vsRef1_to_vsRef2(-0.200, "Ag/AgCl (saturated KCl)", "CSE")
        self.assertAlmostEqual(result, -0.318, places=3)

    def test_convert_CSE_to_SHE(self):
        """Test conversion from CSE to SHE."""
        result = convert_vsRef1_to_vsRef2(-0.600, "CSE", "SHE")
        self.assertAlmostEqual(result, -0.286, places=3)

if __name__ == '__main__':
    unittest.main()
