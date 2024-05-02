class CubeValidator():
    def __init__(self, faces):
        self.faces = faces
        self.colors = ['W', 'O', 'G', 'R', 'B', 'Y']
        self.face_directions = ['U', 'L', 'F', 'R', 'B', 'D']

    def run(self):
        self.validate_face_directions()
        self.validate_structure()
        self.validate_colors()

        return True

    def validate_face_directions(self):
        if list(self.faces.keys()) != self.face_directions:
            raise Exception('Acceptable faces are %s' % ', '.join(self.face_directions))
        
    def validate_structure(self):
        for face in self.faces:
            if len(self.faces[face]) != 3:
                raise Exception('There should be 3 rows per face')

            for row in self.faces[face]:
                if len(row) != 3:
                    raise Exception('There should be 3 cells per row')

    def validate_colors(self):
        color_count = {}
        for color in self.colors:
            color_count[color] = 0

        for face in self.faces:
            for row in self.faces[face]:
                for cell in row:
                    if cell not in self.colors:
                        raise Exception('Acceptable colors are %s' % ', '.join(self.colors))
                    color_count[cell] += 1

        for color in self.colors:
            if color_count[color] != 9:
                raise Exception('There should be 9 cells of each color')
            
        centers = [self.faces[face][1][1] for face in self.faces]
        if centers != self.colors:
            raise Exception('Invalid Center Positions')

