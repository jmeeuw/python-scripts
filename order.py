from os import listdir
from os.path import isfile, join
import os
import shutil

try:
    def sort_files_in_a_folder(mypath):
        files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        file_type_variation_list = []
        filetype_folder_dict = {}
        for file in files:
            filetype = os.path.splitext(file)[1][1:].strip().lower()
            if filetype not in file_type_variation_list and filetype != '':
                file_type_variation_list.append(filetype)
                new_folder_name = mypath+'/' + filetype + '_folder'
                filetype_folder_dict[str(filetype)] = str(new_folder_name)
                if os.path.isdir(new_folder_name) == True or filetype == '':  # folder exists
                    continue
                else:
                    os.mkdir(new_folder_name)
        for file in files:
            src_path = mypath+'/'+file
            filetype = os.path.splitext(file)[1][1:].strip().lower()
            if filetype in filetype_folder_dict.keys() and filetype != '':
                dest_path = filetype_folder_dict[str(filetype)]
                shutil.move(src_path, dest_path)
except:
    print("Error, most likely 2 files with the same name on the same location")

if __name__ == "__main__":
    home = os.path.expanduser("~")
    mypath = os.path.join(home, "Downloads")
    sort_files_in_a_folder(mypath)
