import unittest
from rubik.adapters.to_square import ToSquare

class TestToSquare(unittest.TestCase):
    def setUp(self):
        # Set up a basic face dictionary to use in tests
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
        expected = "\n".join([
            "RBYYWBOGW",
            "YRWWOBRWO",
            "BRGOGGYOY",
            "RYGORYRBG",
            "OWGGBOOWB",
            "BYBGYRWRW"
        ])
        self.assertEqual(result, expected)

    def test_with_prepend_face(self):
        adapter = ToSquare(self.face_dict, prepend_face=True)
        result = adapter.adapt()
        expected = "\n".join([
            "U RBYYWBOGW",
            "L YRWWOBRWO",
            "F BRGOGGYOY",
            "R RYGORYRBG",
            "B OWGGBOOWB",
            "D BYBGYRWRW"
        ])
        self.assertEqual(result, expected)

    def test_with_fill_with(self):
        adapter = ToSquare(self.face_dict, fill_with=' ')
        result = adapter.adapt()
        expected = "\n".join([
            "R B Y Y W B O G W",
            "Y R W W O B R W O",
            "B R G O G G Y O Y",
            "R Y G O R Y R B G",
            "O W G G B O O W B",
            "B Y B G Y R W R W"
        ])
        self.assertEqual(result, expected)

    def test_with_wrap_with(self):
        adapter = ToSquare(self.face_dict, wrap_with='[]')
        result = adapter.adapt()
        expected = "\n".join([
            "[RBYYWBOGW]",
            "[YRWWOBRWO]",
            "[BRGOGGYOY]",
            "[RYGORYRBG]",
            "[OWGGBOOWB]",
            "[BYBGYRWRW]"
        ])
        self.assertEqual(result, expected)

    def test_with_value_map(self):
        value_map = {'R': 'red', 'Y': 'yellow', 'B': 'blue', 'G': 'green', 'W': 'white', 'O': 'orange'}
        adapter = ToSquare(self.face_dict, value_map=value_map) 
        result = adapter.adapt()
        expected = "\n".join([
            "red,blue,yellow,yellow,white,blue,orange,green,white",
            "yellow,red,white,white,orange,blue,red,white,orange",
            "blue,red,green,orange,green,green,yellow,orange,yellow",
            "red,yellow,green,orange,red,yellow,red,blue,green",
            "orange,white,green,green,blue,orange,orange,white,blue",
            "blue,yellow,blue,green,yellow,red,white,red,white"
        ])
        self.assertEqual(result, expected)
    
    def test_with_value_map_fill_with(self):
        value_map = {'R': 'red', 'Y': 'yellow', 'B': 'blue', 'G': 'green', 'W': 'white', 'O': 'orange'}
        adapter = ToSquare(self.face_dict, value_map=value_map, fill_with='/')
        result = adapter.adapt()
        expected = "\n".join([
            "red/blue/yellow/yellow/white/blue/orange/green/white",
            "yellow/red/white/white/orange/blue/red/white/orange",
            "blue/red/green/orange/green/green/yellow/orange/yellow",
            "red/yellow/green/orange/red/yellow/red/blue/green",
            "orange/white/green/green/blue/orange/orange/white/blue",
            "blue/yellow/blue/green/yellow/red/white/red/white"
        ])
        self.assertEqual(result, expected)
        
    

# To run the tests
if __name__ == '__main__':
    unittest.main()
