from rubik.adapters.adapter import CubeAdapter
COLORS = {
    "W": "white",
    "O": "orange",
    "G": "green",
    "R": "red",
    "B": "blue",
    "Y": "yellow"
}

class ToYAML(CubeAdapter):
    
    def adapt(self):
        yaml_string = ""
        for face, rows in self.face_dict.items():
            yaml_string += f"{self._get_face_name(face)}:\n"
            for row in rows:
                yaml_string += "    " + " ".join(COLORS[color] for color in row) + "\n"
        return yaml_string

    def _get_face_name(self, face):
        face_names = {
            'U': 'up',
            'F': 'front',
            'L': 'left',
            'R': 'right',
            'B': 'back',
            'D': 'down'
        }
        return face_names[face]
    