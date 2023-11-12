import shutil
import os

device_source = "C:/Users/Ayush"

from_dir = device_source + "Desktop" if device_source.endswith("/") else device_source + "/Desktop"
to_dir = device_source + "Pictures" if device_source.endswith("/") else device_source + "/Pictures"

all_files = os.listdir(from_dir)
print(all_files)

for file in all_files:
    file_name, ext = os.path.splitext(file)
    can_file_move = False

    available_ext = [".exe", ".png", ".jpeg", ".jpg", ".gif", ".zip", ".doc", ".docx", ".xlsx", ".ppt", ".mp4", ".mp3", ".pdf"]

    if (ext == ""):
        continue
    else:
        for exte in available_ext:
            if (exte == ext):
                can_file_move = True
                break
            else:
                continue

    if (can_file_move):
        src_path = from_dir + "/" + file
        dest_folder = to_dir + "/" + ext.removeprefix(".") + "_files"
        dest_path = dest_folder + "/" + file

        if os.path.exists(dest_folder):
            print("Moving " + file_name + " ...")

            shutil.move(src_path, dest_path)
        else:
            os.makedirs(dest_folder)

            print("Moving " + file_name + " ...")

            shutil.move(src_path, dest_path)
