import subprocess
import json
import pandas as pd
from pathlib import Path

output_path = r"C:\Users\Acer\Downloads\metadata.csv"  # Replace with the desired output path
fields = ["-ISO", "-ShutterSpeedValue", "-ApertureValue", "-FocalLength", "-DateTimeOriginal", "-Model", "-Make", "-LensModel", "-Flash"]
folder = Path(r"C:\Users\Acer\beauty")  # Replace with the actual path to your folder

photos = list(folder.rglob("*.CR3"))

photo_paths_as_str = [str(photo) for photo in photos]
command = ["exiftool", "-j"] + fields + photo_paths_as_str
result = subprocess.run(command, capture_output=True, text=True)
    
if result.returncode == 0:
    metadata = pd.DataFrame(json.loads(result.stdout))
    metadata.to_csv(output_path, index=False)
    print(f"Metadata extracted and saved to {output_path}")
else:
    print(f"Error extracting metadata: {result.stderr}")