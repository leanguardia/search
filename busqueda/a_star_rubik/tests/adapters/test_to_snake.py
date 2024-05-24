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
            adapter.adapt(prepend_face=True, fill_with=' '), "U W W W\n"
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
                                               'YYY\n'
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
            adapter.adapt(sort_by='level', fill_with=' '), "W W W\n" +
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

    def test_adapt_snake_value_map(self):
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
            adapter.adapt(
                value_map='{"W": "white", "O": "orange", "B": "blue", "R": "red", "Y": "yellow", "G": "green"}',
                fill_with=' '), "white white white\n" +
                                "white white white\n" +
                                "white white white\n" +
                                "orange orange orange\n" +
                                "orange orange orange\n" +
                                "orange orange orange\n" +
                                "green green green\n" +
                                "green green green\n" +
                                "green green green\n" +
                                "red red red\n" +
                                "red red red\n" +
                                "red red red\n" +
                                "blue blue blue\n" +
                                "blue blue blue\n" +
                                "blue blue blue\n" +
                                "yellow yellow yellow\n" +
                                "yellow yellow yellow\n" +
                                'yellow yellow yellow\n'
        )


if "__main__" == __name__:
    unittest.main()
