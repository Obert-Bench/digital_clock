import tkinter as tk
import time
import json

window = tk.Tk()

f = open('config.json')
prof = json.load(f)
f.close()

#window.attributes('-toolwindow', False) #taskbar icon, doesnt work w overrideredirect
background_color = prof["background_color"]
foreground_color = prof["foreground_color"]
string_format = prof["string_format"]
font_details = (prof["font_family"],prof["font_size"],prof["font_style"])
window.geometry("+" + prof["x_position"] + "+" + prof["y_position"])
if not prof["decorator_visible"]:
    window.overrideredirect(True)
if prof["always_on_top"]:
    window.wm_attributes("-topmost", 1)
if prof["transparent_background"]:
    window.attributes('-transparentcolor', background_color)
update_interval = 6000
if "%S" in string_format:
    update_interval = 1000
if prof["alpha"] != 0:
    window.attributes("-alpha", 0.7) 

label = tk.Label(window, text="",font=font_details,fg=foreground_color, bg=background_color) 
label.pack(expand=True)

def update_label(): 
    current_time = time.strftime(string_format)
    label.config(text=current_time)
    window.after(update_interval, update_label)  

if __name__ == "__main__":
    update_label() 
    window.mainloop()

