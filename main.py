import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from PIL import Image, ImageTk
import threading

# ✅ Import your actual functions here
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from find_motion import find_motion
from identify import maincall
from attendance import mark_attendance

# ✅ Thread wrapper with error popup
def run_threaded(func):
    def wrapper():
        try:
            func()
            
        except Exception as e:
            print(f"[ERROR] {func.__name__}: {e}")
            messagebox.showerror("Error", f"{func.__name__} crashed:\n{e}")
    threading.Thread(target=wrapper).start()

# ✅ GUI setup
window = tk.Tk()
window.title("Smart CCTV")
window.geometry('1080x700')

frame1 = tk.Frame(window)
frame1.pack(expand=True)

label_title = tk.Label(frame1, text="Smart CCTV Camera")
label_font = font.Font(size=35, weight='bold', family='Helvetica')
label_title['font'] = label_font
label_title.grid(row=0, column=1, columnspan=3, pady=(10, 10))

# Icon Loader
def load_icon(path, size=(50, 50)):
    try:
        img = Image.open(path)
        img = img.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except:
        return None

# Load icons (fallback to None if not found)
btn1_image = load_icon('icons/lamp.png')
btn2_image = load_icon('icons/rectangle-of-cutted-line-geometrical-shape.png')
btn3_image = load_icon('icons/security-camera.png')
btn4_image = load_icon('icons/recording.png')
btn5_image = load_icon('icons/exit.png')
btn6_image = load_icon('icons/incognito.png')
btn7_image = load_icon('icons/recording.png')
btn8_image = load_icon('icons/attendance.png')

btn_font = font.Font(size=20, weight='bold')

# ✅ Buttons
btn1 = tk.Button(frame1, text='Monitor', height=90, width=180, fg='green', command=lambda: run_threaded(find_motion), image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=2, column=0, padx=10, pady=10)

btn7 = tk.Button(frame1, text="Identify", height=90, width=180, fg='orange', command=lambda: run_threaded(maincall), image=btn7_image, compound='left')
btn7['font'] = btn_font
btn7.grid(row=2, column=1, padx=10, pady=10)

btn2 = tk.Button(frame1, text='Rectangle', height=90, width=180, fg='orange', command=lambda: run_threaded(rect_noise), image=btn2_image, compound='left')
btn2['font'] = btn_font
btn2.grid(row=2, column=2, padx=10, pady=10)

btn3 = tk.Button(frame1, text='Noise', height=90, width=180, fg='green', command=lambda: run_threaded(noise), image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=3, column=0, padx=10, pady=10)

btn6 = tk.Button(frame1, text='In Out', height=90, width=180, fg='green', command=lambda: run_threaded(in_out), image=btn6_image, compound='left')
btn6['font'] = btn_font
btn6.grid(row=3, column=1, padx=10, pady=10)

btn4 = tk.Button(frame1, text='Record', height=90, width=180, fg='orange', command=lambda: run_threaded(record), image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=3, column=2, padx=10, pady=10)

btn8 = tk.Button(frame1, text='Attendance', height=90, width=180, fg='blue', command=lambda: run_threaded(mark_attendance), image=btn8_image, compound='left')
btn8['font'] = btn_font
btn8.grid(row=4, column=0, padx=10, pady=20)

btn5 = tk.Button(frame1, text='Exit', height=90, width=180, fg='red', command=window.quit, image=btn5_image, compound='left')
btn5['font'] = btn_font
btn5.grid(row=4, column=2, padx=10, pady=20)

window.mainloop()
