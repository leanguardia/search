import unittest
from rubik.cube_validator import CubeValidator


class TestCubeValidator(unittest.TestCase):
    def test_valid_cube(self):
        validator = CubeValidator({
            'U': ['WWW', 'WWW', 'WWW'],
            'L': ['OOO', 'OOO', 'OOO'],
            'F': ['GGG', 'GGG', 'GGG'],
            'R': ['RRR', 'RRR', 'RRR'],
            'B': ['BBB', 'BBB', 'BBB'],
            'D': ['YYY', 'YYY', 'YYY'],
        })
        self.assertTrue(validator.run())

    def test_invalid_num_of_faces(self):
        with self.assertRaises(Exception) as context:
            CubeValidator({
                'U': ['WWW', 'WWW', 'WWW'],
            }).run()
        self.assertEqual(str(context.exception), 'Acceptable faces are U, L, F, R, B, D')

    def test_invalid_face_names(self):
        with self.assertRaises(Exception) as context:
            CubeValidator({
                'U': ['WWW', 'WWW', 'WWW'],
                'L': ['OOO', 'OOO', 'OOO'],
                'F': ['GGG', 'GGG', 'GGG'],
                'R': ['RRR', 'RRR', 'RRR'],
                'B': ['BBB', 'BBB', 'BBB'],
                'X': ['YYY', 'YYY', 'YYY'],
            }).run()
        self.assertEqual(str(context.exception), 'Acceptable faces are U, L, F, R, B, D')

    def test_invalid_num_of_rows(self):
        with self.assertRaises(Exception) as context:
            CubeValidator({
                'U': ['WWW', 'WWW', 'WWW', 'WWW'],
                'L': ['OOO', 'OOO', 'OOO'],
                'F': ['GGG', 'GGG', 'GGG'],
                'R': ['RRR', 'RRR', 'RRR'],
                'B': ['BBB', 'BBB', 'BBB'],
                'D': ['YYY', 'YYY', 'YYY'],
            }).run()
        self.assertEqual(str(context.exception), 'There should be 3 rows per face')

    def test_invalid_num_of_cells(self):
        with self.assertRaises(Exception) as context:
            CubeValidator({
                'U': ['WWW', 'WWW', 'WWW'],
                'L': ['OOO', 'OO', 'OOO'],
                'F': ['GGG', 'GGG', 'GGGG'],
                'R': ['RRR', 'RRR', 'RRR'],
                'B': ['BBB', 'BBB', 'BBB'],
                'D': ['YYY', 'YYY', 'YYY'],
            }).run()
        self.assertEqual(str(context.exception), 'There should be 3 cells per row')

    def test_invalid_color(self):
        with self.assertRaises(Exception) as context:
            CubeValidator({
                'U': ['WWW', 'WWW', 'WWW'],
                'L': ['OOO', 'OOO', 'OOO'],
                'F': ['GGG', 'GGG', 'GGG'],
                'R': ['RRR', 'RRR', 'RRR'],
                'B': ['BBB', 'BBB', 'BBB'],
                'D': ['YYY', 'YYY', 'YYX'],
            }).run()
            self.assertEqual(str(context.exception), 'Acceptable colors are W, O, G, R, B, Y')

    def test_invalid_color_counts(self):
        with self.assertRaises(Exception) as context:
            CubeValidator({
                'U': ['WWW', 'WWW', 'WWW'],
                'L': ['WOO', 'OOO', 'OOO'],
                'F': ['GGG', 'GGG', 'GGG'],
                'R': ['RRR', 'RRR', 'RRR'],
                'B': ['BBB', 'BBB', 'BBY'],
                'D': ['YYY', 'YYY', 'YYY'],
            }).run()
        self.assertEqual(str(context.exception), 'There should be 9 cells of each color')

    def test_invalid_centers(self):
        with self.assertRaises(Exception) as context:
            CubeValidator({
                'U': ['WWW', 'WOW', 'WWW'],
                'L': ['OOO', 'OWO', 'OOO'],
                'F': ['GGG', 'GGG', 'GGG'],
                'R': ['RRR', 'RRR', 'RRR'],
                'B': ['BBB', 'BBB', 'BBB'],
                'D': ['YYY', 'YYY', 'YYY'],
            }).run()
        self.assertEqual(str(context.exception), 'Invalid Center Positions')


# Run the tests
if __name__ == '__main__':
    unittest.main()
