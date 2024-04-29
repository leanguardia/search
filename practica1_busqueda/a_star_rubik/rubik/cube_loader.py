class CubeLoader():
    def __init__(self):
        self.cube_faces = {
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

        try:
            self.validate(data)
        except Exception as e:
            file.close()
            raise e

        for i in range(0, 9, 3):
            self.cube_faces['U'].append(data[i:i+3])
        for i in range(9, 45, 12):
            self.cube_faces['L'].append(data[i:i+3])
        for i in range(12, 45, 12):
            self.cube_faces['F'].append(data[i:i+3])
        for i in range(15, 45, 12):
            self.cube_faces['R'].append(data[i:i+3])
        for i in range(18, 45, 12):
            self.cube_faces['B'].append(data[i:i+3])
        for i in range(45, 54, 3):
            self.cube_faces['D'].append(data[i:i+3])

        file.close()

    def validate(self, data):
        # data has 54 characters
        if len(data) != 54:
            raise Exception('Invalid cell count')

        # center positions
        centers = [data[4], data[22], data[25], data[28], data[31], data[49]]
        if centers != self.colors:
            raise Exception('Invalid center position')

        # count 9 of each color
        color_count = {}
        for color in self.colors:
            color_count[color] = 0
        for color in data:
            color_count[color] += 1
        for color in self.colors:
            if color_count[color] != 9:
                raise Exception('Invalid color count')

    def faces(self):
        return list(self.cube_faces.keys())
