from PIL import Image
import os

def convert_heic_to_jpeg(heic_file, jpeg_output):
    try:
        img = Image.open(heic_file)
        img.convert("RGB").save(jpeg_output, "JPEG")
        print(f"Converted {heic_file} to {jpeg_output}")
    except Exception as e:
        print(f"Error converting {heic_file}: {str(e)}")

def batch_convert_heic_to_jpeg(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(input_dir, filename)
            jpeg_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".jpeg")
            convert_heic_to_jpeg(heic_path, jpeg_path)

if __name__ == "__main__":
    input_directory = "heic"
    output_directory = "jpeg"
    batch_convert_heic_to_jpeg(input_directory, output_directory)
