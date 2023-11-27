# tifftojpg
# TIFF to JPEG Converter

This Python script is designed to efficiently convert TIFF image files to the JPEG format. It simplifies the conversion process for users who require a batch conversion of TIFF images within a specified directory.

## About

The primary goal of this script is to offer a straightforward solution for converting multiple TIFF files to JPEG format. By utilizing OpenCV, the script streamlines the conversion process, ensuring ease of use and reliability.

## Features

- Batch conversion of TIFF files to JPEG format.
- Simple configuration by defining input and output directories within the script.
- Utilizes the OpenCV library for image processing and conversion.
- Handles filename conflicts by modifying the output file names for clarity.

## Usage

1. Ensure Python is installed on your system.
2. Install necessary libraries using the following command in the terminal or command prompt:

    ```bash
    pip install opencv-python-headless
    ```

3. Edit the `tifftojpg.py` file to define the input and output directories.

4. Run the script:

    ```bash
    python tifftojpg.py
    ```

    - This will process TIFF files in the input directory and save converted JPEG files to the output directory.

## Contributions

Contributions to improve and expand the functionality of this script are welcome. If you wish to contribute:

1. Fork the repository.
2. Make your changes or enhancements.
3. Create a pull request outlining the modifications made.

## License

This project is licensed under the [MIT License](LICENSE). Refer to the License file for detailed information.

