import unittest
from rubik.adapters.to_dictionary import ToDictionary
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
        adapter = ToDictionary(faces_dict)
        self.assertEqual(
            adapter.adapt(),
            {
                'U': [['W','W','W'], ['W','W','W'], ['W','W','W']],
                'L': [['O','O','O'], ['O','O','O'], ['O','O','O']],
                'F': [['G','G','G'], ['G','G','G'], ['G','G','G']],
                'R': [['R','R','R'], ['R','R','R'], ['R','R','R']],
                'B': [['B','B','B'], ['B','B','B'], ['B','B','B']],
                'D': [['Y','Y','Y'], ['Y','Y','Y'], ['Y','Y','Y']],
            }
        )
        
# Run the tests
if __name__ == '__main__':
    unittest.main()
