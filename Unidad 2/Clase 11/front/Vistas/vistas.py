import tkinter
import tkinter.messagebox as messagebox
from Controladores.controladores import Controladores

class Vista:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("API Silla")
        self.root.geometry("350x450")
        self.root.resizable(0, 0)

        self.labelTitulo = tkinter.Label(self.root, text="Datos de la Silla")
        self.labelTitulo.grid(column=0, row=0, padx=15, pady=15, columnspan=2)

        self.labelMaterial = tkinter.Label(self.root, text="Material")
        self.labelMaterial.grid(column=0, row=1, padx=20, pady=20)
        self.txtMaterial = tkinter.Entry(self.root, width=30)
        self.txtMaterial.grid(column=1, row=1)

        self.labelOcultoMaterial = tkinter.Label(self.root, text="")
        self.labelOcultoMaterial.grid(column=0, row=2, columnspan=2)

        self.labelAltura = tkinter.Label(self.root, text="Altura (cms)")
        self.labelAltura.grid(column=0, row=3, padx=20, pady=20)
        self.txtAltura = tkinter.Entry(self.root, width=30)
        self.txtAltura.grid(column=1, row=3)

        self.labelOcultoAltura = tkinter.Label(self.root, text="")
        self.labelOcultoAltura.grid(column=0, row=4, columnspan=2)

        self.labelPeso = tkinter.Label(self.root, text="Peso (kg)")
        self.labelPeso.grid(column=0, row=5, padx=20, pady=20)
        self.txtPeso = tkinter.Entry(self.root, width=30)
        self.txtPeso.grid(column=1, row=5)

        self.labelPesoOculto = tkinter.Label(self.root, text="")
        self.labelPesoOculto.grid(column=0, row=6, columnspan=2)

        self.labelEstilo = tkinter.Label(self.root, text="Estilo")
        self.labelEstilo.grid(column=0, row=7, padx=20, pady=20)
        self.txtEstilo = tkinter.Entry(self.root, width=30)
        self.txtEstilo.grid(column=1, row=7)

        self.labelEstiloOculto = tkinter.Label(self.root, text="")
        self.labelEstiloOculto.grid(column=0, row=8, columnspan=2)

        self.controladores = Controladores(self)

        self.botonDiligenciar = tkinter.Button(self.root, text="Diligenciar", command=self.controladores.diligenciar)
        self.botonDiligenciar.grid(column=0, row=11, columnspan=2, padx=15, pady=15)

        self.txtMaterial.bind("<KeyRelease>", lambda event: self.controladores.validar_material(event, self.txtMaterial))
        self.txtAltura.bind("<KeyRelease>", lambda event: self.controladores.validar_altura(event, self.txtAltura))
        self.txtEstilo.bind("<KeyRelease>", lambda event: self.controladores.validar_estilo(event, self.txtEstilo))
        self.txtPeso.bind("<KeyRelease>", lambda event: self.controladores.validar_peso(event, self.txtPeso))

        self.root.protocol("WM_DELETE_WINDOW", self.controladores.el_usuario_quiere_salir)

        self.root.mainloop()