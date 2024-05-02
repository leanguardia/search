from rubik.adapters.adapter import CubeAdapter
import json

class ToSnake(CubeAdapter):
    def adapt(self, face_order='ULFRBD', prepend_face=False, sort_by=None, add_breakline=False, fill_with='', value_map=None):
        cadena = ""
        for cara in face_order:
            for i in range(3):
                if prepend_face:
                    cadena += cara + fill_with

                if value_map is not None:
                    value_map2 = eval(value_map)
                cadena += self.face_dict[cara][i][0] + fill_with if value_map is None else value_map2[self.face_dict[cara][i][0]] + fill_with
                cadena += self.face_dict[cara][i][1] + fill_with if value_map is None else value_map2[self.face_dict[cara][i][1]] + fill_with
                cadena += self.face_dict[cara][i][2] + '\n' if value_map is None else value_map2[self.face_dict[cara][i][2]] + '\n'

            if add_breakline:
                cadena += '\n'

        if sort_by == 'level':
            cadena = self.sort_by_level(cadena)

        return cadena

    def sort_by_level(self, cadena):
        filas = cadena.strip().split('\n')
        nivel_1 = filas[0] + '\n' + filas[1] + '\n' + filas[2] + '\n'
        nivel_2 = filas[3] + '\n' + filas[6] + '\n' + filas[9] + '\n' + filas[12] + '\n'
        nivel_3 = filas[4] + '\n' + filas[7] + '\n' + filas[10] + '\n' + filas[13] + '\n'
        nivel_4 = filas[5] + '\n' + filas[8] + '\n' + filas[11] + '\n' + filas[14] + '\n'
        nivel_5 = filas[15] + '\n' + filas[16] + '\n' + filas[17] + '\n'
        salida = nivel_1 + nivel_2 + nivel_3 + nivel_4 + nivel_5
        return salida
