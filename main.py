from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("295x250")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=10, padx=1, pady=1)
label = Label(pantalla, width = 40 , height = 2, bg = "black", fg = "white", borderwidth = 0)
num = [0,0]
op = ["+"]

def operador(p):
    global op
    op.append(p)

def operar():
    global op
    global num
    if op[-1] == "+":
        res = num[-1]+num[-2]
    elif op[-1] == "-":
        res = num[-2]-num[-1]
    elif op[-1]=="*":
        res=num[-2]*num[-1]
    elif op[-1]=="/" and num[-1]!=0:
        resultado=num[-2]/num[-1]   
    else:
        resultado=0
    label.config(text=str(resultado))





# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=***, padx=1, pady=***)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=***, column=***, padx=***, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=***, padx=***, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=***, column=***, padx=1, pady=***)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=***, column=1, padx=***, pady=***)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=***, padx=***, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=***, column=***, padx=1, pady=***)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=***, column=***, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=***, pady=***)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=***, columnspan=***, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=***, column=***, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=***, padx=***, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=***, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=***, column=***, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=***, column=***, padx=1, pady=***)

root.mainloop()