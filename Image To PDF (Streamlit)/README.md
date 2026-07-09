# Image to PDF Converter

A simple Streamlit app that converts one or more uploaded images into a single downloadable PDF. Built as a hands-on exercise in Streamlit file handling and UI components.

## Features

- Upload multiple images at once
- Instant preview of the uploaded images
- Combines everything into a single PDF, with one image per page in upload order
- Supports common raster formats (JPG, PNG, BMP, TIFF, etc.) via `img2pdf`
- High-quality output: JPEGs are embedded directly without recompression, preserving original image quality
- One-click download of the generated PDF

## How It Works

1. Upload one or more image files.
2. The app converts them into a single PDF.
3. A preview of the uploaded images is displayed.
4. Click **Download PDF** to save the result as `output.pdf`.

If conversion fails, an error message is shown instead of the preview and download button.

## Requirements

- Python 3.9+ (recommended)
- [Streamlit](https://streamlit.io/) — a recent version, since the app uses Material icon syntax like `:material/download:`
- [img2pdf](https://pypi.org/project/img2pdf/)

## Installation

```bash
git clone <your-repo-url>
cd <your-repo-folder>
pip install -r requirements.txt
```

**requirements.txt**
```
streamlit
img2pdf
```

## Usage

```bash
streamlit run app.py
```
