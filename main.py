from tkinter import *


def check_is_int(type):
    global register
    global y
    if type == "y":
        fcheck = float(y)
        if fcheck.is_integer():
            y = str(int(fcheck))
    if type == "register":
        fcheck = float(register)
        if fcheck.is_integer():
            register = str(int(fcheck))


def update_output(output):
    input_widget.configure(text=output)


def blank_register():
    input_widget.configure(text="")


def debug():
    global register
    global x
    global y
    global current_func
    global first_time
    print(
        f"x: {x}, y: {y}, register: {register}, func: {current_func}, first: {first_time}, reg_disp: {register_displayed}")


def press_plus():
    global last_button_operator
    global register
    global x
    global y
    global first_time
    global register_displayed
    global current_func
    global last_button_equals
    # debug()
    # current_func = "plus"
    if last_button_operator:
        current_func = "plus"
        last_button_operator = True
        return
    if last_button_equals:
        print("FOUND ME!")
        # register = y
        y = ""
        debug()
        current_func = "plus"
        last_button_operator = True
        return
    if first_time is True:
        register = y
        y = ""
        update_output(register)
        register_displayed = True
        first_time = False
    else:
        print("DEBUG THIS")
        debug()
        press_equals()
        # print(float(register) + float(y))
        # debug()
        # x = register
        register_displayed = True
        # first_time = True
        # debug()
        update_output(register)
    # y = ""
    # debug()
    current_func = "plus"
    # update_output()
    last_button_operator = True
    last_button_equals = False
    # blank_register()
    y = ""


def press_minus():
    global last_button_operator
    global register
    global x
    global y
    global first_time
    global register_displayed
    global current_func
    global last_button_equals
    # debug()
    # current_func = "plus"
    if last_button_operator:
        current_func = "minus"
        last_button_operator = True
        return
    if last_button_equals:
        print("FOUND ME!")
        # register = y
        y = ""
        debug()
        current_func = "minus"
        last_button_operator = True
        return
    if first_time is True:
        register = y
        y = ""
        update_output(register)
        register_displayed = True
        first_time = False
    else:
        print("DEBUG THIS")
        debug()
        press_equals()
        # print(float(register) + float(y))
        # debug()
        # x = register
        register_displayed = True
        # first_time = True
        # debug()
        update_output(register)
    # y = ""
    # debug()
    current_func = "minus"
    # update_output()
    last_button_operator = True
    last_button_equals = False
    # blank_register()
    y = ""


def press_times():
    global last_button_operator
    global register
    global x
    global y
    global first_time
    global register_displayed
    global current_func
    global last_button_equals
    # debug()
    # current_func = "plus"
    if last_button_operator:
        current_func = "times"
        last_button_operator = True
        return
    if last_button_equals:
        print("FOUND ME!")
        # register = y
        y = ""
        debug()
        current_func = "times"
        last_button_operator = True
        return
    if first_time is True:
        register = y
        y = ""
        update_output(register)
        register_displayed = True
        first_time = False
    else:
        print("DEBUG THIS")
        debug()
        press_equals()
        # print(float(register) + float(y))
        # debug()
        # x = register
        register_displayed = True
        # first_time = True
        # debug()
        update_output(register)
    # y = ""
    # debug()
    current_func = "times"
    # update_output()
    last_button_operator = True
    last_button_equals = False
    # blank_register()
    y = ""


def press_divide():
    global last_button_operator
    global register
    global x
    global y
    global first_time
    global register_displayed
    global current_func
    global last_button_equals
    # debug()
    # current_func = "plus"
    if last_button_operator:
        current_func = "divide"
        last_button_operator = True
        return
    if last_button_equals:
        print("FOUND ME!")
        # register = y
        y = ""
        debug()
        current_func = "divide"
        last_button_operator = True
        return
    if first_time is True:
        register = y
        y = ""
        update_output(register)
        register_displayed = True
        first_time = False
    else:
        print("DEBUG THIS")
        debug()
        press_equals()
        # print(float(register) + float(y))
        # debug()
        # x = register
        register_displayed = True
        # first_time = True
        # debug()
        update_output(register)
    # y = ""
    # debug()
    current_func = "divide"
    # update_output()
    last_button_operator = True
    last_button_equals = False
    # blank_register()
    y = ""


def press_power():
    global last_button_operator
    global register
    global x
    global y
    global first_time
    global register_displayed
    global current_func
    global last_button_equals
    # debug()
    # current_func = "plus"
    if last_button_operator:
        current_func = "power"
        last_button_operator = True
        return
    if last_button_equals:
        print("FOUND ME!")
        # register = y
        y = ""
        debug()
        current_func = "power"
        last_button_operator = True
        return
    if first_time is True:
        register = y
        y = ""
        update_output(register)
        register_displayed = True
        first_time = False
    else:
        print("DEBUG THIS")
        debug()
        press_equals()
        # print(float(register) + float(y))
        # debug()
        # x = register
        register_displayed = True
        # first_time = True
        # debug()
        update_output(register)
    # y = ""
    # debug()
    current_func = "power"
    # update_output()
    last_button_operator = True
    last_button_equals = False
    # blank_register()
    y = ""


def press_negate():
    global y
    global x
    global register
    global first_time
    global register_displayed
    if not register_displayed:
        if y == "":
            return
        elif float(y) == 0:
            return
        elif float(y) > 0:
            y = "-" + y
            # register = y
        elif float(y) < 0:
            y = y.lstrip("-")
            # register = y
        check_is_int("y")
        update_output(y)
        debug()
        return
    elif register_displayed:
        if float(register) > 0:
            register = "-" + register
            x = register
            y = "0"
            first_time = True
        elif float(register) < 0:
            register = register.lstrip("-")
            x = register
            y = "0"
            first_time = True
        check_is_int("register")
        update_output(register)
        debug()
        return


def press_one():
    global y
    global register_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    register_displayed = False
    y += "1"
    update_output(y)


def press_two():
    global y
    global register_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    register_displayed = False
    y += "2"
    update_output(y)


def press_three():
    global y
    global register_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    register_displayed = False
    y += "3"
    update_output(y)


def press_four():
    global y
    global register_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    register_displayed = False
    y += "4"
    update_output(y)


def press_five():
    global y
    global register_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    register_displayed = False
    y += "5"
    update_output(y)


def press_six():
    global y
    global register_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    register_displayed = False
    y += "6"
    update_output(y)


def press_seven():
    global y
    global register_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    register_displayed = False
    y += "7"
    update_output(y)


def press_eight():
    global y
    global register_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    register_displayed = False
    y += "8"
    update_output(y)


def press_nine():
    global y
    global register_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    register_displayed = False
    y += "9"
    update_output(y)


def press_zero():
    global y
    global register_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    register_displayed = False
    y += "0"
    update_output(y)


def press_decimal():
    global y
    global register_displayed
    global last_button_equals
    global last_button_operator
    last_button_operator = False
    last_button_equals = False
    register_displayed = False
    if "." not in y:
        y += "."
        # check_is_int("y")
        update_output(y)


def press_clear():
    global x
    global y
    global register
    global first_time
    global last_button_operator
    global last_button_equals
    global current_func
    x = "0"
    y = ""
    register = "0"
    current_func = ""
    last_button_operator = False
    last_button_equals = False
    first_time = True
    update_output("")


def press_equals():
    global register
    global register_displayed
    global last_button_equals
    global y
    global current_func
    global last_button_operator
    if last_button_operator is True:
        y = register
        print("last button was operator before equals")
        debug()
    match current_func:
        case "":
            return
        case "plus":
            print("adding")
            debug()
            register = str(float(register) + float(y))
        case "minus":
            print('subtracting')
            # debug()
            register = str(float(register) - float(y))
        case "times":
            register = str(float(register) * float(y))
        case "divide":
            register = str(float(register) / float(y))
        case "power":
            register = str(float(register) ** float(y))
    # debug()
    # y = ""
    check_is_int("register")
    debug()
    update_output(register)
    print(register)
    # update_output(register)
    register_displayed = True
    last_button_operator = False
    last_button_equals = True
    return


register = "0"
x = "0"
first_time = True
register_displayed = False
last_button_operator = False
last_button_equals = False
y = ""
current_func = ""
result = ""

# Create Window
win = Tk()
win.title("Calculator")
win.grid_rowconfigure(6, weight=1)


def do_nothing():
    return


# Create input tracker
input_widget = Label(win, text="", fg="black", relief=SUNKEN, bg="white", font="Helvetica 14")

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

# Bind return to run the app and shift+return to the Random! button
# win.bind('<Return>', lambda e: calculator())

# def main():
#     win.mainloop()
#     register = ""


if __name__ == "__main__":
    register = ""
    win.mainloop()
