from tkinter import *
import re

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def calculate():
    try:
        current = result_label['text']
        # Only allow numbers, operators, and parentheses
        if re.match("^[0-9+\-*/().]*$", current):
            result = str(eval(current))
            # Round result to 2 decimal places for consistency
            result = str(round(float(result), 2))
            # Ensure the result fits in a reasonable display range
            if len(result) > 10:  # Adjust the length limit if necessary
                result = str(round(float(result), 2))
            result_label.config(text=result)
        else:
            raise ValueError("Invalid input.")
    except Exception as e:
        result_label.config(text="Error")
        print(f"Error: {e}")  # Log the error for debugging

root = Tk()
root.title("Calculator")
root.geometry("280x380")
root.configure(background='black')

result_label = Label(root, text='', background='black', foreground='white')
result_label.grid(row=0, column=0, columnspan=5, pady=(50, 25), sticky='W')
result_label.config(font=('verdana', 30, 'bold'))

# Button definitions
Button7 = Button(root, text='7', background='#00a65a', foreground='white', width=5, height=2, command=lambda: get_digit(7))
Button7.grid(row=1, column=0)
Button7.configure(font=('verdana', 14))

Button8 = Button(root, text='8', background='#00a65a', foreground='white', width=5, height=2, command=lambda: get_digit(8))
Button8.grid(row=1, column=1)
Button8.configure(font=('verdana', 14))

Button9 = Button(root, text='9', background='#00a65a', foreground='white', width=5, height=2, command=lambda: get_digit(9))
Button9.grid(row=1, column=2)
Button9.configure(font=('verdana', 14))

Button_add = Button(root, text='+', background='#00a65a', foreground='white', width=5, height=2, command=lambda: get_digit('+'))
Button_add.grid(row=1, column=3)
Button_add.configure(font=('verdana', 14))

Button4 = Button(root, text='4', background='#00a65a', foreground='white', width=5, height=2, command=lambda: get_digit(4))
Button4.grid(row=2, column=0)
Button4.configure(font=('verdana', 14))

Button5 = Button(root, text='5', background='#00a65a', foreground='white', width=5, height=2, command=lambda: get_digit(5))
Button5.grid(row=2, column=1)
Button5.configure(font=('verdana', 14))

Button6 = Button(root, text='6', background='#00a65a', foreground='white', width=5, height=2, command=lambda: get_digit(6))
Button6.grid(row=2, column=2)
Button6.configure(font=('verdana', 14))

Button_sub = Button(root, text='-', background='#00a65a', foreground='white', width=5, height=2, command=lambda: get_digit('-'))
Button_sub.grid(row=2, column=3)
Button_sub.configure(font=('verdana', 14))

Button1 = Button(root, text='1', background='#00a65a', foreground='white', width=5, height=2, command=lambda: get_digit(1))
Button1.grid(row=3, column=0)
Button1.configure(font=('verdana', 14))

Button2 = Button(root, text='2', background='#00a65a', foreground='white', width=5, height=2, command=lambda: get_digit(2))
Button2.grid(row=3, column=1)
Button2.configure(font=('verdana', 14))

Button3 = Button(root, text='3', background='#00a65a', foreground='white', width=5, height=2, command=lambda: get_digit(3))
Button3.grid(row=3, column=2)
Button3.configure(font=('verdana', 14))

Button_mul = Button(root, text='*', background='#00a65a', foreground='white', width=5, height=2, command=lambda: get_digit('*'))
Button_mul.grid(row=3, column=3)
Button_mul.configure(font=('verdana', 14))

Button0 = Button(root, text='0', background='#00a65a', foreground='white', width=5, height=2, command=lambda: get_digit(0))
Button0.grid(row=4, column=0)
Button0.configure(font=('verdana', 14))

Button_clear = Button(root, text='C', background='#00a65a', foreground='white', width=5, height=2, command=clear)
Button_clear.grid(row=4, column=1)
Button_clear.configure(font=('verdana', 14))

Button_eq = Button(root, text='=', background='#00a65a', foreground='white', width=5, height=2, command=calculate)
Button_eq.grid(row=4, column=2)
Button_eq.configure(font=('verdana', 14))

Button_div = Button(root, text='/', background='#00a65a', foreground='white', width=5, height=2, command=lambda: get_digit('/'))
Button_div.grid(row=4, column=3)
Button_div.configure(font=('verdana', 14))

root.mainloop()
