from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import math

#User Interface

root = Tk()
root.title("Calculator")
root.geometry("300x420")

label_frame = Label()

delete_icon = ImageTk.PhotoImage(Image.open("C:/Users/albus/Desktop/Calculator/icons/images.png").resize((20, 20), Image.ANTIALIAS))
x_square_icon = ImageTk.PhotoImage(Image.open("C:/Users/albus/Desktop/Calculator/icons/x-squared.png").resize((60, 60), Image.ANTIALIAS))
square_root_icon = ImageTk.PhotoImage(Image.open("C:/Users/albus/Desktop/Calculator/icons/square_root_x.png").resize((40, 40), Image.ANTIALIAS))
division_icon = ImageTk.PhotoImage(Image.open("C:/Users/albus/Desktop/Calculator/icons/division.png").resize((15, 15), Image.ANTIALIAS))
multiply_icon = ImageTk.PhotoImage(Image.open("C:/Users/albus/Desktop/Calculator/icons/multiply.png").resize((20, 20), Image.ANTIALIAS))
subtraction_icon = ImageTk.PhotoImage(Image.open("C:/Users/albus/Desktop/Calculator/icons/subtraction.png").resize((20, 20), Image.ANTIALIAS))
addition_icon = ImageTk.PhotoImage(Image.open("C:/Users/albus/Desktop/Calculator/icons/addition.png").resize((20, 20), Image.ANTIALIAS))
negate_icon = ImageTk.PhotoImage(Image.open("C:/Users/albus/Desktop/Calculator/icons/negate.png").resize((20, 20), Image.ANTIALIAS))
calculation_icon = ImageTk.PhotoImage(Image.open("C:/Users/albus/Desktop/Calculator/icons/equal.png").resize((20, 20), Image.ANTIALIAS))
dot_icon = ImageTk.PhotoImage(Image.open("C:/Users/albus/Desktop/Calculator/icons/dot.png").resize((10, 10), Image.ANTIALIAS))

current_text = "" 

def button_zero():
    label_frame.config(text="0", font=("Arial", 25, "bold"))
    label_frame.place(x=10, y=70)
    global current_text

    current_text += "0"

    label_frame.config(text=current_text)


def button_one():
    label_frame.config(text="1", font=("Arial", 25, "bold"))
    label_frame.place(x=10, y=70)
    global current_text

    current_text += "1"

    label_frame.config(text=current_text)

def button_two():
    label_frame.config(text="2", font=("Arial", 25, "bold"))
    label_frame.place(x=10, y=70)
    global current_text

    current_text += "2"

    label_frame.config(text=current_text)

def button_three():
    label_frame.config(text="3", font=("Arial", 25, "bold"))
    label_frame.place(x=10, y=70)
    global current_text

    current_text += "3"

    label_frame.config(text=current_text)

def button_four():
    label_frame.config(text="4", font=("Arial", 25, "bold"))
    label_frame.place(x=10, y=70)
    global current_text

    current_text += "4"

    label_frame.config(text=current_text)

def button_five():
    label_frame.config(text="5", font=("Arial", 25, "bold"))
    label_frame.place(x=10, y=70)
    global current_text

    current_text += "5"

    label_frame.config(text=current_text)

def button_six():
    label_frame.config(text="6", font=("Arial", 25, "bold"))
    label_frame.place(x=10, y=70)
    global current_text

    current_text += "6"

    label_frame.config(text=current_text)

def button_seven():
    label_frame.config(text="7", font=("Arial", 25, "bold"))
    label_frame.place(x=10, y=70)
    global current_text

    current_text += "7"

    label_frame.config(text=current_text)

def button_eight():
    label_frame.config(text="8", font=("Arial", 25, "bold"))
    label_frame.place(x=10, y=70)
    global current_text

    current_text += "8"

    label_frame.config(text=current_text)

def button_nine():
    label_frame.config(text="9", font=("Arial", 25, "bold"))
    label_frame.place(x=10, y=70)
    global current_text

    current_text += "9"

    label_frame.config(text=current_text) 

def addition():
    global current_text 

    if current_text and current_text[-1].isdigit():
        current_text += "+"

    label_frame.config(text=current_text)

def subtraction():
    global current_text

    if current_text and current_text[-1].isdigit():
        current_text += "-"

    label_frame.config(text=current_text)

def multiply():
    global current_text

    if current_text and current_text[-1].isdigit():
        current_text += "x"

    label_frame.config(text=current_text)

def division():
    global current_text

    if current_text and current_text[-1].isdigit():
        current_text += "/"
        
    label_frame.config(text=current_text)
     

def divide_one():
    global current_text

    if current_text:

        i = len(current_text) - 1
        
        while i >= 0 and (current_text[i].isdigit() or current_text[i] == '.'):
            i -= 1

        last_number = current_text[i + 1:]

        try:
            reciprocal = 1 / float(last_number)
            current_text = current_text[:i + 1] + str(reciprocal
                                                      )
        except (ValueError, ZeroDivisionError):
            current_text = "Error"

        label_frame.config(text=current_text)

def dot():
    global current_text

    if current_text and current_text[-1].isdigit():
        current_text = current_text + "."

    label_frame.config(text=current_text)

def x_square():
    global current_text

    if current_text and current_text[-1].isdigit():
        i = len(current_text) - 1

        while i >= 0 or current_text[i] == ".":
            i -= 1
        number = current_text[i + 1:]

        x_squared = eval(f"{number} * {number}")
        current_text = current_text[:i + 1] + str(x_squared)
        
        label_frame.config(text=current_text)

def x_square_root():
    global current_text

    try:
        root_value = float(current_text)
        sqrt_result = math.sqrt(root_value)
        
        if sqrt_result.is_integer():
            current_text = str(int(sqrt_result)) 
        else:
            current_text = f"{sqrt_result:.2f}" 

    except (ValueError, ZeroDivisionError):
        current_text = "Error"

    label_frame.config(text=current_text)

    
    
def delete():
    global current_text

    if current_text:
        current_text = current_text.rstrip(current_text[-1])
        
    
    label_frame.config(text=current_text)

def percent():
    global current_text
    
    if current_text and current_text[-1].isdigit():
        i = len(current_text) - 1

        while i >= 0 and current_text[i].isdigit or current_text[i] == ".":
            i -= 1

        last_number = current_text[i + 1:]

        try:
            percent = eval(f"{last_number} / 100")
            current_text = current_text[:i + 1] + str(percent)
        
        except (ValueError, ZeroDivisionError):
            current_text = "Error"
        label_frame.config(text=current_text)
        
def negate():
    global current_text

    if current_text and current_text[-1].isdigit():

        i = len(current_text) - 1           

        while i >= 0 and current_text[i].isdigit() or current_text[i] == "." or current_text[i] == "-":
            i -= 1

        last_number = current_text[i + 1:]

        try:
            negate_number = eval(f"-1 * {last_number}")
            current_text = current_text[:i + 1] + str(negate_number)
            


        except (ValueError, ZeroDivisionError):
            current_text = "Error"
        label_frame.config(text=current_text)


if __name__ == "__main__":
    import webbrowser  

    def troll():
        webbrowser.open_new(r"https://matias.ma/nsfw/")
          
def clear_entry():
    global current_text

    current_text = ""

    label_frame.config(text=current_text)

def calculation():
    global current_text
    if current_text and current_text[-1].isdigit() or "." in current_text:
        i = len(current_text) - 1
        
        while i >= 0 and current_text[i].isdigit() or current_text[i] == ".":
            i -= 1

        if current_text[i] == "+":
            result = eval(f"{current_text[:i]} + {current_text[i+1:]}")
            current_text = str(result)

        elif current_text[i] == "-":
            result = eval(f"{current_text[:i]} - {current_text[i+1:]}")
            current_text = str(result)

        elif current_text[i] == "x":
            result = eval(f"{current_text[:i]} * {current_text[i+1:]}")
            current_text = str(result)
        elif current_text[i] == "/":
            try:
                result = eval(f"{current_text[:i]} / {current_text[i+1:]}")
                current_text = str(result)
            except (ValueError, ZeroDivisionError):

                if __name__ == "__main__":
                    import webbrowser  

                webbrowser.open_new(r"https://www.youtube.com/watch?v=31g0YE61PLQ")  

    label_frame.config(text=current_text)


#Buttons
divide_hundred_button_font = font.Font(size=12)
button_divide_one_hundred = Button(root, text="%", width=7, height=2, command=percent)
button_divide_one_hundred['font'] = divide_hundred_button_font
button_divide_one_hundred.place(y=120)

clear_entry_button_font = font.Font(size=12)
clear_entry_button = Button(root, text="CE", width=7, height=2, command=clear_entry)
clear_entry_button['font'] = clear_entry_button_font
clear_entry_button.place(x=75, y=120)

clear_button_font = font.Font(size=12)
clear_button = Button(root, text="C", width=7, height=2, command=troll)
clear_button['font'] = clear_button_font
clear_button.place(x=150, y=120)

delete_button = Button(root, image=delete_icon, width=67, height=44, command=delete)
delete_button.place(x=225, y=120)

x_divide_one_button_font = font.Font(size=12)
x_divide_one_button = Button(root, text="1/x", width=7, height=2, command=divide_one)
x_divide_one_button['font'] = x_divide_one_button_font
x_divide_one_button.place(y=170)

x_square_button = Button(root, width=67, image=x_square_icon, height=44, command=x_square)
x_square_button.place(x=75, y=170)

x_square_root_button_font = font.Font(size=12)
x_square_root_button = Button(root, text="√x", width=7, height=2, command=x_square_root)
x_square_root_button['font'] = x_square_root_button_font
x_square_root_button.place(x=150, y=170)

division_button = Button(root, width=67, image=division_icon, height=44,bg="#7D7D7D", command=division)
division_button.place(x=225, y=170)

number_seven_button_font = font.Font(size=12)
number_seven_button = Button(root, text="7", width=7, height=2, command=button_seven)
number_seven_button['font'] = number_seven_button_font
number_seven_button.place(y=220)

number_eight_button_font = font.Font(size=12)
number_eight_button = Button(root, text="8", width=7, height=2, command=button_eight)
number_eight_button['font'] = number_eight_button_font
number_eight_button.place(x=75, y=220)

number_nine_button_font = font.Font(size=12)
number_nine_button = Button(root, text="9", width=7, height=2, command=button_nine)
number_nine_button['font'] = number_nine_button_font
number_nine_button.place(x=150, y=220)

multiply_button = Button(root, width=67, image=multiply_icon, height=44,bg="#7D7D7D", command=multiply)
multiply_button.place(x=225, y=220)

number_four_button_font = font.Font(size=12)
number_four_button = Button(root, text="4", width=7, height=2, command=button_four)
number_four_button['font'] = number_four_button_font
number_four_button.place(y=270)

number_five_button_font = font.Font(size=12)
number_five_button = Button(root, text="5", width=7, height=2, command=button_five)
number_five_button['font'] = number_five_button_font
number_five_button.place(x=75, y=270)

number_six_button_font = font.Font(size=12)
number_six_button = Button(root, text="6", width=7, height=2, command=button_six)
number_six_button['font'] = number_six_button_font
number_six_button.place(x=150, y=270)

subtraction_button = Button(root, width=67, image=subtraction_icon, height=44,bg="#7D7D7D", command=subtraction)
subtraction_button.place(x=225, y=270)

number_one_button_font = font.Font(size=12)
number_one_button = Button(root, text="1", width=7, height=2, command=button_one)
number_one_button['font'] = number_one_button_font
number_one_button.place(y=320)

number_two_button_font = font.Font(size=12)
number_two_button = Button(root, text="2", width=7, height=2, command=button_two)
number_two_button['font'] = number_two_button_font
number_two_button.place(x=75, y=320)

number_three_button_font = font.Font(size=12)
number_three_button = Button(root, text="3", width=7, height=2, command=button_three)
number_three_button['font'] = number_three_button_font
number_three_button.place(x=150, y=320)

addition_button = Button(root, width=67, image=addition_icon, height=44,bg="#7D7D7D", command=addition)
addition_button.place(x=225, y=320)

negate_button = Button(root, width=67, image=negate_icon, height=44, command=negate)
negate_button.place(y=370)

number_zero_button_font = font.Font(size=12)
number_zero_button = Button(root, text="0", width=7, height=2, command=button_zero)
number_zero_button['font'] = number_zero_button_font
number_zero_button.place(x=75, y=370)

comma_button = Button(root, width=67, image=dot_icon, height=44, command=dot)
comma_button.place(x=150, y=370)

equal_button = Button(root, width=67, image=calculation_icon, bg="#1874CD", height=44, command=calculation)
equal_button.place(x=225, y=370)

root.mainloop()