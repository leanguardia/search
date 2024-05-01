from rubik.adapters.adapter import CubeAdapter


class ToSnake(CubeAdapter):
    def adapt(self, face_order=None, prepend_face=False, sort_by=None, add_breakline=False, space_between=False):
        cadena = ""
        if face_order is None:
            face_order = ['U', 'L', 'F', 'R', 'B', 'D']  # Formato por defecto
        for cara in face_order:
            for i in range(3):
                if prepend_face:
                    cadena += cara + ' '
                cadena += self.face_dict[cara][i][0] + ' '
                cadena += self.face_dict[cara][i][1] + ' '
                cadena += self.face_dict[cara][i][2] + '\n'
            if add_breakline:
                cadena += '\n'
        if sort_by == 'level':
            cadena = self.sort_by_level(cadena)
        if not space_between:
            cadena = cadena.replace(' ','')
        return cadena.upper()

    def sort_by_level(self, cadena):
        filas = cadena.strip().split('\n')
        nivel_1 = filas[0] + '\n' + filas[1] + '\n' + filas[2] + '\n'
        nivel_2 = filas[3] + '\n' + filas[6] + '\n' + filas[9] + '\n' + filas[12] + '\n'
        nivel_3 = filas[4] + '\n' + filas[7] + '\n' + filas[10] + '\n' + filas[13] + '\n'
        nivel_4 = filas[5] + '\n' + filas[8] + '\n' + filas[11] + '\n' + filas[14] + '\n'
        nivel_5 = filas[15] + '\n' + filas[16] + '\n' + filas[17] + '\n'
        salida = nivel_1 + nivel_2 + nivel_3 + nivel_4 + nivel_5
        return salida
