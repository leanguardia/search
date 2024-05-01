from rubik.adapters.to_square import ToSquare

if __name__ == "__main__":
    face_dict = { 
        'U': ['RBY', 'YWB', 'OGW'],
        'L': ['YRW', 'WOB', 'RWO'],
        'F': ['BRG', 'OGG', 'YOY'],
        'R': ['RYG', 'ORY', 'RBG'],
        'B': ['OWG', 'GBO', 'OWB'],
        'D': ['BYB', 'GYR', 'WRW']
    }
    adapter = ToSquare(face_dict, prepend_face=True, fill_with=' ', wrap_with='[]')
    print(adapter.adapt())