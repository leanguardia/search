import argparse
from rubik.adapters.to_square import ToSquare

def main():
    parser = argparse.ArgumentParser(description="Transform a Rubik's Cube face dictionary to a square string representation.")
    parser.add_argument('--value_map', type=str, help="Map of characters to replace. Example: R:red,Y:yellow", default=None)
    parser.add_argument('--face_order', type=str, help="Comma-separated list of faces in the order to process. Example: U,L,F,R,B,D", default="U,L,F,R,B,D")
    parser.add_argument('--prepend_face', action='store_true', help="Prepend each face's data with its identifier.")
    parser.add_argument('--fill_with', type=str, help="Character to fill between elements. Example: ','", default='')
    parser.add_argument('--wrap_with', type=str, help="Characters to wrap each face's data. Example: []", default=None)
    
    args = parser.parse_args()

    # Process value_map
    value_map = {k:v for k,v in (item.split(':') for item in args.value_map.split(','))} if args.value_map else None

    # Process face_order
    face_order = args.face_order.split(',') if args.face_order else None

    # Process wrap_with
    wrap_with = (args.wrap_with[0], args.wrap_with[-1]) if args.wrap_with else None

    # Create and configure the ToSquare adapter
    face_dict = {
        'U': ['RBY', 'YWB', 'OGW'],
        'L': ['YRW', 'WOB', 'RWO'],
        'F': ['BRG', 'OGG', 'YOY'],
        'R': ['RYG', 'ORY', 'RBG'],
        'B': ['OWG', 'GBO', 'OWB'],
        'D': ['BYB', 'GYR', 'WRW']
    }
    adapter = ToSquare(face_dict, value_map=value_map, face_order=face_order, 
                       prepend_face=args.prepend_face, fill_with=args.fill_with, wrap_with=wrap_with)
    print(adapter.adapt())

if __name__ == '__main__':
    main()
