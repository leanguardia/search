import json
from rubik.adapters.adapter import CubeAdapter

class ToJson(CubeAdapter):
    def __init__(self, face_dict):
        super().__init__(face_dict)

    def adapt(self):
        # Prepare a dictionary to convert to JSON
        data = {face: self.face_dict[face] for face in self.face_dict}
        # Convert the dictionary to a JSON string
        return json.dumps(data, indent=4)

# Example usage (this part can go in a separate script or under if __name__ == "__main__":)
if __name__ == "__main__":
    face_dict = {
        'U': ['RBY', 'YWB', 'OGW'],
        'L': ['YRW', 'WOB', 'RWO'],
        'F': ['BRG', 'OGG', 'YOY'],
        'R': ['RYG', 'ORY', 'RBG'],
        'B': ['OWG', 'GBO', 'OWB'],
        'D': ['BYB', 'GYR', 'WRW']
    }
    adapter = ToJson(face_dict)
    json_output = adapter.adapt()
    print(json_output)
