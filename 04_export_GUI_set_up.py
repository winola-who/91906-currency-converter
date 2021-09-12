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
        self.converter_frame = Frame(bg=background,
                                     pady=10,
                                     padx=10,
                                     )
        self.converter_frame.grid()

        # Currency converter heading (row0)
        self.converter_label = Label(self.converter_frame,
                                     text="Currency Converter",
                                     font="TkDefaultFont 16 normal",
                                     padx=115, pady=10,
                                     bg=background,
                                     fg=txt_colour,
                                     )
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
                                        bg="white", pady=7, padx=5,
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
                                      bg=box_bg, )
        self.to_convert_entry.grid(row=3, pady=4, )

        self.empty_row = Label(self.converter_frame,
                               text="",
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
                                      bg="white", pady=12, padx=5,
                                      )
        self.to_buttons_frame.grid(row=6)

        # 'Convert to' buttons
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
                                  anchor=W, )
        self.output_label.grid(row=7, ipady=3)

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
                                  fg=txt_colour,
                                  command=lambda: self.history())
        self.hist_button.grid(row=0, column=0, padx=9)

        # 'Help' button
        self.help_button = Button(self.hist_help_frame,
                                  padx=30, pady=10,
                                  relief=GROOVE,
                                  text="Help",
                                  bg=background,
                                  fg=txt_colour,
                                  command=lambda: self.help(), )
        self.help_button.grid(row=0, column=2, padx=9)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Program instructions")

    def history(self):
        print("Show conversion history")
        History(self)


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
                                  font="TkDefaultFont 16 normal",
                                  bg=background,
                                  fg=txt, padx=85, pady=15)
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
        self.dismiss_button.grid(row=2, pady=10, padx=10, sticky=E)

    def close_help(self, partner):
        # put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class History:
    def __init__(self, partner):
        background = "White",
        txt = "#396CDE"

        # disable help button
        partner.hist_button.config(state=DISABLED)

        # sets up child window (ie:help box)
        self.hist_box = Toplevel()

        # if users press cross at top, closes help and 'release' help button
        self.hist_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_hist, partner)
                               )

        # set up GUI frame
        self.hist_frame = Frame(self.hist_box,
                                bg=background,
                                width=300, )
        self.hist_frame.grid()

        # set up Help heading (row 0)
        self.hist_heading = Label(self.hist_frame,
                                  text="Conversion History",
                                  font="TkDefaultFont 16 normal",
                                  bg=background,
                                  fg=txt,
                                  padx=100, pady=15)
        self.hist_heading.grid(row=0)

        # Exporting instructions (label, row1)
        self.hist_text = Label(self.hist_frame,
                               text="Press the Export/Save button to save all conversion history as a text "
                                    "file...",
                               justify=CENTER,
                               width=40,
                               wrap=250,
                               bg=background,
                               fg=txt,
                               )
        self.hist_text.grid(row=1)

        conv_hist = "Conversion History"

        self.conv_label = Label(self.hist_frame,
                                bg=background,
                                fg=txt,
                                justify=LEFT,
                                font="TkDefaultFont 11",
                                text=conv_hist,
                                pady=15,
                                )
        self.conv_label.grid(row=2)

        # History buttons frame (row2)
        self.hist_btn_frame = Frame(self.hist_frame,
                                    bg=background, )
        self.hist_btn_frame.grid(row=3, sticky=E)

        # Export button
        self.export_button = Button(self.hist_btn_frame,
                                    text="Export/Save",
                                    width=10,
                                    bg=background,
                                    fg=txt,
                                    relief=GROOVE,
                                    font="TkDefaultFont 11",
                                    command=lambda: self.export(),
                                    )
        self.export_button.grid(row=0, column=0, pady=10, padx=0, ipady=2, )

        # dismiss button
        self.dismiss_button = Button(self.hist_btn_frame,
                                     text="Dismiss",
                                     width=10,
                                     bg=background,
                                     fg=txt,
                                     relief=GROOVE,
                                     font="TkDefaultFont 11",
                                     command=partial(self.close_hist,
                                                     partner)
                                     )
        self.dismiss_button.grid(row=0, column=1, pady=10, padx=10, ipady=2, )

    def close_hist(self, partner):
        # put help button back to normal
        partner.hist_button.config(state=NORMAL)
        self.hist_box.destroy()

    def export(self):
        print("Export conversion history")
        Export(self)


class Export:
    def __init__(self, partner):
        background = "White"
        txt = "#396CDE"
        box_bg = "#F0F8FF"

        # disable help button
        partner.export_button.config(state=DISABLED)

        # sets up child window (ie:help box)
        self.export_box = Toplevel()

        # if users press cross at top, closes help and 'release' help button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner)
                                 )

        # set up GUI frame
        self.export_frame = Frame(self.export_box,
                                  bg=background)
        self.export_frame.grid()

        # export text (label, row0)
        self.export_text = Label(self.export_frame,
                                 text="Enter a file name to save your conversion history as...",
                                 justify=LEFT,
                                 width=50,
                                 bg=background,
                                 fg=txt,
                                 font="TkDefaultFont 10 bold",
                                 pady=12,
                                 )
        self.export_text.grid(column=0, row=0)

        # filename entry box
        self.filename_entry = Entry(self.export_frame,
                                    bg=box_bg,
                                    width=37,
                                    fg=txt,
                                    font="TkDefaultFont 13 italic",
                                    relief=GROOVE,
                                    )
        self.filename_entry.grid(row=1, pady=4,)

        # export text
        self.export_text2 = Label(self.export_frame,
                                  text="Your conversion history will be saved as a text file in the same folder of "
                                       "this program...",
                                  justify=LEFT,
                                  width=40,
                                  wrap=250,
                                  bg=background,
                                  fg=txt,
                                  pady=15, padx=15,
                                  )
        self.export_text2.grid(column=0, row=2, sticky=W)

        # Export buttons frame (row2)
        self.exp_btn_frame = Frame(self.export_frame,
                                   bg=background)
        self.exp_btn_frame.grid(row=3, sticky=E)

        # save button
        self.save_button = Button(self.exp_btn_frame,
                                  text="Save",
                                  width=10,
                                  bg=background,
                                  fg=txt,
                                  relief=GROOVE,
                                  font="TkDefaultFont 11",
                                  )
        self.save_button.grid(row=0, column=0, pady=10, padx=0, )

        # cancel button
        self.cancel_button = Button(self.exp_btn_frame,
                                    text="Cancel",
                                    width=10,
                                    bg=background,
                                    fg=txt,
                                    relief=GROOVE,
                                    font="TkDefaultFont 11",
                                    command=partial(self.close_export,
                                                    partner)
                                    )
        self.cancel_button.grid(row=0, column=1, pady=10, padx=10, )

    def close_export(self, partner):
        # put help button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    something = Converter()
    root.mainloop()
