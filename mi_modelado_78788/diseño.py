def calcular_presupuesto(conceptos):
    """
    Recibe una lista de conceptos con (nombre, cantidad, precio_unitario)
    Devuelve una lista con subtotales y el total general.
    """
    resultados = []
    total_general = 0

    for nombre, cantidad, precio_unitario in conceptos:
        subtotal = cantidad * precio_unitario
        resultados.append((nombre, cantidad, precio_unitario, subtotal))
        total_general += subtotal

    return resultados, total_general