import argparse
import os
from rubik.cube_loader import CubeLoader
from rubik.adapters.to_snake import ToSnake


def load_sample_cubes_file_names():
    file_names = os.listdir('cubes')
    file_names = [f for f in file_names if f[:4] == 'cube']
    return file_names


def save_snake_cube(snake, folder_output, file_name):
    with open(os.path.join(folder_output, file_name), 'w') as archivo:
        archivo.write(snake)
    print("Cube", file_name, "adapted to new format")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cube adapter to Snake')
    parser.add_argument('--prefix', default='', help='Prefix for output files')
    parser.add_argument('--face_order', default='ULFRBD', help='Sort faces in the inserted order, example DBRFUL ')
    parser.add_argument('--prepend_face', action='store_true', help='Prepend face to each row')
    parser.add_argument('--sort_by', choices=['face', 'level'], help='Sort face by face or level')
    parser.add_argument('--add_breakline', action='store_true', help='Add a breakline between each face')
    parser.add_argument('--fill_with', default='', help='Add a separator between each element')
    parser.add_argument('--value_map', default=None,
                        help='Replaces the colors of the pieces with the inserted value, respect the dictionary format, '
                             "example \"{'W':'white','O':'orange','B':'blue','R':'red',"
                             "'Y':'yellow','G':'green'}\" ")
    args = parser.parse_args()
    cube_file_names = load_sample_cubes_file_names()
    print(len(cube_file_names), "files found in /cubes/ folder")
    folder_output = 'cubes/snake/'
    for file_name in cube_file_names:
        loader = CubeLoader()
        print("Loading cube", file_name)
        face_dict = loader.load(os.path.join('cubes', file_name))
        adapter = ToSnake(face_dict)
        snake = adapter.adapt(
            face_order=args.face_order,
            prepend_face=args.prepend_face,
            sort_by=args.sort_by,
            add_breakline=args.add_breakline,
            fill_with=args.fill_with,
            value_map=args.value_map
        )
        save_snake_cube(snake, folder_output, args.prefix + file_name)
