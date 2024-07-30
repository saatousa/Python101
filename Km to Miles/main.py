# FINAL PROJECT:
import tkinter


def miles_to_km():
    user_miles = float(user_entry.get())
    kilometer = round(user_miles * 1.609, 2)
    kilometer_result.config(text=kilometer)
    print(kilometer_result)


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=50,pady=30)

user_entry = tkinter.Entry(width=8)
user_entry.insert(index=0, string="0")
user_entry.focus()
user_entry.grid(column=1, row=0)

miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

kilometer_result = tkinter.Label(text=0)
kilometer_result.grid(column=1, row=1)

km = tkinter.Label(text="Km")
km.grid(column=2, row=1)

calculate = tkinter.Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
