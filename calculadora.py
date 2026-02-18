from os import system
from tkinter import Tk, Button, Entry, StringVar
from tkinter.ttk import Frame


class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        
        # Variables para guardar los numeros y la operacion
        self.valor1 = 0
        self.valor2 = 0
        self.operacion = ""
        self.display_var = StringVar()
        
        # Display
        self.display = Entry(ventana, textvariable=self.display_var, font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Botones numericos y operaciones
        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0),
        ]
        
        for texto, fila, columna in botones:
            btn = Button(ventana, text=texto, font=("Arial", 20), command=lambda t=texto: self.btn_click(t))
            btn.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")
    
    def btn_click(self, texto):
        if texto == "C":
            self.limpiar()
        elif texto == "=":
            self.igual()
        elif texto in "+-*/":
            self.operacion_click(texto)
        else:
            self.display_var.set(self.display_var.get() + texto)
    
    def operacion_click(self, op):
        try:
            self.valor1 = float(self.display_var.get())
            self.operacion = op
            self.display_var.set("")
        except ValueError:
            self.display_var.set("Error")
    
    def igual(self):
        try:
            self.valor2 = float(self.display_var.get())
            resultado = 0
            
            if self.operacion == "+":
                resultado = self.valor1 + self.valor2
            elif self.operacion == "-":
                resultado = self.valor1 - self.valor2
            elif self.operacion == "*":
                resultado = self.valor1 * self.valor2
            elif self.operacion == "/":
                if self.valor2 != 0:
                    resultado = self.valor1 / self.valor2
                else:
                    self.display_var.set("Error: División por cero")
                    return
            
            self.display_var.set(str(resultado))
        except ValueError:
            self.display_var.set("Error")
    
    def limpiar(self):
        self.valor1 = 0
        self.valor2 = 0
        self.operacion = ""
        self.display_var.set("")


if __name__ == "__main__":
    ventana = Tk()
    calc = Calculadora(ventana)
    ventana.mainloop()