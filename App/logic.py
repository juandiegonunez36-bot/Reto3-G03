import time
import csv
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st
from DataStructures.Map import map_linear_probing as lp
from DataStructures.Map import map_separate_chaining as msc
from DataStructures.Map import map_entry as me
from DataStructures.Tree import red_black_tree as rb
from DataStructures.Tree import rbt_node as rbtn

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog ={
        "key_order_id": lp.new_map(100000, 0.5),
        "key_order_date": rb.new_map(),
        "key_discount_percent": rb.new_map()
    }
    # Cada estructura creada tiene una diferente llave
    # Aqui pueden inicializar estructuras de datos secundarias si las necesitan
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    csv.field_size_limit(2147483647)
    
    start_time = get_time()
    
    counter = 0
    
    min_price = float("inf")
    max_price = float("-inf")

    min_order = None
    max_order = None

    first_5 = al.new_list()
    last_5 = al.new_list()
    
    with open(filename, encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Llaves que vamos a utilizar
            order_id = row["order_id"]
            order_date = row["order_date"]
            discount_percent = row["discount_percent"]
            
            record = {
                "order_id":row["order_id"],
                "order_date":row["order_date"],
                "brand":row["brand"],
                "model_name":row["model_name"],
                "category":row["category"],
                "gender":row["gender"],
                "size":int(row["size"]),
                "color":row["color"],
                "base_price_usd":float(row["base_price_usd"]),
                "discount_percent":int(row["discount_percent"]),
                "final_price_usd":float(row["final_price_usd"]),
                "units_sold":int(row["units_sold"]),
                "revenue_usd":float(row["revenue_usd"]),
                "payment_method":row["payment_method"],
                "sales_channel":row["sales_channel"],
                "country":row["country"],
                "customer_income_level":row["customer_income_level"],
                "customer_rating":float(row["customer_rating"])
            }
            
            #Alimentando cada estructura de datos indivisualmente
            catalog["key_order_id"] = lp.put(catalog["key_order_id"],
                                             order_id,
                                             record)
            catalog["key_order_date"] = rb.put(catalog["key_order_date"],
                                               order_date,
                                               catalog)
            catalog["key_discount_percent"] = rb.put(catalog["key_discount_percent"],
                                                 discount_percent,
                                                 record)
            
            # Se hace el calculo de todas las funciones de estadistica
            
            counter += 1
            
            item = {
                "order_id":row["order_id"],
                "order_date":row["order_date"],
                "brand":row["brand"],
                "model_name":row["model_name"],
                "category":row["category"],
                "final_price_usd":row["final_price_usd"],
                "units_sold":row["units_sold"],
                "revenue_usd":row["revenue_usd"],
                "country":row["country"],
                "sales_channel":row["sales_channel"]
            }
            
            if float(row["final_price_usd"]) < min_price:
                min_price = float(row["final_price_usd"])
                min_order = item
                
            if float(row["final_price_usd"]) > max_price:
                max_price = float(row["final_price_usd"])
                max_order = item
                
            if al.size(first_5) < 5:
                al.add_last(first_5, item)

            al.add_last(last_5, item)

            if al.size(last_5) > 5:
                al.remove_first(last_5)
                
    load_time = delta_time(start_time, get_time())
    
    return {
        "load_time": load_time,
        "total_orders": counter,
        "min_order": min_order,
        "max_order": max_order,
        "first_5": first_5,
        "last_5": last_5
    }

# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
