import argparse
import os.path

from src.utils import get_dir_structure
from src.translation import SRTranslator
from src.rw_srt_file import write_srt_file


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path")
    args = parser.parse_args()

    return args


def init(args):
    dir_in, dir_out, files = get_dir_structure(
        path=args.path,
    )

    return dir_in, dir_out, files


def translate_files(files, dir_in, dir_out):

    translator = SRTranslator()
    for file in files:
        print(f'----- TRANSLATION: {file}')
        full_filename_in = os.path.join(dir_in, file)
        full_filename_out = os.path.join(dir_out, os.path.splitext(file)[0] + '_FR' + os.path.splitext(file)[1])

        df = translator.translate_file(full_filename_in)
        write_srt_file(
            df=df,
            column_name_sentence='sentence_translated',
            output_file_path=full_filename_out,
        )


def main():

    args = arg_parser()
    dir_in, dir_out, files = init(args)
    translate_files(files, dir_in, dir_out)


if __name__ == '__main__':
    main()
