import json
from rubik.adapters.adapter import CubeAdapter

class ToJson(CubeAdapter):
    def __init__(self, face_dict, state_label='start'):
        super().__init__(face_dict)
        self.state_label = state_label

    def adapt(self):
        formatted_dict = {
            self.state_label: {}
        }
        for face, rows in self.face_dict.items():
            formatted_dict[self.state_label][face] = rows

        return json.dumps(formatted_dict, indent=4)
