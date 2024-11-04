import argparse
from PIL import Image
from PIL.ExifTags import TAGS

def print_exif_data(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Extract EXIF data
        exif_data = img._getexif()
        
        if exif_data:
            # Loop through and print each tag
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f"{tag_name}: {value}")
        else:
            print("No EXIF data found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display EXIF metadata from a JPEG image.")
    parser.add_argument("image_path", help="Path to the JPEG image file")

    args = parser.parse_args()
    print_exif_data(args.image_path)