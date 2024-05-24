import pprint
import os
from rubik.cube_loader import CubeLoader
from rubik.adapters.to_dictionary import ToDictionary

def load_file_from_user_input():
    file_name = input('Nombre de archivo: /cubes/')
    file_path = "cubes/" + file_name
    if file_name[-4:] != '.txt':
        file_path += '.txt'
    print("Loading cube from file: " + file_path)

    loader = CubeLoader()
    print(loader.load(file_path))

def load_sample_cubes_file_names():
    file_names = os.listdir('cubes')
    # filter the ones starting with cube
    file_names = [f for f in file_names if f[:4] == 'cube']
    return file_names

if __name__ == '__main__':
    # load_file_from_user_input()

    cube_file_names = load_sample_cubes_file_names()
    print(len(cube_file_names), "files found in /cubes/ folder")

    # NOTE: this folder must exist
    folder_output = 'cubes/dictionary/'

    for file_name in cube_file_names:
        loader = CubeLoader()
        print("Loading cube", file_name)
        face_dict = loader.load('cubes/' + file_name)
        adapter = ToDictionary(face_dict)
        dictionary = adapter.adapt()
        with open(folder_output + file_name, 'w') as f:
            f.write(pprint.pformat(dictionary, sort_dicts=False, indent=4))
        print("Cube", file_name, "adapted to new format")
