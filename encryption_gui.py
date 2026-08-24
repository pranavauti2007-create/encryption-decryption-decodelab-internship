# encryption_gui.py

import customtkinter as ctk
from tkinter import messagebox

# -------------------------
# App Theme
# -------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# -------------------------
# Caesar Cipher Functions
# -------------------------
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char
    return result

# -------------------------
# Button Functions
# -------------------------
def encrypt_text():
    try:
        text = input_box.get("1.0", "end").strip()
        shift = int(shift_entry.get())

        encrypted = encrypt(text, shift)

        output_box.delete("1.0", "end")
        output_box.insert("end", encrypted)

        status_label.configure(text="✅ Encryption Successful")

    except:
        messagebox.showerror("Error", "Please enter a valid shift key.")

def decrypt_text():
    try:
        text = input_box.get("1.0", "end").strip()
        shift = int(shift_entry.get())

        decrypted = decrypt(text, shift)

        output_box.delete("1.0", "end")
        output_box.insert("end", decrypted)

        status_label.configure(text="✅ Decryption Successful")

    except:
        messagebox.showerror("Error", "Please enter a valid shift key.")

def copy_result():
    text = output_box.get("1.0", "end").strip()
    app.clipboard_clear()
    app.clipboard_append(text)

    status_label.configure(text="📋 Result Copied")

# -------------------------
# Main Window
# -------------------------
app = ctk.CTk()
app.title("Cyber Security Project 2")
app.geometry("900x650")
app.resizable(False, False)

# Header
title = ctk.CTkLabel(
    app,
    text="🔐 BASIC ENCRYPTION & DECRYPTION",
    font=("Segoe UI", 28, "bold")
)
title.pack(pady=20)

subtitle = ctk.CTkLabel(
    app,
    text="DecodeLabs Cyber Security Internship Project",
    font=("Segoe UI", 14)
)
subtitle.pack()

# Main Frame
frame = ctk.CTkFrame(app, corner_radius=20)
frame.pack(padx=30, pady=25, fill="both", expand=True)

# Input Label
input_label = ctk.CTkLabel(
    frame,
    text="Enter Your Message",
    font=("Segoe UI", 18, "bold")
)
input_label.pack(pady=(20, 10))

# Input Box
input_box = ctk.CTkTextbox(
    frame,
    width=700,
    height=120,
    font=("Consolas", 15)
)
input_box.pack()

# Shift Key
shift_label = ctk.CTkLabel(
    frame,
    text="Shift Key",
    font=("Segoe UI", 16)
)
shift_label.pack(pady=(20, 5))

shift_entry = ctk.CTkEntry(
    frame,
    width=180,
    height=40,
    placeholder_text="Enter Key"
)
shift_entry.pack()

# Buttons Frame
button_frame = ctk.CTkFrame(frame, fg_color="transparent")
button_frame.pack(pady=25)

encrypt_btn = ctk.CTkButton(
    button_frame,
    text="🔒 Encrypt",
    width=180,
    height=45,
    command=encrypt_text
)
encrypt_btn.pack(side="left", padx=10)

decrypt_btn = ctk.CTkButton(
    button_frame,
    text="🔓 Decrypt",
    width=180,
    height=45,
    command=decrypt_text
)
decrypt_btn.pack(side="left", padx=10)

copy_btn = ctk.CTkButton(
    button_frame,
    text="📋 Copy Result",
    width=180,
    height=45,
    command=copy_result
)
copy_btn.pack(side="left", padx=10)

# Output Label
output_label = ctk.CTkLabel(
    frame,
    text="Result",
    font=("Segoe UI", 18, "bold")
)
output_label.pack(pady=(15, 10))

# Output Box
output_box = ctk.CTkTextbox(
    frame,
    width=700,
    height=120,
    font=("Consolas", 15)
)
output_box.pack()

# Status Bar
status_label = ctk.CTkLabel(
    app,
    text="Ready...",
    font=("Segoe UI", 13)
)
status_label.pack(pady=10)

app.mainloop()