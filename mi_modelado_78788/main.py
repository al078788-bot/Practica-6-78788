from analisis import obtener_datos
from diseno import calcular_presupuesto

def main():
    conceptos = obtener_datos()
    resultados, total = calcular_presupuesto(conceptos)

    print("\nPRESUPUESTO DE OBRA\n")
    print(f"{'CONCEPTO':40} {'CANT.':>8} {'P.U.':>12} {'SUBTOTAL':>12}")
    print("-" * 75)
    for nombre, cantidad, precio, subtotal in resultados:
        print(f"{nombre:40} {cantidad:8.2f} {precio:12.2f} {subtotal:12.2f}")
    print("-" * 75)
    print(f"{'TOTAL GENERAL:':>60} {total:12.2f}")

if __name__ == "__main__":
    main()