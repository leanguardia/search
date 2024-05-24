import os
import argparse
from ast import literal_eval
from rubik.cube_loader import CubeLoader
from rubik.adapters.to_square import ToSquare

def main():
    parser = argparse.ArgumentParser(description='Adaptar cubos a formato cuadrado')
    parser.add_argument('--prefix', default='', help='Prefijo para los nombres de archivo de salida')
    parser.add_argument('--prepend_face', action='store_true', help='Anteponer el nombre de la cara al principio de cada línea')
    parser.add_argument('--fill_with', default='', help='Carácter para rellenar los espacios vacíos')
    parser.add_argument('--wrap_with', nargs=2, metavar=('START', 'END'), default=None, help='Caracteres para envolver cada línea')
    parser.add_argument('--value-map', type=literal_eval, default=None, help='Diccionario para mapear valores de colores')

    args = parser.parse_args()

    # Cargar los archivos de cubos desde la carpeta 'cubes'
    cube_file_names = [f for f in os.listdir('cubes') if f.startswith('cube')]
    print(f"{len(cube_file_names)} archivos encontrados en la carpeta /cubes/")

    # Crear la carpeta de salida si no existe
    output_folder = 'cubes/square/'
    os.makedirs(output_folder, exist_ok=True)

    for file_name in cube_file_names:
        print(f"Cargando cubo {file_name}")
        loader = CubeLoader()
        face_dict = loader.load(os.path.join('cubes', file_name))
        adapter = ToSquare(face_dict, value_map=args.value_map, prepend_face=args.prepend_face, fill_with=args.fill_with, wrap_with=args.wrap_with)
        square_cube = adapter.adapt()
        output_file = os.path.join(output_folder, f"{args.prefix}{file_name}")
        with open(output_file, 'w') as f:
            f.write(square_cube)
        print(f"Cubo {file_name} adaptado y guardado en {output_file}")

if __name__ == '__main__':
    main()
