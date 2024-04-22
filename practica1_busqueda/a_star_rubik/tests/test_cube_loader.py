import unittest
from rubik.cube_loader import CubeLoader


class TestBoard(unittest.TestCase):
    def test_loads_a_sorted_cube(self):
        loader = CubeLoader()
        loader.load('tests/fixtures/sorted_cube.txt')

        print("cube_dict")
        print(loader.cube_dict)
        self.assertEqual(len(loader.cube_dict['U']), 3)
        self.assertEqual(len(loader.cube_dict['D']), 3)
        self.assertEqual(len(loader.cube_dict['L']), 3)
        self.assertEqual(len(loader.cube_dict['R']), 3)
        self.assertEqual(len(loader.cube_dict['F']), 3)
        self.assertEqual(len(loader.cube_dict['B']), 3)

    # def test_a_sorted_cube_is_valid(self):
    #     loader = CubeLoader()
    #     loader.load('tests/fixtures/sorted_cube.txt')

    #     self.assertTrue(loader.validate())

    # def test_loads_invalid_center(self):
    #     loader = CubeLoader()
    #     loader.load('tests/fixtures/invalid_centers.txt')

    #     self.assertFalse(loader.validate())


# Run the tests
if __name__ == '__main__':
    unittest.main()
