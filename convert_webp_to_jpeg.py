import os
import argparse
from PIL import Image

def convert_webp_to_jpeg(input_dir, output_dir, quality):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.webp'):
            # Load the .webp image
            with Image.open(os.path.join(input_dir, filename)) as img:
                # Save as .jpeg with specified quality
                jpeg_filename = os.path.splitext(filename)[0] + '.jpeg'
                img.convert('RGB').save(
                    os.path.join(output_dir, jpeg_filename), 'JPEG', quality=quality
                )
            print(f"Converted {filename} to {jpeg_filename} with quality={quality}")
        else:
            print(f"Skipping non-webp file: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert .webp images to .jpeg format with specified quality.")
    parser.add_argument("input_dir", help="Directory containing .webp images")
    parser.add_argument("output_dir", help="Directory to save .jpeg images")
    parser.add_argument("-q", "--quality", type=int, default=100, help="JPEG quality (1-100, default is 100)")

    args = parser.parse_args()
    convert_webp_to_jpeg(args.input_dir, args.output_dir, args.quality)