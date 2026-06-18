# 🖼️ Wallpaper Viewer

A simple Tkinter desktop app that loads every image from a local `Wallpapers` folder and lets you cycle through them one at a time with a "Next" button.

> Note: despite the name, this doesn't set your OS desktop background — it's a standalone viewer window for browsing through a folder of images.

---

## ✨ Features

- Loads all images from a `Wallpapers` folder at startup
- Displays them in a fixed-size window (340x550)
- "Next" button cycles forward through the images, looping back to the first after the last

---

## 🛠️ Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) (`PIL`) — used for opening and resizing images

Install Pillow with:

```bash
pip install Pillow
```

Tkinter ships with most standard Python installations, so no separate install is usually needed.

---

## 📂 Folder Structure

Before running the script, create a `Wallpapers` folder in the same directory as the script and add your images to it:

```
Wallpaper Viewer/
├── main.py
└── Wallpapers/
    ├── image1.jpg
    ├── image2.png
    └── ...
```

The script reads images directly from this folder using a relative path, so it must be run from inside the `Wallpaper Viewer` directory.

---

## 🚀 Usage

1. Make sure the `Wallpapers` folder exists alongside the script and contains at least one image
2. Run the script:

```bash
python main.py
```

3. Click **Next** to cycle through the images in the folder

---

## 📝 Notes

- Images are resized to 300x450 to fit the window
- The image order depends on `os.listdir()`, which is not guaranteed to be alphabetical or consistent across operating systems
- Supported image formats are whatever Pillow's `Image.open()` can read (JPEG, PNG, BMP, GIF, etc.)