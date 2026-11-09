import sys
from App import logic
from pprint import pprint
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl


def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    return logic.new_logic()

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    # Aqui cambiamos el archivo que estamos usando
    return logic.load_data(control, "Data/Data/global_sports_footwear_sales-small.csv")


def print_load(control):
    """
        Función que carga los datos y muestra en consola
        el resultado de la carga (opción 0 del menú).

        Uso de IA para usar pprint
    """
    print("Cargando información de los archivos ....\n")
    data = load_data(control)
    print("Tiempo de carga =", round(data["load_time"], 3), "ms")
    print("Elementos cargados =", data["total_orders"])
    print("Orden de menor valor =")
    pprint(data["min_order"])
    print("Orden de mayor valor =")
    pprint(data["max_order"])
    print("Primeros 5 elementos")
    pprint(data["first_5"])
    print("Últimos 5 elementos =")
    pprint( data["last_5"])


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    marca = str(input("Ingresa la marca por la que quieres filtrar: "))
    
    low_pct = int(input("Ingresa el limite inferior del porcentaje por el que quieres filtrar: "))
    high_pct = int(input("ingresa el limite superior para los porcentajes que quieres filtrar"))
    
    result = logic.req_1(control, marca, low_pct, high_pct)
    
    print(f"Número de entradas que cumplen el filtro: {result["order_num"]}")
    print("")
    print(f"Costo total de las entradas filtradas: {result["final_cost"]}")
    print("Primeras y últimas 10 entradas: ")
    for i in range(al.size(result["result"])):
        curent = al.get_element(result["result"], i)
        filtrado = {"order_id":curent["order_id"],
                    "order_date":curent["order_date"],
                    "brand":curent["brand"],
                    "model_name":curent["model_name"],
                    "category":curent["category"],
                    "final_price_usd":float(curent["final_price_usd"]),
                    "units_sold":int(curent["units_sold"]),
                    "revenue_usd":float(curent["revenue_usd"]),
                    "country":curent["country"],
                    "sales_channel":curent["sales_channel"],
                    "discount":curent["discount_percent"]}
        al.change_info(result["result"], i, filtrado)
        
    pprint(result["result"])
    return


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            print_load(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 5:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
