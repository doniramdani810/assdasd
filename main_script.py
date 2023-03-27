import requests
import win32api
import win32gui
import win32con
import win32console
import psutil
import getpass
import os

# Menutup program "libEGL.exe"
for proc in psutil.process_iter(['name']):
    if proc.info['name'] == 'libEGL.exe':
        proc.kill()

# Menutup program "Psiphon 3"
handle = win32gui.FindWindow(None, 'Psiphon 3')
if handle:
    win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)

# Memeriksa koneksi internet dan menampilkan pesan jika tidak tersedia
try:
    requests.get('https://www.google.com', timeout=5)
except requests.exceptions.RequestException:
    win32api.MessageBox(
        win32gui.GetForegroundWindow(),
        'Tidak ada koneksi internet. Pastikan koneksi internet Anda tersedia.',
        'Status Koneksi'
    )

import urllib.request
import platform
import requests
import wmi
import uuid
from tkinter import messagebox    
import tkinter as tk
from tkinter import *
from tkinter import ttk        
import webbrowser
import datetime
import json
from datetime import datetime
import tkinter.messagebox as messagebox
import pystray
from PIL import Image
from PIL import ImageTk, Image
import urllib.request
from tkinter.ttk import Combobox
from tkinter import filedialog
import os
import pywhatkit as kit
import pywhatkit as pwk
import string
import random
import urllib.request
import subprocess
import threading
import time
import dns.resolver
import socket
import ipaddress
import time
import subprocess
import pyautogui
from PIL import ImageGrab
import keyboard
import cv2
import numpy as np
import glob
import pytesseract
import mss
import urllib.request
import random
import signal
import sys
import math

c = wmi.WMI()
mac_addresses = [adapter.MACAddress for adapter in c.Win32_NetworkAdapterConfiguration(IPEnabled=True)]

# Konfigurasi autentikasi GitHub
username = "doniramdani810"
access_token = "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"
gist_id = "c5e3168ca282ed14fc5a763423cea8d7"

# Membuat payload untuk mengupdate file pada Gist
payload = {
    "files": {
        "mac_addresses.txt": {
            "content": "\n".join(mac_addresses).lower()
        }
    }
}

# Mengirimkan data ke API GitHub Gist
url = f"https://api.github.com/gists/{gist_id}"
response = requests.patch(
    url,
    auth=(username, access_token),
    json=payload
)

if response.status_code == 200:
    print("Data berhasil dikirim ke Gist.")
else:
    print(f"Gagal mengirim data ke Gist. Kode status: {response.status_code}")

def is_virtual_environment():
    if platform.system() == 'Linux':
        with open('/proc/cpuinfo', 'r') as f:
            cpuinfo = f.read()
        if 'hypervisor' in cpuinfo or 'kvm' in cpuinfo:
            return True
    elif platform.system() == 'Windows':
        import wmi
        c = wmi.WMI()
        for os in c.Win32_OperatingSystem():
            if 'Virtual' in os.Caption:
                return True
    return False

# memeriksa apakah sedang berjalan di dalam virtual machine
if is_virtual_environment():
    print("Skrip tidak dapat dijalankan di dalam mesin virtual!")
    exit()
else:
    # jalankan kode utama di sini
    print("Skrip dijalankan di komputer fisik.")

root = Tk()
root.title("Captcha kings 0.0.4")
root.geometry("650x500+300+50")
root.resizable(False, False)
root.configure(bg="#f8f9fa")
root.iconbitmap("icon.ico")

def signal_handler(signal, frame):
    print('Aplikasi berhenti dengan sinyal SIGTERM')
    # Menutup program "libEGL.exe"
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'libEGL.exe':
            proc.kill()
    # Menutup program "Psiphon 3"
    handle = win32gui.FindWindow(None, 'Psiphon 3')
    if handle:
        win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_handler)

def close_captcha():
    # Menutup program "libEGL.exe"
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'libEGL.exe':
            proc.kill()
    # Menutup program "Psiphon 3"
    handle = win32gui.FindWindow(None, 'Psiphon 3')
    if handle:
        win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)

def close_root_window():
    close_captcha()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close_root_window)

def get_id_info(id_value):
    url = "https://bitbucket.org/don-kgs/v04/raw/master/data.json"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        return any(user["id"] == id_value for user in data["users"])

# membuat fungsi saat mouse berada di atas tab
def enter(e):
    e.widget.config(bg="#343a40", fg="#ffffff")

# membuat fungsi saat mouse tidak berada di atas tab
def leave(e):
    e.widget.config(bg="#f8f9fa", fg="#343a40")

# membuat fungsi saat tombol "Hubungi whatsapp kami" ditekan
def hubungi():
    phone_number = "+6283112934894"
    message = "Halo, bang. Saya membutuhkan bantuan!"
    kit.sendwhatmsg_instantly(phone_number, message)

# Membuat tombol untuk membuka detail tingkatan premium
def show_detail():
    # membuat jendela baru
    detail_window = Toplevel()
    detail_window.title("Detail Premium")
    detail_window.geometry("600x500")
    detail_window.configure(bg="#f5f5f5")
    detail_window.resizable(False, False)
    detail_window.iconbitmap("icon.ico")

    # membuat widget scrollbar
    scrollbar = Scrollbar(detail_window)
    scrollbar.pack(side=RIGHT, fill=Y)

    # membuat widget text
    detail_text = Text(detail_window, font=("Arial", 12), yscrollcommand=scrollbar.set)
    detail_text.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=detail_text.yview)

    # detail dari setiap tingkatan premium
    premium_levels = {
        "Tingkat Prajurit": {
            "harga": "100Rb [PERBULAN]",
            "fitur": [
                "5 UA PREMIUM",
                "VPN PREMIUM",
                "Aplikasi yang sudah dimodifikasi",
                "Aplikasi lebih ringan / Cepat",
                "Prioritas chat",
                "Tidak ada dadu di jendela kecil / besar funcaptcha persentase 70%",
                "Tidak ada akurasi",
                "VPN berganti Auto",
                "Ping Internet",
                "Reset Internet Auto",
                "Hanya bisa menggunakan 8 akun",
                "Tanpa menggunakan Sandboxie"
            ]
        },
        "Tingkat Panglima": {
            "harga": "200Rb [PERBULAN]",
            "fitur": [
                "10 UA PREMIUM Dan Fitur Saat Memulai[Berganti Random]",
                "VPN PREMIUM",
                "VPN berganti Auto",
                "Aplikasi yang sudah dimodifikasi",
                "Aplikasi lebih ringan / Cepat",
                "Prioritas chat lebih diutamakan dari tingkat Prajurit",
                "Tidak ada dadu di jendela kecil / besar funcaptcha persentase 73%",
                "Tidak ada akurasi",
                "Fitur penghapusan cache, temp",
                "Ping Internet",
                "Reset Internet Auto",
                "Auto Start captcha",
                "Hanya bisa menggunakan 12 akun",
                "Tanpa menggunakan Sandboxie"
            ]
        },
        "Tingkat Raja": {
            "harga": "300Rb [PERBULAN]",
            "fitur": [
                "15 UA PREMIUM Dan Fitur Saat Memulai[Berganti Random]",
                "VPN PREMIUM",
                "VPN berganti Auto",
                "Aplikasi yang sudah dimodifikasi",
                "Aplikasi lebih ringan / Cepat",
                "Prioritas chat lebih diutamakan dari tingkat Panglima",
                "Tidak ada dadu di jendela kecil / besar funcaptcha persentase 78%",
                "Tidak ada akurasi",
                "Fitur penghapusan cache, temp, dan cookies Auto",
                "Reset Internet Auto",
                "Ping Internet",
                "Auto Start captcha",
                "Auto Skip dadu",
                "Shortcut keyboard Play[F11], block[Esc], Berpindah ke kolom text[TAB]",
                "Auto click pada Horse image",
                "Bisa menggunakan 15 akun",
                "Tanpa menggunakan Sandboxie"
            ]
        },
        "Tingkat DEWA [MODAL DEVICE] [PERBULAN]": {
            "harga": "700Rb [PERBULAN]",
            "fitur": [
                "PERINGATAN!!! PC HARUS MEMADAI UNTUK KELANCARAN [belum dirilis]",
                "Harga: [700Rb]",
                "24 UA PREMIUM Dan Fitur Saat Memulai[Berganti Random]",
                "VPN PREMIUM",
                "VPN berganti Auto",
                "Aplikasi yang sudah dimodifikasi",
                "Aplikasi lebih ringan / Cepat",
                "Prioritas chat lebih diutamakan dari tingkat Raja",
                "Tidak ada dadu di jendela kecil / besar funcaptcha persentase 83%",
                "Tidak ada akurasi",
                "Fitur penghapusan cache, temp, dan cookies Auto",
                "Reset Internet Auto",
                "Ping Internet",
                "Shortcut keyboard Play[F11], block[Esc], Berpindah ke kolom text[TAB]",
                "Tidak ada akurasi",
                "ALL SOLVED CAPTCHA[Update bertahap]",
                "Bisa menggunakan 20 akun",
                "Tanpa menggunakan Sandboxie"
            ]
        }
    }

    for level, detail in premium_levels.items():
        detail_text.insert(END, f"{level}\n")
        detail_text.insert(END, f"Harga: {detail['harga']}\n")
        detail_text.insert(END, "Fitur:\n")
        for fitur in detail['fitur']:
            detail_text.insert(END, f"- {fitur}\n")
        detail_text.insert(END, "\n")

    # menampilkan jendela detail premium
    detail_window.mainloop()
def def_registrasi():
    # Membuat jendela baru untuk registrasi
    register_window = Toplevel()
    register_window.title("Registrasi Akun")
    register_window.geometry("705x600")
    register_window.configure(bg="#f5f5f5")
    register_window.iconbitmap("icon.ico")
    register_window.resizable(False, False)  # menambahkan baris ini

    title_label = Label(register_window, text="Registrasi Akun", font=("Arial", 18), bg="#f5f5f5")
    title_label.grid(row=0, column=0, padx=10, pady=10, sticky="n")

    # Membuat label untuk judul jendela
    title_label = Label(register_window, text="Password minimal 8 karakter dan harus mempunyai angka!", font=("Arial", 9), fg="red", bg="#f5f5f5")
    title_label.grid(row=1, column=0, padx=10, pady=10, sticky="n")

    # Membuat label dan entry untuk id
    id_label = Label(register_window, text="ID", font=("Arial", 14), bg="#f5f5f5")
    id_label.grid(row=2, column=0, padx=10, pady=10, sticky="n")
    id_entry = Entry(register_window, font=("Arial", 14))
    id_entry.grid(row=3, column=0, padx=10, pady=10, sticky="n")
        
    def show_password():
        if password_entry.cget('show') == '':
            password_entry.config(show="*")
            verif_password_entry.config(show="*")
            show_button.config(text="Show Password")
        else:
            password_entry.config(show="")
            verif_password_entry.config(show="")
            show_button.config(text="Hide Password")
            
    password_label = Label(register_window, text="Password", font=("Arial", 14), bg="#f5f5f5")
    password_label.grid(row=4, column=0, padx=10, pady=10, sticky="n")
    password_entry = Entry(register_window, font=("Arial", 14), show="*")
    password_entry.grid(row=5, column=0, padx=10, pady=10, sticky="n")

    # Membuat label dan entry untuk verifikasi password
    verif_password_label = Label(register_window, text="Verifikasi Password", font=("Arial", 14), bg="#f5f5f5")
    verif_password_label.grid(row=6, column=0, padx=10, pady=10, sticky="n")
    verif_password_entry = Entry(register_window, font=("Arial", 14), show="*")
    verif_password_entry.grid(row=7, column=0, padx=10, pady=10, sticky="n")

    # Membuat tombol "Show Password"
    show_button = Button(register_window, text="Show Password", bg="Green",fg="white" , command=show_password)
    show_button.grid(row=8, column=0, padx=10, pady=10, sticky="n")

    label = Label(register_window, text="Pilih Tingkat Anda:", font=("Arial", 17))
    label.grid(row=0, column=1, padx=10, pady=10, sticky="n")

    # membuat ComboBox tidak dapat diedit
    tingkat_options = {
        "Tingkat Prajurit": "Rp 100.000 Dollar 7$",
        "Tingkat Panglima": "Rp 200.000 Dollar 14$",
        "Tingkat Raja": "Rp 300.000 Dollar 20$",
        "Tingkat Dewa": "Rp 700.000 Dollar 50$"
    }

    tingkat_combo = ttk.Combobox(register_window, values=list(tingkat_options.keys()), state="readonly")
    tingkat_combo.grid(row=3, column=1, padx=10, pady=10, sticky="n")
    tingkat_combo.current(0)

    # membuat label untuk menampilkan nomor rekening
    Tingkatan_pp_value = StringVar()
    Tingkatan_pp_value.set(tingkat_options[tingkat_combo.get()])
    Tingkatan_pp_value_label = ttk.Label(register_window, textvariable=Tingkatan_pp_value, font=("Helvetica", 16, "bold"), borderwidth=2, relief="solid", background="white", foreground="black")
    Tingkatan_pp_value_label.grid(row=5, column=1, padx=10, pady=10, sticky="n")

    def change_tingkatan_pp(event):
        Tingkatan_pp_value.set(tingkat_options[tingkat_combo.get()])

    tingkat_combo.bind("<<ComboboxSelected>>", change_tingkatan_pp)

    info_button = ttk.Button(register_window, text="Baca ini untuk melihat apa saja yang didapat di setiap tingkatan!", 
                             style='C.TButton', command=show_detail)
    info_button.grid(row=1, column=1, padx=10, pady=10, sticky="n")

    style = ttk.Style()

    # Membuat style baru dengan nama "C.TButton" untuk tombol
    style.configure('C.TButton', foreground='black', font=("Arial", 8), padding=10, 
                    background='#1E90FF', borderwidth=0, anchor="center")

    # Menambahkan efek hover pada tombol
    style.map('C.TButton', background=[('active', '#FFA500')])

    tingkat_pilihan = tingkat_combo.get()
    harga = tingkat_options[tingkat_pilihan]

    # membuat label jenis pembayaran
    jenis_pembayaran_label = ttk.Label(register_window, text="Jenis Pembayaran", font=("Helvetica", 10, "bold"))
    jenis_pembayaran_label.grid(row=2, column=1, padx=10, pady=10, sticky="n")

    # membuat ComboBox untuk pilihan jenis pembayaran
    jenis_pembayaran_options = {
        "BRI": "443001031596532",
        "DANA": "082118602200",
        "Perfectmoney": "U37116979",
        "Payeer": "P1080644427",
        "Paypal": "doniramdani82001@gmail.com",
        "Advcash": "U 0633 9095 7813"
    }

    jenis_pembayaran = ttk.Combobox(register_window, values=list(jenis_pembayaran_options.keys()), state="readonly")
    jenis_pembayaran.grid(row=4, column=1, padx=10, pady=10, sticky="n")
    jenis_pembayaran.current(0)

    # membuat label untuk menampilkan nomor rekening
    nomor_rekening_value = StringVar()
    nomor_rekening_value.set(jenis_pembayaran_options[jenis_pembayaran.get()])
    nomor_rekening_value_label = ttk.Label(register_window, textvariable=nomor_rekening_value, font=("Helvetica", 16, "bold"), borderwidth=2, relief="solid", background="white", foreground="black")
    nomor_rekening_value_label.grid(row=6, column=1, padx=10, pady=10, sticky="n")

    def change_nomor_rekening(event):
        nomor_rekening_value.set(jenis_pembayaran_options[jenis_pembayaran.get()])

    # membuat label atas nama
    atas_nama_label = ttk.Label(register_window, text="Atas Nama: DONI RAMDANI", font=("Helvetica", 10, "bold"))
    atas_nama_label.grid(row=7, column=1, padx=10, pady=10, sticky="n")

    # bind ComboBox dengan event handler
    jenis_pembayaran.bind("<<ComboboxSelected>>", change_nomor_rekening)

    # Membuat label untuk menampilkan hasil registrasi
    result_label = Label(register_window, font=("Arial", 14), bg="#f5f5f5")
    result_label.grid(row=10, column=1, padx=10, pady=10, sticky="n")

    referal_frame = ttk.Frame(register_window, borderwidth=1, relief="solid")
    referal_frame.grid(row=7, column=1, padx=5, pady=5, sticky="n")

    referal_label = ttk.Label(referal_frame, text="Kode Referal (jika ada):")
    referal_label.grid(row=7, column=1, padx=5, pady=5, sticky="n")

    def referral_info():
        message = "Ini adalah kolom referal, jadi jika Anda di ajak teman, Anda bisa memasukkan kode teman Anda. Anda juga dapat mulai berpartisipasi dengan cara mengajak teman bergabung dengan program premium. Setiap kali Anda berhasil mengajak teman Anda bergabung dengan program premium, Anda akan mendapatkan potongan harga sebesar 20% pada aplikasi dan bisa diklaim 2 kali setiap satu bulan sekali, sehingga total per bulan bisa mencapai 40%. Terima kasih."
        messagebox.showinfo(title="Informasi Referal", message=message)
        register_window.lift()

    referral_button = ttk.Button(referal_frame, text="?", command=referral_info)
    referral_button.grid(row=7, column=2, padx=5, pady=5, sticky="n")

    referal_entry = ttk.Entry(referal_frame)
    referal_entry.grid(row=8, column=1, padx=5, pady=5, sticky="n")

    def generate_random_string(length):
        letters_and_digits = string.digits + string.ascii_letters
        result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
        return result_str

    random_password = generate_random_string(8)

    def code_rahasia(length):
        letters_and_digits = string.digits + string.ascii_letters
        result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
        return result_str

    code_rahasia = code_rahasia(8)

    def register():
        # Ambil data JSON dari Bitbucket
        url = "https://bitbucket.org/don-kgs/v04/raw/master/data.json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        # Ambil nilai yang dimasukkan oleh pengguna pada kolom Ref
        user_ref = referal_entry.get()

        # Cek apakah nilai user_ref ada di dalam JSON
        ref_exists = False
        for user in data['users']:
            if user_ref == user.get('Ref'):
                ref_exists = True
                break

        if ref_exists or user_ref == '':
            id_value = id_entry.get()
            password_value = password_entry.get()
            verif_password_value = verif_password_entry.get()
                    
            # Cek apakah kolom referal diisi atau tidak
            if len(referal_entry.get()) > 0:
                referal_value = referal_entry.get()
            else:
                referal_value = None

            if get_id_info(id_value):
                # Tampilkan pesan error jika id sudah terdaftar
                result_label.config(text="ID sudah terdaftar. Mohon gunakan id lain.", font=("Arial", 12,))
            elif len(password_value) < 8 or not any(char.isdigit() for char in password_value):
                # Tampilkan pesan error jika password tidak memenuhi syarat
                result_label.config(text="Password tidak sama atau kesalahan lain", font=("Arial", 13,), fg="red")
            elif password_value == verif_password_value:
                message = "Sebelum menekan OK, silakan siapkan WhatsApp Web Anda untuk mengirim data ini!"
                messagebox.showinfo(title="Info Daftar", message=message)
                register_window.lift()
                # mengirim pesan WhatsApp setelah pendaftaran berhasil
                phone_number = "+6283112934894"
                # mengirim pesan WhatsApp setelah pendaftaran berhasil
                if referal_entry.get() != "":
                    message = f"Tunggu admin Untuk Verifikasi,Untuk mempercepat verfikasi tolong sertakan bukti Pembayaran!\nDan tolong simpan kode rahasia Anda dengan baik. Ini digunakan ketika Anda lupa kata sandi.\nID: {id_value}\nPassword: {password_value}\nTingkat: {tingkat_combo.get()}\nReferal Teman: {referal_entry.get()}\nJenis Pembayaran: {jenis_pembayaran.get()}\nKode Rahasia : {code_rahasia}\nKode Referal Anda : {random_password}\nHarga : {harga}"
                else:
                    message = f"Tunggu admin Untuk Verifikasi,Untuk mempercepat verfikasi tolong sertakan bukti Pembayaran!\nDan tolong simpan kode rahasia Anda dengan baik. Ini digunakan ketika Anda lupa kata sandi.\nID: {id_value}\nPassword: {password_value}\nTingkat: {tingkat_combo.get()}\nJenis Pembayaran: {jenis_pembayaran.get()}\nKode Referal Anda : {random_password}\nKode Rahasia : {code_rahasia}\nHarga : {harga}"
                kit.sendwhatmsg_instantly(phone_number, message)

                result_label.config(text="Registrasi berhasil dilakukan!")
                register_window.destroy()
            else:
                # Tampilkan pesan error jika password tidak sesuai
                result_label.config(text="Password tidak sesuai. Mohon coba lagi.")
        else:
            msg = "Nilai yang dimasukkan pada kolom Ref tidak valid."
            messagebox.showerror("Error", msg)
            register_window.lift()

    # Membuat tombol untuk melakukan registrasi
    register_button = Button(register_window, text="Daftar", bg="green", fg="#ffffff", font=("Arial", 14), padx=30,command=register)
    register_button.grid(row=8, column=1, padx=5, pady=5, sticky="n")

def Lupa_katasandi():
    # Membuat jendela baru untuk lupa kata sandi
    forgot_password_window = tk.Toplevel()
    forgot_password_window.title("Lupa Kata Sandi")
    forgot_password_window.geometry("610x400")
    forgot_password_window.configure(bg="black")
    forgot_password_window.resizable(False, False)
    forgot_password_window.iconbitmap("icon.ico")
    
    # Judul halaman
    title_label = tk.Label(forgot_password_window, text="Lupa Kata Sandi", font=("Helvetica", 20), bg="black", fg="white")
    title_label.pack(pady=10)
    
    # Label instruksi
    instruction_label = tk.Label(forgot_password_window, text="Masukkan ID Sebelumnya Dan Kode Rahasia untuk mengatur ulang kata sandi Anda.", font=("Helvetica", 12), bg="black", fg="#666666")
    instruction_label.pack(pady=10)
    
    input_frame = tk.Frame(forgot_password_window, bg="black")
    input_frame.pack(pady=10)
    input_label = tk.Label(input_frame, text="ID Sebelumnya", font=("Helvetica", 12), bg="black", fg="white")
    input_label.grid(row=0, column=0, padx=10)
    input_entry = tk.Entry(input_frame, font=("Helvetica", 12), bg="#f9f9f9", fg="#333333", relief="flat")
    input_entry.grid(row=0, column=1, padx=10, ipadx=50, ipady=5)

    kode_rahasia_frame = tk.Frame(forgot_password_window, bg="black")
    kode_rahasia_frame.pack(pady=10)
    kode_rahasia_label = tk.Label(kode_rahasia_frame, text="Kode Rahasia ", font=("Helvetica", 12), bg="black", fg="white")
    kode_rahasia_label.grid(row=0, column=0, padx=10)
    kode_rahasia_entry = tk.Entry(kode_rahasia_frame, font=("Helvetica", 12), bg="#f9f9f9", fg="#333333", relief="flat")
    kode_rahasia_entry.grid(row=0, column=1, padx=10, ipadx=50, ipady=5)

    def info_kode_rahasia(kode_rahasia_value):
        url = "https://bitbucket.org/don-kgs/v04/raw/master/data.json"
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
            for user in data["users"]:
                if user["Kode_Rahasia"] == kode_rahasia_value:
                    return True
            return False

    def lupa_pass():
        Kode_R = kode_rahasia_entry.get()
        Kode_S = input_entry.get()
        # periksa apakah kolom input tidak kosong
        if Kode_R and Kode_S:
            # periksa apakah ID dan kode rahasia yang dimasukkan oleh pengguna sesuai dengan data yang tersedia di Bitbucket
            if not get_id_info(Kode_S):
                messagebox.showerror(title="Error", message="ID yang dimasukkan tidak ada di server!")
                forgot_password_window.lift()
                return
            if not info_kode_rahasia(Kode_R):
                messagebox.showerror(title="Error", message="Kode rahasia yang dimasukkan tidak ada di server!")
                forgot_password_window.lift()
                return
            message = "Sebelum menekan OK, silakan siapkan WhatsApp Web Anda untuk mengirim data ini!"
            messagebox.showinfo(title="Info Daftar", message=message)
            forgot_password_window.lift()
            # mengirim pesan WhatsApp setelah pendaftaran berhasil
            phone_number = "+6283112934894"
            message = f"Bang saya lupa Kata sandi di bantu dong!\nID Sebelumnya: {Kode_S}\nKode Rahasia: {Kode_R}"
            kit.sendwhatmsg_instantly(phone_number, message)
            forgot_password_window.destroy()
        else:
            # tampilkan pesan kesalahan jika kolom input kosong
            messagebox.showerror(title="Error", message="Kolom input tidak boleh kosong!")
            forgot_password_window.lift()

    # Tombol Submit
    submit_button = tk.Button(forgot_password_window, text="Kirim Kode Rahasia Dan ID", font=("Helvetica", 12), bg="#f5555d", fg="#ffffff", relief="flat", activebackground="#f5555d", activeforeground="#ffffff", padx=20, pady=10, command=lupa_pass)
    submit_button.pack(pady=10)
    
    # Link kembali ke halaman login
    back_label = tk.Label(forgot_password_window, text="Kembali ke halaman login", font=("Helvetica", 12), bg="black", fg="white", cursor="hand2")
    back_label.pack(pady=10)
    back_label.bind("<Button-1>", lambda event: forgot_password_window.destroy())
    
    forgot_password_window.mainloop()

def Tambah_Waktu():
    # Membuat jendela baru untuk lupa kata sandi
    Tambah_waktu_window = tk.Toplevel()
    Tambah_waktu_window.title("Tambah waktu")
    Tambah_waktu_window.geometry("650x610")
    Tambah_waktu_window.configure(bg="black")
    Tambah_waktu_window.iconbitmap("icon.ico")
    #Tambah_waktu_window.resizable(False, False)

    def get_user_info(user_id, user_password):
        url = "https://bitbucket.org/don-kgs/v04/raw/master/data.json"
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
            for user in data["users"]:
                if user["id"] == user_id and user["password"] == user_password:
                    return user
            return None

    # Judul halaman
    title_label = tk.Label(Tambah_waktu_window, text="Tambah Waktu", font=("Helvetica", 20), bg="black", fg="white")
    title_label.pack(pady=10)
    
    # Label instruksi
    instruction_label = tk.Label(Tambah_waktu_window, text="Masukkan ID Sebelumnya Dan Password Untuk Menambah Waktu Anda.", font=("Helvetica", 12), bg="black", fg="#666666")
    instruction_label.pack(pady=10)
    
    input_frame = tk.Frame(Tambah_waktu_window, bg="black")
    input_frame.pack(pady=10)
    input_label = tk.Label(input_frame, text="ID Sebelumnya     :", font=("Helvetica", 12), bg="black", fg="white")
    input_label.grid(row=0, column=0, padx=10)
    input_entry = tk.Entry(input_frame, font=("Helvetica", 12), bg="#f9f9f9", fg="#333333", relief="flat")
    input_entry.grid(row=0, column=1, padx=10, ipadx=50, ipady=5)

    password_frame = tk.Frame(Tambah_waktu_window, bg="black")
    password_frame.pack(pady=10)
    password_label = tk.Label(password_frame, text="Password [Pass] :", font=("Helvetica", 12), bg="black", fg="white")
    password_label.grid(row=0, column=0, padx=10)
    password_entry = tk.Entry(password_frame, font=("Helvetica", 12), bg="#f9f9f9", fg="#333333", relief="flat")
    password_entry.grid(row=0, column=1, padx=10, ipadx=50, ipady=5)

    def tambah_waktu_oke():
        Kode_ID = input_entry.get()
        Kode_PW = password_entry.get()
        # periksa apakah kolom input tidak kosong
        if Kode_ID and Kode_PW:
            # periksa apakah ID dan kode rahasia yang dimasukkan oleh pengguna sesuai dengan data yang tersedia di Bitbucket
            user_data = get_user_info(Kode_ID, Kode_PW)
            if not user_data:
                messagebox.showerror(title="Error", message="ID atau password yang dimasukkan salah!")
                Tambah_waktu_window.lift()
                return
            
            # Ambil harga dari user yang sesuai dengan ID dan password yang dimasukkan
            harga = user_data["Harga"]

            Tambah_waktu2_window = tk.Toplevel()
            Tambah_waktu2_window.title("Tambah waktu")
            Tambah_waktu2_window.geometry("650x610")
            Tambah_waktu2_window.configure(bg="black")
            Tambah_waktu2_window.iconbitmap("icon.ico")


                # membuat label jenis pembayaran
            jenis_pembayaran_label = ttk.Label(Tambah_waktu2_window, text="Jenis Pembayaran", font=("Helvetica", 15, "bold"), foreground="white", background="black")
            jenis_pembayaran_label.pack(pady=10)
        
            # membuat ComboBox untuk pilihan jenis pembayaran
            jenis_pembayaran_options = {
                "BRI": "443001031596532",
                "DANA": "082118602200",
                "Perfectmoney": "U37116979",
                "Payeer": "P1080644427"
            }
            jenis_pembayaran = ttk.Combobox(Tambah_waktu2_window, values=list(jenis_pembayaran_options.keys()), state="readonly")
            jenis_pembayaran.pack(pady=10)
            jenis_pembayaran.current(0)

            # membuat label untuk menampilkan nomor rekening
            nomor_rekening_value = StringVar()
            nomor_rekening_value.set(jenis_pembayaran_options[jenis_pembayaran.get()])
            nomor_rekening_value_label = ttk.Label(Tambah_waktu2_window, textvariable=nomor_rekening_value, font=("Helvetica", 16, "bold"), borderwidth=2, relief="solid", background="white", foreground="black")
            nomor_rekening_value_label.pack(pady=10)

            def change_nomor_rekening(event):
                nomor_rekening_value.set(jenis_pembayaran_options[jenis_pembayaran.get()])

            # membuat label atas nama
            atas_nama_label = ttk.Label(Tambah_waktu2_window, text="Atas Nama: DONI RAMDANI", font=("Helvetica", 10, "bold"))
            atas_nama_label.pack(pady=10)

            # bind ComboBox dengan event handler
            jenis_pembayaran.bind("<<ComboboxSelected>>", change_nomor_rekening)

            Ref_teman_frame = tk.Frame(Tambah_waktu2_window, bg="black")
            Ref_teman_frame.pack(pady=10)
            Ref_teman_label = tk.Label(Ref_teman_frame, text="Ref Teman Yang anda undang (Jika ada):", font=("Helvetica", 12), bg="black", fg="white")
            Ref_teman_label.grid(row=1, column=0, padx=10)
            Ref_teman_entry = tk.Entry(Ref_teman_frame, font=("Helvetica", 12), bg="#f9f9f9", fg="#333333", relief="flat")
            Ref_teman_entry.grid(row=1, column=1, padx=10, ipadx=50, ipady=5)

                        # Cek apakah kolom referal diisi atau tidak
            if len(Ref_teman_entry.get()) > 0:
                referal_value = Ref_teman_entry.get()
            else:
                referal_value = None

            #Mulaiiiiiiiiiiiiiiiiiiiiii
            # membuat ComboBox untuk pilihan jenis pembayaran
            harga = float(user_data["Harga"].replace(',', ''))
            jenis_tingkatan_options = {
                "1 Minggu": f"Rp.{int(harga*0.30)}",
                "1 Bulan": f"Rp.{int(harga)}",
                "2 Bulan": f"Rp.{int(harga*2)}",
                "3 Bulan": f"Rp.{int(harga*3)}"
            }
            jenis_tingkatan = ttk.Combobox(Tambah_waktu2_window, values=list(jenis_tingkatan_options.keys()), state="readonly")
            jenis_tingkatan.pack(pady=10)
            jenis_tingkatan.current(0)


            # membuat label untuk menampilkan nomor rekening
            menapilkan_harga = StringVar()
            menapilkan_harga.set(jenis_tingkatan_options[jenis_tingkatan.get()])
            menapilkan_harga_label = ttk.Label(Tambah_waktu2_window, textvariable=menapilkan_harga, font=("Helvetica", 16, "bold"), borderwidth=2, relief="solid", background="white", foreground="black")
            menapilkan_harga_label.pack(pady=10)

            def change_nomor_rekening(event):
                menapilkan_harga.set(jenis_tingkatan_options[jenis_tingkatan.get()])

            # bind ComboBox dengan event handler
            jenis_tingkatan.bind("<<ComboboxSelected>>", change_nomor_rekening)


            def button_gas_wa():
                # Ambil data JSON dari Bitbucket
                url = "https://bitbucket.org/don-kgs/v04/raw/master/data.json"
                response = urllib.request.urlopen(url)
                data = json.loads(response.read())

                # Ambil nilai yang dimasukkan oleh pengguna pada kolom Ref
                user_ref = Ref_teman_entry.get()

                # Cek apakah nilai user_ref ada di dalam JSON
                ref_exists = False
                for user in data['users']:
                    if user_ref == user.get('Ref'):
                        ref_exists = True
                        break

                if ref_exists or user_ref == '':
                    message = f"Siapkan WhatsApp Web Anda untuk mengirim data ini!"
                    messagebox.showinfo(title="Info Harga", message=message)
                    Tambah_waktu2_window.lift()

                    #mengirim pesan WhatsApp setelah pendaftaran berhasil
                    phone_number = "+6283112934894"
                    if Ref_teman_entry.get() != "":
                        message = f"Bang saya mau Tambah waktu di bantu dong![Tolong Sertakan Bukti permbayaran agar cepat di proses!]\nID Sebelumnya: {Kode_ID}\nPassword: {Kode_PW}\nTambah berapa: {jenis_tingkatan.get()}\nJenis pembayaran: {jenis_pembayaran.get()}\nRef Teman anda yang di undang: {Ref_teman_entry.get()}\nHarga: {menapilkan_harga.get()}"
                    else:
                        message = f"Bang saya mau Tambah waktu di bantu dong![Tolong Sertakan Bukti permbayaran agar cepat di proses!]\nID Sebelumnya: {Kode_ID}\nPassword: {Kode_PW}\nTambah berapa: {jenis_tingkatan.get()}\nJenis pembayaran: {jenis_pembayaran.get()}\nHarga: {menapilkan_harga.get()}"
                    kit.sendwhatmsg_instantly(phone_number, message)
                    Tambah_waktu2_window.destroy()
                else:
                     # Nilai user_ref tidak ada di dalam JSON
                     # Tampilkan pesan error
                    msg = "Nilai yang dimasukkan pada kolom Ref tidak valid."
                    messagebox.showerror("Error", msg)
                    Tambah_waktu2_window.lift()
            # Tombol Submit
            submit_button = tk.Button(Tambah_waktu2_window, text="Kirim data ini", font=("Helvetica", 12), bg="#b58200", fg="#ffffff", relief="flat", activebackground="#f5555d", activeforeground="#ffffff", padx=20, pady=10, command=button_gas_wa)
            submit_button.pack(pady=10)
        else:
            # tampilkan pesan kesalahan jika kolom input kosong
            messagebox.showerror(title="Error", message="Kolom input tidak boleh kosong!")
            Tambah_waktu_window.lift()

    # Tombol Submit
    submit_button = tk.Button(Tambah_waktu_window, text="Login Dan Tambah Waktu", font=("Helvetica", 12), bg="#b58200", fg="#ffffff", relief="flat", activebackground="#f5555d", activeforeground="#ffffff", padx=20, pady=10, command=tambah_waktu_oke)
    submit_button.pack(pady=10)

    # membuat function untuk event enter
    def enter_pressed(event):
        submit_button.invoke()

    # mengaitkan event enter pada widget yang dipilih
    Tambah_waktu_window.bind('<Return>', enter_pressed)
    
    # Link kembali ke halaman login
    back_label = tk.Label(Tambah_waktu_window, text="Kembali ke halaman login", font=("Helvetica", 12), bg="black", fg="white", cursor="hand2")
    back_label.pack(pady=10)
    back_label.bind("<Button-1>", lambda event: Tambah_waktu_window.destroy())
    
    Tambah_waktu_window.mainloop()

 # membuat tampilan tab
tab_frame = Frame(root, bg="#343a40")
tab_frame.pack(fill=X)

tab_frame_1 = Frame(tab_frame, bg="#343a40")
tab_frame_1.pack(side=TOP)

menu_tab = Button(tab_frame_1, text="Menu", width=15, bg="#f8f9fa", fg="#343a40", padx=20, pady=10)
menu_tab.pack(side=LEFT, padx=5, pady=5)
menu_tab.bind("<Enter>", enter)
menu_tab.bind("<Leave>", leave)

convert_tab = Button(tab_frame_1, text="Penukaran Uang/Convert", width=15, bg="#f8f9fa", fg="#343a40", padx=20, pady=10)
convert_tab.pack(side=LEFT, padx=5, pady=5)
convert_tab.bind("<Enter>", enter)
convert_tab.bind("<Leave>", leave)

auto_wd_tab = Button(tab_frame_1, text="Auto WD", width=15, bg="#f8f9fa", fg="#343a40", padx=20, pady=10)
auto_wd_tab.pack(side=LEFT, padx=5, pady=5)
auto_wd_tab.bind("<Enter>", enter)
auto_wd_tab.bind("<Leave>", leave)

auto_create_email_tab = Button(tab_frame_1, text="Auto Buat Email", width=15, bg="#f8f9fa", fg="#343a40", padx=20, pady=10)
auto_create_email_tab.pack(side=LEFT, padx=5, pady=5)
auto_create_email_tab.bind("<Enter>", enter)
auto_create_email_tab.bind("<Leave>", leave)

# membuat frame baru untuk baris tab kedua
tab_frame_2 = Frame(tab_frame, bg="#343a40")
tab_frame_2.pack(side=BOTTOM)

demo_key_tab = Button(tab_frame_2, text="Demo Key", width=15, bg="#f8f9fa", fg="#343a40", padx=20, pady=10)
demo_key_tab.pack(side=LEFT, padx=5, pady=5)
demo_key_tab.bind("<Enter>", enter)
demo_key_tab.bind("<Leave>", leave)

shop_tab = Button(tab_frame_2, text="Toko", width=15, bg="#f8f9fa", fg="#343a40", padx=20, pady=10)
shop_tab.pack(side=LEFT, padx=5, pady=5)
shop_tab.bind("<Enter>", enter)
shop_tab.bind("<Leave>", leave)

tutorial_tab = Button(tab_frame_2, text="Tutorial", width=15, bg="#f8f9fa", fg="#343a40", padx=20, pady=10)
tutorial_tab.pack(side=LEFT, padx=5, pady=5)
tutorial_tab.bind("<Enter>", enter)
tutorial_tab.bind("<Leave>", leave)

diskusi_tab = Button(tab_frame_2, text="Diskusi & FAQ/BUG", width=15, bg="#f8f9fa", fg="#343a40", padx=20, pady=10)
diskusi_tab.pack(side=LEFT, padx=5, pady=5)
diskusi_tab.bind("<Enter>", enter)
diskusi_tab.bind("<Leave>", leave)

remember_me_var = BooleanVar(value=True)

def show_login_window(root):
    # membuat tampilan untuk login
    login_frame = Frame(root, bg="#f8f9fa")
    login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    login_id_label = Label(login_frame, text="ID", bg="#f8f9fa", font=("Arial", 14))
    login_id_label.grid(row=0, column=0, padx=10)

    login_id_entry = Entry(login_frame, bg="#ffffff", font=("Arial", 14))
    login_id_entry.grid(row=0, column=1, padx=10)

    login_password_label = Label(login_frame, text="Pass", bg="#f8f9fa", font=("Arial", 14))
    login_password_label.grid(row=1, column=0, padx=10)

    # Function to toggle the password visibility
    global password_visible
    def toggle_password_visibility():
        global password_visible

        if password_visible:
            login_password_entry.config(show="*")
            password_visible = False
        else:
            login_password_entry.config(show="")
            password_visible = True

    # Create the password entry field
    login_password_entry = Entry(login_frame, bg="#ffffff", show="*", font=("Arial", 14))
    login_password_entry.grid(row=1, column=1)

    # Create the eye button
    show_password_button = Button(login_frame, text="👁", bg="#adcc3d", relief=FLAT, command=toggle_password_visibility)
    show_password_button.grid(row=1, column=2)

    # Create a variable to keep track of password visibility
    password_visible = False

    login_password_entry.bind('<Return>', lambda event: login_button.invoke())

    # membuka file teks jika ada dan mengisi kotak input jika terakhir disimpan
    try:
        with open("user_info.txt", "r") as f:
            lines = f.readlines()
            if len(lines) >= 2:
                login_id_entry.insert(0, lines[0].strip())
                login_password_entry.insert(0, lines[1].strip())
    except FileNotFoundError:
        pass

    login_button = Button(login_frame, text="Login", width=7, bg="#343a40", fg="#ffffff", command=lambda: check_login(login_id_entry, login_password_entry))
    login_button.grid(row=0, column=2, pady=10)

    remember_me_checkbox = Checkbutton(root, text="Simpan ID dan Password", variable=remember_me_var)
    remember_me_checkbox.pack(side="top", padx=0, pady=7)

    register_button = Button(login_frame, text="Daftar", bg="#343a40", fg="#ffffff", font=("Arial", 14), padx=10, command=def_registrasi)
    register_button.grid(row=6, column=1, pady=10)

    forgot_password_button = Button(login_frame, text="Lupa Kata Sandi", bg="#343a40", fg="#ffffff", font=("Arial", 10), padx=10, command=Lupa_katasandi)
    forgot_password_button.grid(row=2, column=1, pady=10)

    Tambah_Waktu_button = Button(login_frame, text="Tambah Waktu", bg="#0b45b3", fg="#ffffff", font=("Arial", 10), padx=10, command=Tambah_Waktu)
    Tambah_Waktu_button.grid(row=10, column=1, pady=10)

    # membuat tampilan untuk "Butuh bantuan lanjutan?"
    help_label = Label(root, text="Butuh bantuan lanjutan?", bg="#f8f9fa", font=("Arial", 14))
    help_label.place(relx=0.5, rely=0.8, anchor=CENTER)

    whatsapp_button = Button(root, text="Hubungi WhatsApp kami", bg="Green", fg="#ffffff", font=("Arial", 14), command=hubungi)
    whatsapp_button.place(relx=0.5, rely=0.9, anchor=CENTER)


def check_login(login_id_entry, login_password_entry):
    global remember_me_var
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                            for ele in range(0,8*6,8)][::-1])
    
    def save_user_info(username, password, mac_address, remember_me):
        with open("user_info.txt", "w") as f:
            f.write(username + "\n")
            f.write(password + "\n")
            f.write(mac_address + "\n")

    save_user_info(login_id_entry.get(), login_password_entry.get(), mac_address, remember_me_var.get())
    id = login_id_entry.get()
    password = login_password_entry.get()

    url = 'https://bitbucket.org/don-kgs/v04/raw/master/data.json'

    try:
        response = requests.get(url)
        data = json.loads(response.text)

        for user in data["users"]:
            if user["id"] == id and user["password"] == password:
                if "mac_address" not in user:
                    messagebox.showinfo("Captcha kings", "Akun anda sedang dalam proses verifikasi oleh admin. Silahkan tunggu dan hubungi kami melalui WhatsApp jika belum terselesaikan.")
                    return
                exp_date = datetime.strptime(user["exp_date"], '%d %B %Y %H:%M:%S')
                tingkatan = user["Tingkatan"]
                user_mac_address = user["mac_address"]

                if exp_date <= datetime.now():
                    msg = "Waktu telah habis. Silahkan beli akun atau tambah waktu di akun anda untuk melanjutkan menggunakan layanan ini."
                    messagebox.showwarning("Peringatan", msg)
                    return

                if user_mac_address != mac_address:
                    msg = "Anda tidak diperbolehkan untuk login menggunakan komputer ini."
                    messagebox.showwarning("Peringatan", msg)
                    return

                if tingkatan == "Prajurit":
                    show_account_window_prajurit(root, id, tingkatan, exp_date)
                elif tingkatan == "Panglima":
                    show_account_window_panglima(root, id, tingkatan, exp_date)
                elif tingkatan == "King":
                    show_account_window_king(root, id, tingkatan, exp_date)
                elif tingkatan == "Dewa":
                    show_account_window_dewa(root, id, tingkatan, exp_date)
                
                return
        messagebox.showerror("Captcha kings", "username atau password yang dimasukkan salah.")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Captcha kings", "Gagal mengambil data login dari server: {}".format(e))
    except ValueError as e:
        messagebox.showerror("Captcha kings", "Format tanggal salah: {}".format(e))
    except Exception as e:
        messagebox.showerror("Captcha kings", "Terjadi kesalahan: {}".format(e))


show_login_window(root)
auto_click_enabled = False
auto_click_start_enabled = False
auto_hotkey_enable = False
auto_silang_enable = False

def show_account_window_prajurit(root, id, tingkatan, exp_date):
    root.withdraw()
    show_login_window
    # buat jendela baru
    account_window = tk.Toplevel()
    account_window.title("Informasi Akun")
    account_window.geometry("600x600+300+50")  # ubah ukuran dan posisi jendela sesuai keinginan
    account_window.iconbitmap("icon.ico")
    account_window.resizable(0, 0)

    def close_captcha():
        for proc in psutil.process_iter():
            if proc.name() == "libEGL.exe":
                proc.kill()
        # Mendapatkan handle dari jendela program
        handle = win32gui.FindWindow(None, 'Psiphon 3')

        # Mengirim pesan ke jendela program untuk menutup program dengan aman
        win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)

    def close_account_window():
        auto_click_enabled = False
        auto_click_start_enabled = False
        auto_hotkey_enable = False
        auto_silang_enable = False

        close_captcha()
        account_window.destroy()
        root.deiconify()

    account_window.protocol("WM_DELETE_WINDOW", close_account_window)

    def waktu_habis_exp(root, account_window):
        close_account_window()
        msg = "Waktu telah habis. Silahkan beli akun atau tambah waktu di akun anda untuk melanjutkan menggunakan layanan ini."
        messagebox.showwarning("Peringatan", msg)

    def check_expiry(account_window, root):
        while True:
            if account_window.winfo_exists() == 0:
                # keluar dari while loop jika jendela telah ditutup
                break

            if exp_date <= datetime.now():
                # panggil fungsi waktu_habis_exp() jika waktu kadaluwarsa telah berakhir
                waktu_habis_exp(root, account_window)
                break
            
            time.sleep(2)

    # Membuat thread baru
    thread = threading.Thread(target=check_expiry, args=(account_window, root))
    # Menjalankan thread
    thread.start()

    # atur tampilan tema ttk
    style = ttk.Style(account_window)
    style.theme_use("clam")

    # buat label untuk judul
    title_label = ttk.Label(account_window, text="INFORMASI AKUN", font=("Arial Black", 20), foreground="#3366CC")
    title_label.pack(pady=20)

    subprocess.call(["netsh", "int", "tcp", "set", "global", "autotuninglevel=highlyrestricted"])

    # buat frame untuk menampilkan informasi akun
    account_frame = ttk.Frame(account_window)
    account_frame.pack(pady=10)

    # buat frame untuk menampilkan pilihan
    option_frame = ttk.Frame(account_window)
    option_frame.pack(pady=10)

    # buat label untuk pilihan
    ttk.Label(option_frame, text="Mau main berapa Akun ?", font=("Helvetica", 13)).grid(column=0, row=0, padx=5, pady=5)

    # buat combobox untuk memilih opsi
    option_value = tk.StringVar()
    option_combobox = ttk.Combobox(option_frame, textvariable=option_value, values=["1", "2","3", "4","5", "6","7", "8"], state='readonly')
    option_combobox.grid(column=1, row=0, padx=5, pady=5)
    option_combobox.current(0) # set opsi pertama sebagai default

    # menggabungkan direktori pengguna saat ini dengan nama file config.json
    CONFIG_PATH = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "config.json")
    TEMP_CONFIG_PATH = r"C:\Users\Administrator\Desktop\V4\temp_config.json"
    CAPTCHAKINGS_PATH = r"C:\Users\Administrator\Desktop\V4\libEGL.exe"
    USERAGENT_URL = "https://raw.githubusercontent.com/doniramdani810/Captcha-kings-V4/main/USERAGENT.txt"

    def edit_config(api_key):
        # Clear the config file
        with open(CONFIG_PATH, "w") as f:
            json.dump({}, f)
        print("Config.json cleared")

        # Load the temporary config file and update it with the API key and a random user agent
        with urllib.request.urlopen(USERAGENT_URL) as response:
            user_agents = response.read().decode().split('\n')
            user_agent = random.choice(user_agents).strip()

        with open(TEMP_CONFIG_PATH, "r") as f:
            config_data = json.load(f)
            config_data["ApiKey"] = api_key
            config_data["Window"]["UserAgent"] = user_agent

        with open(TEMP_CONFIG_PATH, "w") as f:
            json.dump(config_data, f)
            print(f"Temp config file updated with API key: {api_key}")

        # Update the config file and start the Captchakings program
        with open(CONFIG_PATH, "w") as f:
            json.dump(config_data, f)
            print(f"Config file updated with API key: {api_key}")

        if account_window.winfo_exists():
            if os.name == "nt":
                subprocess.Popen(["start", "/HIGH", CAPTCHAKINGS_PATH], shell=True, stdin=subprocess.DEVNULL, bufsize=0, cwd=r"C:\Users\Administrator\Desktop\V4")
            elif os.name == "posix":
                subprocess.Popen(["/bin/sh", "-c", "wine libEGL.exe &"], stdin=subprocess.DEVNULL, bufsize=0, cwd=r"C:\Users\Administrator\Desktop\V4")
            else:
                messagebox.showerror("Unsupported OS", "Your operating system is not supported.")
            time.sleep(10)
        else:
            # kill all running processes with the name "libEGL.exe"
            for proc in psutil.process_iter(["name"]):
                if proc.info["name"] == "libEGL.exe":
                    proc.kill()

    def run_captcha(api_key):
        edit_config(api_key)

    def download_file(url, file_path):
        try:
            urllib.request.urlretrieve(url, file_path)
            print("File downloaded successfully!")
            return True
        except Exception as e:
            print("Failed to download file:", e)
            return False

    def do_action():
        selected_option = int(option_value.get())
        file_path = r"C:\Users\Administrator\Desktop\V4\key.txt"
        
        while not os.path.isfile(file_path):
            # download file from GitHub if it does not exist
            url = "https://bitbucket.org/don-kgs/v04/raw/master/key.txt"
            download_file(url, file_path)
            time.sleep(1) # wait for 1 second before checking again
        
        with open(file_path, "r") as key_file:
            keys = key_file.readlines()
        for api_key in keys[:selected_option]:
            run_captcha(api_key.strip())

    def time_tunggu():
        option_button.config(state='disabled')
        time.sleep(10)
        do_action()

    def task1():
        time.sleep(30)
        app_path = r"C:\Users\Administrator\Desktop\V4\PsiphonPortable.exe"        
        while account_window.winfo_exists():
            my_resolver = dns.resolver.Resolver()

            # Set cache size to 0 to disable caching
            my_resolver.cache = dns.resolver.Cache(dns.rdatatype.ANY)

            # Clear the resolver cache by creating a new instance of the cache
            my_resolver.cache = dns.resolver.Cache()

            print("DNS cache has been cleared.")

            # Reset IP and Winsock configuration
            subprocess.call("netsh int ip reset c:\\resetlog.txt", shell=True)
            subprocess.call("netsh winsock reset", shell=True)

            # Flush DNS cache and register DNS
            subprocess.call("ipconfig /flushdns", shell=True)
            subprocess.call("ipconfig /registerdns", shell=True)

            # Release and renew IP address
            subprocess.call("ipconfig /release", shell=True)
            subprocess.call("ipconfig /renew", shell=True)

            subprocess.Popen(app_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(7)  # tunggu beberapa detik agar aplikasi dimuat sepenuhnya
            hwnd = win32gui.FindWindow(None, "Psiphon 3")  # ganti dengan judul jendela aplikasi yang diinginkan
            # Fungsi untuk meminimalkan jendela seperti manual
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            time.sleep(600)
            # Mendapatkan handle dari jendela program
            handle = win32gui.FindWindow(None, 'Psiphon 3')

            # Mengirim pesan ke jendela program untuk menutup program dengan aman
            win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)


    def pingms():
        ping_button.config(state=tk.DISABLED)
        # Jalankan perintah ipconfig/all dan simpan hasilnya dalam variabel output
        output = subprocess.check_output(['ipconfig', '/all'], universal_newlines=True)

        # Cari baris yang berisi "DNS Servers" dalam output
        dns_servers_line = [line.strip() for line in output.split('\n') if 'DNS Servers' in line]

        # Peroleh informasi DNS server dari baris yang sesuai
        dns_servers = dns_servers_line[0].split(':')[1].strip()

        # Buka jendela command prompt baru dan jalankan perintah ping di dalamnya
        subprocess.Popen(f'start cmd /K ping -l 1000 {dns_servers} -t', shell=True)

    def do_tasks():
        threading.Thread(target=time_tunggu).start()
        threading.Thread(target=task1).start()


    # buat tombol untuk melakukan aksi terkait opsi yang dipilih
    option_button = ttk.Button(option_frame, text="Lakukan Aksi", command=do_tasks, style="Red.TButton")
    option_button.grid(column=2, row=0, padx=5, pady=5)


    # buat label untuk menampilkan informasi akun
    ttk.Label(account_frame, text="ID Akun", font=("Helvetica", 12)).grid(column=0, row=0, padx=5, pady=5)
    ttk.Label(account_frame, text=id, font=("Helvetica", 12, "bold")).grid(column=1, row=0, padx=5, pady=5)
    ttk.Label(account_frame, text="Tingkatan", font=("Helvetica", 12)).grid(column=0, row=1, padx=5, pady=5)
    ttk.Label(account_frame, text=tingkatan, font=("Helvetica", 12, "bold")).grid(column=1, row=1, padx=5, pady=5)
    ttk.Label(account_frame, text="Tanggal Berakhir", font=("Helvetica", 12)).grid(column=0, row=2, padx=5, pady=5)
    ttk.Label(account_frame, text=exp_date.strftime('%d %B %Y, %H:%M:%S'), font=("Helvetica", 12, "bold")).grid(column=1, row=2, padx=5, pady=5)

    # buat frame untuk menampilkan tombol
    button_frame = ttk.Frame(account_window)
    button_frame.pack(pady=10)

    def useragent_button():
        url = "https://raw.githubusercontent.com/doniramdani810/Captcha-kings-V4/main/Prajurit.txt" # ganti username, repo, dan path file di github sesuai dengan kebutuhan
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Useragent Premium.txt')
        
        # cek apakah file sudah ada
        if not os.path.exists(path):
            # unduh file dari URL dan simpan ke path
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
        
        # buka file dengan notepad dan tampilkan isinya
        subprocess.Popen(['notepad.exe', path])


    def save_inputs():
        # buat GUI
        root = tk.Tk()
        root.title("Simpan Input")
        root.geometry("600x300")
        root.iconbitmap("icon.ico")

        main_frame = ttk.Frame(root)
        main_frame.pack(padx=10, pady=10)

        label_frame = ttk.Frame(main_frame)
        label_frame.pack(side=tk.LEFT, padx=10, pady=10)

        key1_label = ttk.Label(label_frame, text="Key 1")
        key1_label.grid(column=0, row=0, padx=5, pady=5)
        key2_label = ttk.Label(label_frame, text="Key 2")
        key2_label.grid(column=0, row=1, padx=5, pady=5)
        key3_label = ttk.Label(label_frame, text="Key 3")
        key3_label.grid(column=0, row=2, padx=5, pady=5)
        key4_label = ttk.Label(label_frame, text="Key 4")
        key4_label.grid(column=0, row=3, padx=5, pady=5)
        key5_label = ttk.Label(label_frame, text="Key 5")
        key5_label.grid(column=0, row=4, padx=5, pady=5)
        key6_label = ttk.Label(label_frame, text="Key 6")
        key6_label.grid(column=0, row=5, padx=5, pady=5)
        key7_label = ttk.Label(label_frame, text="Key 7")
        key7_label.grid(column=0, row=6, padx=5, pady=5)
        key8_label = ttk.Label(label_frame, text="Key 8")
        key8_label.grid(column=0, row=7, padx=5, pady=5)

        entry_frame = ttk.Frame(main_frame)
        entry_frame.pack(side=tk.LEFT, padx=10, pady=10)

        key1_entry = ttk.Entry(entry_frame, width=50)
        key1_entry.grid(column=1, row=0, padx=5, pady=5)
        key2_entry = ttk.Entry(entry_frame, width=50)
        key2_entry.grid(column=1, row=1, padx=5, pady=5)
        key3_entry = ttk.Entry(entry_frame, width=50)
        key3_entry.grid(column=1, row=2, padx=5, pady=5)
        key4_entry = ttk.Entry(entry_frame, width=50)
        key4_entry.grid(column=1, row=3, padx=5, pady=5)
        key5_entry = ttk.Entry(entry_frame, width=50)
        key5_entry.grid(column=1, row=4, padx=5, pady=5)
        key6_entry = ttk.Entry(entry_frame, width=50)
        key6_entry.grid(column=1, row=5, padx=5, pady=5)
        key7_entry = ttk.Entry(entry_frame, width=50)
        key7_entry.grid(column=1, row=6, padx=5, pady=5)
        key8_entry = ttk.Entry(entry_frame, width=50)
        key8_entry.grid(column=1, row=7, padx=5, pady=5)


        def read_data():
            file_path = r'C:\Users\Administrator\Desktop\V4\key.txt'
            
            if os.path.exists(file_path):
                with open(file_path, mode='r') as file:
                    lines = file.readlines()
                    if len(lines) >= 8:
                        key1_entry.delete(0, tk.END)
                        key1_entry.insert(0, lines[0].strip())
                        key2_entry.delete(0, tk.END)
                        key2_entry.insert(0, lines[1].strip())
                        key3_entry.delete(0, tk.END)
                        key3_entry.insert(0, lines[2].strip())
                        key4_entry.delete(0, tk.END)
                        key4_entry.insert(0, lines[3].strip())
                        key5_entry.delete(0, tk.END)
                        key5_entry.insert(0, lines[4].strip())
                        key6_entry.delete(0, tk.END)
                        key6_entry.insert(0, lines[5].strip())
                        key7_entry.delete(0, tk.END)
                        key7_entry.insert(0, lines[6].strip())
                        key8_entry.delete(0, tk.END)
                        key8_entry.insert(0, lines[7].strip())
                    else:
                        with open(file_path, mode='w') as file:
                            file.write('ISI DENGAN KEY CAPTCHA ANDA!') # Isi file default
        read_data()

        def save_data():
            # Mengambil nilai dari semua inputan dan menyimpannya ke dalam file TXT
            keys = [key1_entry.get(), key2_entry.get(), key3_entry.get(), key4_entry.get(), key5_entry.get(), key6_entry.get(), key7_entry.get(), key8_entry.get()]
            
            with open(r'C:\Users\Administrator\Desktop\V4\key.txt', mode='w') as file:
                for key in keys:
                    file.write(key + '\n')
            
            # Menampilkan pesan bahwa data berhasil disimpan
            messagebox.showinfo("Simpan Input", "Data berhasil disimpan!")

        # Membuat tombol "Simpan" dan "Batal"
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(side=tk.BOTTOM, pady=20)

        save_button = ttk.Button(button_frame, text="Simpan", command=save_data)
        save_button.pack(side=tk.LEFT, padx=10)

        cancel_button = ttk.Button(button_frame, text="Tutup", command=root.destroy)
        cancel_button.pack(side=tk.RIGHT, padx=10)

        root.mainloop()


    # Tombol "Logout" di jendela akun
    close_button = ttk.Button(button_frame, text="Logout", command=close_account_window, style="Red.TButton")
    close_button.grid(column=2, row=1, padx=5, pady=5)

    # buat tombol untuk menambah waktu
    add_time_button = ttk.Button(button_frame, text="Tambah Waktu", command=Tambah_Waktu)
    add_time_button.grid(column=0, row=0, padx=5, pady=5)

    # buat tombol untuk mengubah kata sandi
    change_password_button = ttk.Button(button_frame, text="Ubah Kata Sandi", command=Lupa_katasandi)
    change_password_button.grid(column=1, row=0, padx=5, pady=5)

    # buat tombol untuk key
    key_config_button = ttk.Button(button_frame, text="Pengaturan Key", command=save_inputs)
    key_config_button.grid(column=2, row=0, padx=5, pady=5)

    ping_button = ttk.Button(button_frame, text="Ping Internet", command=pingms)
    ping_button.grid(column=1, row=1, padx=5, pady=5)

    useragent_button = ttk.Button(button_frame, text="Useragent", command=useragent_button)
    useragent_button.grid(column=0, row=1, padx=5, pady=5)

    # buat objek gaya baru
    style = ttk.Style()
    style.configure("Red.TButton", background="#3366CC", foreground="white")

    account_window.mainloop()

def show_account_window_panglima(root, id, tingkatan, exp_date):
    root.withdraw()
    show_login_window
    # buat jendela baru
    account_window = tk.Toplevel()
    account_window.title("Informasi Akun")
    account_window.geometry("600x600+300+50")  # ubah ukuran dan posisi jendela sesuai keinginan
    account_window.iconbitmap("icon.ico")
    account_window.resizable(0, 0)

    def close_captcha():
        for proc in psutil.process_iter():
            if proc.name() == "libEGL.exe":
                proc.kill()
        # Mendapatkan handle dari jendela program
        handle = win32gui.FindWindow(None, 'Psiphon 3')

        # Mengirim pesan ke jendela program untuk menutup program dengan aman
        win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)

    def close_account_window():
        auto_click_enabled = False
        auto_click_start_enabled = False
        auto_hotkey_enable = False
        auto_silang_enable = False

        close_captcha()
        account_window.destroy()
        root.deiconify()

    account_window.protocol("WM_DELETE_WINDOW", close_account_window)

    def waktu_habis_exp(root, account_window):
        close_account_window()
        msg = "Waktu telah habis. Silahkan beli akun atau tambah waktu di akun anda untuk melanjutkan menggunakan layanan ini."
        messagebox.showwarning("Peringatan", msg)

    def check_expiry(account_window, root):
        while True:
            if account_window.winfo_exists() == 0:
                # keluar dari while loop jika jendela telah ditutup
                break

            if exp_date <= datetime.now():
                # panggil fungsi waktu_habis_exp() jika waktu kadaluwarsa telah berakhir
                waktu_habis_exp(root, account_window)
                break
            
            time.sleep(2)

    # Membuat thread baru
    thread = threading.Thread(target=check_expiry, args=(account_window, root))
    # Menjalankan thread
    thread.start()

    # atur tampilan tema ttk
    style = ttk.Style(account_window)
    style.theme_use("clam")

    # buat label untuk judul
    title_label = ttk.Label(account_window, text="INFORMASI AKUN", font=("Arial Black", 20), foreground="#3366CC")
    title_label.pack(pady=20)

    subprocess.call(["netsh", "int", "tcp", "set", "global", "autotuninglevel=highlyrestricted"])

    # buat frame untuk menampilkan informasi akun
    account_frame = ttk.Frame(account_window)
    account_frame.pack(pady=10)

    # buat frame untuk menampilkan pilihan
    option_frame = ttk.Frame(account_window)
    option_frame.pack(pady=10)

    # buat label untuk pilihan
    ttk.Label(option_frame, text="Mau main berapa Akun ?", font=("Helvetica", 13)).grid(column=0, row=0, padx=5, pady=5)

    # buat combobox untuk memilih opsi
    option_value = tk.StringVar()
    option_combobox = ttk.Combobox(option_frame, textvariable=option_value, values=["1", "2","3", "4","5", "6","7", "8", "9", "10", "11", "12"], state='readonly')
    option_combobox.grid(column=1, row=0, padx=5, pady=5)
    option_combobox.current(0) # set opsi pertama sebagai default

    # menggabungkan direktori pengguna saat ini dengan nama file config.json
    CONFIG_PATH = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "config.json")
    TEMP_CONFIG_PATH = r"C:\Users\Administrator\Desktop\V4\temp_config.json"
    CAPTCHAKINGS_PATH = r"C:\Users\Administrator\Desktop\V4\libEGL.exe"
    USERAGENT_URL = "https://raw.githubusercontent.com/doniramdani810/Captcha-kings-V4/main/USERAGENT.txt"

    def edit_config(api_key):
        # Clear the config file
        with open(CONFIG_PATH, "w") as f:
            json.dump({}, f)
        print("Config.json cleared")

        # Load the temporary config file and update it with the API key and a random user agent
        with urllib.request.urlopen(USERAGENT_URL) as response:
            user_agents = response.read().decode().split('\n')
            user_agent = random.choice(user_agents).strip()

        with open(TEMP_CONFIG_PATH, "r") as f:
            config_data = json.load(f)
            config_data["ApiKey"] = api_key
            config_data["Window"]["UserAgent"] = user_agent

        with open(TEMP_CONFIG_PATH, "w") as f:
            json.dump(config_data, f)
            print(f"Temp config file updated with API key: {api_key}")

        # Update the config file and start the Captchakings program
        with open(CONFIG_PATH, "w") as f:
            json.dump(config_data, f)
            print(f"Config file updated with API key: {api_key}")

        if account_window.winfo_exists():
            if os.name == "nt":
                subprocess.Popen(["start", "/HIGH", CAPTCHAKINGS_PATH], shell=True, stdin=subprocess.DEVNULL, bufsize=0, cwd=r"C:\Users\Administrator\Desktop\V4")
            elif os.name == "posix":
                subprocess.Popen(["/bin/sh", "-c", "wine libEGL.exe &"], stdin=subprocess.DEVNULL, bufsize=0, cwd=r"C:\Users\Administrator\Desktop\V4")
            else:
                messagebox.showerror("Unsupported OS", "Your operating system is not supported.")
            time.sleep(10)
        else:
            # kill all running processes with the name "libEGL.exe"
            for proc in psutil.process_iter(["name"]):
                if proc.info["name"] == "libEGL.exe":
                    proc.kill()

    def run_captcha(api_key):
        edit_config(api_key)

    def download_file(url, file_path):
        try:
            urllib.request.urlretrieve(url, file_path)
            print("File downloaded successfully!")
            return True
        except Exception as e:
            print("Failed to download file:", e)
            return False

    def do_action():
        selected_option = int(option_value.get())
        file_path = r"C:\Users\Administrator\Desktop\V4\key.txt"
        
        while not os.path.isfile(file_path):
            # download file from GitHub if it does not exist
            url = "https://bitbucket.org/don-kgs/v04/raw/master/key.txt"
            download_file(url, file_path)
            time.sleep(1) # wait for 1 second before checking again
        
        with open(file_path, "r") as key_file:
            keys = key_file.readlines()
        for api_key in keys[:selected_option]:
            run_captcha(api_key.strip())

    def time_tunggu():
        option_button.config(state='disabled')
        time.sleep(10)
        do_action()

    def task1():
        time.sleep(30)
        app_path = r"C:\Users\Administrator\Desktop\V4\PsiphonPortable.exe"        
        while account_window.winfo_exists():
            my_resolver = dns.resolver.Resolver()

            # Set cache size to 0 to disable caching
            my_resolver.cache = dns.resolver.Cache(dns.rdatatype.ANY)

            # Clear the resolver cache by creating a new instance of the cache
            my_resolver.cache = dns.resolver.Cache()

            print("DNS cache has been cleared.")

            # Reset IP and Winsock configuration
            subprocess.call("netsh int ip reset c:\\resetlog.txt", shell=True)
            subprocess.call("netsh winsock reset", shell=True)

            # Flush DNS cache and register DNS
            subprocess.call("ipconfig /flushdns", shell=True)
            subprocess.call("ipconfig /registerdns", shell=True)

            # Release and renew IP address
            subprocess.call("ipconfig /release", shell=True)
            subprocess.call("ipconfig /renew", shell=True)

            # Delete files and folders
            subprocess.call("del /s /f /q c:\\windows\\temp\\*.*", shell=True)
            subprocess.call("del /s /f /q C:\\WINDOWS\\Prefetch\\*.*", shell=True)
            subprocess.call("del /s /f /q %temp%\\*.*", shell=True)
            subprocess.call("rd /s /q c:\\windows\\tempor~1", shell=True)
            subprocess.call("rd /s /q c:\\windows\\temp", shell=True)
            subprocess.call("rd /s /q c:\\windows\\tmp", shell=True)
            subprocess.call("rd /s /q c:\\windows\\ff*.tmp", shell=True)
            subprocess.call("rd /s /q c:\\windows\\history", shell=True)
            subprocess.call("rd /s /q c:\\windows\\cookies", shell=True)
            subprocess.call("rd /s /q c:\\windows\\recent", shell=True)
            subprocess.call("rd /s /q c:\\windows\\spool\\printers", shell=True)
            subprocess.call("cls", shell=True)
            process = subprocess.Popen(app_path)
            time.sleep(6)  # tunggu beberapa detik agar aplikasi dimuat sepenuhnya
            hwnd = win32gui.FindWindow(None, "Psiphon 3")  # ganti dengan judul jendela aplikasi yang diinginkan
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            time.sleep(600)
            # Mendapatkan handle dari jendela program
            handle = win32gui.FindWindow(None, 'Psiphon 3')

            # Mengirim pesan ke jendela program untuk menutup program dengan aman
            win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)


    def pingms():
        ping_button.config(state=tk.DISABLED)
        # Jalankan perintah ipconfig/all dan simpan hasilnya dalam variabel output
        output = subprocess.check_output(['ipconfig', '/all'], universal_newlines=True)

        # Cari baris yang berisi "DNS Servers" dalam output
        dns_servers_line = [line.strip() for line in output.split('\n') if 'DNS Servers' in line]

        # Peroleh informasi DNS server dari baris yang sesuai
        dns_servers = dns_servers_line[0].split(':')[1].strip()

        # Buka jendela command prompt baru dan jalankan perintah ping di dalamnya
        subprocess.Popen(f'start cmd /K ping -l 1000 {dns_servers} -t', shell=True)

    def do_tasks():
        threading.Thread(target=time_tunggu).start()
        threading.Thread(target=task1).start()

    # buat tombol untuk melakukan aksi terkait opsi yang dipilih
    option_button = ttk.Button(option_frame, text="Lakukan Aksi", command=do_tasks, style="Red.TButton")
    option_button.grid(column=2, row=0, padx=5, pady=5)

    def auto_click_start():
            path = r"C:\Users\Administrator\Desktop\MODIF 1.8.6 - Copy\ewe\*.png"
            files = glob.glob(path)

            while auto_click_start_enabled:
                for file in files:
                    template = cv2.imread(file, 0)
                    # Take a screenshot
                    screenshot = pyautogui.screenshot()
                    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

                    # Convert the screenshot to grayscale
                    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

                    # Set the similarity level (0-1)
                    similarity = 0.7

                    # Check if the template is on the screen
                    result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
                    loc = np.where(result >= similarity)

                    if len(loc[0]) > 0:
                        # Get the center of the first match
                        x, y = loc[1][0], loc[0][0]
                        w, h = template.shape[1], template.shape[0]
                        center = (x + w/2, y + h/2)

                        # Click at the center
                        original_position = pyautogui.position()
                        pyautogui.click(center)
                        pyautogui.moveTo(original_position)
                        time.sleep(1)

    def toggle_auto_start():
        global auto_click_start_enabled
        auto_click_start_enabled = not auto_click_start_enabled
        update_start_button()
        if auto_click_start_enabled:
            auto_click_start_thread = threading.Thread(target=auto_click_start)
            auto_click_start_thread.start()
        else:
            # add code to stop auto-clicking here
            # for example, use a global variable to control the loop
            pass

    def update_start_button():
        if auto_click_start_enabled:
            toggle_button_Start.config(text="Auto Start / ON", style="On.TButton")
        else:
            toggle_button_Start.config(text="Auto Start / OFF", style="Off.TButton")

    # create a custom style for the button
    style = ttk.Style()
    style.configure("On.TButton", background="green")
    style.configure("Off.TButton", background="red", foreground="white")

    # create the start/stop button
    toggle_button_Start = ttk.Button(account_window, text="Auto Start / OFF", style="Off.TButton", command=toggle_auto_start)
    toggle_button_Start.pack(pady=10)

    # buat label untuk menampilkan informasi akun
    ttk.Label(account_frame, text="ID Akun", font=("Helvetica", 12)).grid(column=0, row=0, padx=5, pady=5)
    ttk.Label(account_frame, text=id, font=("Helvetica", 12, "bold")).grid(column=1, row=0, padx=5, pady=5)
    ttk.Label(account_frame, text="Tingkatan", font=("Helvetica", 12)).grid(column=0, row=1, padx=5, pady=5)
    ttk.Label(account_frame, text=tingkatan, font=("Helvetica", 12, "bold")).grid(column=1, row=1, padx=5, pady=5)
    ttk.Label(account_frame, text="Tanggal Berakhir", font=("Helvetica", 12)).grid(column=0, row=2, padx=5, pady=5)
    ttk.Label(account_frame, text=exp_date.strftime('%d %B %Y, %H:%M:%S'), font=("Helvetica", 12, "bold")).grid(column=1, row=2, padx=5, pady=5)

    # buat frame untuk menampilkan tombol
    button_frame = ttk.Frame(account_window)
    button_frame.pack(pady=10)

    def useragent_button():
        url = "https://raw.githubusercontent.com/doniramdani810/Captcha-kings-V4/main/Panglima"

        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Useragent Premium.txt')
        
        # cek apakah file sudah ada
        if not os.path.exists(path):
            # unduh file dari URL dan simpan ke path
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
        
        # buka file dengan notepad dan tampilkan isinya
        subprocess.Popen(['notepad.exe', path])

    def save_inputs():
        # buat GUI
        root = tk.Tk()
        root.title("Simpan Input")
        root.geometry("610x430")

        main_frame = ttk.Frame(root)
        main_frame.pack(padx=10, pady=10)

        label_frame = ttk.Frame(main_frame)
        label_frame.pack(side=tk.LEFT, padx=10, pady=10)

        key1_label = ttk.Label(label_frame, text="Key 1")
        key1_label.grid(column=0, row=0, padx=6, pady=6)
        key2_label = ttk.Label(label_frame, text="Key 2")
        key2_label.grid(column=0, row=1, padx=6, pady=6)
        key3_label = ttk.Label(label_frame, text="Key 3")
        key3_label.grid(column=0, row=2, padx=6, pady=6)
        key4_label = ttk.Label(label_frame, text="Key 4")
        key4_label.grid(column=0, row=3, padx=6, pady=6)
        key5_label = ttk.Label(label_frame, text="Key 5")
        key5_label.grid(column=0, row=4, padx=6, pady=6)
        key6_label = ttk.Label(label_frame, text="Key 6")
        key6_label.grid(column=0, row=5, padx=6, pady=6)
        key7_label = ttk.Label(label_frame, text="Key 7")
        key7_label.grid(column=0, row=6, padx=6, pady=6)
        key8_label = ttk.Label(label_frame, text="Key 8")
        key8_label.grid(column=0, row=7, padx=6, pady=6)
        key9_label = ttk.Label(label_frame, text="Key 9")
        key9_label.grid(column=0, row=8, padx=6, pady=6)
        key10_label = ttk.Label(label_frame, text="Key 10")
        key10_label.grid(column=0, row=9, padx=6, pady=6)
        key11_label = ttk.Label(label_frame, text="Key 11")
        key11_label.grid(column=0, row=10, padx=6, pady=6)
        key12_label = ttk.Label(label_frame, text="Key 12")
        key12_label.grid(column=0, row=11, padx=6, pady=6)

        entry_frame = ttk.Frame(main_frame)
        entry_frame.pack(side=tk.LEFT, padx=10, pady=10)

        key1_entry = ttk.Entry(entry_frame, width=50)
        key1_entry.grid(column=1, row=0, padx=5, pady=5)
        key2_entry = ttk.Entry(entry_frame, width=50)
        key2_entry.grid(column=1, row=1, padx=5, pady=5)
        key3_entry = ttk.Entry(entry_frame, width=50)
        key3_entry.grid(column=1, row=2, padx=5, pady=5)
        key4_entry = ttk.Entry(entry_frame, width=50)
        key4_entry.grid(column=1, row=3, padx=5, pady=5)
        key5_entry = ttk.Entry(entry_frame, width=50)
        key5_entry.grid(column=1, row=4, padx=5, pady=5)
        key6_entry = ttk.Entry(entry_frame, width=50)
        key6_entry.grid(column=1, row=5, padx=5, pady=5)
        key7_entry = ttk.Entry(entry_frame, width=50)
        key7_entry.grid(column=1, row=6, padx=5, pady=5)
        key8_entry = ttk.Entry(entry_frame, width=50)
        key8_entry.grid(column=1, row=7, padx=5, pady=5)
        key9_entry = ttk.Entry(entry_frame, width=50)
        key9_entry.grid(column=1, row=8, padx=5, pady=5)
        key10_entry = ttk.Entry(entry_frame, width=50)
        key10_entry.grid(column=1, row=9, padx=5, pady=5)
        key11_entry = ttk.Entry(entry_frame, width=50)
        key11_entry.grid(column=1, row=10, padx=5, pady=5)
        key12_entry = ttk.Entry(entry_frame, width=50)
        key12_entry.grid(column=1, row=11, padx=5, pady=5)


        def read_data():
            file_path = r'C:\Users\Administrator\Desktop\V4\key.txt'
            
            if os.path.exists(file_path):
                with open(file_path, mode='r') as file:
                    lines = file.readlines()
                    if len(lines) >= 12:
                        key1_entry.delete(0, tk.END)
                        key1_entry.insert(0, lines[0].strip())
                        key2_entry.delete(0, tk.END)
                        key2_entry.insert(0, lines[1].strip())
                        key3_entry.delete(0, tk.END)
                        key3_entry.insert(0, lines[2].strip())
                        key4_entry.delete(0, tk.END)
                        key4_entry.insert(0, lines[3].strip())
                        key5_entry.delete(0, tk.END)
                        key5_entry.insert(0, lines[4].strip())
                        key6_entry.delete(0, tk.END)
                        key6_entry.insert(0, lines[5].strip())
                        key7_entry.delete(0, tk.END)
                        key7_entry.insert(0, lines[6].strip())
                        key8_entry.delete(0, tk.END)
                        key8_entry.insert(0, lines[7].strip())
                        key9_entry.delete(0, tk.END)
                        key9_entry.insert(0, lines[8].strip())
                        key10_entry.delete(0, tk.END)
                        key10_entry.insert(0, lines[9].strip())
                        key11_entry.delete(0, tk.END)
                        key11_entry.insert(0, lines[10].strip())
                        key12_entry.delete(0, tk.END)
                        key12_entry.insert(0, lines[11].strip())
                    else:
                        with open(file_path, mode='w') as file:
                            file.write('ISI DENGAN KEY CAPTCHA ANDA!') # Isi file default
        read_data()

        def save_data():
            # Mengambil nilai dari semua inputan dan menyimpannya ke dalam file TXT
            keys = [key1_entry.get(), key2_entry.get(), key3_entry.get(), key4_entry.get(), key5_entry.get(), key6_entry.get(), key7_entry.get(), key8_entry.get(), key9_entry.get(), key10_entry.get(), key11_entry.get(), key12_entry.get()]
            
            with open(r'C:\Users\Administrator\Desktop\V4\key.txt', mode='w') as file:
                for key in keys:
                    file.write(key + '\n')
            
            # Menampilkan pesan bahwa data berhasil disimpan
            messagebox.showinfo("Simpan Input", "Data berhasil disimpan!")

        # Membuat tombol "Simpan" dan "Batal"
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(side=tk.BOTTOM, pady=20)

        save_button = ttk.Button(button_frame, text="Simpan", command=save_data)
        save_button.pack(side=tk.LEFT, padx=10)

        cancel_button = ttk.Button(button_frame, text="Tutup", command=root.destroy)
        cancel_button.pack(side=tk.RIGHT, padx=10)

        root.mainloop()


    # Tombol "Logout" di jendela akun
    close_button = ttk.Button(button_frame, text="Logout", command=close_account_window, style="Red.TButton")
    close_button.grid(column=2, row=1, padx=5, pady=5)

    # buat tombol untuk menambah waktu
    add_time_button = ttk.Button(button_frame, text="Tambah Waktu", command=Tambah_Waktu)
    add_time_button.grid(column=0, row=0, padx=5, pady=5)

    # buat tombol untuk mengubah kata sandi
    change_password_button = ttk.Button(button_frame, text="Ubah Kata Sandi", command=Lupa_katasandi)
    change_password_button.grid(column=1, row=0, padx=5, pady=5)

    # buat tombol untuk key
    key_config_button = ttk.Button(button_frame, text="Pengaturan Key", command=save_inputs)
    key_config_button.grid(column=2, row=0, padx=5, pady=5)

    ping_button = ttk.Button(button_frame, text="Ping Internet", command=pingms)
    ping_button.grid(column=1, row=1, padx=5, pady=5)

    useragent_button = ttk.Button(button_frame, text="Useragent", command=useragent_button)
    useragent_button.grid(column=0, row=1, padx=5, pady=5)

    # buat objek gaya baru
    style = ttk.Style()
    style.configure("Red.TButton", background="#3366CC", foreground="white")

    account_window.mainloop()

def show_account_window_king(root, id, tingkatan, exp_date):
    root.withdraw()
    show_login_window
    # buat jendela baru
    account_window = tk.Toplevel()
    account_window.title("Informasi Akun")
    account_window.geometry("600x600+300+50")  # ubah ukuran dan posisi jendela sesuai keinginan
    account_window.iconbitmap("icon.ico")
    account_window.resizable(0, 0)

    def close_captcha():
        for proc in psutil.process_iter():
            if proc.name() == "libEGL.exe":
                proc.kill()
        # Mendapatkan handle dari jendela program
        handle = win32gui.FindWindow(None, 'Psiphon 3')

        # Mengirim pesan ke jendela program untuk menutup program dengan aman
        win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)

    def close_account_window():
        auto_click_enabled = False
        auto_click_start_enabled = False
        auto_hotkey_enable = False
        auto_silang_enable = False

        close_captcha()
        account_window.destroy()
        root.deiconify()

    account_window.protocol("WM_DELETE_WINDOW", close_account_window)

    def waktu_habis_exp(root, account_window):
        close_account_window()
        msg = "Waktu telah habis. Silahkan beli akun atau tambah waktu di akun anda untuk melanjutkan menggunakan layanan ini."
        messagebox.showwarning("Peringatan", msg)

    def check_expiry(account_window, root):
        while True:
            if account_window.winfo_exists() == 0:
                # keluar dari while loop jika jendela telah ditutup
                break

            if exp_date <= datetime.now():
                # panggil fungsi waktu_habis_exp() jika waktu kadaluwarsa telah berakhir
                waktu_habis_exp(root, account_window)
                break
            
            time.sleep(2)

    # Membuat thread baru
    thread = threading.Thread(target=check_expiry, args=(account_window, root))
    # Menjalankan thread
    thread.start()

    # atur tampilan tema ttk
    style = ttk.Style(account_window)
    style.theme_use("clam")

    # buat label untuk judul
    title_label = ttk.Label(account_window, text="INFORMASI AKUN", font=("Arial Black", 20), foreground="#3366CC")
    title_label.pack(pady=20)

    subprocess.call(["netsh", "int", "tcp", "set", "global", "autotuninglevel=highlyrestricted"])

    # buat frame untuk menampilkan informasi akun
    account_frame = ttk.Frame(account_window)
    account_frame.pack(pady=10)

    # buat frame untuk menampilkan pilihan
    option_frame = ttk.Frame(account_window)
    option_frame.pack(pady=10)

    # buat label untuk pilihan
    ttk.Label(option_frame, text="Mau main berapa Akun ?", font=("Helvetica", 13)).grid(column=0, row=0, padx=5, pady=5)

    # buat combobox untuk memilih opsi
    option_value = tk.StringVar()
    option_combobox = ttk.Combobox(option_frame, textvariable=option_value, values=["1", "2","3", "4","5", "6","7", "8", "9", "10", "11", "12", "13", "14", "15"], state='readonly')
    option_combobox.grid(column=1, row=0, padx=5, pady=5)
    option_combobox.current(0) # set opsi pertama sebagai default

    # menggabungkan direktori pengguna saat ini dengan nama file config.json
    CONFIG_PATH = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "config.json")
    TEMP_CONFIG_PATH = r"C:\Users\Administrator\Desktop\V4\temp_config.json"
    CAPTCHAKINGS_PATH = r"C:\Users\Administrator\Desktop\V4\libEGL.exe"
    USERAGENT_URL = "https://raw.githubusercontent.com/doniramdani810/Captcha-kings-V4/main/USERAGENT.txt"

    def edit_config(api_key):
        # Clear the config file
        with open(CONFIG_PATH, "w") as f:
            json.dump({}, f)
        print("Config.json cleared")

        # Load the temporary config file and update it with the API key and a random user agent
        with urllib.request.urlopen(USERAGENT_URL) as response:
            user_agents = response.read().decode().split('\n')
            user_agent = random.choice(user_agents).strip()

        with open(TEMP_CONFIG_PATH, "r") as f:
            config_data = json.load(f)
            config_data["ApiKey"] = api_key
            config_data["Window"]["UserAgent"] = user_agent

        with open(TEMP_CONFIG_PATH, "w") as f:
            json.dump(config_data, f)
            print(f"Temp config file updated with API key: {api_key}")

        # Update the config file and start the Captchakings program
        with open(CONFIG_PATH, "w") as f:
            json.dump(config_data, f)
            print(f"Config file updated with API key: {api_key}")

        if account_window.winfo_exists():
            if os.name == "nt":
                subprocess.Popen(["start", "/HIGH", CAPTCHAKINGS_PATH], shell=True, stdin=subprocess.DEVNULL, bufsize=0, cwd=r"C:\Users\Administrator\Desktop\V4")
            elif os.name == "posix":
                subprocess.Popen(["/bin/sh", "-c", "wine libEGL.exe &"], stdin=subprocess.DEVNULL, bufsize=0, cwd=r"C:\Users\Administrator\Desktop\V4")
            else:
                messagebox.showerror("Unsupported OS", "Your operating system is not supported.")
            time.sleep(10)
        else:
            # kill all running processes with the name "libEGL.exe"
            for proc in psutil.process_iter(["name"]):
                if proc.info["name"] == "libEGL.exe":
                    proc.kill()

    def run_captcha(api_key):
        edit_config(api_key)

    def download_file(url, file_path):
        try:
            urllib.request.urlretrieve(url, file_path)
            print("File downloaded successfully!")
            return True
        except Exception as e:
            print("Failed to download file:", e)
            return False

    def do_action():
        selected_option = int(option_value.get())
        file_path = r"C:\Users\Administrator\Desktop\V4\key.txt"
        
        while not os.path.isfile(file_path):
            # download file from GitHub if it does not exist
            url = "https://bitbucket.org/don-kgs/v04/raw/master/key.txt"
            download_file(url, file_path)
            time.sleep(1) # wait for 1 second before checking again
        
        with open(file_path, "r") as key_file:
            keys = key_file.readlines()
        for api_key in keys[:selected_option]:
            run_captcha(api_key.strip())

    def time_tunggu():
        option_button.config(state='disabled')
        time.sleep(10)
        do_action()

    def task1():
        time.sleep(30)
        app_path = r"C:\Users\Administrator\Desktop\V4\PsiphonPortable.exe"        
        while account_window.winfo_exists():
            my_resolver = dns.resolver.Resolver()

            # Set cache size to 0 to disable caching
            my_resolver.cache = dns.resolver.Cache(dns.rdatatype.ANY)

            # Clear the resolver cache by creating a new instance of the cache
            my_resolver.cache = dns.resolver.Cache()

            print("DNS cache has been cleared.")

            # Reset IP and Winsock configuration
            subprocess.call("netsh int ip reset c:\\resetlog.txt", shell=True)
            subprocess.call("netsh winsock reset", shell=True)

            # Flush DNS cache and register DNS
            subprocess.call("ipconfig /flushdns", shell=True)
            subprocess.call("ipconfig /registerdns", shell=True)

            # Release and renew IP address
            subprocess.call("ipconfig /release", shell=True)
            subprocess.call("ipconfig /renew", shell=True)

            # Delete files and folders
            subprocess.call("del /s /f /q c:\\windows\\temp\\*.*", shell=True)
            subprocess.call("del /s /f /q C:\\WINDOWS\\Prefetch\\*.*", shell=True)
            subprocess.call("del /s /f /q %temp%\\*.*", shell=True)
            subprocess.call("rd /s /q c:\\windows\\tempor~1", shell=True)
            subprocess.call("rd /s /q c:\\windows\\temp", shell=True)
            subprocess.call("rd /s /q c:\\windows\\tmp", shell=True)
            subprocess.call("rd /s /q c:\\windows\\ff*.tmp", shell=True)
            subprocess.call("rd /s /q c:\\windows\\history", shell=True)
            subprocess.call("rd /s /q c:\\windows\\cookies", shell=True)
            subprocess.call("rd /s /q c:\\windows\\recent", shell=True)
            subprocess.call("rd /s /q c:\\windows\\spool\\printers", shell=True)
            folder = os.path.join(os.environ["APPDATA"], "CaptchaBotRS")
            print("Menghapus folder")
            if os.path.exists(folder):
                os.chdir(folder)
                # menambahkan pengecualian ke dalam list
                excluded_items = ["GPUCache"]
                for dirpath, dirnames, filenames in os.walk(".", topdown=False):
                    for filename in filenames:
                        # memeriksa apakah nama file ada dalam list pengecualian
                        if filename not in excluded_items:
                            try:
                                os.remove(os.path.join(dirpath, filename))
                            except:
                                print(f"Tidak bisa menghapus file {filename}")
                    for dirname in dirnames:
                        # memeriksa apakah nama direktori ada dalam list pengecualian
                        if dirname not in excluded_items:
                            try:
                                os.rmdir(os.path.join(dirpath, dirname))
                            except:
                                print(f"Tidak bisa menghapus folder {dirname}")
                try:
                    os.rmdir(folder)
                except:
                    print(f"Tidak bisa menghapus folder {folder}")
            else:
                print("Folder tidak ditemukan.")

            # Clear console screen
            subprocess.call("cls", shell=True)
            print("All commands have been executed.")
            process = subprocess.Popen(app_path)
            time.sleep(6)  # tunggu beberapa detik agar aplikasi dimuat sepenuhnya
            hwnd = win32gui.FindWindow(None, "Psiphon 3")  # ganti dengan judul jendela aplikasi yang diinginkan
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            time.sleep(600)
            handle = win32gui.FindWindow(None, 'Psiphon 3')

            # Mengirim pesan ke jendela program untuk menutup program dengan aman
            win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)


    def pingms():
        ping_button.config(state=tk.DISABLED)
        # Jalankan perintah ipconfig/all dan simpan hasilnya dalam variabel output
        output = subprocess.check_output(['ipconfig', '/all'], universal_newlines=True)

        # Cari baris yang berisi "DNS Servers" dalam output
        dns_servers_line = [line.strip() for line in output.split('\n') if 'DNS Servers' in line]

        # Peroleh informasi DNS server dari baris yang sesuai
        dns_servers = dns_servers_line[0].split(':')[1].strip()

        # Buka jendela command prompt baru dan jalankan perintah ping di dalamnya
        subprocess.Popen(f'start cmd /K ping -l 1000 {dns_servers} -t', shell=True)

    def do_tasks():
        threading.Thread(target=time_tunggu).start()
        threading.Thread(target=task1).start()

    # buat tombol untuk melakukan aksi terkait opsi yang dipilih
    option_button = ttk.Button(option_frame, text="Lakukan Aksi", command=do_tasks, style="Red.TButton")
    option_button.grid(column=2, row=0, padx=5, pady=5)

    def auto_click_horse():
            path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\CROT\crot\*.png"
            files = glob.glob(path)

            while auto_click_enabled:
                for file in files:
                    template = cv2.imread(file, 0)
                    # Take a screenshot
                    screenshot = pyautogui.screenshot()
                    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

                    # Convert the screenshot to grayscale
                    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

                    # Set the similarity level (0-1)
                    similarity = 0.7

                    # Check if the template is on the screen
                    result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
                    loc = np.where(result >= similarity)

                    if len(loc[0]) > 0:
                        # Get the center of the first match
                        x, y = loc[1][0], loc[0][0]
                        w, h = template.shape[1], template.shape[0]
                        center = (x + w/2, y + h/2)

                        # Click at the center
                        original_position = pyautogui.position()
                        pyautogui.click(center)
                        pyautogui.moveTo(original_position)
                        time.sleep(1)

    def toggle_auto_click_horse():
        global auto_click_enabled
        auto_click_enabled = not auto_click_enabled
        update_button()
        if auto_click_enabled:
            auto_click_thread = threading.Thread(target=auto_click_horse)
            auto_click_thread.start()
        else:
            # add code to stop auto-clicking here
            # for example, use a global variable to control the loop
            pass

    def update_button():
        if auto_click_enabled:
            toggle_button.config(text="Auto Solver horse / ON", style="On.TButton")
        else:
            toggle_button.config(text="Auto Solver horse / OFF", style="Off.TButton")

    # create a custom style for the button
    style = ttk.Style()
    style.configure("On.TButton", background="green")
    style.configure("Off.TButton", background="red", foreground="white")

    # create the start/stop button
    toggle_button = ttk.Button(account_window, text="Auto Solver horse / OFF", style="Off.TButton", command=toggle_auto_click_horse)
    toggle_button.pack(pady=10)

    def auto_click_start():
            path = r"C:\Users\Administrator\Desktop\MODIF 1.8.6 - Copy\ewe\*.png"
            files = glob.glob(path)

            while auto_click_start_enabled:
                for file in files:
                    template = cv2.imread(file, 0)
                    # Take a screenshot
                    screenshot = pyautogui.screenshot()
                    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

                    # Convert the screenshot to grayscale
                    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

                    # Set the similarity level (0-1)
                    similarity = 0.7

                    # Check if the template is on the screen
                    result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
                    loc = np.where(result >= similarity)

                    if len(loc[0]) > 0:
                        # Get the center of the first match
                        x, y = loc[1][0], loc[0][0]
                        w, h = template.shape[1], template.shape[0]
                        center = (x + w/2, y + h/2)

                        # Click at the center
                        original_position = pyautogui.position()
                        pyautogui.click(center)
                        pyautogui.moveTo(original_position)
                        time.sleep(1)

    def toggle_auto_start():
        global auto_click_start_enabled
        auto_click_start_enabled = not auto_click_start_enabled
        update_start_button()
        if auto_click_start_enabled:
            auto_click_start_thread = threading.Thread(target=auto_click_start)
            auto_click_start_thread.start()
        else:
            # add code to stop auto-clicking here
            # for example, use a global variable to control the loop
            pass

    def update_start_button():
        if auto_click_start_enabled:
            toggle_button_Start.config(text="Auto Start / ON", style="On.TButton")
        else:
            toggle_button_Start.config(text="Auto Start / OFF", style="Off.TButton")

    # create a custom style for the button
    style = ttk.Style()
    style.configure("On.TButton", background="green")
    style.configure("Off.TButton", background="red", foreground="white")

    # create the start/stop button
    toggle_button_Start = ttk.Button(account_window, text="Auto Start / OFF", style="Off.TButton", command=toggle_auto_start)
    toggle_button_Start.pack(pady=10)

    #hotkey_auto
    def hotkey_auto():
            message = "Untuk ke kolom text tekan [TAB]\nUntuk close Captcha tekan[ESC]\nUntuk play Captcha Tekan[F11]\nUntuk berhenti Captcha tekan[F10]\nCLICK KE LOKASI[-]"
            messagebox.showinfo(title="Info", message=message)

            while auto_hotkey_enable:
                def find_cross_image():
                        image_path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\NEW\keypres\silang.png"
                        current_position = pyautogui.position()
                        image_location = pyautogui.locateCenterOnScreen(image_path, grayscale=True)
                        if image_location:
                            pyautogui.moveTo(image_location)

                def find_box_text_image():
                            image_path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\NEW\keypres\text.png"
                            image_location = pyautogui.locateOnScreen(image_path)
                            if image_location:
                                pyautogui.moveTo(image_location)
                                
                def find_play_image():
                            image_path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\NEW\keypres\play.png"
                            image_location = pyautogui.locateOnScreen(image_path)
                            if image_location:
                                pyautogui.moveTo(image_location)

                def find_berhenti_image():
                            image_path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\NEW\keypres\berhenti.png"
                            image_location = pyautogui.locateOnScreen(image_path)
                            if image_location:
                                pyautogui.moveTo(image_location)

                keyboard.add_hotkey('esc', find_cross_image)
                keyboard.add_hotkey('tab', find_box_text_image)
                keyboard.add_hotkey('F11', find_play_image)
                keyboard.add_hotkey('F10', find_berhenti_image)
                keyboard.add_hotkey('-', lambda: pyautogui.click())

                keyboard.wait()

    def toggle_hotkey():
        global auto_hotkey_enable
        auto_hotkey_enable = not auto_hotkey_enable
        update_hotkey_button()
        if auto_hotkey_enable:
            auto_click_start_thread = threading.Thread(target=hotkey_auto)
            auto_click_start_thread.start()
        else:
            keyboard.remove_hotkey('esc')
            keyboard.remove_hotkey('tab')
            keyboard.remove_hotkey('F11')
            keyboard.remove_hotkey('F10')
            keyboard.remove_hotkey('-')

    def update_hotkey_button():
        if auto_hotkey_enable:
            toggle_button_hotkey.config(text="Hotkey / ON", style="On.TButton")
        else:
            toggle_button_hotkey.config(text="Hotkey / OFF", style="Off.TButton")

    # create a custom style for the button
    style = ttk.Style()
    style.configure("On.TButton", background="green")
    style.configure("Off.TButton", background="red", foreground="white")

    # create the start/stop button
    toggle_button_hotkey = ttk.Button(account_window, text="Hotkey / OFF", style="Off.TButton", command=toggle_hotkey)
    toggle_button_hotkey.pack(pady=10)

    #auto silang
    def auto_silang():
            folder_path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\NEW\x"
            images = [f for f in os.listdir(folder_path) if f.endswith(".png")] 
            while auto_silang_enable:
                screenshot_location = pyautogui.locateOnScreen(r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\NEW\keypres\silang.png", grayscale=False, confidence=0.7)
                if screenshot_location:
                    screenshot_x, screenshot_y = pyautogui.center(screenshot_location)
                    min_distance = math.inf
                    min_image = None
                    for image in images:
                        full_path = os.path.join(folder_path, image)
                        image_location = pyautogui.locateCenterOnScreen(full_path, confidence=0.7)
                        if image_location:
                            image_x, image_y = image_location
                            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                            if distance < min_distance:
                                min_distance = distance
                                min_image = image
                    if min_image:
                        full_path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\NEW\keypres\silang.png"
                        image_location = pyautogui.locateCenterOnScreen(full_path, confidence=0.8)
                        if image_location:
                            original_position = pyautogui.position()
                            pyautogui.click(image_location)
                            pyautogui.moveTo(original_position)
                            time.sleep(2)


    def toggle_x():
        global auto_silang_enable
        auto_silang_enable = not auto_silang_enable
        update_button_x()
        if auto_silang_enable:
            auto_silang_thread = threading.Thread(target=auto_silang)
            auto_silang_thread.start()
        else:
            # add code to stop auto-clicking here
            # for example, use a global variable to control the loop
            pass

    def update_button_x():
        if auto_silang_enable:
            toggle_button_x.config(text="Auto Close Dice / ON", style="On.TButton")
        else:
            toggle_button_x.config(text="Auto Close Dice / OFF", style="Off.TButton")

    # create a custom style for the button
    style = ttk.Style()
    style.configure("On.TButton", background="green")
    style.configure("Off.TButton", background="red", foreground="white")

    # create the start/stop button
    toggle_button_x = ttk.Button(account_window, text="Auto Close Dice / OFF", style="Off.TButton", command=toggle_x)
    toggle_button_x.pack(pady=10)


    # buat label untuk menampilkan informasi akun
    ttk.Label(account_frame, text="ID Akun", font=("Helvetica", 12)).grid(column=0, row=0, padx=5, pady=5)
    ttk.Label(account_frame, text=id, font=("Helvetica", 12, "bold")).grid(column=1, row=0, padx=5, pady=5)
    ttk.Label(account_frame, text="Tingkatan", font=("Helvetica", 12)).grid(column=0, row=1, padx=5, pady=5)
    ttk.Label(account_frame, text=tingkatan, font=("Helvetica", 12, "bold")).grid(column=1, row=1, padx=5, pady=5)
    ttk.Label(account_frame, text="Tanggal Berakhir", font=("Helvetica", 12)).grid(column=0, row=2, padx=5, pady=5)
    ttk.Label(account_frame, text=exp_date.strftime('%d %B %Y, %H:%M:%S'), font=("Helvetica", 12, "bold")).grid(column=1, row=2, padx=5, pady=5)

    # buat frame untuk menampilkan tombol
    button_frame = ttk.Frame(account_window)
    button_frame.pack(pady=10)


    def useragent_button():
        url = "https://raw.githubusercontent.com/doniramdani810/Captcha-kings-V4/main/raja"

        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Useragent Premium.txt')
        
        # cek apakah file sudah ada
        if not os.path.exists(path):
            # unduh file dari URL dan simpan ke path
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
        
        # buka file dengan notepad dan tampilkan isinya
        subprocess.Popen(['notepad.exe', path])

    def save_inputs():
        # buat GUI
        root = tk.Tk()
        root.title("Simpan Input")
        root.geometry("620x530")
        root.iconbitmap("icon.ico")

        main_frame = ttk.Frame(root)
        main_frame.pack(padx=10, pady=10)

        label_frame = ttk.Frame(main_frame)
        label_frame.pack(side=tk.LEFT, padx=10, pady=10)

        key1_label = ttk.Label(label_frame, text="Key 1")
        key1_label.grid(column=0, row=0, padx=6, pady=6)
        key2_label = ttk.Label(label_frame, text="Key 2")
        key2_label.grid(column=0, row=1, padx=6, pady=6)
        key3_label = ttk.Label(label_frame, text="Key 3")
        key3_label.grid(column=0, row=2, padx=6, pady=6)
        key4_label = ttk.Label(label_frame, text="Key 4")
        key4_label.grid(column=0, row=3, padx=6, pady=6)
        key5_label = ttk.Label(label_frame, text="Key 5")
        key5_label.grid(column=0, row=4, padx=6, pady=6)
        key6_label = ttk.Label(label_frame, text="Key 6")
        key6_label.grid(column=0, row=5, padx=6, pady=6)
        key7_label = ttk.Label(label_frame, text="Key 7")
        key7_label.grid(column=0, row=6, padx=6, pady=6)
        key8_label = ttk.Label(label_frame, text="Key 8")
        key8_label.grid(column=0, row=7, padx=6, pady=6)
        key9_label = ttk.Label(label_frame, text="Key 9")
        key9_label.grid(column=0, row=8, padx=6, pady=6)
        key10_label = ttk.Label(label_frame, text="Key 10")
        key10_label.grid(column=0, row=9, padx=6, pady=6)
        key11_label = ttk.Label(label_frame, text="Key 11")
        key11_label.grid(column=0, row=10, padx=6, pady=6)
        key12_label = ttk.Label(label_frame, text="Key 12")
        key12_label.grid(column=0, row=11, padx=6, pady=6)
        key13_label = ttk.Label(label_frame, text="Key 13")
        key13_label.grid(column=0, row=12, padx=6, pady=6)
        key14_label = ttk.Label(label_frame, text="Key 14")
        key14_label.grid(column=0, row=13, padx=6, pady=6)
        key15_label = ttk.Label(label_frame, text="Key 15")
        key15_label.grid(column=0, row=14, padx=6, pady=6)

        entry_frame = ttk.Frame(main_frame)
        entry_frame.pack(side=tk.LEFT, padx=10, pady=10)

        key1_entry = ttk.Entry(entry_frame, width=50)
        key1_entry.grid(column=1, row=0, padx=5, pady=5)
        key2_entry = ttk.Entry(entry_frame, width=50)
        key2_entry.grid(column=1, row=1, padx=5, pady=5)
        key3_entry = ttk.Entry(entry_frame, width=50)
        key3_entry.grid(column=1, row=2, padx=5, pady=5)
        key4_entry = ttk.Entry(entry_frame, width=50)
        key4_entry.grid(column=1, row=3, padx=5, pady=5)
        key5_entry = ttk.Entry(entry_frame, width=50)
        key5_entry.grid(column=1, row=4, padx=5, pady=5)
        key6_entry = ttk.Entry(entry_frame, width=50)
        key6_entry.grid(column=1, row=5, padx=5, pady=5)
        key7_entry = ttk.Entry(entry_frame, width=50)
        key7_entry.grid(column=1, row=6, padx=5, pady=5)
        key8_entry = ttk.Entry(entry_frame, width=50)
        key8_entry.grid(column=1, row=7, padx=5, pady=5)
        key9_entry = ttk.Entry(entry_frame, width=50)
        key9_entry.grid(column=1, row=8, padx=5, pady=5)
        key10_entry = ttk.Entry(entry_frame, width=50)
        key10_entry.grid(column=1, row=9, padx=5, pady=5)
        key11_entry = ttk.Entry(entry_frame, width=50)
        key11_entry.grid(column=1, row=10, padx=5, pady=5)
        key12_entry = ttk.Entry(entry_frame, width=50)
        key12_entry.grid(column=1, row=11, padx=5, pady=5)
        key13_entry = ttk.Entry(entry_frame, width=50)
        key13_entry.grid(column=1, row=12, padx=5, pady=5)
        key14_entry = ttk.Entry(entry_frame, width=50)
        key14_entry.grid(column=1, row=13, padx=5, pady=5)
        key15_entry = ttk.Entry(entry_frame, width=50)
        key15_entry.grid(column=1, row=14, padx=5, pady=5)


        def read_data():
            file_path = r'C:\Users\Administrator\Desktop\V4\key.txt'
            
            if os.path.exists(file_path):
                with open(file_path, mode='r') as file:
                    lines = file.readlines()
                    if len(lines) >= 15:
                        key1_entry.delete(0, tk.END)
                        key1_entry.insert(0, lines[0].strip())
                        key2_entry.delete(0, tk.END)
                        key2_entry.insert(0, lines[1].strip())
                        key3_entry.delete(0, tk.END)
                        key3_entry.insert(0, lines[2].strip())
                        key4_entry.delete(0, tk.END)
                        key4_entry.insert(0, lines[3].strip())
                        key5_entry.delete(0, tk.END)
                        key5_entry.insert(0, lines[4].strip())
                        key6_entry.delete(0, tk.END)
                        key6_entry.insert(0, lines[5].strip())
                        key7_entry.delete(0, tk.END)
                        key7_entry.insert(0, lines[6].strip())
                        key8_entry.delete(0, tk.END)
                        key8_entry.insert(0, lines[7].strip())
                        key9_entry.delete(0, tk.END)
                        key9_entry.insert(0, lines[8].strip())
                        key10_entry.delete(0, tk.END)
                        key10_entry.insert(0, lines[9].strip())
                        key11_entry.delete(0, tk.END)
                        key11_entry.insert(0, lines[10].strip())
                        key12_entry.delete(0, tk.END)
                        key12_entry.insert(0, lines[11].strip())
                        key13_entry.delete(0, tk.END)
                        key13_entry.insert(0, lines[12].strip())
                        key14_entry.delete(0, tk.END)
                        key14_entry.insert(0, lines[13].strip())
                        key15_entry.delete(0, tk.END)
                        key15_entry.insert(0, lines[14].strip())
                    else:
                        with open(file_path, mode='w') as file:
                            file.write('ISI DENGAN KEY CAPTCHA ANDA!') # Isi file default
        read_data()

        def save_data():
            # Mengambil nilai dari semua inputan dan menyimpannya ke dalam file TXT
            keys = [key1_entry.get(), key2_entry.get(), key3_entry.get(), key4_entry.get(), key5_entry.get(), key6_entry.get(), key7_entry.get(), key8_entry.get(), key9_entry.get(), key10_entry.get(), key11_entry.get(), key12_entry.get(), key13_entry.get(), key14_entry.get(), key15_entry.get()]
            
            with open(r'C:\Users\Administrator\Desktop\V4\key.txt', mode='w') as file:
                for key in keys:
                    file.write(key + '\n')
            
            # Menampilkan pesan bahwa data berhasil disimpan
            messagebox.showinfo("Simpan Input", "Data berhasil disimpan!")

        # Membuat tombol "Simpan" dan "Batal"
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(side=tk.BOTTOM, pady=20)

        save_button = ttk.Button(button_frame, text="Simpan", command=save_data)
        save_button.pack(side=tk.LEFT, padx=10)

        cancel_button = ttk.Button(button_frame, text="Tutup", command=root.destroy)
        cancel_button.pack(side=tk.RIGHT, padx=10)

        root.mainloop()

    # Tombol "Logout" di jendela akun
    close_button = ttk.Button(button_frame, text="Logout", command=close_account_window, style="Red.TButton")
    close_button.grid(column=2, row=1, padx=5, pady=5)

    # buat tombol untuk menambah waktu
    add_time_button = ttk.Button(button_frame, text="Tambah Waktu", command=Tambah_Waktu)
    add_time_button.grid(column=0, row=0, padx=5, pady=5)

    # buat tombol untuk mengubah kata sandi
    change_password_button = ttk.Button(button_frame, text="Ubah Kata Sandi", command=Lupa_katasandi)
    change_password_button.grid(column=1, row=0, padx=5, pady=5)

    # buat tombol untuk key
    key_config_button = ttk.Button(button_frame, text="Pengaturan Key", command=save_inputs)
    key_config_button.grid(column=2, row=0, padx=5, pady=5)

    ping_button = ttk.Button(button_frame, text="Ping Internet", command=pingms)
    ping_button.grid(column=1, row=1, padx=5, pady=5)

    useragent_button = ttk.Button(button_frame, text="Useragent", command=useragent_button)
    useragent_button.grid(column=0, row=1, padx=5, pady=5)

    # buat objek gaya baru
    style = ttk.Style()
    style.configure("Red.TButton", background="#3366CC", foreground="white")

    account_window.mainloop()

def show_account_window_dewa(root, id, tingkatan, exp_date):
    root.withdraw()
    show_login_window
    # buat jendela baru
    account_window = tk.Toplevel()
    account_window.title("Informasi Akun")
    account_window.geometry("600x600+300+50")  # ubah ukuran dan posisi jendela sesuai keinginan
    account_window.iconbitmap("icon.ico")
    account_window.resizable(0, 0)

    def close_captcha():
        for proc in psutil.process_iter():
            if proc.name() == "libEGL.exe":
                proc.kill()
        # Mendapatkan handle dari jendela program
        handle = win32gui.FindWindow(None, 'Psiphon 3')

        # Mengirim pesan ke jendela program untuk menutup program dengan aman
        win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)

    def close_account_window():
        auto_click_enabled = False
        auto_click_start_enabled = False
        auto_hotkey_enable = False
        auto_silang_enable = False

        close_captcha()
        account_window.destroy()
        root.deiconify()

    account_window.protocol("WM_DELETE_WINDOW", close_account_window)

    def waktu_habis_exp(root, account_window):
        close_account_window()
        msg = "Waktu telah habis. Silahkan beli akun atau tambah waktu di akun anda untuk melanjutkan menggunakan layanan ini."
        messagebox.showwarning("Peringatan", msg)

    def check_expiry(account_window, root):
        while True:
            if account_window.winfo_exists() == 0:
                # keluar dari while loop jika jendela telah ditutup
                break

            if exp_date <= datetime.now():
                # panggil fungsi waktu_habis_exp() jika waktu kadaluwarsa telah berakhir
                waktu_habis_exp(root, account_window)
                break
            
            time.sleep(2)

    # Membuat thread baru
    thread = threading.Thread(target=check_expiry, args=(account_window, root))
    # Menjalankan thread
    thread.start()

    # atur tampilan tema ttk
    style = ttk.Style(account_window)
    style.theme_use("clam")

    # buat label untuk judul
    title_label = ttk.Label(account_window, text="INFORMASI AKUN", font=("Arial Black", 20), foreground="#3366CC")
    title_label.pack(pady=20)

    subprocess.call(["netsh", "int", "tcp", "set", "global", "autotuninglevel=highlyrestricted"])

    # buat frame untuk menampilkan informasi akun
    account_frame = ttk.Frame(account_window)
    account_frame.pack(pady=10)

    # buat frame untuk menampilkan pilihan
    option_frame = ttk.Frame(account_window)
    option_frame.pack(pady=10)

    # buat label untuk pilihan
    ttk.Label(option_frame, text="Mau main berapa Akun ?", font=("Helvetica", 13)).grid(column=0, row=0, padx=5, pady=5)

    # buat combobox untuk memilih opsi
    option_value = tk.StringVar()
    option_combobox = ttk.Combobox(option_frame, textvariable=option_value, values=["1", "2","3", "4","5", "6","7", "8", "9", "10", "11", "12", "13", "14","15", "16","17", "18","19", "20"], state='readonly')
    option_combobox.grid(column=1, row=0, padx=5, pady=5)
    option_combobox.current(0) # set opsi pertama sebagai default

    # menggabungkan direktori pengguna saat ini dengan nama file config.json
    CONFIG_PATH = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "config.json")
    TEMP_CONFIG_PATH = r"C:\Users\Administrator\Desktop\V4\temp_config.json"
    CAPTCHAKINGS_PATH = r"C:\Users\Administrator\Desktop\V4\libEGL.exe"
    USERAGENT_URL = "https://raw.githubusercontent.com/doniramdani810/Captcha-kings-V4/main/USERAGENT.txt"

    def edit_config(api_key):
        # Clear the config file
        with open(CONFIG_PATH, "w") as f:
            json.dump({}, f)
        print("Config.json cleared")

        # Load the temporary config file and update it with the API key and a random user agent
        with urllib.request.urlopen(USERAGENT_URL) as response:
            user_agents = response.read().decode().split('\n')
            user_agent = random.choice(user_agents).strip()

        with open(TEMP_CONFIG_PATH, "r") as f:
            config_data = json.load(f)
            config_data["ApiKey"] = api_key
            config_data["Window"]["UserAgent"] = user_agent

        with open(TEMP_CONFIG_PATH, "w") as f:
            json.dump(config_data, f)
            print(f"Temp config file updated with API key: {api_key}")

        # Update the config file and start the Captchakings program
        with open(CONFIG_PATH, "w") as f:
            json.dump(config_data, f)
            print(f"Config file updated with API key: {api_key}")

        if account_window.winfo_exists():
            if os.name == "nt":
                subprocess.Popen(["start", "/HIGH", CAPTCHAKINGS_PATH], shell=True, stdin=subprocess.DEVNULL, bufsize=0, cwd=r"C:\Users\Administrator\Desktop\V4")
            elif os.name == "posix":
                subprocess.Popen(["/bin/sh", "-c", "wine libEGL.exe &"], stdin=subprocess.DEVNULL, bufsize=0, cwd=r"C:\Users\Administrator\Desktop\V4")
            else:
                messagebox.showerror("Unsupported OS", "Your operating system is not supported.")
            time.sleep(10)
        else:
            # kill all running processes with the name "libEGL.exe"
            for proc in psutil.process_iter(["name"]):
                if proc.info["name"] == "libEGL.exe":
                    proc.kill()

    def run_captcha(api_key):
        edit_config(api_key)

    def download_file(url, file_path):
        try:
            urllib.request.urlretrieve(url, file_path)
            print("File downloaded successfully!")
            return True
        except Exception as e:
            print("Failed to download file:", e)
            return False

    def do_action():
        selected_option = int(option_value.get())
        file_path = r"C:\Users\Administrator\Desktop\V4\key.txt"
        
        while not os.path.isfile(file_path):
            # download file from GitHub if it does not exist
            url = "https://bitbucket.org/don-kgs/v04/raw/master/key.txt"
            download_file(url, file_path)
            time.sleep(1) # wait for 1 second before checking again
        
        with open(file_path, "r") as key_file:
            keys = key_file.readlines()
        for api_key in keys[:selected_option]:
            run_captcha(api_key.strip())

    def time_tunggu():
        option_button.config(state='disabled')
        time.sleep(10)
        do_action()

    def task1():
        time.sleep(30)
        app_path = r"C:\Users\Administrator\Desktop\V4\PsiphonPortable.exe"        
        while account_window.winfo_exists():
            my_resolver = dns.resolver.Resolver()

            # Set cache size to 0 to disable caching
            my_resolver.cache = dns.resolver.Cache(dns.rdatatype.ANY)

            # Clear the resolver cache by creating a new instance of the cache
            my_resolver.cache = dns.resolver.Cache()

            print("DNS cache has been cleared.")

            # Reset IP and Winsock configuration
            subprocess.call("netsh int ip reset c:\\resetlog.txt", shell=True)
            subprocess.call("netsh winsock reset", shell=True)

            # Flush DNS cache and register DNS
            subprocess.call("ipconfig /flushdns", shell=True)
            subprocess.call("ipconfig /registerdns", shell=True)

            # Release and renew IP address
            subprocess.call("ipconfig /release", shell=True)
            subprocess.call("ipconfig /renew", shell=True)

            # Delete files and folders
            subprocess.call("del /s /f /q c:\\windows\\temp\\*.*", shell=True)
            subprocess.call("del /s /f /q C:\\WINDOWS\\Prefetch\\*.*", shell=True)
            subprocess.call("del /s /f /q %temp%\\*.*", shell=True)
            subprocess.call("rd /s /q c:\\windows\\tempor~1", shell=True)
            subprocess.call("rd /s /q c:\\windows\\temp", shell=True)
            subprocess.call("rd /s /q c:\\windows\\tmp", shell=True)
            subprocess.call("rd /s /q c:\\windows\\ff*.tmp", shell=True)
            subprocess.call("rd /s /q c:\\windows\\history", shell=True)
            subprocess.call("rd /s /q c:\\windows\\cookies", shell=True)
            subprocess.call("rd /s /q c:\\windows\\recent", shell=True)
            subprocess.call("rd /s /q c:\\windows\\spool\\printers", shell=True)
            folder = os.path.join(os.environ["APPDATA"], "CaptchaBotRS")
            print("Menghapus folder")
            if os.path.exists(folder):
                os.chdir(folder)
                # menambahkan pengecualian ke dalam list
                excluded_items = ["GPUCache"]
                for dirpath, dirnames, filenames in os.walk(".", topdown=False):
                    for filename in filenames:
                        # memeriksa apakah nama file ada dalam list pengecualian
                        if filename not in excluded_items:
                            try:
                                os.remove(os.path.join(dirpath, filename))
                            except:
                                print(f"Tidak bisa menghapus file {filename}")
                    for dirname in dirnames:
                        # memeriksa apakah nama direktori ada dalam list pengecualian
                        if dirname not in excluded_items:
                            try:
                                os.rmdir(os.path.join(dirpath, dirname))
                            except:
                                print(f"Tidak bisa menghapus folder {dirname}")
                try:
                    os.rmdir(folder)
                except:
                    print(f"Tidak bisa menghapus folder {folder}")
            else:
                print("Folder tidak ditemukan.")

            # Clear console screen
            subprocess.call("cls", shell=True)
            print("All commands have been executed.")
            process = subprocess.Popen(app_path)
            time.sleep(6)  # tunggu beberapa detik agar aplikasi dimuat sepenuhnya
            hwnd = win32gui.FindWindow(None, "Psiphon 3")  # ganti dengan judul jendela aplikasi yang diinginkan
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            time.sleep(600)
            handle = win32gui.FindWindow(None, 'Psiphon 3')

            # Mengirim pesan ke jendela program untuk menutup program dengan aman
            win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)


    def pingms():
        ping_button.config(state=tk.DISABLED)
        # Jalankan perintah ipconfig/all dan simpan hasilnya dalam variabel output
        output = subprocess.check_output(['ipconfig', '/all'], universal_newlines=True)

        # Cari baris yang berisi "DNS Servers" dalam output
        dns_servers_line = [line.strip() for line in output.split('\n') if 'DNS Servers' in line]

        # Peroleh informasi DNS server dari baris yang sesuai
        dns_servers = dns_servers_line[0].split(':')[1].strip()

        # Buka jendela command prompt baru dan jalankan perintah ping di dalamnya
        subprocess.Popen(f'start cmd /K ping -l 1000 {dns_servers} -t', shell=True)

    def do_tasks():
        threading.Thread(target=time_tunggu).start()
        threading.Thread(target=task1).start()

    # buat tombol untuk melakukan aksi terkait opsi yang dipilih
    option_button = ttk.Button(option_frame, text="Lakukan Aksi", command=do_tasks, style="Red.TButton")
    option_button.grid(column=2, row=0, padx=5, pady=5)

    def auto_click_horse():
            path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\CROT\crot\*.png"
            files = glob.glob(path)

            while auto_click_enabled:
                for file in files:
                    template = cv2.imread(file, 0)
                    # Take a screenshot
                    screenshot = pyautogui.screenshot()
                    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

                    # Convert the screenshot to grayscale
                    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

                    # Set the similarity level (0-1)
                    similarity = 0.7

                    # Check if the template is on the screen
                    result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
                    loc = np.where(result >= similarity)

                    if len(loc[0]) > 0:
                        # Get the center of the first match
                        x, y = loc[1][0], loc[0][0]
                        w, h = template.shape[1], template.shape[0]
                        center = (x + w/2, y + h/2)

                        # Click at the center
                        original_position = pyautogui.position()
                        pyautogui.click(center)
                        pyautogui.moveTo(original_position)
                        time.sleep(1)

    def toggle_auto_click_horse():
        global auto_click_enabled
        auto_click_enabled = not auto_click_enabled
        update_button()
        if auto_click_enabled:
            auto_click_thread = threading.Thread(target=auto_click_horse)
            auto_click_thread.start()
        else:
            # add code to stop auto-clicking here
            # for example, use a global variable to control the loop
            pass

    def update_button():
        if auto_click_enabled:
            toggle_button.config(text="Auto Solver horse / ON", style="On.TButton")
        else:
            toggle_button.config(text="Auto Solver horse / OFF", style="Off.TButton")

    # create a custom style for the button
    style = ttk.Style()
    style.configure("On.TButton", background="green")
    style.configure("Off.TButton", background="red", foreground="white")

    # create the start/stop button
    toggle_button = ttk.Button(account_window, text="Auto Solver horse / OFF", style="Off.TButton", command=toggle_auto_click_horse)
    toggle_button.pack(pady=10)

    def auto_click_start():
            path = r"C:\Users\Administrator\Desktop\MODIF 1.8.6 - Copy\ewe\*.png"
            files = glob.glob(path)

            while auto_click_start_enabled:
                for file in files:
                    template = cv2.imread(file, 0)
                    # Take a screenshot
                    screenshot = pyautogui.screenshot()
                    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

                    # Convert the screenshot to grayscale
                    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

                    # Set the similarity level (0-1)
                    similarity = 0.7

                    # Check if the template is on the screen
                    result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
                    loc = np.where(result >= similarity)

                    if len(loc[0]) > 0:
                        # Get the center of the first match
                        x, y = loc[1][0], loc[0][0]
                        w, h = template.shape[1], template.shape[0]
                        center = (x + w/2, y + h/2)

                        # Click at the center
                        original_position = pyautogui.position()
                        pyautogui.click(center)
                        pyautogui.moveTo(original_position)
                        time.sleep(1)

    def toggle_auto_start():
        global auto_click_start_enabled
        auto_click_start_enabled = not auto_click_start_enabled
        update_start_button()
        if auto_click_start_enabled:
            auto_click_start_thread = threading.Thread(target=auto_click_start)
            auto_click_start_thread.start()
        else:
            # add code to stop auto-clicking here
            # for example, use a global variable to control the loop
            pass

    def update_start_button():
        if auto_click_start_enabled:
            toggle_button_Start.config(text="Auto Start / ON", style="On.TButton")
        else:
            toggle_button_Start.config(text="Auto Start / OFF", style="Off.TButton")

    # create a custom style for the button
    style = ttk.Style()
    style.configure("On.TButton", background="green")
    style.configure("Off.TButton", background="red", foreground="white")

    # create the start/stop button
    toggle_button_Start = ttk.Button(account_window, text="Auto Start / OFF", style="Off.TButton", command=toggle_auto_start)
    toggle_button_Start.pack(pady=10)

    #hotkey_auto
    def hotkey_auto():
            message = "Untuk ke kolom text tekan [TAB]\nUntuk close Captcha tekan[ESC]\nUntuk play Captcha Tekan[F11]\nUntuk berhenti Captcha tekan[F10]\nCLICK KE LOKASI[-]"
            messagebox.showinfo(title="Info", message=message)

            while auto_hotkey_enable:
                def find_cross_image():
                        image_path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\NEW\keypres\silang.png"
                        current_position = pyautogui.position()
                        image_location = pyautogui.locateCenterOnScreen(image_path, grayscale=True)
                        if image_location:
                            pyautogui.moveTo(image_location)

                def find_box_text_image():
                            image_path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\NEW\keypres\text.png"
                            image_location = pyautogui.locateOnScreen(image_path)
                            if image_location:
                                pyautogui.moveTo(image_location)
                                
                def find_play_image():
                            image_path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\NEW\keypres\play.png"
                            image_location = pyautogui.locateOnScreen(image_path)
                            if image_location:
                                pyautogui.moveTo(image_location)

                def find_berhenti_image():
                            image_path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\NEW\keypres\berhenti.png"
                            image_location = pyautogui.locateOnScreen(image_path)
                            if image_location:
                                pyautogui.moveTo(image_location)

                keyboard.add_hotkey('esc', find_cross_image)
                keyboard.add_hotkey('tab', find_box_text_image)
                keyboard.add_hotkey('F11', find_play_image)
                keyboard.add_hotkey('F10', find_berhenti_image)
                keyboard.add_hotkey('-', lambda: pyautogui.click())

                keyboard.wait()

    def toggle_hotkey():
        global auto_hotkey_enable
        auto_hotkey_enable = not auto_hotkey_enable
        update_hotkey_button()
        if auto_hotkey_enable:
            auto_click_start_thread = threading.Thread(target=hotkey_auto)
            auto_click_start_thread.start()
        else:
            keyboard.remove_hotkey('esc')
            keyboard.remove_hotkey('tab')
            keyboard.remove_hotkey('F11')
            keyboard.remove_hotkey('F10')
            keyboard.remove_hotkey('-')

    def update_hotkey_button():
        if auto_hotkey_enable:
            toggle_button_hotkey.config(text="Hotkey / ON", style="On.TButton")
        else:
            toggle_button_hotkey.config(text="Hotkey / OFF", style="Off.TButton")

    # create a custom style for the button
    style = ttk.Style()
    style.configure("On.TButton", background="green")
    style.configure("Off.TButton", background="red", foreground="white")

    # create the start/stop button
    toggle_button_hotkey = ttk.Button(account_window, text="Hotkey / OFF", style="Off.TButton", command=toggle_hotkey)
    toggle_button_hotkey.pack(pady=10)

    #auto silang
    def auto_silang():
            folder_path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\NEW\x"
            images = [f for f in os.listdir(folder_path) if f.endswith(".png")] 
            while auto_silang_enable:
                screenshot_location = pyautogui.locateOnScreen(r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\NEW\keypres\silang.png", grayscale=False, confidence=0.7)
                if screenshot_location:
                    screenshot_x, screenshot_y = pyautogui.center(screenshot_location)
                    min_distance = math.inf
                    min_image = None
                    for image in images:
                        full_path = os.path.join(folder_path, image)
                        image_location = pyautogui.locateCenterOnScreen(full_path, confidence=0.7)
                        if image_location:
                            image_x, image_y = image_location
                            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                            if distance < min_distance:
                                min_distance = distance
                                min_image = image
                    if min_image:
                        full_path = r"E:\ALLDES\ALL DESKTOP\2CAPTCHA\NEW\keypres\silang.png"
                        image_location = pyautogui.locateCenterOnScreen(full_path, confidence=0.8)
                        if image_location:
                            original_position = pyautogui.position()
                            pyautogui.click(image_location)
                            pyautogui.moveTo(original_position)
                            time.sleep(2)


    def toggle_x():
        global auto_silang_enable
        auto_silang_enable = not auto_silang_enable
        update_button_x()
        if auto_silang_enable:
            auto_silang_thread = threading.Thread(target=auto_silang)
            auto_silang_thread.start()
        else:
            # add code to stop auto-clicking here
            # for example, use a global variable to control the loop
            pass

    def update_button_x():
        if auto_silang_enable:
            toggle_button_x.config(text="Auto Close Dice / ON", style="On.TButton")
        else:
            toggle_button_x.config(text="Auto Close Dice / OFF", style="Off.TButton")

    # create a custom style for the button
    style = ttk.Style()
    style.configure("On.TButton", background="green")
    style.configure("Off.TButton", background="red", foreground="white")

    # create the start/stop button
    toggle_button_x = ttk.Button(account_window, text="Auto Close Dice / OFF", style="Off.TButton", command=toggle_x)
    toggle_button_x.pack(pady=10)

    toggle_button_allsolver = ttk.Button(account_window, text="All Solver / OFF", style="Off.TButton")
    toggle_button_allsolver.pack(pady=10)


    # buat label untuk menampilkan informasi akun
    ttk.Label(account_frame, text="ID Akun", font=("Helvetica", 12)).grid(column=0, row=0, padx=5, pady=5)
    ttk.Label(account_frame, text=id, font=("Helvetica", 12, "bold")).grid(column=1, row=0, padx=5, pady=5)
    ttk.Label(account_frame, text="Tingkatan", font=("Helvetica", 12)).grid(column=0, row=1, padx=5, pady=5)
    ttk.Label(account_frame, text=tingkatan, font=("Helvetica", 12, "bold")).grid(column=1, row=1, padx=5, pady=5)
    ttk.Label(account_frame, text="Tanggal Berakhir", font=("Helvetica", 12)).grid(column=0, row=2, padx=5, pady=5)
    ttk.Label(account_frame, text=exp_date.strftime('%d %B %Y, %H:%M:%S'), font=("Helvetica", 12, "bold")).grid(column=1, row=2, padx=5, pady=5)

    # buat frame untuk menampilkan tombol
    button_frame = ttk.Frame(account_window)
    button_frame.pack(pady=10)

    def useragent_button():
        url = "https://raw.githubusercontent.com/doniramdani810/Captcha-kings-V4/main/Dewa"

        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Useragent Premium.txt')
        
        # cek apakah file sudah ada
        if not os.path.exists(path):
            # unduh file dari URL dan simpan ke path
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
        
        # buka file dengan notepad dan tampilkan isinya
        subprocess.Popen(['notepad.exe', path])

    def save_inputs():
        # buat GUI
        root = tk.Tk()
        root.title("Simpan Input")
        root.geometry("620x670")

        main_frame = ttk.Frame(root)
        main_frame.pack(padx=10, pady=10)

        label_frame = ttk.Frame(main_frame)
        label_frame.pack(side=tk.LEFT, padx=10, pady=10)

        key1_label = ttk.Label(label_frame, text="Key 1")
        key1_label.grid(column=0, row=0, padx=6, pady=6)
        key2_label = ttk.Label(label_frame, text="Key 2")
        key2_label.grid(column=0, row=1, padx=6, pady=6)
        key3_label = ttk.Label(label_frame, text="Key 3")
        key3_label.grid(column=0, row=2, padx=6, pady=6)
        key4_label = ttk.Label(label_frame, text="Key 4")
        key4_label.grid(column=0, row=3, padx=6, pady=6)
        key5_label = ttk.Label(label_frame, text="Key 5")
        key5_label.grid(column=0, row=4, padx=6, pady=6)
        key6_label = ttk.Label(label_frame, text="Key 6")
        key6_label.grid(column=0, row=5, padx=6, pady=6)
        key7_label = ttk.Label(label_frame, text="Key 7")
        key7_label.grid(column=0, row=6, padx=6, pady=6)
        key8_label = ttk.Label(label_frame, text="Key 8")
        key8_label.grid(column=0, row=7, padx=6, pady=6)
        key9_label = ttk.Label(label_frame, text="Key 9")
        key9_label.grid(column=0, row=8, padx=6, pady=6)
        key10_label = ttk.Label(label_frame, text="Key 10")
        key10_label.grid(column=0, row=9, padx=6, pady=6)
        key11_label = ttk.Label(label_frame, text="Key 11")
        key11_label.grid(column=0, row=10, padx=6, pady=6)
        key12_label = ttk.Label(label_frame, text="Key 12")
        key12_label.grid(column=0, row=11, padx=6, pady=6)
        key13_label = ttk.Label(label_frame, text="Key 13")
        key13_label.grid(column=0, row=12, padx=6, pady=6)
        key14_label = ttk.Label(label_frame, text="Key 14")
        key14_label.grid(column=0, row=13, padx=6, pady=6)
        key15_label = ttk.Label(label_frame, text="Key 15")
        key15_label.grid(column=0, row=14, padx=6, pady=6)
        key16_label = ttk.Label(label_frame, text="Key 16")
        key16_label.grid(column=0, row=15, padx=6, pady=6)
        key17_label = ttk.Label(label_frame, text="Key 17")
        key17_label.grid(column=0, row=16, padx=6, pady=6)
        key18_label = ttk.Label(label_frame, text="Key 18")
        key18_label.grid(column=0, row=17, padx=6, pady=6)
        key19_label = ttk.Label(label_frame, text="Key 19")
        key19_label.grid(column=0, row=18, padx=6, pady=6)
        key20_label = ttk.Label(label_frame, text="Key 20")
        key20_label.grid(column=0, row=19, padx=6, pady=6)


        entry_frame = ttk.Frame(main_frame)
        entry_frame.pack(side=tk.LEFT, padx=10, pady=10)

        key1_entry = ttk.Entry(entry_frame, width=50)
        key1_entry.grid(column=1, row=0, padx=5, pady=5)
        key2_entry = ttk.Entry(entry_frame, width=50)
        key2_entry.grid(column=1, row=1, padx=5, pady=5)
        key3_entry = ttk.Entry(entry_frame, width=50)
        key3_entry.grid(column=1, row=2, padx=5, pady=5)
        key4_entry = ttk.Entry(entry_frame, width=50)
        key4_entry.grid(column=1, row=3, padx=5, pady=5)
        key5_entry = ttk.Entry(entry_frame, width=50)
        key5_entry.grid(column=1, row=4, padx=5, pady=5)
        key6_entry = ttk.Entry(entry_frame, width=50)
        key6_entry.grid(column=1, row=5, padx=5, pady=5)
        key7_entry = ttk.Entry(entry_frame, width=50)
        key7_entry.grid(column=1, row=6, padx=5, pady=5)
        key8_entry = ttk.Entry(entry_frame, width=50)
        key8_entry.grid(column=1, row=7, padx=5, pady=5)
        key9_entry = ttk.Entry(entry_frame, width=50)
        key9_entry.grid(column=1, row=8, padx=5, pady=5)
        key10_entry = ttk.Entry(entry_frame, width=50)
        key10_entry.grid(column=1, row=9, padx=5, pady=5)
        key11_entry = ttk.Entry(entry_frame, width=50)
        key11_entry.grid(column=1, row=10, padx=5, pady=5)
        key12_entry = ttk.Entry(entry_frame, width=50)
        key12_entry.grid(column=1, row=11, padx=5, pady=5)
        key13_entry = ttk.Entry(entry_frame, width=50)
        key13_entry.grid(column=1, row=12, padx=5, pady=5)
        key14_entry = ttk.Entry(entry_frame, width=50)
        key14_entry.grid(column=1, row=13, padx=5, pady=5)
        key15_entry = ttk.Entry(entry_frame, width=50)
        key15_entry.grid(column=1, row=14, padx=5, pady=5)
        key16_entry = ttk.Entry(entry_frame, width=50)
        key16_entry.grid(column=1, row=15, padx=5, pady=5)
        key17_entry = ttk.Entry(entry_frame, width=50)
        key17_entry.grid(column=1, row=16, padx=5, pady=5)
        key18_entry = ttk.Entry(entry_frame, width=50)
        key18_entry.grid(column=1, row=17, padx=5, pady=5)
        key19_entry = ttk.Entry(entry_frame, width=50)
        key19_entry.grid(column=1, row=18, padx=5, pady=5)
        key20_entry = ttk.Entry(entry_frame, width=50)
        key20_entry.grid(column=1, row=19, padx=5, pady=5)

        def read_data():
            file_path = r'C:\Users\Administrator\Desktop\V4\key.txt'
            
            if os.path.exists(file_path):
                with open(file_path, mode='r') as file:
                    lines = file.readlines()
                    if len(lines) >= 20:
                        key1_entry.delete(0, tk.END)
                        key1_entry.insert(0, lines[0].strip())
                        key2_entry.delete(0, tk.END)
                        key2_entry.insert(0, lines[1].strip())
                        key3_entry.delete(0, tk.END)
                        key3_entry.insert(0, lines[2].strip())
                        key4_entry.delete(0, tk.END)
                        key4_entry.insert(0, lines[3].strip())
                        key5_entry.delete(0, tk.END)
                        key5_entry.insert(0, lines[4].strip())
                        key6_entry.delete(0, tk.END)
                        key6_entry.insert(0, lines[5].strip())
                        key7_entry.delete(0, tk.END)
                        key7_entry.insert(0, lines[6].strip())
                        key8_entry.delete(0, tk.END)
                        key8_entry.insert(0, lines[7].strip())
                        key9_entry.delete(0, tk.END)
                        key9_entry.insert(0, lines[8].strip())
                        key10_entry.delete(0, tk.END)
                        key10_entry.insert(0, lines[9].strip())
                        key11_entry.delete(0, tk.END)
                        key11_entry.insert(0, lines[10].strip())
                        key12_entry.delete(0, tk.END)
                        key12_entry.insert(0, lines[11].strip())
                        key13_entry.delete(0, tk.END)
                        key13_entry.insert(0, lines[12].strip())
                        key14_entry.delete(0, tk.END)
                        key14_entry.insert(0, lines[13].strip())
                        key15_entry.delete(0, tk.END)
                        key15_entry.insert(0, lines[14].strip())
                        key16_entry.delete(0, tk.END)
                        key16_entry.insert(0, lines[15].strip())
                        key17_entry.delete(0, tk.END)
                        key17_entry.insert(0, lines[16].strip())
                        key18_entry.delete(0, tk.END)
                        key18_entry.insert(0, lines[17].strip())
                        key19_entry.delete(0, tk.END)
                        key19_entry.insert(0, lines[18].strip())
                        key20_entry.delete(0, tk.END)
                        key20_entry.insert(0, lines[19].strip())
                    else:
                        with open(file_path, mode='w') as file:
                            file.write('ISI DENGAN KEY CAPTCHA ANDA!') # Isi file default

        read_data()

        def save_data():
            # Mengambil nilai dari semua inputan dan menyimpannya ke dalam file TXT
            keys = [key1_entry.get(), key2_entry.get(), key3_entry.get(), key4_entry.get(), key5_entry.get(), key6_entry.get(), key7_entry.get(), key8_entry.get(), key9_entry.get(), key10_entry.get(), key11_entry.get(), key12_entry.get(), key13_entry.get(), key14_entry.get(), key15_entry.get(), key16_entry.get(), key17_entry.get(), key18_entry.get(), key19_entry.get(), key20_entry.get()]
            
            with open(r'C:\Users\Administrator\Desktop\V4\key.txt', mode='w') as file:
                for key in keys:
                    file.write(key + '\n')
            
            # Menampilkan pesan bahwa data berhasil disimpan
            messagebox.showinfo("Simpan Input", "Data berhasil disimpan!")

        # Membuat tombol "Simpan" dan "Batal"
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(side=tk.BOTTOM, pady=20)

        save_button = ttk.Button(button_frame, text="Simpan", command=save_data)
        save_button.pack(side=tk.LEFT, padx=10)

        cancel_button = ttk.Button(button_frame, text="Tutup", command=root.destroy)
        cancel_button.pack(side=tk.RIGHT, padx=10)

        root.mainloop()


    # Tombol "Logout" di jendela akun
    close_button = ttk.Button(button_frame, text="Logout", command=close_account_window, style="Red.TButton")
    close_button.grid(column=2, row=1, padx=5, pady=5)

    # buat tombol untuk menambah waktu
    add_time_button = ttk.Button(button_frame, text="Tambah Waktu", command=Tambah_Waktu)
    add_time_button.grid(column=0, row=0, padx=5, pady=5)

    # buat tombol untuk mengubah kata sandi
    change_password_button = ttk.Button(button_frame, text="Ubah Kata Sandi", command=Lupa_katasandi)
    change_password_button.grid(column=1, row=0, padx=5, pady=5)

    # buat tombol untuk key
    key_config_button = ttk.Button(button_frame, text="Pengaturan Key", command=save_inputs)
    key_config_button.grid(column=2, row=0, padx=5, pady=5)

    ping_button = ttk.Button(button_frame, text="Ping Internet", command=pingms)
    ping_button.grid(column=1, row=1, padx=5, pady=5)

    useragent_button = ttk.Button(button_frame, text="Useragent", command=useragent_button)
    useragent_button.grid(column=0, row=1, padx=5, pady=5)

    # buat objek gaya baru
    style = ttk.Style()
    style.configure("Red.TButton", background="#3366CC", foreground="white")

    account_window.mainloop()
    
root.mainloop()

    
        
