from adapters.adapter import CubeAdapter

class ToDictionary(CubeAdapter):
    def adapt(self):
        return {
            face: [list(row) for row in rows]
            for face, rows in self.face_dict.items()
        }
