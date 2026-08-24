# 🔐 Basic Encryption & Decryption

## 📌 Project Overview

This project is developed as part of the **DecodeLabs Cyber Security Internship - Project 2**.

The application demonstrates the fundamentals of **Encryption and Decryption** using the **Caesar Cipher Algorithm**. Users can enter text, choose a shift key, encrypt the message, and decrypt it back to the original form through a modern GUI built with Python and CustomTkinter.

---

## 🎯 Objective

* Understand basic cryptography concepts
* Implement Caesar Cipher Encryption
* Implement Caesar Cipher Decryption
* Create a professional GUI application
* Learn data confidentiality fundamentals

---

## 🛠 Technologies Used

* Python 3.x
* CustomTkinter
* Tkinter
* Caesar Cipher Algorithm

---

## ✨ Features

✅ Encrypt plain text using Caesar Cipher

✅ Decrypt encrypted text

✅ User-defined shift key

✅ Modern Dark-Themed GUI

✅ Copy Result Function

✅ Error Handling

✅ Beginner-Friendly Interface

---

## 📂 Project Structure

```text
CyberSecurity_Project2/
│
├── encryption_gui.py
├── README.md
```

---

## ⚙️ Installation

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

### Step 2: Install Required Library

```bash
pip install customtkinter
```

---

## ▶️ Running the Application

Navigate to the project folder:

```bash
cd "C:\Users\YourName\Desktop\CyberSecurity_Project2"
```

Run the application:

```bash
python encryption_gui.py
```

---

## 🔍 How It Works

### Encryption

Each letter is shifted forward by the specified key.

Example:

```text
Input Text : HELLO
Shift Key : 3

Encrypted Text : KHOOR
```

### Decryption

Each letter is shifted backward by the same key.

Example:

```text
Encrypted Text : KHOOR
Shift Key : 3

Decrypted Text : HELLO
```

---

## 📸 Sample Output

```text
Input:
HELLO WORLD

Shift Key:
3

Output:
KHOOR ZRUOG
```

---

## 🔐 Caesar Cipher Formula

Encryption:

```text
E(x) = (x + n) mod 26
```

Decryption:

```text
D(x) = (x - n) mod 26
```

Where:

* x = Alphabet Position
* n = Shift Key

---

## 📚 Learning Outcomes

After completing this project, you will understand:

* Basic Cryptography Concepts
* Encryption Techniques
* Decryption Techniques
* Data Protection Fundamentals
* GUI Development using Python

---

## 👨‍💻 Author

**Pranav Auti**

Cyber Security Intern

DecodeLabs Internship Program

---

## 📄 License

This project is created for educational and internship learning purposes only.
