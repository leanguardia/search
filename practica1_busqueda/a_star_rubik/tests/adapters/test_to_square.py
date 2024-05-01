import unittest
from rubik.adapters.to_square import ToSquare

class TestToSquare(unittest.TestCase):
    def setUp(self):
        # Setup a basic cube configuration
        self.face_dict = {
            'U': ['RBY', 'YWB', 'OGW'],
            'L': ['YRW', 'WOB', 'RWO'],
            'F': ['BRG', 'OGG', 'YOY'],
            'R': ['RYG', 'ORY', 'RBG'],
            'B': ['OWG', 'GBO', 'OWB'],
            'D': ['BYB', 'GYR', 'WRW']
        }

    def test_basic_output(self):
        adapter = ToSquare(self.face_dict)
        result = adapter.adapt()
        expected = "RBYYWBOGWYRWWOBRWOBRRBGOGGYOYORYGORYRBGOWGGBOWOWBBYBGYRWRW"
        self.assertEqual(result, expected)

    def test_with_prepend_face(self):
        adapter = ToSquare(self.face_dict, prepend_face=True)
        result = adapter.adapt()
        expected = "URBYYWBOGWLYRWWOBRWOFFBRGOGGYOYRRRYGORYRBGBOWGGBOWOWBDBYBGYRWRW"
        self.assertEqual(result, expected)

    def test_with_fill_with(self):
        adapter = ToSquare(self.face_dict, fill_with=' ')
        result = adapter.adapt()
        expected = "R B Y Y W B O G W Y R W W O B R W O B R G O G G Y O Y R Y G O R Y R B G O W G G B O O W B D B Y B G Y R W R W"
        self.assertEqual(result, expected)

    def test_with_wrap_with(self):
        adapter = ToSquare(self.face_dict, wrap_with=('(', ')'))
        result = adapter.adapt()
        expected = "(RBY)(YWB)(OGW)(YRW)(WOB)(RWO)(BRG)(OGG)(YOY)(RYG)(ORY)(RBG)(OWG)(GBO)(OWB)(BYB)(GYR)(WRW)"
        self.assertEqual(result, expected)

# To run the tests
if __name__ == '__main__':
    unittest.main()
