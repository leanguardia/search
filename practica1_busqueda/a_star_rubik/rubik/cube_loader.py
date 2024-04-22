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
        self.colors.sort()

    def load(self, file_path):
        file = open(file_path, 'r')
        lines = file.readlines()

        # remove all spaces and breaklines
        lines = [line.replace(' ', '').replace('\n', '') for line in lines]
        # merge lines into a single one

        data = ''.join(lines)

        self.validate(data)
        

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
        # check if data has 54 characters
        if len(data) != 54:
            raise Exception('Invalid cell count')

        # count colors
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
