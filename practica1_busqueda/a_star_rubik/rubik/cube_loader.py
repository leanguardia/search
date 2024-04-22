class CubeLoader():
    def __init__(self):
        self.cube_dict = {
            'U': [],
            'L': [],
            'F': [],
            'R': [],
            'B': [],
            'D': [],
        }

    def load(self, file_path):
        file = open(file_path, 'r')
        lines = file.readlines()

        # remove all spaces and breaklines
        lines = [line.replace(' ', '').replace('\n', '') for line in lines]
        # merge lines into a single one
        data = ''.join(lines)
        print(data)
        for i in range(0, 54, 3):
            if i < 9:
                self.cube_dict['U'].append(data[i:i+3])
            elif i < 18:
                self.cube_dict['L'].append(data[i:i+3])
            elif i < 27:
                self.cube_dict['F'].append(data[i:i+3])
            elif i < 36:
                self.cube_dict['R'].append(data[i:i+3])
            elif i < 45:
                self.cube_dict['B'].append(data[i:i+3])
            else:
                self.cube_dict['D'].append(data[i:i+3])

        file.close()
    
    def validate(self):
        return True
