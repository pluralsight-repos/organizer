import os
import shutil

# Path of the desktop folder
desktop_path = os.path.expanduser("~\OneDrive\Desktop")

# Dictionary containig the folder names and their corresponding file extensions
folders = {
    "Images": [".jpeg", ".jpg", ".png", ".gif"],
    "Documents": [".doc", ".docx", ".pdf", ".txt"],
    "Archives": [".zip", ".rar"]
}

# Create the subfolders if they don't exist
for folder_name in folders:
    folder_path = os.path.join(desktop_path, folder_name)
    # print('Folder_path:', folder_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to the corresponding subfolder
for file_name in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, file_name)
    # print("adasdasd", file_path)
    if os.path.isfile(file_path):
        for folder_name, extensions in folders.items():
            for extension in extensions:
                if file_name.endswith(extension):
                    destination_folder = os.path.join(desktop_path, folder_name)
                    print(file_path, destination_folder)
                    shutil.move(file_path, destination_folder)

