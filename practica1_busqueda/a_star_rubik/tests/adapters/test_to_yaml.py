import unittest
from rubik.adapters.to_yaml import ToYAML
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
        adapter = ToYAML(faces_dict)
        self.assertEqual(
            adapter.adapt(),
"""up:
    white white white
    white white white
    white white white
left:
    orange orange orange
    orange orange orange
    orange orange orange
front:
    green green green
    green green green
    green green green
right:
    red red red
    red red red
    red red red
back:
    blue blue blue
    blue blue blue
    blue blue blue
down:
    yellow yellow yellow
    yellow yellow yellow
    yellow yellow yellow
"""
        )
        
