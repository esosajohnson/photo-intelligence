import subprocess
import json

photo_path = r"C:\Users\Acer\beauty\IMG_0203.CR3"  # Replace with the actual path to your photo
output_path = r"C:\Users\Acer\Downloads\metadata.json"  # Replace with the desired output path
fields = ["-ISO", "-ShutterSpeedValue", "-ApertureValue", "-FocalLength", "-DateTimeOriginal", "-Model", "-Make", "-LensModel", "-Flash"]

command = ["exiftool", "-j"] + fields + [photo_path]

result = subprocess.run(command, capture_output=True, text=True)

if result.returncode == 0:
    metadata = json.loads(result.stdout)
    with open(output_path, 'w') as f:
        json.dump(metadata, f, indent=4)
    print(f"Metadata extracted and saved to {output_path}")
else:
    print(f"Error extracting metadata: {result.stderr}")