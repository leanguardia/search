from cube_loader import CubeLoader


if __name__ == '__main__':
    cube_loader = CubeLoader()
    cube_loader.load('cubes/cubo-2.txt')
    print(cube_loader.cube_faces)