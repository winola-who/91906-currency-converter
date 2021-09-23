from tkinter import *
# to prevent unwanted windows
from functools import partial


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
                                      relief=GROOVE,
                                      command=lambda: self.convert_from("USD")
                                      )
        self.from_usd_button.grid(row=0, column=0)

        self.from_nzd_button = Button(self.from_buttons_frame,
                                      text="NZD $",
                                      padx=0, pady=0,
                                      bg=background,
                                      fg=txt_colour,
                                      width=15, height=2,
                                      relief=GROOVE,
                                      command=lambda: self.convert_from("NZD")
                                      )
        self.from_nzd_button.grid(row=0, column=1)

        self.from_rmb_button = Button(self.from_buttons_frame,
                                      text="RMB ¥",
                                      padx=0, pady=0,
                                      bg=background,
                                      fg=txt_colour,
                                      width=15, height=2,
                                      relief=GROOVE,
                                      command=lambda: self.convert_from("RMB")
                                      )
        self.from_rmb_button.grid(row=0, column=2)

        # Currency amount entry box (row3)
        self.to_convert_entry = Entry(self.converter_frame,
                                      width=37,
                                      font="TkDefaultFont 13 italic",
                                      relief=GROOVE,
                                      fg=txt_colour,
                                      bg=box_bg,
                                      )
        self.to_convert_entry.grid(row=3, pady=4, )

        # Empty row
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
                                    relief=GROOVE,
                                    command=lambda: self.convert_to("USD")
                                    )
        self.to_usd_button.grid(row=0, column=0)

        self.to_nzd_button = Button(self.to_buttons_frame,
                                    text="NZD $",
                                    bg=background,
                                    fg=txt_colour,
                                    width=15, height=2,
                                    relief=GROOVE,
                                    command=lambda: self.convert_to("NZD")
                                    )
        self.to_nzd_button.grid(row=0, column=1)

        self.to_rmb_button = Button(self.to_buttons_frame,
                                    text="RMB ¥",
                                    bg=background,
                                    fg=txt_colour,
                                    width=15, height=2,
                                    relief=GROOVE,
                                    command=lambda: self.convert_to("RMB")
                                    )
        self.to_rmb_button.grid(row=0, column=2)

        # Convert button and output frame
        self.conv_out_frame = Frame(self.converter_frame,
                                    pady=10, width=37,
                                    bg=background
                                    )
        self.conv_out_frame.grid(row=7)

        self.convert_button = Button(self.conv_out_frame,
                                     text="Convert",
                                     font="TkDefaultFont 11 bold",
                                     bg="#6495ED",
                                     relief=GROOVE,
                                     fg=background,
                                     pady=5, padx=5,
                                     command=lambda: self.conversion(chosen_currencies[0], chosen_currencies[1]),
                                     )
        self.convert_button.grid(row=0, column=0, padx=5, )

        # Output label
        self.output_label = Label(self.conv_out_frame,
                                  text="Answer output",
                                  font="TkDefaultFont 11 italic",
                                  bg=box_bg,
                                  borderwidth=1,
                                  relief=GROOVE,
                                  fg=txt_colour,
                                  width=25,
                                  pady=4, padx=12,
                                  )
        self.output_label.grid(row=0, column=1, padx=5, ipady=6, )

        # History and Help buttons frame
        self.hist_help_frame = Frame(self.converter_frame,
                                     pady=10, width=37,
                                     bg=background, )
        self.hist_help_frame.grid(row=8)

        # 'History' button
        self.hist_button = Button(self.hist_help_frame,
                                  padx=25, pady=10,
                                  relief=GROOVE,
                                  text="History",
                                  bg=background,
                                  fg=txt_colour, )
        self.hist_button.grid(row=0, column=0, padx=12)

        # 'Help' button
        self.help_button = Button(self.hist_help_frame,
                                  padx=30, pady=10,
                                  relief=GROOVE,
                                  text="Help",
                                  bg=background,
                                  fg=txt_colour, )
        self.help_button.grid(row=0, column=2, padx=12)

        # Hidden entry boxes to store chosen currencies to convert
        self.from_curr = Entry(self.converter_frame)
        self.from_curr.grid(row=9, column=0)
        self.from_curr.grid_forget()

        self.to_curr = Entry(self.converter_frame)
        self.to_curr.grid(row=9, column=1)
        self.to_curr.grid_forget()

    # function to add chosen currency to convert from to a list
    def convert_from(self, curr):
        self.from_curr.delete(0, END)
        self.from_curr.insert(0, curr)
        chosen = self.from_curr.get()
        chosen_currencies.insert(0, chosen)

    # function to insert chosen currency to convert to into the chosen_currencies list
    def convert_to(self, curr):
        self.to_curr.delete(0, END)
        self.to_curr.insert(0, curr)
        chosen = self.to_curr.get()
        chosen_currencies.insert(1, chosen)

    # answer rounding function, called before outputting the answer
    def rounding(self, answer):
        if answer % 1 == 0:
            rounded = answer
            return rounded
        else:
            rounded = round(answer, 2)
            return rounded

    # function to convert currency amounts
    def conversion(self, from_, to_):
        value = self.to_convert_entry.get()
        error_msg = ""
        answer = ""
        converted = ""
        symbol_to = ""
        symbol_from = ""
        txt_colour = "#396CDE"

        try:
            # check that the amount input is a number
            value = float(value)

            if from_ == "USD" and value > 0:
                symbol_from = "$"
                if to_ == "USD":
                    # output error when the user chose the same currency to convert to
                    error_msg = "Please choose a different currency"
                elif to_ == "NZD" and value > 0:
                    # setting conversion ratios based on the currency chosen
                    ratio = 1.42
                    # converts the amount inputted
                    converted = value * ratio
                    symbol_to = "$"
                elif to_ == "RMB" and value > 0:
                    ratio = 6.47
                    converted = value * ratio
                    symbol_to = "¥"

            elif from_ == "NZD" and value > 0:
                symbol_from = "$"
                if to_ == "USD":
                    ratio = 0.7
                    converted = value * ratio
                    symbol_to = "$"
                elif to_ == "NZD" and value > 0:
                    error_msg = "Please choose a different currency"
                elif to_ == "RMB" and value > 0:
                    ratio = 4.55
                    converted = value * ratio
                    symbol_to = "¥"

            elif from_ == "RMB" and value > 0:
                symbol_from = "¥"
                if to_ == "USD":
                    ratio = 0.15
                    converted = value * ratio
                    symbol_to = "$"
                elif to_ == "NZD" and value > 0:
                    ratio = 0.22
                    converted = value * ratio
                    symbol_to = "$"
                elif to_ == "RMB" and value > 0:
                    error_msg = "Please choose a different currency"

            else:
                # error for when the input is less than 0
                error_msg = "Please enter a number that is greater than 0."

        except ValueError:
            # error when the input is not a number
            error_msg = "Please enter a number!"

        # round converted values before output
        if converted != "":
            converted = self.rounding(converted)
            # format answer output
            answer = "{}{}".format(symbol_to, converted)

        if error_msg == "":
            # change text in output label to the converted answer when there are no error
            self.output_label.configure(text=answer, fg=txt_colour)
            # adds converted answer to conversion history list
            history = "{} {}{} to {} {}".format(from_, symbol_from, value, to_, answer)
            all_conversions.append(history)
        else:
            # change text in output label to show the error message when there are errors
            self.output_label.configure(text=error_msg, fg=txt_colour)
            history = ""
            all_conversions.append(history)

        # clears the list for chosen currencies
        chosen_currencies.clear()

        # prints the history list for testing (will be removed in assembled outcome)
        last_conversion = all_conversions[-1]
        print(last_conversion)


# list for storing the currencies the user chose
chosen_currencies = []

# list for storing calculation history
all_conversions = []


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    something = Converter()
    root.mainloop()
