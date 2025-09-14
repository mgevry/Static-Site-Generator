import os
import shutil

def copy_files_recursive(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    source_dir_list = os.listdir(source_dir)
    for entry in source_dir_list:
        source_file_path = os.path.join(source_dir, entry)
        dest_file_path = os.path.join(dest_dir, entry)
        print(f"* {source_file_path} -> {dest_file_path}")
        if os.path.isfile(source_file_path):
            shutil.copy(source_file_path, dest_file_path)
        else:
            copy_files_recursive(source_file_path, dest_file_path)