from rubik.adapters.adapter import CubeAdapter

class ToSnake(CubeAdapter):
    def adapt(self, face_order='ULFRBD', prepend_face=False, sort_by=None, add_breakline=False, fill_with='', value_map=None):
        string = ""
        breaklines = ['\n', '\n', '\n', '\n', '\n', '']

        for cara in face_order:
            for i in range(3):
                if prepend_face:
                    string += cara + fill_with

                if value_map is not None:
                    value_map_dic = eval(value_map)
                string += self.face_dict[cara][i][0] + fill_with if value_map is None else value_map_dic[self.face_dict[cara][i][0]] + fill_with
                string += self.face_dict[cara][i][1] + fill_with if value_map is None else value_map_dic[self.face_dict[cara][i][1]] + fill_with
                string += self.face_dict[cara][i][2] + '\n' if value_map is None else value_map_dic[self.face_dict[cara][i][2]] + '\n'

            if add_breakline:
                string += breaklines.pop(0)

        if sort_by == 'level':
            string = self.sort_by_level(string)

        return string

    def sort_by_level(self, string):
        rows = string.strip().split('\n')
        level_1 = rows[0] + '\n' + rows[1] + '\n' + rows[2] + '\n'
        level_2 = rows[3] + '\n' + rows[6] + '\n' + rows[9] + '\n' + rows[12] + '\n'
        level_3 = rows[4] + '\n' + rows[7] + '\n' + rows[10] + '\n' + rows[13] + '\n'
        level_4 = rows[5] + '\n' + rows[8] + '\n' + rows[11] + '\n' + rows[14] + '\n'
        level_5 = rows[15] + '\n' + rows[16] + '\n' + rows[17] + '\n'
        new_string = level_1 + level_2 + level_3 + level_4 + level_5
        return new_string
