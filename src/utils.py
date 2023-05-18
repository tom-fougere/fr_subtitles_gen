import os


def is_file(path):
    return path is not None and os.path.isfile(path)


def is_dir(path):
    return path is not None and os.path.isdir(path)


def list_files_in_dir(path, extension=".srt"):
    list_files = []

    for file in os.listdir(path):
        if file.endswith(extension):
            list_files.append(file)

    return list_files


def get_files(path):
    files = []
    if is_file(path):
        files.append(os.path.basename(path))
    elif is_dir(path):
        files = files + list_files_in_dir(path)

    return files


def get_dir_structure(path, default_dir_in='d01_data/english', default_dir_out='d01_data/french'):

    if is_dir(path):
        dir_files_in = path
        dir_files_out = path
        files = get_files(path)
    elif is_file(path):
        dir_files_in = os.path.dirname(path)
        dir_files_out = os.path.dirname(path)
        files = get_files(path)
    else:
        dir_files_in = default_dir_in
        dir_files_out = default_dir_out
        files = get_files(default_dir_in)

    return dir_files_in, dir_files_out, files
