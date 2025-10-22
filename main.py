import tkinter as tk
from tkinter import font
import random
import win32gui
import win32process
import psutil
import ctypes
import os
import sys
import webbrowser

# ==============================
# Config & Constants
# ==============================
BG_COLOR = '#1E2227'
LINE_COLOR = '#4EB5F7'
TEXT_COLOR = '#FFFFFF'
FONT_FAMILY = 'Consolas'
FONT_SIZE = 13
CELL_WIDTH = 159
CELL_HEIGHT = 30
LINE_WIDTH = 1
DIVIDER_WIDTH = 1
SCALE = 1.07

BASE_DIR = os.path.dirname(sys.executable) if getattr(sys, "frozen", False) else os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, 'config.txt')

# ==============================
# Config Load/Save
# ==============================
def load_config():
    defaults = {'FPS': 515, 'PING': 20, 'PL': 2, 'CPU': 60}
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            for key, val in defaults.items():
                f.write(f"{key}={val}\n")
        return defaults

    values = defaults.copy()
    try:
        with open(CONFIG_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if '=' not in line:
                    continue
                key, val = [x.strip() for x in line.split('=', 1)]
                key = key.upper()
                if key in values and val.isdigit():
                    values[key] = int(val)
    except Exception:
        return defaults
    return values

def save_config(values):
    try:
        with open(CONFIG_FILE, 'w') as f:
            for key, val in values.items():
                f.write(f"{key}={val}\n")
    except Exception as e:
        print("Save config error:", e)

config = load_config()
last_config_time = os.path.getmtime(CONFIG_FILE)

CELL_HEIGHT = int(CELL_HEIGHT * SCALE)
FONT_SIZE = int(FONT_SIZE * SCALE)
DIVIDER_HEIGHT = CELL_HEIGHT
PAD_Y = max(1, int(1 * SCALE))
PAD_X = 5

# ==============================
# Tkinter GUI Setup
# ==============================
labels_text = [
    f"FPS: {config['FPS']}",
    f"PING: {config['PING']} ms",
    f"PL: {config['PL']}%",
    f"CPU: {config['CPU']}%"
]
cell_widths = [CELL_WIDTH, CELL_WIDTH, CELL_WIDTH, 86]

root = tk.Tk()
root.overrideredirect(True)
root.configure(bg=LINE_COLOR)
root.attributes('-topmost', True)
root.attributes('-alpha', 0.83)

total_width = sum(cell_widths) + LINE_WIDTH*2 + DIVIDER_WIDTH*(len(labels_text)-1)
total_height = CELL_HEIGHT + LINE_WIDTH*2
root.geometry(f"{total_width}x{total_height}+0+0")

inner_frame = tk.Frame(root, bg=LINE_COLOR)
inner_frame.place(x=LINE_WIDTH, y=LINE_WIDTH, width=total_width-LINE_WIDTH*2, height=total_height-2.5*LINE_WIDTH)

custom_font = font.Font(family=FONT_FAMILY, size=FONT_SIZE)
labels = []

for i, text in enumerate(labels_text):
    width = cell_widths[i]
    cell = tk.Frame(inner_frame, width=width, height=CELL_HEIGHT, bg=BG_COLOR)
    cell.pack(side='left', fill='y')
    cell.pack_propagate(False)
    label = tk.Label(cell, text=text, fg=TEXT_COLOR, bg=BG_COLOR, font=custom_font, anchor='w', padx=PAD_X, pady=PAD_Y)
    label.pack(fill='both', expand=True)
    labels.append(label)
    if i < len(labels_text) - 1:
        divider = tk.Frame(inner_frame, bg=LINE_COLOR, width=DIVIDER_WIDTH, height=DIVIDER_HEIGHT)
        divider.pack(side='left')

# ==============================
# Update Functions
# ==============================
def update_fps():
    fps_value = config['FPS']
    change = random.choice([-3, -2, -1, 0, 1, 2, 3])
    new_fps = max(0, fps_value + change)
    labels[0].config(text=f"FPS: {new_fps}")
    root.after(random.randint(300, 500), update_fps)

def update_ping():
    ping_value = config['PING']
    change = random.choice([-3, -2, -1, 0, 1, 2, 3])
    new_ping = max(5, min(200, ping_value + change))
    labels[1].config(text=f"PING: {new_ping} ms")
    root.after(random.randint(700, 1000), update_ping)

def update_pl():
    pl_value = config['PL']
    change = random.choice([-1, 0, 1])
    new_pl = max(0, min(100, pl_value + change))
    labels[2].config(text=f"PL: {new_pl}%")
    root.after(10000, update_pl)

def update_cpu():
    cpu_value = config['CPU']
    change = random.choice([-2, -1, 0, 1, 2])
    new_cpu = max(0, min(100, cpu_value + change))
    labels[3].config(text=f"CPU: {new_cpu}%")
    root.after(random.randint(600, 1200), update_cpu)

# ==============================
# Full Screen Exclusive Support     ใช้งานยังไม่ได้
# ==============================
def find_fivem_window():
    def callback(hwnd, hwnds):
        title = win32gui.GetWindowText(hwnd)
        if 'FiveM' in title:
            hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds[0] if hwnds else None

def get_window_rect(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    return rect

def position_overlay_over_game():
    hwnd = find_fivem_window()
    if hwnd:
        try:
            left, top, right, bottom = get_window_rect(hwnd)
            root.geometry(f"{total_width}x{total_height}+{left}+{top}")
            root.deiconify()
        except Exception:
            root.withdraw()
    else:
        root.geometry(f"{total_width}x{total_height}+0+0")
        root.deiconify()
    root.after(100, position_overlay_over_game)

# ==============================
# Focus Detection
# ==============================
def is_fivem_active():
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        exe_name = psutil.Process(pid).name().lower()
        return 'fivem' in exe_name
    except Exception:
        return False

def check_window_focus():
    if is_fivem_active():
        root.deiconify()
    else:
        root.withdraw()
    root.after(100, check_window_focus)

# ==============================
# Entry Fields
# ==============================
def create_entry(parent, label_index, key):
    entry_var = tk.StringVar()
    entry_var.set(str(config[key]))

    def on_change(*args):
        val = entry_var.get()
        if val.isdigit():
            config[key] = int(val)
            if key == 'FPS':
                labels[label_index].config(text=f"FPS: {config[key]}")
            elif key == 'PING':
                labels[label_index].config(text=f"PING: {config[key]} ms")
            else:
                labels[label_index].config(text=f"{key}: {config[key]}%")
            save_config(config)

    entry_var.trace_add('write', on_change)
    entry = tk.Entry(parent, textvariable=entry_var, width=8, font=custom_font)
    entry.pack(side='left', padx=2)
    return entry

entry_frame = tk.Frame(root, bg=BG_COLOR)
entry_frame.place(x=0, y=total_height+5)

entries = []
for i, key in enumerate(['FPS', 'PING', 'PL', 'CPU']):
    entries.append(create_entry(entry_frame, i, key))

# ==============================
# Auto Reload Config
# ==============================
def auto_reload_config():
    try:
        current_time = os.path.getmtime(CONFIG_FILE)
        global last_config_time
        if current_time != last_config_time:
            new_config = load_config()
            config.update(new_config)
            for i, key in enumerate(['FPS','PING','PL','CPU']):
                entries[i].delete(0, tk.END)
                entries[i].insert(0, str(config[key]))
            last_config_time = current_time
    except Exception:
        pass
    root.after(2000, auto_reload_config)

# ==============================
# Start Updates
# ==============================
update_fps()
update_ping()
update_pl()
update_cpu()
position_overlay_over_game()
check_window_focus()
auto_reload_config()
root.mainloop()
