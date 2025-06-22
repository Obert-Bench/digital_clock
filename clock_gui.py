from tkinter import Tk, Label
from time import strftime
from json import load

window = Tk()
alpha = 1

f = open('config.json')
prof = load(f)
f.close()

def update_label(): 
    current_time = strftime(string_format)
    label.config(text=current_time)
    window.after(update_interval, update_label) 

def on_enter(event):
    window.attributes("-alpha", 0.2) 

def on_leave(event):
    window.attributes("-alpha", alpha) 

def on_click(event):
    print("click")

def on_drag(event):
    print("drag")

window.attributes('-toolwindow', False) 
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
    alpha = prof["alpha"]

window.attributes("-alpha", alpha) 

label = Label(window, text="",font=font_details,fg=foreground_color, bg=background_color) 
label.pack(expand=True)
label.bind("<Enter>",on_enter)
label.bind("<Leave>",on_leave)
label.bind("<Button-1>", on_click)
#label.bind("<Button-1>",on_drag)

if __name__ == "__main__":
    update_label() 
    window.mainloop()

