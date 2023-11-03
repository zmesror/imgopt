import argparse
import os
import sys
import tinify
import shutil
from typing import Iterator

from config import load_config


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder", help="directory containing the original images")
    parser.add_argument(
        "-o", "--output-folder", help="directory to save converted images"
    )
    parser.add_argument("-O", "--overwrite-output", help="overwrite the output folder")
    args = parser.parse_args()

    # Create output directory
    if args.overwrite_output:
        output_folder = args.overwrite_output
        if os.path.exists(output_folder):
            shutil.rmtree(output_folder)
    else:
        output_folder = args.output_folder or "output_images"

    os.makedirs(output_folder, exist_ok=True)

    validate_folder(output_folder)
    validate_folder(args.input_folder)

    # Reduce the size of the images in the input folder
    tinify.key = load_api_key()
    convert_images(args.input_folder, output_folder)


def validate_folder(folder: str) -> None:
    if not os.path.exists(folder):
        sys.exit(f"{folder} does not exist.")
    if not os.path.isdir(folder):
        sys.exit(f"{folder} is not a directory.")


def load_api_key() -> str:
    config = load_config()
    api_key = config.get("api_key")
    if api_key is None:
        raise ValueError("API key is not specified in the configuration file")
    return api_key


def get_images(input_folder: str) -> Iterator[str]:
    image_extensions = (".png", ".jpg", ".jpeg")

    return filter(
        lambda file: file.lower().endswith(image_extensions), os.listdir(input_folder)
    )


def convert_images(input_folder: str, output_folder: str) -> None:
    images = list(get_images(input_folder))
    for image in images:
        name, _ = image.rsplit(".", 1)
        src_path = os.path.join(input_folder, image)
        dst_path = os.path.join(output_folder, name)
        convert(src_path, dst_path)


def convert(src: str, dst: str):
    try:
        source = tinify.from_file(src)
        converted = source.convert(type=["image/webp"])
        extension = converted.result().extension
        converted.to_file(dst + "." + extension)
    except tinify.Error as e:
        sys.exit(f"An error occured: {e}")


if __name__ == "__main__":
    main()
