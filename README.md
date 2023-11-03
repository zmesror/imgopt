# Web Image Optimization with TinyPNG API

## Overview

This Python script automates the process of optimizing images for the web using the TinyPNG API. It's a simple yet powerful tool to reduce image file sizes for faster web page loading and improved user experience.

## Features

- **Automatic Image Optimization:** The script scans a specified directory, identifies image files, and optimizes them using the TinyPNG API.
- **Output Customization:** You can specify the output directory for the optimized images or use default settings.
- **Error Handling:** The script handles errors and provides informative error messages in case of issues with image optimization.
- **API Key Management:** Easily manage your TinyPNG API key for seamless integration.

## Prerequisites

- **Python:** This script requires Python to run.
- **TinyPNG API Key:** You need to obtain an API key from TinyPNG.

## Installation

1. Clone or download the repository to your local machine.
2. Install tinify :

   ```bash
   pip install --upgrade tinify
   ```
# Usage

Create a Configuration File `config.json` and Add Your TinyPNG API Key

```json
{
    "api_key": "YOUR_API_KEY"
}
```

To use this script, you can specify the output folder and optional flags for overwriting the output folder.

- `input-folder`: Directory containing the original images.
- `-o` or `--output-folder`: Directory to save converted images.
- `-O` or `--overwrite-output`: Overwrite the output folder if it already exists.

Here's an example of how to run the script:

```bash
python imgopt.py input_folder -o output_folder
```
