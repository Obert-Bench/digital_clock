from tkinter import Tk, Label
from time import strftime
from json import load

# TODO: right click to display settings, drag to move gui

class DigitalClock(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.clock_label = Label( text="foooo") 

        self.update_interval = 6000
        self.config = {
            "alpha": 1,
            "always_on_top": True,
            "decorator_visible": False,
            "transparent_background": False,
            "taskbar_icon": False,
            "x_position": 0,
            "y_position": 0,
            "string_format": "%I:%M %p",
            "background_color": "#000001",
            "foreground_color": "#00FF00",
            "font_family": "Impact",
            "font_style": "",
            "font_size": 10
        }
        self.load_config()
        self.set_config()
        self.update_label()

        self.clock_label.pack(expand=True)

        #needed to adjust relative position of mouse to gui during drag event
        self.init = [0,0]
        self.bind("<Enter>",lambda e:self.update_alpha(e,0.2))
        self.bind("<Leave>",lambda e:self.update_alpha(e,self.config["alpha"]))
        self.bind("<Button-1>", self.on_click)
        self.bind("<B1-Motion>",self.on_drag)

    def load_config(self,file_name = "config.json"):
        try:
            with open(file_name, 'r') as file:
                profile = load(file)
        except:
            print("The file '" + file_name + "' could not be found, the default configuration will be loaded")
            return
        for setting in self.config:
            if profile[setting] != None:
                self.config[setting] = profile[setting]
    
    def set_config(self):
        self.geometry("+" + str(self.config["x_position"]) + "+" + str(self.config["y_position"]))
        self.attributes("-alpha", self.config["alpha"]) 
        if not self.config["taskbar_icon"]:
            self.attributes('-toolwindow', True) 
        if not self.config["decorator_visible"]:
            self.overrideredirect(True)
        if self.config["always_on_top"]:
            self.wm_attributes("-topmost", 1)
        if self.config["transparent_background"]:
            self.attributes('-transparentcolor', self.config["background_color"])

        font_details = (self.config["font_family"],self.config["font_size"],self.config["font_style"])
        self.clock_label.config(font=font_details, bg= self.config["background_color"], fg = self.config["foreground_color"])

        if "%S" in self.config["string_format"]:
            self.update_interval = 1000 

    def update_label(self): 
        current_time = strftime(self.config["string_format"])
        self.clock_label.config(text=current_time)
        self.after(self.update_interval, self.update_label) 

    def update_alpha(self, event, value):
        self.attributes("-alpha", value) 

    def on_click(self,event):
        self.init = [event.x,event.y]

    def on_drag(self,event):
        self.update_alpha(event,self.config["alpha"])
        x = self.winfo_x() + (event.x)
        y = self.winfo_y() + (event.y)
        self.geometry(f"+{x - self.init[0]}+{y - self.init[1]}")

    
if __name__ == "__main__":
    clock = DigitalClock()  
    clock.mainloop()
