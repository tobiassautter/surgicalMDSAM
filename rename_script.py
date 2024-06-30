import os

seq_arr = [1, 3, 4, 6, 7, 10, 11, 12, 13, 14, 16]
for i in range(1, 41):
    for j in seq_arr:
        # Define the folder path
        folder_path = "data/endovis_2018/train/"+ str(i) +"/sam_features_h/seq" + str(j)
        print("In " + folder_path)
        # Iterate over all files in the folder
        for filename in os.listdir(folder_path):
            # Check if the filename contains the redundant "npy"
            if "npy" in filename:
                # Create the new filename by removing the redundant "npy"
                new_filename = filename.replace("npy", "")
                
                # Get the full path to the old and new filenames
                old_file = os.path.join(folder_path, filename)
                new_file = os.path.join(folder_path, new_filename)
                
                # Rename the file
                os.rename(old_file, new_file)

        print("Renaming complete.")
