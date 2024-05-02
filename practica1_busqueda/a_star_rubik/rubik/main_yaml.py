import os
from rubik.cube_loader import CubeLoader
from rubik.adapters.to_yaml import ToYAML

def load_sample_cubes_file_names():
    file_names = os.listdir('cubes')
    # filter the ones starting with cube
    file_names = [f for f in file_names if f[:4] == 'cube']
    return file_names

if __name__ == '__main__':
  

    cube_file_names = load_sample_cubes_file_names()
    print(len(cube_file_names), "files found in /cubes/ folder")

    # NOTE: this folder must exist
    folder_output = 'cubes/yaml/'

    for file_name in cube_file_names:
        loader = CubeLoader()
        print("Loading cube", file_name)
        face_dict = loader.load('cubes/' + file_name)
        
        adapter = ToYAML(face_dict)
        yaml_cube = adapter.adapt()
        
        with open(folder_output + file_name, 'w') as f:
             f.write(yaml_cube)
        print("Cube", file_name, "adapted to new format")
