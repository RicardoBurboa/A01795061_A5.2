"""Módulos para cargar archivos JSONs, para el sistema y grabar el tiempo."""
import json
import sys
import time


def load_json_file(filename):
    """Función que carga un archivo JSON."""
    try:
        with open(filename, 'r', encoding="UTF-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: Archivo '{filename}' no encontrado.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Formato JSON inválido en archivo '{filename}'.")
        return {}


def compute_total_cost(price_catalogue, sales_record):
    """Función que computa el costo total."""
    total_cost = 0
    sales = sales_record

    products = price_catalogue
    product_catalogue_unique = set(product["title"] for product in products)

    for sale in sales:
        product_title = sale["Product"]
        quantity = sale["Quantity"]

        if product_title in product_catalogue_unique:
            price = 0
            for product in products:
                if product["title"] == product_title:
                    price = product["price"]

            total_cost += price * quantity
        else:
            print(f"Error: Producto '{product_title}' no está en el catálogo.")
    return total_cost


def main():
    """Función que carga el programa principal."""
    if len(sys.argv) != 3:
        print("Necesitas 3 args de archivos (programa, catálogo, ventas).")
        sys.exit(1)

    price_catalogue_file = sys.argv[1]
    sales_record_file = sys.argv[2]

    start_time = time.time()

    price_catalogue = load_json_file(price_catalogue_file)
    sales_record = load_json_file(sales_record_file)

    total_cost = compute_total_cost(price_catalogue, sales_record)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Costo Total de Ventas: ${total_cost: .2f}")
    print(f"Tiempo de Ejecución: {execution_time: .2f} s")

    with open("SalesResults.txt", "w", encoding="UTF-8") as results_file:
        results_file.write(f"Costo Total de Ventas: ${total_cost: .2f}\n")
        results_file.write(f"Tiempo de Ejecución: {execution_time: .2f} s\n")


if __name__ == "__main__":
    main()
