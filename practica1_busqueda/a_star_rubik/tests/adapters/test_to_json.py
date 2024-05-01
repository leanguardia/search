import unittest
import json

from rubik.adapters.to_json import ToJson

class TestToJson(unittest.TestCase):
    def setUp(self):
        self.face_dict = {
            'U': ['RBY', 'YWB', 'OGW'],
            'L': ['YRW', 'WOB', 'RWO'],
            'F': ['BRG', 'OGG', 'YOY'],
            'R': ['RYG', 'ORY', 'RBG'],
            'B': ['OWG', 'GBO', 'OWB'],
            'D': ['BYB', 'GYR', 'WRW']
        }
        self.expected_output = {
            "start": {
                "U": [
                    ["R", "B", "Y"],
                    ["Y", "W", "B"],
                    ["O", "G", "W"]
                ],
                "L": [
                    ["Y", "R", "W"],
                    ["W", "O", "B"],
                    ["R", "W", "O"]
                ],
                "F": [
                    ["B", "R", "G"],
                    ["O", "G", "G"],
                    ["Y", "O", "Y"]
                ],
                "R": [
                    ["R", "Y", "G"],
                    ["O", "R", "Y"],
                    ["R", "B", "G"]
                ],
                "B": [
                    ["O", "W", "G"],
                    ["G", "B", "O"],
                    ["O", "W", "B"]
                ],
                "D": [
                    ["B", "Y", "B"],
                    ["G", "Y", "R"],
                    ["W", "R", "W"]
                ]
            }
        }

    def test_adapt(self):
        adapter = ToJson(self.face_dict, state_label='start')
        result = adapter.adapt()
        expected_output = json.dumps(self.expected_output, indent=4)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()