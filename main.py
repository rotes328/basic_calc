from tkinter import *


def check_is_int(arg):
    global accumulator
    global register
    if arg == "register":
        fcheck = float(register)
        if fcheck.is_integer():
            register = str(int(fcheck))
    elif arg == "accumulator":
        fcheck = float(accumulator)
        if fcheck.is_integer():
            accumulator = str(int(fcheck))


def update_output(output):
    input_widget.configure(text=output)


def blank_accumulator():
    input_widget.configure(text="")


def press_plus():
    global last_button_operator
    global accumulator
    global register
    global first_time
    global accumulator_displayed
    global current_func
    global last_button_equals
    if last_button_operator:
        current_func = "plus"
        last_button_operator = True
        return
    if last_button_equals:
        register = ""
        current_func = "plus"
        last_button_operator = True
        return
    if first_time:
        if register == "":
            return
        accumulator = register
        register = ""
        update_output(accumulator)
        accumulator_displayed = True
        first_time = False
    else:
        press_equals()
        accumulator_displayed = True
        update_output(accumulator)
    current_func = "plus"
    last_button_operator = True
    last_button_equals = False
    register = ""


def press_minus():
    global last_button_operator
    global accumulator
    global register
    global first_time
    global accumulator_displayed
    global current_func
    global last_button_equals
    if last_button_operator:
        current_func = "minus"
        last_button_operator = True
        return
    if last_button_equals:
        register = ""
        current_func = "minus"
        last_button_operator = True
        return
    if first_time:
        if register == "":
            return
        accumulator = register
        register = ""
        update_output(accumulator)
        accumulator_displayed = True
        first_time = False
    else:
        press_equals()
        accumulator_displayed = True
        update_output(accumulator)
    current_func = "minus"
    last_button_operator = True
    last_button_equals = False
    register = ""


def press_times():
    global last_button_operator
    global accumulator
    global register
    global first_time
    global accumulator_displayed
    global current_func
    global last_button_equals
    if last_button_operator:
        current_func = "times"
        last_button_operator = True
        return
    if last_button_equals:
        register = ""
        current_func = "times"
        last_button_operator = True
        return
    if first_time:
        if register == "":
            return
        accumulator = register
        register = ""
        update_output(accumulator)
        accumulator_displayed = True
        first_time = False
    else:
        press_equals()
        accumulator_displayed = True
        update_output(accumulator)
    current_func = "times"
    last_button_operator = True
    last_button_equals = False
    register = ""


def press_divide():
    global last_button_operator
    global accumulator
    global register
    global first_time
    global accumulator_displayed
    global current_func
    global last_button_equals
    if last_button_operator:
        current_func = "divide"
        last_button_operator = True
        return
    if last_button_equals:
        register = ""
        current_func = "divide"
        last_button_operator = True
        return
    if first_time:
        if register == "":
            return
        accumulator = register
        register = ""
        update_output(accumulator)
        accumulator_displayed = True
        first_time = False
    else:
        press_equals()
        accumulator_displayed = True
        update_output(accumulator)
    current_func = "divide"
    last_button_operator = True
    last_button_equals = False
    register = ""


def press_power():
    global last_button_operator
    global accumulator
    global register
    global first_time
    global accumulator_displayed
    global current_func
    global last_button_equals
    if last_button_operator:
        current_func = "power"
        last_button_operator = True
        return
    if last_button_equals:
        register = ""
        current_func = "power"
        last_button_operator = True
        return
    if first_time:
        if register == "":
            return
        accumulator = register
        register = ""
        update_output(accumulator)
        accumulator_displayed = True
        first_time = False
    else:
        press_equals()
        accumulator_displayed = True
        update_output(accumulator)
    current_func = "power"
    last_button_operator = True
    last_button_equals = False
    register = ""


def press_negate():
    global register
    global accumulator
    global first_time
    global accumulator_displayed
    if first_time:
        if register == "":
            return
    if not accumulator_displayed:
        if register == "":
            return
        elif float(register) == 0:
            return
        elif float(register) > 0:
            register = "-" + register
        elif float(register) < 0:
            register = register.lstrip("-")
        check_is_int("register")
        update_output(register)
        return
    elif accumulator_displayed:
        if float(accumulator) > 0:
            accumulator = "-" + accumulator
            register = "0"
            first_time = True
        elif float(accumulator) < 0:
            accumulator = accumulator.lstrip("-")
            register = "0"
            first_time = True
        check_is_int("accumulator")
        update_output(accumulator)
        return


def press_one():
    global register
    global accumulator_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    accumulator_displayed = False
    register += "1"
    update_output(register)


def press_two():
    global register
    global accumulator_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    accumulator_displayed = False
    register += "2"
    update_output(register)


def press_three():
    global register
    global accumulator_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    accumulator_displayed = False
    register += "3"
    update_output(register)


def press_four():
    global register
    global accumulator_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    accumulator_displayed = False
    register += "4"
    update_output(register)


def press_five():
    global register
    global accumulator_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    accumulator_displayed = False
    register += "5"
    update_output(register)


def press_six():
    global register
    global accumulator_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    accumulator_displayed = False
    register += "6"
    update_output(register)


def press_seven():
    global register
    global accumulator_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    accumulator_displayed = False
    register += "7"
    update_output(register)


def press_eight():
    global register
    global accumulator_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    accumulator_displayed = False
    register += "8"
    update_output(register)


def press_nine():
    global register
    global accumulator_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    accumulator_displayed = False
    register += "9"
    update_output(register)


def press_zero():
    global register
    global accumulator_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    accumulator_displayed = False
    register += "0"
    update_output(register)


def press_decimal():
    global register
    global accumulator_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    accumulator_displayed = False
    if "." not in register:
        register += "."
        update_output(register)


def press_clear():
    global register
    global accumulator
    global first_time
    global last_button_operator
    global last_button_equals
    global current_func
    register = ""
    accumulator = "0"
    current_func = ""
    last_button_operator = False
    last_button_equals = False
    first_time = True
    update_output("")


def press_equals():
    global accumulator
    global accumulator_displayed
    global last_button_equals
    global register
    global current_func
    global last_button_operator
    if last_button_operator is True:
        register = accumulator
    match current_func:
        case "":
            return
        case "plus":
            accumulator = str(float(accumulator) + float(register))
        case "minus":
            accumulator = str(float(accumulator) - float(register))
        case "times":
            accumulator = str(float(accumulator) * float(register))
        case "divide":
            accumulator = str(float(accumulator) / float(register))
        case "power":
            accumulator = str(float(accumulator) ** float(register))
    check_is_int("accumulator")
    update_output(accumulator)
    accumulator_displayed = False
    last_button_operator = False
    last_button_equals = True
    return


# Set initial values
accumulator = "0"
first_time = True
accumulator_displayed = False
last_button_operator = False
last_button_equals = False
register = ""
current_func = ""
result = ""

# Create Window
win = Tk()
win.title("Calculator")
win.grid_rowconfigure(6, weight=1)

# Create input tracker
input_widget = Label(win, text="", fg="black", relief=SUNKEN, bg="white")

# Create buttons
clear_button = Button(win, text="AC", command=lambda: press_clear())
negate_button = Button(win, text="+/-", command=lambda: press_negate())
exp_button = Button(win, text="^", command=lambda: press_power())
divide_button = Button(win, text="÷", command=lambda: press_divide())
seven_button = Button(win, text="7", command=lambda: press_seven())
eight_button = Button(win, text="8", command=lambda: press_eight())
nine_button = Button(win, text="9", command=lambda: press_nine())
multiply_button = Button(win, text="x", command=lambda: press_times())
four_button = Button(win, text="4", command=lambda: press_four())
five_button = Button(win, text="5", command=lambda: press_five())
six_button = Button(win, text="6", command=lambda: press_six())
minus_button = Button(win, text="-", command=lambda: press_minus())
one_button = Button(win, text="1", command=lambda: press_one())
two_button = Button(win, text="2", command=lambda: press_two())
three_button = Button(win, text="3", command=lambda: press_three())
plus_button = Button(win, text="+", command=lambda: press_plus())
zero_button = Button(win, text="0", command=lambda: press_zero())
decimal_button = Button(win, text=".", command=lambda: press_decimal())
equals_button = Button(win, text="=", command=lambda: press_equals())

# Organize grid
input_widget.grid(row=0, column=0, columnspan=4, sticky=W + E)
clear_button.grid(row=1, column=0)
negate_button.grid(row=1, column=1)
exp_button.grid(row=1, column=2)
divide_button.grid(row=1, column=3)
seven_button.grid(row=2, column=0)
eight_button.grid(row=2, column=1)
nine_button.grid(row=2, column=2)
multiply_button.grid(row=2, column=3)
four_button.grid(row=3, column=0)
five_button.grid(row=3, column=1)
six_button.grid(row=3, column=2)
minus_button.grid(row=3, column=3)
one_button.grid(row=4, column=0)
two_button.grid(row=4, column=1)
three_button.grid(row=4, column=2)
plus_button.grid(row=4, column=3)
zero_button.grid(row=5, column=0)
decimal_button.grid(row=5, column=1)
equals_button.grid(row=5, column=2, columnspan=2, sticky=W + E)

# Bind keys
win.bind("<Return>", lambda e: press_equals())
win.bind("1", lambda e: press_one())
win.bind("2", lambda e: press_two())
win.bind("3", lambda e: press_three())
win.bind("4", lambda e: press_four())
win.bind("5", lambda e: press_five())
win.bind("6", lambda e: press_six())
win.bind("7", lambda e: press_seven())
win.bind("8", lambda e: press_eight())
win.bind("9", lambda e: press_nine())
win.bind("0", lambda e: press_zero())
win.bind(".", lambda e: press_decimal())
win.bind("+", lambda e: press_plus())
win.bind("-", lambda e: press_minus())
win.bind("*", lambda e: press_times())
win.bind("/", lambda e: press_divide())
win.bind("^", lambda e: press_power())
win.bind("<Escape>", lambda e: press_clear())

if __name__ == "__main__":
    accumulator = ""
    win.mainloop()
