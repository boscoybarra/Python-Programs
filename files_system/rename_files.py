import os

def rename_files():
    # 1 get file name from a folder
    file_list = os.listdir("/Users/$USER/Desktop/prank/")

    # print(file_list)

    # 1.1 Check our current working directory
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)

    # Change directory folder
    os.chdir("/Users/$USER/Desktop/prank/")

    # 2 for each file name, rename filename
    for file_name in file_list:
        translation_table = str.maketrans("0123456789", "          ", "0123456789")

        # Print in the console the New and Old Names
        print("Old Name File - " +file_name)
        print("New Name File - " +file_name.translate(translation_table))
        os.rename(file_name, file_name.translate(translation_table))
    # We change the path back to where we find it before applying chdir
    os.chdir(saved_path)

# Execute Function
rename_files()
