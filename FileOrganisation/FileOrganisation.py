import os

# Path to the folder that needs to be organized
source_directory = r"C:\" # Replace with your own path

# Mapping from folder name to file extensions
file_mappings = {
    'Pictures': ['.jpg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Documents': ['.docx', '.pdf', '.txt'],
    'Programs': ['.exe', '.msi'],
    'Music': ['.mp3', '.wav'],
    'ZIP': ['.zip', '.rar']
}

# Create folders if they don't exist
for folder in file_mappings.keys():
    folder_path = os.path.join(source_directory, folder)
    # Check if the folder exists, if not, create it
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# Move files to corresponding folders based on their extensions
for filename in os.listdir(source_directory):
    # Check if it's a file and not a directory
    if os.path.isfile(os.path.join(source_directory, filename)):
        moved = False  # To track if the file was moved
        # Go through the mapping to find where to move the file
        for folder, extensions in file_mappings.items():
            # If the file ends with a known extension, move it
            if filename.lower().endswith(tuple(extensions)):
                try:
                    # Attempt to move the file
                    os.rename(os.path.join(source_directory, filename),
                              os.path.join(source_directory, folder, filename))
                    moved = True  # Indicate success
                    break  # No need to check other extensions
                except FileExistsError as e:
                    # If file already exists in the target folder, print an error message
                    print(f"File {filename} already exists in the destination folder {folder}.")
                except Exception as e:
                    # For any other exceptions, print an error message
                    print(f"Error moving {filename}: {e}")
        # If file didn't fit any category, print a message
        if not moved:
            print("File not categorized: " + filename)

# Confirmation message that the process is complete
print("Files successfully organized!")