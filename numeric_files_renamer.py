import argparse
import os


def init_args():
    parser = argparse.ArgumentParser(
        description=
        """Renames files from directory from "title_ch01_asd.mp4" to "01.mp4" using text before and after number.
        Example:
        before_number="ch" and after_number="_as.ds" will rename 
        "title_ch01_as.dsd.mp4" to "01.mp4"
        and "ch02_as.ds.mkv" to "02.mkv".
        """
    )
    parser.add_argument("path", help="Path to directory with files.", type=str)
    parser.add_argument("before_number", help="Text of filename before number.", type=str)
    parser.add_argument("after_number", help="Text of filename after number (without extension).", type=str)
    # parser.add_argument("-v", "--verbose", help="Make output more verbosity (more logs).", action="store_true")
    return parser.parse_args()


def get_files(path):
    if not os.path.exists(path):
        print(f"Directory \"{path}\" does not exist.")
        return []
    if not os.path.isdir(path):
        print(f"\"{path}\" is not a directory.")
        return []
    return os.listdir(path)


def get_new_filename(filename, before_number, after_number):
    ext_split = filename.split(os.extsep)
    if len(ext_split) != 1:
        ext = ext_split.pop(len(ext_split) - 1)
        filename = '.'.join(ext_split)
    else:
        ext = ""
    l_parts = filename.split(before_number)
    r_parts = l_parts[len(l_parts) - 1].split(after_number)
    return f"{r_parts[0]}{os.extsep}{ext}"


def main():
    args = init_args()
    # Firstly, we will check path and get files from it.
    files = get_files(args.path)

    for file_path in files:
        # Secondly, for each path to file in dir get new filename.
        new_filename = get_new_filename(file_path, args.before_number, args.after_number)
        print(f"Changing filename from \"{file_path}\" to \"{new_filename}\"")
        # Thirdly, set new filename.
        os.rename(os.path.join(args.path, file_path), os.path.join(args.path, new_filename))


if __name__ == '__main__':
    main()
