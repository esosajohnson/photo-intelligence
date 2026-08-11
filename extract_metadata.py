import subprocess
import json
import pandas as pd
from pathlib import Path

def find_photos(folder):
    photos = list(folder.rglob("*.CR3"))
    return photos

def extract_metadata(photos):
    fields = ["-ISO", "-ShutterSpeedValue", "-ApertureValue", "-FocalLength", "-DateTimeOriginal", "-Model", "-Make", "-LensModel", "-Flash"]
    photo_paths_as_str = [str(photo) for photo in photos]
    command = ["exiftool", "-j"] + fields + photo_paths_as_str
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        metadata = pd.DataFrame(json.loads(result.stdout))
        return metadata
    else:
        print(f"Error extracting metadata: {result.stderr}")
        return None
    
def save_metadata_to_csv(metadata, output_path):
    metadata.to_csv(output_path, index=False)
    print(f"Metadata extracted and saved to {output_path}")

def main():
    output_path = r"C:\Users\Acer\Downloads\metadata.csv"  # Replace with the desired output path
    folder = Path(r"C:\Users\Acer\beauty")  # Replace with the actual path to your folder
    photos = find_photos(folder)
    metadata = extract_metadata(photos)
    
    if not photos:
        print("No photos found in the specified folder.")
        return
    
    if metadata is not None:
        save_metadata_to_csv(metadata, output_path)

if __name__ == "__main__":
    main()