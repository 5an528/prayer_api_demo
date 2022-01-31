import os
import shutil
from pathlib import Path
from datetime import datetime


# Read counter
def read_counter():
    # Read counter
    path = Path(__file__).parent / "counter.txt"
    f = open(path, 'r+')
    data = int(f.read())
    return data


# Read and Update counter
def read_and_update_counter():
    # Read counter
    path = Path(__file__).parent / "counter.txt"
    f = open(path, 'r+')
    data = int(f.read())
    # Update counter
    new_counter = str(data + 1)
    # Write new counter
    f.seek(0)
    f.write(new_counter)
    f.truncate()
    f.close()
    return new_counter


# Read current date
def read_date():
    return str(datetime.today().strftime('%Y-%m-%d'))


# Delete folder and its content except last n number of dirs
def del_dir(num_of_dir, dir_name):
    basedir = Path(__file__).resolve().parent.parent
    dir_name = dir_name
    dir_path = os.path.join(basedir, dir_name)
    dir_list = [os.path.join(dir_path, f) for f in sorted(os.listdir(dir_path))]
    dir_list = dir_list[:len(dir_list) - num_of_dir]
    for folder in dir_list:
        try:
            shutil.rmtree(folder)
        except OSError as e:
            print("Error: %s : %s" % (folder, e.strerror))


# Delete file except last n number of files
def del_file(num_of_file, dir_name):
    basedir = Path(__file__).resolve().parent.parent
    dir_name = dir_name
    dir_path = os.path.join(basedir, dir_name)
    file_list = [os.path.join(dir_path, f) for f in sorted(os.listdir(dir_path))]
    file_list = file_list[:len(file_list) - num_of_file]
    for file in file_list:
        os.remove(file)


# Keep number of directories and files
def keep_reports(number, dir_name, file_dir):
    del_dir(number, dir_name)
    del_file(number, file_dir)
