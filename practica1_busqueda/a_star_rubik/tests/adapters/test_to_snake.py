import unittest
from rubik.adapters.to_snake import ToSnake


class TestSnakeAdapter(unittest.TestCase):
    def test_adapt(self):
        faces_dict = {
            'U': ['WWW', 'WWW', 'WWW'],
            'L': ['OOO', 'OOO', 'OOO'],
            'F': ['GGG', 'GGG', 'GGG'],
            'R': ['RRR', 'RRR', 'RRR'],
            'B': ['BBB', 'BBB', 'BBB'],
            'D': ['YYY', 'YYY', 'YYY'],
        }
        adapter = ToSnake(faces_dict)
        self.assertEqual(
            adapter.adapt(), "WWW\n" +
                             "WWW\n" +
                             "WWW\n" +
                             "OOO\n" +
                             "OOO\n" +
                             "OOO\n" +
                             "GGG\n" +
                             "GGG\n" +
                             "GGG\n" +
                             "RRR\n" +
                             "RRR\n" +
                             "RRR\n" +
                             "BBB\n" +
                             "BBB\n" +
                             "BBB\n" +
                             "YYY\n" +
                             "YYY\n" +
                             'YYY\n'
        )

    def test_adapt_snake_face_order(self):
        faces_dict = {
            'U': ['WWW', 'WWW', 'WWW'],
            'L': ['OOO', 'OOO', 'OOO'],
            'F': ['GGG', 'GGG', 'GGG'],
            'R': ['RRR', 'RRR', 'RRR'],
            'B': ['BBB', 'BBB', 'BBB'],
            'D': ['YYY', 'YYY', 'YYY'],
        }
        adapter = ToSnake(faces_dict)
        self.assertEqual(
            adapter.adapt(face_order=['D', 'F', 'R', 'B', 'L', 'U']), "YYY\n" +
                                                                      "YYY\n" +
                                                                      "YYY\n" +
                                                                      "GGG\n" +
                                                                      "GGG\n" +
                                                                      "GGG\n" +
                                                                      "RRR\n" +
                                                                      "RRR\n" +
                                                                      "RRR\n" +
                                                                      "BBB\n" +
                                                                      "BBB\n" +
                                                                      "BBB\n" +
                                                                      "OOO\n" +
                                                                      "OOO\n" +
                                                                      "OOO\n" +
                                                                      "WWW\n" +
                                                                      "WWW\n" +
                                                                      'WWW\n'
        )

    def test_adapt_snake_prepend_face(self):
        faces_dict = {
            'U': ['WWW', 'WWW', 'WWW'],
            'L': ['OOO', 'OOO', 'OOO'],
            'F': ['GGG', 'GGG', 'GGG'],
            'R': ['RRR', 'RRR', 'RRR'],
            'B': ['BBB', 'BBB', 'BBB'],
            'D': ['YYY', 'YYY', 'YYY'],
        }
        adapter = ToSnake(faces_dict)
        self.assertEqual(
            adapter.adapt(prepend_face=True, space_between=True), "U W W W\n"
                                                                  "U W W W\n"
                                                                  "U W W W\n"
                                                                  "L O O O\n"
                                                                  "L O O O\n"
                                                                  "L O O O\n"
                                                                  "F G G G\n"
                                                                  "F G G G\n"
                                                                  "F G G G\n"
                                                                  "R R R R\n"
                                                                  "R R R R\n"
                                                                  "R R R R\n"
                                                                  "B B B B\n"
                                                                  "B B B B\n"
                                                                  "B B B B\n"
                                                                  "D Y Y Y\n"
                                                                  "D Y Y Y\n"
                                                                  'D Y Y Y\n'
        )

    def test_adapt_snake_break_line(self):
        faces_dict = {
            'U': ['WWW', 'WWW', 'WWW'],
            'L': ['OOO', 'OOO', 'OOO'],
            'F': ['GGG', 'GGG', 'GGG'],
            'R': ['RRR', 'RRR', 'RRR'],
            'B': ['BBB', 'BBB', 'BBB'],
            'D': ['YYY', 'YYY', 'YYY'],
        }
        adapter = ToSnake(faces_dict)
        self.assertEqual(
            adapter.adapt(add_breakline=True), "WWW\n" +
                                               "WWW\n" +
                                               "WWW\n\n" +
                                               "OOO\n" +
                                               "OOO\n" +
                                               "OOO\n\n" +
                                               "GGG\n" +
                                               "GGG\n" +
                                               "GGG\n\n" +
                                               "RRR\n" +
                                               "RRR\n" +
                                               "RRR\n\n" +
                                               "BBB\n" +
                                               "BBB\n" +
                                               "BBB\n\n" +
                                               "YYY\n" +
                                               "YYY\n" +
                                               'YYY\n\n'
        )

    def test_adapt_snake_sort_by_level(self):
        faces_dict = {
            'U': ['WWW', 'WWW', 'WWW'],
            'L': ['OOO', 'OOO', 'OOO'],
            'F': ['GGG', 'GGG', 'GGG'],
            'R': ['RRR', 'RRR', 'RRR'],
            'B': ['BBB', 'BBB', 'BBB'],
            'D': ['YYY', 'YYY', 'YYY'],
        }
        adapter = ToSnake(faces_dict)
        self.assertEqual(
            adapter.adapt(sort_by='level', space_between=True), "W W W\n" +
                                                                "W W W\n" +
                                                                "W W W\n" +
                                                                "O O O\n" +
                                                                "G G G\n" +
                                                                "R R R\n" +
                                                                "B B B\n" +
                                                                "O O O\n" +
                                                                "G G G\n" +
                                                                "R R R\n" +
                                                                "B B B\n" +
                                                                "O O O\n" +
                                                                "G G G\n" +
                                                                "R R R\n" +
                                                                "B B B\n" +
                                                                "Y Y Y\n" +
                                                                "Y Y Y\n" +
                                                                'Y Y Y\n'
        )
