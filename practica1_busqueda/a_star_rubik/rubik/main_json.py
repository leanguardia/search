import os
from rubik.cube_loader import CubeLoader
from rubik.adapters.to_json import ToJson

if __name__ == "__main__":
    # Cargar los archivos de cubos desde la carpeta 'cubes'
    cube_file_names = [f for f in os.listdir('cubes') if f.startswith('cube')]
    print(f"{len(cube_file_names)} archivos encontrados en la carpeta /cubes/")

    # Crear la carpeta de salida si no existe
    output_folder = 'cubes/json/'
    os.makedirs(output_folder, exist_ok=True)

    for file_name in cube_file_names:
        print(f"Cargando cubo {file_name}")
        loader = CubeLoader()
        face_dict = loader.load(os.path.join('cubes', file_name))
        adapter = ToJson(face_dict, state_label='start')
        json_output = adapter.adapt()
        output_file = os.path.join(output_folder, f"{file_name}.json")
        with open(output_file, 'w') as f:
            f.write(json_output)
        print(f"Cubo {file_name} adaptado y guardado en {output_file}")
