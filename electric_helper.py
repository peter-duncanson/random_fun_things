import tkinter as tk
from tkinter import ttk


color_values = {
    'b': '0', 'br': '1', 'r': '2', 'o': '3', 'y': '4', 'g': '5', 'bl': '6'
}

color_multiplier = {
    'b': 1, 'br': 10, 'r': 100, 'o': 1000, 'y': 10000, 'g': 100000, 'bl': 1000000
}

tolerance = {
    'br': '+-1%', 'r': '+-2%', 'g': '+-5%', 's': '+-10'
}

def format_output():
    pass

class calculator(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent, padding="10")
        self.pack(expand=True, fill="both")
        
        self.input_var = tk.StringVar()
        self.result_var = tk.StringVar()
        
        self.create_widgets()
        self.calculate()

    def create_widgets(self):
        ttk.Label(self, text='''how to use this:
enter prefix r for resistor
enter prefix c for capacitor
value colors:
b = black
br = brown
r = red
o = orange
y = yellow
g = green
bl = blue
tolerances:
br = brown
r = red
g = gold
s = silver''').pack()
        
        entry = ttk.Entry(self, textvariable=self.input_var, font=("Helvetica", 12))
        entry.pack(padx=5, pady=5, fill="x")

        result_label = ttk.Label(self, textvariable=self.result_var, font=("Helvetica", 14, "bold"))
        result_label.pack(pady=10)

        self.input_var.trace_add("write", self.calculate)

    def calculate(self, *inputs):

        user_input = self.input_var.get().split()

        try:

            if user_input[0].lower() == 'c':

                d1 = user_input[1]
                d2 = user_input[2]
                mult_digit = int(user_input[3])
                c_value = int(d1 + d2) * (10 ** (-12 + mult_digit))
                self.result_var.set(c_value)

            
            elif user_input[0].lower() == 'r':

                if len(user_input) == 4:
                    d1 = color_values[user_input[1]]
                    d2 = color_values[user_input[2]]
                    mult = color_multiplier[user_input[3]]
                    resistance = (int(d1 + d2)) * mult
                    tol = ''

                
                elif len(user_input) == 5:
                    d1 = color_values[user_input[1]]
                    d2 = color_values[user_input[2]]
                    mult = color_multiplier[user_input[3]]
                    tol = tolerance[user_input[4]]
                    resistance = (int(d1 + d2)) * int(mult)
        

                elif len(user_input) == 6:
                    d1 = color_values[user_input[1]]
                    d2 = color_values[user_input[2]]
                    d3 = color_values[user_input[3]]
                    mult = color_multiplier[user_input[4]]
                    tol = tolerance[user_input[5]]
                    resistance = (int(d1 + d2 + d3)) * int(mult)

                self.result_var.set('{} {}'.format(resistance, tol))


        except (UnboundLocalError, IndexError, KeyError, TypeError):
            self.result_var.set('invalid input')

class App(tk.Tk):

    def __init__(self):

        super().__init__()
        self.title("booga")
        self.geometry("450x350")
        self.calculator = calculator(self)

if __name__ == "__main__":
    app = App()
    App.mainloop(app)