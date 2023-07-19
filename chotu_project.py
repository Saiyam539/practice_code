from tkinter import *
import random

window = Tk()
window.geometry('600x500')
window.title('Maths Practice')

def multiply():
    num1 = random.randrange(1,3000)
    num2 = random.randrange(1,3000)
    num3 = random.randrange(1,3000)
    num4 = random.randrange(1,3000)
    
    show_number.config(text=f'{num1} X {num2} X {num3} X {num4}')

def plus():
    num1 = random.randrange(1,3000)
    num2 = random.randrange(1,3000)
    num3 = random.randrange(1,3000)
    num4 = random.randrange(1,3000)
    
    show_number.config(text=f'{num1} + {num2} + {num3} + {num4}')

def minus():
    num1 = random.randrange(1,3000)
    num2 = random.randrange(1,3000)
    num3 = random.randrange(1,3000)
    num4 = random.randrange(1,3000)
    
    show_number.config(text=f'{num1} - {num2} - {num3} - {num4}')

def factorial():
    random_number = random.randrange(3,20)

    factorial = '' 

    while (random_number>0):
        factorial = factorial + f"{random_number} X "
        random_number= random_number -1
        
    show_number.config(text=factorial)

text_area = Message(window,text="MATH",font=("Arial", 37, "bold"),bg='cyan',fg='blue')
text_area.pack(fill=X)

show_number = Message(window,text=f'Click the button to start the game',font=("Arial", 40, "bold"),width=500,justify="center", anchor="center")
show_number.place(x=48,y=150)

# user = Entry(window,font=("Arial", 30, "bold"))
# user.pack(padx=100,pady=13)

show_result = Message(window,font=("Arial", 30, "bold"),width=500)
show_result.pack()

button_2 = Button(window,text='Factorial',font=("Arial", 30, "bold"),bg='cyan',fg='blue',command=lambda:factorial())
button_2.place(x=80,y=350)

button_1 = Button(window,text='Multiplication',font=("Arial", 30, "bold"),bg='cyan',fg='blue',command=lambda:multiply())
button_1.place(x=320,y=350)

button_3 = Button(window,text='Addition',font=("Arial", 30, "bold"),bg='cyan',fg='blue',command=lambda:plus())
button_3.place(x=84,y=400)

button_4 = Button(window,text='Subtraction',font=("Arial", 30, "bold"),bg='cyan',fg='blue',command=lambda:minus())
button_4.place(x=330,y=400)


# score_count = Message(window,font=("Arial", 30, "bold"),width=500)
# score_count.place(x=100,y=400)

window.mainloop()