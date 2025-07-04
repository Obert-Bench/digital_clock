from tkinter import HORIZONTAL, Button, Checkbutton, Label, Scale, Toplevel, colorchooser
from tkinter.ttk import Combobox

class Settings(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.wm_title("Settings")
        c = 0
        for setting in self.config:
            l = Label(self, text=setting)
            l.grid(row=c,column=0,sticky="W")
            c+=1

        w_alpha = Scale(self, from_=0, to=1, orient=HORIZONTAL, resolution= 0.1, length=150)
        w_alpha.grid(row=0,column=1,columnspan=4)

        w_aot = Checkbutton(self,onvalue=1,offvalue=0)
        w_aot.grid(row=1,column=1)

        w_decorator = Checkbutton(self,onvalue=1,offvalue=0)
        w_decorator.grid(row=2,column=1)

        w_tpb = Checkbutton(self,onvalue=1,offvalue=0)
        w_tpb.grid(row=3,column=1)

        w_tbi = Checkbutton(self,onvalue=1,offvalue=0)
        w_tbi.grid(row=4,column=1)
        
        w_xpos = Scale(self, from_=0, to=3000, orient=HORIZONTAL, length=150)
        w_xpos.grid(row=5,column=1,columnspan=4)

        w_ypos = Scale(self, from_=0, to=3000, orient=HORIZONTAL, length=150)
        w_ypos.grid(row=6,column=1,columnspan=4)

        #w_hours_dur = Combobox(self).grid(row=7,column=1,columnspan=1)
        #w_hours_dur['values'] = ('12Hr','24Hr')
        w_hours = Checkbutton(self,onvalue=1,offvalue=0, text="Hr")
        w_hours.grid(row=7,column=1)
        w_mins = Checkbutton(self,onvalue=1,offvalue=0, text="Min")
        w_mins.grid(row=7,column=2)
        w_secs = Checkbutton(self,onvalue=1,offvalue=0, text="Sec")
        w_secs.grid(row=7,column=3)
        w_ampm = Checkbutton(self,onvalue=1,offvalue=0, text="ampm")
        w_ampm.grid(row=7,column=4)
        
        w_bgc = Button(self,text="select color",command=self.color_chooser)
        w_bgc.grid(row=8,column=1,columnspan=2)
        w_fgc = Button(self,text="select color",command=self.color_chooser)
        w_fgc.grid(row=9,column=1,columnspan=2)

        w_ffam = Combobox(self, values=['Impact','Sans Serif'])
        w_ffam.grid(row=10,column=1,columnspan=4)

        w_bold = Checkbutton(self,onvalue=1,offvalue=0, text="bold")
        w_bold.grid(row=11,column=1)
        w_italic = Checkbutton(self,onvalue=1,offvalue=0, text="italic")
        w_italic.grid(row=11,column=2)


        w_fsize = Scale(self, from_=1, to=100, orient=HORIZONTAL, length=150)
        w_fsize.grid(row=12,column=1,columnspan=4)

    def color_chooser():
        color_code = colorchooser.askcolor(title ="Choose color") 
        print(color_code)