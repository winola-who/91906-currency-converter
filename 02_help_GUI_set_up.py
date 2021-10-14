from tkinter import *
# to prevent unwanted windows
from functools import partial
import random


from tkinter import *
# to prevent unwanted windows
from functools import partial
import random


class Converter:
    def __init__(self):
        background = "White"
        txt_colour = "#396CDE"
        box_bg = "#F0F8FF"
        # Converter main screen GUI
        self.converter_frame = Frame(width=500, height=500,
                                     bg=background,
                                     pady=10,
                                     padx=10,
                                     )
        self.converter_frame.grid()

        # Currency converter heading (row0)
        self.converter_label = Label(self.converter_frame,
                                     text="Currency Converter",
                                     font="TkDefaultFont 16 normal",
                                     padx=10, pady=10,
                                     bg=background,
                                     fg=txt_colour)
        self.converter_label.grid(row=0)

        # 'Convert from:' label (row1)
        self.convert_from_label = Label(self.converter_frame,
                                        text="Convert from: ",
                                        font="TkDefaultFont 11",
                                        fg=txt_colour,
                                        bg=background,
                                        width=37,
                                        anchor=W,
                                        pady=0,
                                        )
        self.convert_from_label.grid(row=1)

        # 'Convert from' buttons frame (row2)
        self.from_buttons_frame = Frame(self.converter_frame,
                                        width=50,
                                        bg="white", pady=20, padx=5,
                                        )
        self.from_buttons_frame.grid(row=2)

        # 'Convert from' buttons
        self.from_usd_button = Button(self.from_buttons_frame,
                                      text="USD $",
                                      padx=0, pady=0,
                                      bg=background,
                                      fg=txt_colour,
                                      width=15, height=2,
                                      relief=GROOVE
                                      )
        self.from_usd_button.grid(row=0, column=0)

        self.from_nzd_button = Button(self.from_buttons_frame,
                                      text="NZD $",
                                      padx=0, pady=0,
                                      bg=background,
                                      fg=txt_colour,
                                      width=15, height=2,
                                      relief=GROOVE
                                      )
        self.from_nzd_button.grid(row=0, column=1)

        self.from_rmb_button = Button(self.from_buttons_frame,
                                      text="RMB ¥",
                                      padx=0, pady=0,
                                      bg=background,
                                      fg=txt_colour,
                                      width=15, height=2,
                                      relief=GROOVE,
                                      )
        self.from_rmb_button.grid(row=0, column=2)

        # Currency amount entry box (row3)
        self.to_convert_entry = Entry(self.converter_frame,
                                      width=37,
                                      font="TkDefaultFont 13 italic",
                                      relief=GROOVE,
                                      fg=txt_colour,
                                      bg=box_bg,)
        self.to_convert_entry.grid(row=3, pady=4,)

        self.empty_row = Label(self.converter_frame,
                               text="\n",
                               bg=background,
                               pady=0,
                               )
        self.empty_row.grid(row=4)

        # 'Convert to:' label (row5)
        self.convert_to_label = Label(self.converter_frame,
                                      text="Convert to: ",
                                      font="TkDefaultFont 11",
                                      fg=txt_colour,
                                      bg=background,
                                      width=37,
                                      anchor=W,
                                      )
        self.convert_to_label.grid(row=5)

        # 'Convert to' buttons frame (row6)
        self.to_buttons_frame = Frame(self.converter_frame,
                                      width=50,
                                      bg="white", pady=19, padx=5,
                                      )
        self.to_buttons_frame.grid(row=6)

        # 'Convert from' buttons
        self.to_usd_button = Button(self.to_buttons_frame,
                                    text="USD $",
                                    bg=background,
                                    fg=txt_colour,
                                    width=15, height=2,
                                    relief=GROOVE
                                    )
        self.to_usd_button.grid(row=0, column=0)

        self.to_nzd_button = Button(self.to_buttons_frame,
                                    text="NZD $",
                                    bg=background,
                                    fg=txt_colour,
                                    width=15, height=2,
                                    relief=GROOVE
                                    )
        self.to_nzd_button.grid(row=0, column=1)

        self.to_rmb_button = Button(self.to_buttons_frame,
                                    text="RMB ¥",
                                    bg=background,
                                    fg=txt_colour,
                                    width=15, height=2,
                                    relief=GROOVE,
                                    )
        self.to_rmb_button.grid(row=0, column=2)

        # Output label (row7)
        self.output_label = Label(self.converter_frame,
                                  text="Answer output",
                                  font="TkDefaultFont 11 italic",
                                  bg=box_bg,
                                  borderwidth=1,
                                  relief=GROOVE,
                                  fg=txt_colour,
                                  width=38,
                                  anchor=W,
                                  pady=4,
                                  )
        self.output_label.grid(row=7)

        self.empty_row = Label(self.converter_frame,
                               text="",
                               bg=background,
                               pady=0,
                               )
        self.empty_row.grid(row=8)

        # History and Help buttons frame
        self.hist_help_frame = Frame(self.converter_frame,
                                     pady=10, width=37,
                                     bg=background, )
        self.hist_help_frame.grid(row=9)

        # 'History' button
        self.hist_button = Button(self.hist_help_frame,
                                  padx=25, pady=10,
                                  relief=GROOVE,
                                  text="History",
                                  bg=background,
                                  fg=txt_colour, )
        self.hist_button.grid(row=0, column=0, padx=9)

        # 'Help' button
        self.help_button = Button(self.hist_help_frame,
                                  padx=30, pady=10,
                                  relief=GROOVE,
                                  text="Help",
                                  bg=background,
                                  fg=txt_colour,
                                  command=lambda: self.help(),)
        self.help_button.grid(row=0, column=2, padx=9)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Program instructions")


# Help GUI
class Help:
    def __init__(self, partner):
        background = "White",
        txt = "#396CDE"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie:help box)
        self.help_box = Toplevel()

        # if users press cross at top, closes help and 'release' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner)
                               )

        # set up GUI frame
        self.help_frame = Frame(self.help_box,
                                bg=background)
        self.help_frame.grid()

        # set up Help heading (row 0)
        self.help_heading = Label(self.help_frame,
                                  text="Help / Instructions",
                                  font="TkDefaultFont 11",
                                  bg=background,
                                  fg=txt,)
        self.help_heading.grid(row=0)

        # Help text (label, row1)
        self.help_text = Label(self.help_frame,
                               text=" ",
                               justify=LEFT,
                               width=40,
                               wrap=250,
                               bg=background,
                               fg=txt,
                               )
        self.help_text.grid(column=0, row=1)

        # dismiss button (row 2)
        self.dismiss_button = Button(self.help_frame,
                                     text="Dismiss",
                                     width=10,
                                     bg=background,
                                     fg=txt,
                                     relief=GROOVE,
                                     font="TkDefaultFont 11",
                                     command=partial(self.close_help,
                                                     partner)
                                     )
        self.dismiss_button.grid(row=2, pady=10)

    def close_help(self, partner):
        # put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    something = Converter()
    root.mainloop()
