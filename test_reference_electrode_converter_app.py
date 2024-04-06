import unittest
from reference_electrode_converter_app import convert_vsRef1_to_vsRef2

class TestElectrodePotentials(unittest.TestCase):

    def test_convert_SCE_to_CSE(self):
        """Test conversion from SCE to CSE."""
        result = convert_vsRef1_to_vsRef2(-0.777, "SCE", "CSE", 25, 25)
        self.assertAlmostEqual(result, -0.854, places=3)

    def test_convert_SHE_to_SCE(self):
        """Test conversion from SHE to SCE."""
        result = convert_vsRef1_to_vsRef2(1.229, "SHE", "SCE", 25, 25)
        self.assertAlmostEqual(result, 0.988, places=3)

    def test_convert_AgAgCl_to_CSE(self):
        """Test conversion from Ag/AgCl (saturated KCl) to CSE."""
        result = convert_vsRef1_to_vsRef2(-0.200, "Ag/AgCl (sat'd KCl)", "CSE", 25, 25)
        self.assertAlmostEqual(result, -0.322, places=3)

    def test_convert_CSE_to_SHE(self):
        """Test conversion from CSE to SHE."""
        result = convert_vsRef1_to_vsRef2(-0.600, "CSE", "SHE", 25, 25)
        self.assertAlmostEqual(result, -0.282, places=3)

if __name__ == '__main__':
    unittest.main()
