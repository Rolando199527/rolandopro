import json
import os

FILE_PATH = "budget_items.json"

def load_items():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return []

def save_items(items):
    with open(FILE_PATH, "w") as file:
        json.dump(items, file, indent=4)

def add_item():
    name = input("Nombre del artículo: ")
    cost = float(input("Costo del artículo: "))
    item = {"name": name, "cost": cost}
    items = load_items()
    items.append(item)
    save_items(items)
    print(f"Artículo '{name}' añadido con éxito.\n")

def search_item():
    name = input("Nombre del artículo a buscar: ")
    items = load_items()
    found = [item for item in items if item['name'].lower() == name.lower()]
    if found:
        print("Artículo(s) encontrado(s):")
        for item in found:
            print(f"Nombre: {item['name']}, Costo: ${item['cost']:.2f}")
    else:
        print("Artículo no encontrado.")

def edit_item():
    name = input("Nombre del artículo a editar: ")
    items = load_items()
    for item in items:
        if item['name'].lower() == name.lower():
            new_name = input(f"Nuevo nombre para '{name}' (dejar en blanco para mantener el mismo): ")
            new_cost = input(f"Nuevo costo para '{name}' (dejar en blanco para mantener el mismo): ")
            if new_name:
                item['name'] = new_name
            if new_cost:
                item['cost'] = float(new_cost)
            save_items(items)
            print(f"Artículo '{name}' actualizado con éxito.\n")
            return
    print("Artículo no encontrado.")

def delete_item():
    name = input("Nombre del artículo a eliminar: ")
    items = load_items()
    items = [item for item in items if item['name'].lower() != name.lower()]
    save_items(items)
    print(f"Artículo '{name}' eliminado con éxito.\n")

def main():
    while True:
        print("\nGestor de Presupuesto")
        print("1. Añadir artículo")
        print("2. Buscar artículo")
        print("3. Editar artículo")
        print("4. Eliminar artículo")
        print("5. Salir")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            add_item()
        elif choice == '2':
            search_item()
        elif choice == '3':
            edit_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            print("Saliendo del gestor de presupuesto.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
