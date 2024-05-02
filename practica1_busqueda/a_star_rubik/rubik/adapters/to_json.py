import json
from rubik.adapters.adapter import CubeAdapter

HARDCODED_END = {
    "w": [
        ["w6", "w7", "w8"],
        ["w3", "w4", "w5"],
        ["w0", "w1", "w2"]
    ],
    "r": [
        ["r6", "r7", "r8"],
        ["r3", "r4", "r5"],
        ["r0", "r1", "r2"]
    ],
    "g": [
        ["g6", "g7", "g8"],
        ["g3", "g4", "g5"],
        ["g0", "g1", "g2"]
    ],
    "o": [
        ["o6", "o7", "o8"],
        ["o3", "o4", "o5"],
        ["o0", "o1", "o2"]
    ],
    "y": [
        ["y6", "y7", "y8"],
        ["y3", "y4", "y5"],
        ["y0", "y1", "y2"]
    ],
    "b": [
        ["b6", "b7", "b8"],
        ["b3", "b4", "b5"],
        ["b0", "b1", "b2"]
    ]
}

class ToJson(CubeAdapter):
    def __init__(self, face_dict, state_label='start'):
        super().__init__(face_dict)
        self.state_label = state_label

    def adapt(self):
        formatted_dict = {
            self.state_label: {},
            "end": HARDCODED_END
        }

        for face, rows in self.face_dict.items():
            formatted_rows = []
            for row in rows:
                formatted_row = [char for char in row]
                formatted_rows.append(formatted_row)
            formatted_dict[self.state_label][face] = formatted_rows

        return json.dumps(formatted_dict, indent=4)