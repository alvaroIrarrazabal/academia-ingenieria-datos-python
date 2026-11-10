from operaciones import calcular_venta

def main():
    precio = 15000
    cantidad = 4

    total_venta = calcular_venta(precio, cantidad)
    print(f"Total de la venta: {total_venta}")



if __name__ == "__main__":
    main()

