from adapters.adapter import CubeAdapter

class ToSquare(CubeAdapter):
    def adapt(self,fill_with="",face_order=["U", "L", "F", "R", "B", "D"],
              prepend_face=False, wrap_with=None):
       pattern = []
       for faces, rows in self.face_dict.items():
            for row in rows:
                pattern.extend(list(row))
            sublists = [pattern[i:i+9] for i in range(0, len(pattern), 9)]
            cube_string = '\n'.join([fill_with.join(sublist) for sublist in sublists])
       if prepend_face:
            sublists = [face_order[i] + "".join(sublist) for i, sublist in enumerate(sublists)]
            cube_string = '\n'.join([fill_with.join(sublist) for sublist in sublists])
       if wrap_with:
            cube_string = "\n".join([wrap_with[0] + row + wrap_with[1] for row in cube_string.split('\n')])
       
       return cube_string

