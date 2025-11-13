import tkinter as tk
from tkinter import ttk, messagebox
from analisis import obtener_datos
from diseno import calcular_presupuesto

def mostrar_presupuesto():
    conceptos = obtener_datos()
    resultados, total = calcular_presupuesto(conceptos)

    for fila in tabla.get_children():
        tabla.delete(fila)

    for nombre, cantidad, precio, subtotal in resultados:
        tabla.insert("", "end", values=(nombre, cantidad, f"${precio:,.2f}", f"${subtotal:,.2f}"))

    lbl_total.config(text=f"Total de Obra: ${total:,.2f}")

ventana = tk.Tk()
ventana.title("💰 Presupuesto de Obra - Ingeniería Civil")
ventana.geometry("750x400")
ventana.config(bg="#f5f5f5")

titulo = tk.Label(ventana, text="Presupuesto de Obra con Base en Precios Unitarios", font=("Arial", 14, "bold"), bg="#f5f5f5")
titulo.pack(pady=10)

tabla = ttk.Treeview(ventana, columns=("Concepto", "Cantidad", "Precio Unitario", "Subtotal"), show="headings")
tabla.heading("Concepto", text="Concepto")
tabla.heading("Cantidad", text="Cantidad")
tabla.heading("Precio Unitario", text="Precio Unitario")
tabla.heading("Subtotal", text="Subtotal")
tabla.column("Concepto", width=300)
tabla.pack(padx=10, pady=10, fill="x")

btn_calcular = tk.Button(ventana, text="Calcular Presupuesto", command=mostrar_presupuesto, bg="#0078D7", fg="white", font=("Arial", 10, "bold"))
btn_calcular.pack(pady=10)

lbl_total = tk.Label(ventana, text="Total de Obra: $0.00", font=("Arial", 12, "bold"), bg="#f5f5f5")
lbl_total.pack(pady=5)

ventana.mainloop()