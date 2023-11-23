from pathlib import Path

# Path to the folder that needs to be organized
source_directory = Path("C:")  # Replace with your own path

# Mapping from folder name to file extensions
file_mappings = {
    'Bilder': ['.jpg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Dokumente': ['.docx', '.pdf', '.txt'],
    'Programme': ['.exe', '.msi'],
    'Musik': ['.mp3', '.wav'],
    'ZIP': ['.zip', '.rar']
}

# Create folders if they don't exist
for folder in file_mappings.keys():
    folder_path = source_directory / folder
    folder_path.mkdir(exist_ok=True)  # Create the folder, ignore if it already exists

# Move files to corresponding folders based on their extensions
for file_path in source_directory.iterdir():
    if file_path.is_file():
        moved = False  # To track if the file was moved
        for folder, extensions in file_mappings.items():
            if file_path.suffix.lower() in extensions:
                target_path = source_directory / folder / file_path.name
                if not target_path.exists():
                    file_path.rename(target_path)  # Move the file
                    moved = True  # Mark as moved
                    break  # No need to check other extensions
                else:
                    print(f"File {file_path.name} already exists in the destination folder {folder}.")
        if not moved:
            print("File not categorized: " + file_path.name)

print("Files successfully organized!")
