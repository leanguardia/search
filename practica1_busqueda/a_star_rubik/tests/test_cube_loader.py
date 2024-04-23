import unittest
from rubik.cube_loader import CubeLoader


class TestBoard(unittest.TestCase):
    def test_loads_a_sorted_cube(self):
        loader = CubeLoader()
        loader.load('tests/fixtures/sorted_cube.txt')

        faces = loader.cube_faces

        up_face = faces['U']
        self.assertEqual(len(up_face), 3)
        for row in up_face:
            self.assertEqual(row, 'WWW')

        left_face = faces['L']
        self.assertEqual(len(left_face), 3)
        for row in left_face:
            self.assertEqual(row, 'OOO')

        front_face = faces['F']
        self.assertEqual(len(front_face), 3)
        for row in front_face:
            self.assertEqual(row, 'GGG')

        right_face = faces['R']
        self.assertEqual(len(right_face), 3)
        for row in right_face:
            self.assertEqual(row, 'RRR')

        back_face = faces['B']
        self.assertEqual(len(back_face), 3)
        for row in back_face:
            self.assertEqual(row, 'BBB')

        down_face = faces['D']
        self.assertEqual(len(down_face), 3)
        for row in down_face:
            self.assertEqual(row, 'YYY')

    def test_an_unsorted_cube(self):
        loader = CubeLoader()
        loader.load('tests/fixtures/unsorted_cube.txt')

        faces = loader.cube_faces

        up_face = faces['U']
        self.assertEqual(len(up_face), 3)
        left_face = faces['L']
        self.assertEqual(len(left_face), 3)
        front_face = faces['F']
        self.assertEqual(len(front_face), 3)
        right_face = faces['R']
        self.assertEqual(len(right_face), 3)
        back_face = faces['B']
        self.assertEqual(len(back_face), 3)
        down_face = faces['D']
        self.assertEqual(len(down_face), 3)

    def test_invalid_center_position(self):
        loader = CubeLoader()
        try:
            loader.load('tests/fixtures/invalid_center_position.txt')
        except Exception as e:
            self.assertEqual(str(e), 'Invalid center position')

    def test_loads_invalid_cell_count(self):
        loader = CubeLoader()
        try:
            loader.load('tests/fixtures/invalid_cell_count.txt')
        except Exception as e:
            self.assertEqual(str(e), 'Invalid cell count')

    def test_loads_invalid_color_count(self):
        loader = CubeLoader()
        try:
            loader.load('tests/fixtures/invalid_color_count.txt')
        except Exception as e:
            self.assertEqual(str(e), 'Invalid color count')


# Run the tests
if __name__ == '__main__':
    unittest.main()
