import os
import shutil
from pathlib import Path
from collections import Counter

def get_category(extension):
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
        'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.wmv', '.flv', '.webm'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.ppt', '.pptx', '.csv', '.rtf', '.odt'],
        'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'],
        'Compressed': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        'Executables': ['.exe', '.msi', '.bat', '.sh'],
        'Code': ['.py', '.java', '.cpp', '.c', '.js', '.html', '.css', '.json', '.xml']
    }
    
    ext = extension.lower()
    for category, extensions in categories.items():
        if ext in extensions:
            return category
    return 'Others'

def get_unique_filename(destination_folder, filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    destination_path = os.path.join(destination_folder, new_filename)
    
    while os.path.exists(destination_path):
        new_filename = f"{base} ({counter}){extension}"
        destination_path = os.path.join(destination_folder, new_filename)
        counter += 1
        
    return new_filename

def organize_downloads(target_dir):
    target_path = Path(target_dir)
    
    if not target_path.exists():
        print(f"Directory not found: {target_dir}")
        return

    messages = []
    messages.append(f"Organizing files in: {target_dir}")
    
    stats = Counter()

    for item in target_path.iterdir():
        if item.is_dir():
            continue
            
        if item.name.startswith('.'): # Skip hidden files
            continue

        category = get_category(item.suffix)
        destination_folder = target_path / category
        
        # Create category folder if it doesn't exist
        destination_folder.mkdir(exist_ok=True)
        
        # Handle duplicate filenames
        new_filename = get_unique_filename(destination_folder, item.name)
        destination_path = destination_folder / new_filename
        
        try:
            shutil.move(str(item), str(destination_path))
            stats[category] += 1
            messages.append(f"Moved: {item.name} -> {category}/{new_filename}")
        except Exception as e:
            messages.append(f"Error moving {item.name}: {e}")

    messages.append("\nOrganization Complete!")
    messages.append("Summary:")
    for category, count in stats.items():
        messages.append(f"  {category}: {count} files")
        
    return "\n".join(messages)

if __name__ == "__main__":
    # For testing purposes, we can set the default directory here or ask for input
    # In a real scenario, this might default to the user's Downloads folder
    # directory_to_organize = os.path.expanduser("~/Downloads")
    
    # Using a customizable path for safety/testing
    import sys
    if len(sys.argv) > 1:
        target_directory = sys.argv[1]
    else:
        # Default to current directory if not specified, or prompt
        target_directory = input("Enter the path to the folder you want to organize: ")

    result = organize_downloads(target_directory)
    print(result)
