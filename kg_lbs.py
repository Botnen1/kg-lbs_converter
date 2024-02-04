import tkinter as tk

def calculate_kg_to_lbs():
    x = entry1.get()
    try:
        calculated = float(x) * 2.20462
        result_label1.config(text=f'{x} kg = {calculated:.3f} lbs', fg='white')
    except ValueError:
        result_label1.config(text="Invalid input. Please enter a number.", fg='red')

def calculate_lbs_to_kg():
    x = entry2.get()
    try:
        calculated = float(x) / 2.20462
        result_label2.config(text=f'{x} lbs = {calculated:.3f} kg', fg='white')
    except ValueError:
        result_label2.config(text="Invalid input. Please enter a number.", fg='red')

window = tk.Tk()
window.title("Weight Converter")
window.geometry('400x200')
window.resizable(False, False)
window.configure(bg='#319D88')

title_label = tk.Label(window, text='Kilograms // Pounds', font=('Helvetica', 16, 'bold'), bg='#319D88', fg='white')
title_label.pack(pady=10)

frame1 = tk.Frame(window, bg='#319D88')
frame1.pack(pady=10)

label_entry1 = tk.Label(frame1, text='Enter value in Kilograms:', bg='#319D88', fg='white')
label_entry1.grid(row=0, column=0, padx=5)

entry1 = tk.Entry(frame1, bg='#34495e', fg='white')
entry1.grid(row=0, column=1, padx=5)

button1 = tk.Button(frame1, text='Calculate', command=calculate_kg_to_lbs, bg='#3498db', fg='white')
button1.grid(row=0, column=2, padx=5)

result_label1 = tk.Label(frame1, text='', font=('Helvetica', 10), bg='#319D88', fg='white')
result_label1.grid(row=1, column=0, columnspan=3)

frame2 = tk.Frame(window, bg='#319D88')
frame2.pack(pady=10)

label_entry2 = tk.Label(frame2, text='Enter value in Pounds:', bg='#319D88', fg='white')
label_entry2.grid(row=0, column=0, padx=5)

entry2 = tk.Entry(frame2, bg='#34495e', fg='white')
entry2.grid(row=0, column=1, padx=5)

button2 = tk.Button(frame2, text='Calculate', command=calculate_lbs_to_kg, bg='#3498db', fg='white')
button2.grid(row=0, column=2, padx=5)

result_label2 = tk.Label(frame2, text='', font=('Helvetica', 10), bg='#319D88', fg='white')
result_label2.grid(row=1, column=0, columnspan=3)

window.mainloop()
