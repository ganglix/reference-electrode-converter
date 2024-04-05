import unittest
from reference_electrode_converter_app import convert_vsRef1_to_vsRef2, REF_POT_SHE

class TestConversion(unittest.TestCase):
    def test_convert_vsRef1_to_vsRef2(self):
        expected_result = -0.777 + REF_POT_SHE['SCE'] - REF_POT_SHE['CSE']
        self.assertAlmostEqual(convert_vsRef1_to_vsRef2(-0.777, 'SCE', 'CSE'), expected_result, places=3,
                               msg="The conversion from SCE to CSE did not match the expected result.")

if __name__ == '__main__':
    unittest.main()
