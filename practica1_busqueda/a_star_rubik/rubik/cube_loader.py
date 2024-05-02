from rubik.cube_validator import CubeValidator

class CubeLoader():
    def __init__(self):
        self.faces = {
            'U': [],
            'L': [],
            'F': [],
            'R': [],
            'B': [],
            'D': [],
        }
        self.colors = ['W', 'O', 'G', 'R', 'B', 'Y']

    def load(self, file_path):
        file = open(file_path, 'r')
        lines = file.readlines()

        # remove all spaces and breaklines
        lines = [line.replace(' ', '').replace('\n', '') for line in lines]
        # merge lines into a single one

        data = ''.join(lines)

        for i in range(0, 9, 3):
            self.faces['U'].append(data[i:i+3])
        for i in range(9, 45, 12):
            self.faces['L'].append(data[i:i+3])
        for i in range(12, 45, 12):
            self.faces['F'].append(data[i:i+3])
        for i in range(15, 45, 12):
            self.faces['R'].append(data[i:i+3])
        for i in range(18, 45, 12):
            self.faces['B'].append(data[i:i+3])
        for i in range(45, 54, 3):
            self.faces['D'].append(data[i:i+3])

        file.close()

        CubeValidator(self.faces).run()

        return self.faces
