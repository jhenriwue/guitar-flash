# Guitar Flash Special Bot

This repository contains a Python script that implements a bot to automatically activate the **Special** in Guitar Flash-like games. It uses screen capture, text recognition (OCR) with Tesseract, and keyboard automation to detect and press the special key at the right time.

---

## ⚙️ Features

- Automatically detects the special notes counter on the game screen.
- Activates the Special by pressing a specific key (`SPACE` by default) when the counter reaches predefined values.
- Uses libraries like `cv2`, `pytesseract`, `pynput`, and `mss` for efficient screen analysis and keyboard automation.

---

## 🛠 Requirements

Make sure you have the following dependencies installed:

- Python 3.7+
- Required Python libraries:
  - `cv2` (OpenCV)
  - `numpy`
  - `mss`
  - `pytesseract`
  - `pynput`
  - `Pillow`
- Tesseract OCR installed and configured in your system.

---

## 🚀 Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/jhenriwue/guitar-flash.git
   cd guitar-flash
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Adjust the Monitor measures

4. Run the script:
    ```bash
   python guitar_flash.py
   ```

## ⚙️ Configuration

### Special Key
The default special key is set to `SPACE`. You can change this by modifying the `SPECIAL_KEY` variable in the script:

```python
SPECIAL_KEY = ' '  # Key to activate the special
```


### Note Thresholds

The bot triggers the special key when the counter matches the values in `NOTAS_ESPECIAL`. Customize these values as needed:

```python
NOTAS_ESPECIAL = [186, 274, 410, 669]  # Counter thresholds for special activation
```

### Screen Area

Adjust the `monitor` dictionary to match the area of the game window you want to capture:

```python
monitor = {"top": 100, "left": 100, "width": 500, "height": 400}
```

## 🖥 Dependencies Installation

### Install Tesseract OCR

#### On Linux (Ubuntu/Debian):
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```
#### On Windows:
1. Download and install Tesseract from the [official website](https://github.com/tesseract-ocr/tesseract).
2. After installation, make sure to add Tesseract's path to the `PATH` environment variable.

## ⚠️ Notes

- Ensure the game screen is fully visible and the counter area is not obscured for the OCR to work effectively.
- Adjust the `x_inicial`, `y_inicial`, `largura`, and `altura` variables if the counter's position differs on your screen.

---

## 🚀 Upcoming Features

### 1. **Dynamic Special Notes Detection**
- Automatically fetch the special notes thresholds from the website [Guitar Flash Special Notes](https://pathsguitarflash.wixsite.com/my-site-3) based on the song and difficulty level displayed on the game screen.
- Dynamically adjust the `NOTAS_ESPECIAL` array for precise gameplay automation.

### 2. **Error Handling for Missed Notes**
- Implement logic to handle scenarios where the player misses a note, causing the counter to reset.
- Ensure the bot recalibrates and continues tracking the new counter value without interruptions or incorrect triggers.

Stay tuned for updates and new functionalities!

## 💬 Contact

For any questions or suggestions, please contact [joao.ramalho@ccc.ufcg.edu.br].

