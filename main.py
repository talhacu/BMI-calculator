from tkinter import *

#window
window = Tk()
window.minsize(300,300)
window.configure(background="white", pady=45)
window.title("BMI Calculator")
#weight
weight_label= Label(text="Enter your weight in kg", bg="white", foreground="black")
weight_label.pack(pady=5)
weight_entry = Entry(width=4)
weight_entry.pack(pady=5)
#height
height_label= Label(text="Enter your height in cm", bg="white", foreground="black")
height_label.pack(pady=5)
height_entry = Entry(width=4)
height_entry.pack(pady=5)


def calculateBMI():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100
    bmi = weight / (height**2)
    bmi_category = commentBMI(bmi)
    result_label.config(text=f"Your BMI is {bmi: .2f}\n Kilonuz {bmi_category}")
def commentBMI(bmi):
    if bmi < 18.5:
        return "normalin altında."
    elif 18.5 <= bmi < 24.9:
        return "gayet normal."
    elif 24.9 <= bmi < 29.9:
        return "normalin üstünde."
    else:
        return "çok fazlai obezsiniz."

calculate_button = Button(text="Calculate BMI", command=calculateBMI, background="white", foreground="black")
calculate_button.pack(pady=10)

result_label= Label(text="", bg="white", foreground="black")
result_label.pack(pady=10)









window.mainloop()