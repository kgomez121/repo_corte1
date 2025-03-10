piezas= int(input("ingrese el numero de piezas que va a comprar:"))
precio_piezas= int(input("ingrese el precio de las piezas:"))
monto_total= precio_piezas * piezas
if monto_total> 500000:
    dinero_empresa = (monto_total * 0.55)
    banco = (monto_total * 0.30)
    credito_fabricante = (monto_total* 0.15)
    reditos= credito_fabricante+(credito_fabricante * 0.20)
    print("numero de piezas a comprar",piezas)
    print("precio de las piezas",precio_piezas)
    print(f"el monto total de la compra fue de {monto_total}")
    print(f"la inversion de la empresa fue de {dinero_empresa}")
    print(f"el prestamo al banco fue de {banco}")
    print(f"el credito del fabricante fue de {reditos} sumando el 20% de los intereses")
else:
    dinero_empresa = (monto_total * 0.70)
    credito_fabricante = (monto_total * 0.30)
    reditos= credito_fabricante + (credito_fabricante * 0.20)
    print("numero de piezas a comprar",piezas)
    print("precio de las piezas",precio_piezas)
    print(f"el monto total de la compra fue de {monto_total}")
    print(f"la inversion de la empresa fue de {dinero_empresa}")
    print(f"el credito del fabricante fue de {reditos} sumando los intereses")

#creador del codigo KEVIN GOMEZ MUGNO
