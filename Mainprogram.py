##mainprogram
from tkinter import *
import Themes

root = Tk()

topleft = Frame(root,
                bg = Themes.flat_ui[1], bd='3',
                height = '300', width = '300',
                relief='ridge'
                ).grid(row=0, column=0, rowspan=3, columnspan=3)
topmid = Frame(root,
               bg = Themes[1], bd='3',
               height = '200', width = '200',
               relief='ridge'
               ).grid(row=0, column=3, rowspan=2, columnspan=2)
topright = Frame(root,
                 bg = Themes[1], bd='3',
                 height = '800', width = '800',
                 relief='ridge'
                 ).grid(row=0, column=5, rowspan=8, columnspan=8)
bottomleft = Frame(root,
                   bg = Themes[1], bd='3',
                   height = '500', width = '500',
                   relief='sunken'
                   ).grid(row=3, column=0, rowspan=5, columnspan=5)
bottommid = Frame(root,
                  bg = Themes[1], bd ='3',
                  height = '100', width = '100',
                  relief='raised'
                  ).grid(row=2, column=3, rowspan=1, columnspan=1)
bottomright = Frame(root,
                    bg = Themes[1], bd='3',
                    height = '100', width = '100',
                    relief='raised'
                    ).grid(row=2, column=4, rowspan=1, columnspan=1)


root.mainloop()
