from rubik.adapters.adapter import CubeAdapter

class ToCsv(CubeAdapter):
    def adapt(self):
        patterns = [[] for _ in range(9)]
        for face, rows in self.face_dict.items():
            for i, row in enumerate(rows):
                for j, color in enumerate(row):
                    patterns[i * 3 + j].append(color)

        formatted_strings = '\n'.join([','.join(pattern) for pattern in patterns])
        return 'Up,Front,Left,Right,Down,Back\n' + formatted_strings
    