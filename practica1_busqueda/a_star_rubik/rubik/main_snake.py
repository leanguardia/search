import cmd, sys
import os
from rubik.cube_loader import CubeLoader
from rubik.adapters.to_snake import ToSnake


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


def save_snake_cube(snake):
    with open(folder_output + file_name, 'w') as archivo:
        archivo.write(snake)
    print("Cube", file_name, "adapted to new format")


class SnakeAdapterShell(cmd.Cmd):
    intro = ('Welcome to the snake adapter shell.   Type help or ? to list the options.\n'
             'Introduzca default para transformar los cubos a formato snake por defecto.\n')
    prompt = '(snake adapter) '
    file = None

    def do_default(self, arg):
        "Sin ningun parámetro, simplemente transforma el cubo al formato Snake "
        snake = adapter.adapt()
        save_snake_cube(snake)
        return True

    def do_face_order(self, arg):
        "Ingrese en formato cadena el orden a escoger, por ejemplo DBRFLU "
        snake = adapter.adapt(face_order=arg)
        save_snake_cube(snake)
        return True

    def do_prepend_face(self, arg):
        "Sin ningun parámetro, simplemente agrega delante de cada fila, la cara a la que corresponde"
        snake = adapter.adapt(prepend_face=True, space_between=True)
        save_snake_cube(snake)
        return True

    def do_sort_by(self, arg):
        "Seleccione un criterio de ordenamiento [face, level]"
        snake = adapter.adapt(sort_by=arg, space_between=True)
        save_snake_cube(snake)
        return True

    def do_add_breakline(self,arg):
        "Sin ningun parámetro, simplemente agrega un salto de línea entre cada cara del cubo"
        snake = adapter.adapt(add_breakline=True)
        save_snake_cube(snake)
        return True



if __name__ == '__main__':
    cube_file_names = load_sample_cubes_file_names()
    print(len(cube_file_names), "files found in /cubes/ folder")

    folder_output = 'cubes/snake/'

    for file_name in cube_file_names:
        loader = CubeLoader()
        print("Loading cube", file_name)
        face_dict = loader.load('cubes/' + file_name)
        adapter = ToSnake(face_dict)
        SnakeAdapterShell().cmdloop()

