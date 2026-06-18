# 🔲 QR Code Generator

A lightweight Python script that generates a QR code from any URL or text string and saves it as a PNG image.

---

## Features

- Accepts any URL or plain text as input
- Customizable output file name
- Saves QR code as a `.png` image
- Defaults to `QRCode.png` if no file name is provided
- Clean black-on-white QR code output

---

## Requirements

- Python 3.x
- `qrcode` library
- `Pillow` library (required by `qrcode` for image generation)

Install dependencies with:

```bash
pip install qrcode
pip install Pillow
```

---

## Usage

Run the script from your terminal:

```bash
python main.py
```

You will be prompted for two inputs:

```
Enter a URL or a string : https://example.com
Set your desired file name : my_qr
```

The QR code will be saved as `my_qr.png` in the current directory.

### Default

Only the file name has a default. The URL/string input is **required** — leaving it blank will generate an empty QR code.

| Prompt | Default Value |
|---|---|
| URL / String | *(none — input required)* |
| File name | `QRCode` (saved as `QRCode.png`) |

---

## Configuration

The QR code is generated with the following settings (editable in the script):

| Parameter | Value | Description |
|---|---|---|
| `version` | `4` | Controls the size of the QR matrix (1–40) |
| `error_correction` | `ERROR_CORRECT_L` | ~7% of data can be restored if damaged |
| `box_size` | `10` | Pixels per box/module |
| `border` | `1` | Width of the quiet zone in boxes |
| `fill_color` | `black` | Foreground (module) color |
| `back_color` | `white` | Background color |

---

## Example Output

Running the script with `https://github.com` and file name `github` produces a file named `github.png` — a scannable QR code pointing to that URL.

---

## Project Structure

```
.
├── main.py           # Main script
└── README.md         # This file
```

---

## License

This project is open source and free to use under the [MIT License](https://opensource.org/licenses/MIT).
