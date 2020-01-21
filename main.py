import export_path
import argparse

if __name__ == '__main__':
    # Construct the argument parser and parse the arguments
    # EXAMPLES: python main.py -p patient_images_lowres.h5 -sv n -sw y
    ap = argparse.ArgumentParser()
    ap.add_argument('-p', '--path-file', type=str, required=True,
                    help='Path to the .h5 or .hdf5 file.')
    ap.add_argument('-sv', '--save-option', choices=['y','n'], type=str, required=True,
                    help='Save images: y/n')
    ap.add_argument('-sw', '--show-option', choices=['y','n'], type=str, required=True,
                    help='Show images: y/n')

    args = vars(ap.parse_args())

    export_path.directory_images(args['path_file'], save=args['show_option'], show=args['show_option'])
    print("[INFO] Program finish")