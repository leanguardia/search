import unittest
from rubik.adapters.to_csv import ToCsv

class TestDictionaryAdapter(unittest.TestCase):
    def test_adapt(self):
        faces_dict = {
            'U': ['WWW', 'WWW', 'WWW'],
            'L': ['OOO', 'OOO', 'OOO'],
            'F': ['GGG', 'GGG', 'GGG'],
            'R': ['RRR', 'RRR', 'RRR'],
            'B': ['BBB', 'BBB', 'BBB'],
            'D': ['YYY', 'YYY', 'YYY'],
        }
        adapter = ToCsv(faces_dict)
        self.assertEqual(
            adapter.adapt(),
"""Up,Front,Left,Right,Down,Back
W,O,G,R,B,Y
W,O,G,R,B,Y
W,O,G,R,B,Y
W,O,G,R,B,Y
W,O,G,R,B,Y
W,O,G,R,B,Y
W,O,G,R,B,Y
W,O,G,R,B,Y
W,O,G,R,B,Y"""
        )
        
