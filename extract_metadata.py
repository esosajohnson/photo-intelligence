import subprocess
import json
import pandas as pd
from pathlib import Path
import argparse

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
    parser = argparse.ArgumentParser(description="Extract metadata from photos and save to CSV.")
    parser.add_argument("folder", type=str, help="Path to the folder containing photos.")
    parser.add_argument("--output", type=str, default="photo_dataset.csv", help="Output CSV file name.")
    args = parser.parse_args()
    
    folder = Path(args.folder)
    output_path = Path(args.output)
    photos = find_photos(folder)
    
    if not photos:
        print("No photos found in the specified folder.")
        return
    
    metadata = extract_metadata(photos)
    
    if metadata is not None:
        save_metadata_to_csv(metadata, output_path)

if __name__ == "__main__":
    main()