import subprocess
import cv2
import numpy as np
from pathlib import Path

folder = Path(r"D:\leamington 04.07")

def extract_preview_bytes(image_path):
    command = ["exiftool", "-b","-PreviewImage", str(image_path)]
    result = subprocess.run(command, capture_output=True)
    if result.returncode == 0:
        return result.stdout
    else:
        print(f"Error extracting preview image: {result.stderr.decode()}")
        return None
    
def compute_sharpness(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Compute the Laplacian
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    # Compute the variance
    variance = laplacian.var()
    return variance

def main():
    for image_path in folder.rglob("*.CR3"):
        print(f"Processing image: {image_path}")
        preview_bytes = extract_preview_bytes(image_path)
        
        if preview_bytes is not None:
            # Convert bytes to a NumPy array
            nparr = np.frombuffer(preview_bytes, np.uint8)
            # Decode the image
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if img is not None:
                sharpness = compute_sharpness(img)
                print(f"Sharpness: {sharpness}")
            else:
                print("Failed to decode the image.")
        else:
            print("No preview image found.")

if __name__ == "__main__":
    main()