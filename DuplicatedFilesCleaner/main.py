import os

def clean_duplicated(path):

    duplicated_files = {}
    for root,directories, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root,file)
            file_size = os.path.getsize(file_path)
            if file_size > 0:
                try:
                    if file_size in duplicated_files.keys():
                        print(file_path)
                        decision = input("Type yes to exclude file:\n")
                        if (decision == "yes"):
                            os.remove(file_path)
                        continue
                    else:
                        duplicated_files[file_size] = file_path
                except:
                    continue

if __name__ == "__main__":
    path = input("Enter the folder path:\n")
    clean_duplicated(path)
