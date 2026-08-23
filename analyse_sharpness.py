import subprocess
import cv2
import numpy as np

image_path = r"D:\15.08\IMG_0749.CR3"  # Replace with the actual path to your image

def extract_preview_bytes(image_path):
    command = ["exiftool", "-b","-PreviewImage", str(image_path)]
    result = subprocess.run(command, capture_output=True)
    if result.returncode == 0:
        return result.stdout
    else:
        print(f"Error extracting preview image: {result.stderr.decode()}")
        return None

def main():
    preview_bytes = extract_preview_bytes(image_path)
    if preview_bytes is not None:
        # Convert bytes to a NumPy array
        nparr = np.frombuffer(preview_bytes, np.uint8)
        # Decode the image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is not None:
            # Display the image
            cv2.imshow("Preview Image", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Failed to decode the image.")
    else:
        print("No preview image found.")

if __name__ == "__main__":
    main()