# Calculator-App
A clean, responsive Android Calculator App built using Python &amp; Kivy, designed specifically for mobile phone screens. This app provides a smooth, full-screen calculator experience with essential arithmetic operations and proper bracket handling — packaged as an APK using Buildozer.
---

# 📱 **Kivy Calculator App (Android Phone Calculator)**

A clean, responsive **Android Calculator App** built using **Python & Kivy**, designed specifically for **mobile phone screens**.
This app provides a smooth, full-screen calculator experience with essential arithmetic operations and proper bracket handling — packaged as an **APK using Buildozer**.

---

## ✨ **Features**

* ➕ Basic arithmetic operations (+, −, ×, ÷)
* 🔢 Bracket support `( )` for complex expressions
* 🧹 **AC** (All Clear) & **DEL** (Delete last digit)
* 📱 Fully **phone-size responsive layout**
* 🖐 Accurate touch input (no button mismatch)
* 🧮 Real-time expression evaluation
* 🚀 Android APK ready
* 💻 Cross-platform development (Ubuntu / WSL)

---

## 🎮 **Calculator Controls**

| Button      | Action                |
| ----------- | --------------------- |
| **0–9**     | Number input          |
| **+ − × ÷** | Arithmetic operations |
| **( )**     | Group expressions     |
| **DEL**     | Delete last character |
| **AC**      | Clear all input       |
| **=**       | Calculate result      |

---

## 🛠 **Tech Stack**

* **Python 3.x**
* **Kivy** → UI & touch handling
* **Buildozer** → Android APK packaging
* **Android SDK / NDK**

---

## 📦 **Installation (Development)**

### 1️⃣ Clone Repository

```bash
git clone https://github.com/codertheashish/kivy-calculator-app.git
cd kivy-calculator-app
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python3 -m venv kivy-env
source kivy-env/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install kivy buildozer
```

---

## ▶️ **Run on Desktop (Preview Only)**

```bash
python main.py
```

⚠️ Desktop view is only for logic testing —
📱 **Real phone size appears only in APK**

---

## 📱 **Build Android APK**

```bash
buildozer android debug
```

APK will be generated in:

```
bin/calculator-0.1-arm64-v8a-debug.apk
```

---

## 📲 **Install on Phone**

1. Copy APK to phone (USB / WhatsApp / Drive)
2. Enable **Install unknown apps**
3. Tap APK → Install → Open

---

## 🤖 **How the App Works**

1. Kivy layouts (`BoxLayout`, `GridLayout`) auto-scale to phone screen
2. Buttons use `size_hint` + `dp/sp` for DPI-safe touch handling
3. User input is built as a mathematical expression
4. Expression is evaluated on `=` press
5. Result is displayed instantly in the top display panel

---

## 🌟 **Future Enhancements**

* 🌙 Dark / Light mode
* 🧪 Scientific calculator functions
* 📐 History panel
* 🎨 Google Calculator–style UI
* 🏪 Play Store release build

---

## 📜 **License**

Released under the **MIT License** — free to use, modify, and distribute.

---

## 👨‍💻 **Author**

**Ashish Kumar Prajapati**
Python | Kivy | Android | AI & Computer Vision

---
