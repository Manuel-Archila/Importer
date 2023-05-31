from py2neo import Graph, Node
import csv

# Establecer la conexión con el servidor de Neo4j
graph = Graph("neo4j+s://ea07d90c.databases.neo4j.io", auth=("neo4j", "vZFuK5tph9xgxeyowin-mDP7elsYq4ZNNnPfhjhYmBY"))

# Ruta al archivo CSV
csv_file = "Productos.csv"

# Crear nodos y relaciones a partir del archivo CSV
with open(csv_file, "r", newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Obtener las presentaciones como una lista
        presentaciones = row["presentaciones"].split(".")

        # Crear un nodo con los datos de la fila actual
        node = Node("Producto",
                    descripcion=row["descripcion"],
                    precio_unitario=int(row["precio_unitario"]),
                    id_inventario=row["id_inventario"],
                    presentaciones=presentaciones,
                    nombre=row["nombre"])
        graph.create(node)


# Ruta al archivo CSV
csv_file = "Servicios.csv"

# Crear nodos a partir del archivo CSV
with open(csv_file, "r", newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Crear un nodo con el nombre de la fila actual
        node = Node("Servicio", nombre=row["nombre"])
        graph.create(node)



# Ruta al archivo CSV
csv_file = "Personas.csv"

# Crear nodos a partir del archivo CSV
with open(csv_file, "r", newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Crear un nodo con los datos de la fila actual
        node = Node("Persona",
                    apellido=row["apellido"],
                    nit=row["nit"],
                    sexo=row["sexo"],
                    edad=int(row["edad"]),
                    nombre=row["nombre"])
        graph.create(node)
