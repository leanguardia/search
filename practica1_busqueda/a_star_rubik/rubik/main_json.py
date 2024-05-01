import json
from rubik.adapters.adapter import CubeAdapter
from rubik.adapters.to_json import ToJson

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
    adapter = ToJson(face_dict, state_label='start')
    json_output = adapter.adapt()
    print(json_output)
