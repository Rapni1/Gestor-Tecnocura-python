trabajos_taller = []
try:
    with open("base_tecnocura.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        
        for renglon in lineas:
            renglon_limpio = renglon.strip()
            if not renglon_limpio:
                continue    
            pedazos = renglon_limpio.split(",")
            if len(pedazos) >= 2:
                expediente_recuperado = {
                    "Cliente": pedazos[0].strip(), 
                    "Celular": pedazos[1].strip(),
                    "Precio": pedazos[2].strip()
                }
                trabajos_taller.append(expediente_recuperado)
                
    print(f"Proceso terminado. Se cargaron {len(trabajos_taller)} registros.")

except FileNotFoundError:
    print("El archivo 'base_tecnocura.txt' no existe en el sistema.")
def bienvenida_menu():
    print ("--- MENU DE OPCIONES ---")
    print("1. Registro de nuevo equipo.\n2. Ver equipos registrados.\n3. Entregar equipo (Eliminar).\n4. Buscar cliente.\n5. Editar orden (Equipo).\n6. Proyeccion de ganancias.\n7. Apagar sistema.")

def registrar_equipos():
    nombre = input("Ingrese su nombre: ")
    modelo = input("Ingrese el modelo de su celular: ")
    precio = int(input("Precio estimado: "))
    {
        "Precio": precio
    }
    with open ("base_tecnocura.txt", "a") as archivo:
        archivo.write(f"{nombre}, {modelo} , {precio}\n")
        nuevo_expediente = {
            "Cliente": nombre,
            "Celular": modelo,
            "Precio": precio
            }
        trabajos_taller.append(nuevo_expediente)
        print(f"Se registro el celular {modelo} a nombre del cliente {nombre} con importe a pagar de ${precio}")
    
def mostrar_equipos():
        if len(trabajos_taller) == 0:
            print("No hay equipos registrados.")
        else:
            print("--- EQUIPOS REGISTRADOS ---")
            for numero, orden in  enumerate(trabajos_taller, 1):
                print(f"{numero}. Nombre: {orden['Cliente']}.\nEquipo: {orden['Celular']}. Total a cobrar: ${orden['Precio']}")
                
def eliminar_equipos():
    if len(trabajos_taller) == 0:
                print("--- Lista vacia ---")
    else:
        numero_eliminar = int(input("Ingrese el numero de orden a eliminar: "))
        indice = numero_eliminar - 1
        try:
            equipo_eliminar = trabajos_taller.pop(indice)
            with open (f"Recibo_{equipo_eliminar['Cliente']}.txt", "w", encoding="utf-8") as recibo:
                recibo.write("--- TICKET DE ENTREGA TECNOCURA ---\n" f"Cliente: {equipo_eliminar['Cliente']}.\n" f"Equipo Reparado: {equipo_eliminar['Celular']}.\n" f"Total pagado: ${equipo_eliminar['Precio']}\n" "¡Gracias por su preferencia!\n")
            with open("base_tecnocura.txt","w", encoding="utf-8") as archivo:
                for orden in trabajos_taller:
                    archivo.write(f"{orden['Cliente']}, {orden['Celular']}, {orden['Precio']}\n")
                print(f"La orden a nombre de {equipo_eliminar['Cliente']} Con celular {equipo_eliminar['Celular']} se ha eliminado con exito del sistema.")
        except IndexError:
            print("ERROR!, Ese numero de orden no existe en la base de datos")

def buscar_equipos():
    nombre_buscar = input("¿Que cliente quieres buscar en el sistema?: ")
    coincidencias = 0
    for orden in trabajos_taller:
        if nombre_buscar.lower() in orden["Cliente"].lower():
            print(f"Encontrado -> Cliente: {orden['Cliente']} | Celular: {orden['Celular']} | Monto: ${orden['Precio']}")
            coincidencias = coincidencias + 1
    if coincidencias == 0:
        print("No se encontro ningun equipo o cliente con ese nombre en la base de datos.")

def editar_equipo():
    mostrar_equipos()
    try:
        numero = int(input("¿Que numero de orden quieres corregir?: "))
        indice = numero - 1
        nuevo_celular = input("Escribe el celular correcto: ")
        trabajos_taller[indice]["Celular"] = nuevo_celular
        with open("base_tecnocura.txt","w", encoding="utf-8") as archivo:
            for orden in trabajos_taller:
                archivo.write(f"{orden['Cliente']}, {orden['Celular']}, {orden['Precio']}\n")
                print("Expediente actualizado")
    except IndexError:
        print("Ese numero de orden no se encuentra en la base de datos")
    except ValueError:
        print("Error: Por favor, introduce un número válido (ej. 1, 2, 3).")
        
def proyectar_ganancias():
    total_dinero = 0
    for orden in trabajos_taller:
        total_dinero = total_dinero + int(orden["Precio"])
    print(f"El total proyectado en reparaciones pedientes es de: ${total_dinero}")
    
def apagado_sistema():
    print("Sistema apagado con exito.")

while True:
    try:
        bienvenida_menu()
        eleccion = int(input("Por favor escoja una opcio: "))
        if eleccion == 1:
            registrar_equipos()
        elif eleccion == 2:
            mostrar_equipos()
        elif eleccion == 3:
            eliminar_equipos()
        elif eleccion == 4:
            buscar_equipos()
        elif eleccion == 5:
            editar_equipo() 
        elif eleccion == 6:
            proyectar_ganancias()
        elif eleccion == 7:
            apagado_sistema()
            break
        else:
            print("Solo escoge opcion del 1 al 7")   
            
    except ValueError:
        print("Error! Opcion no valida, Favor de solo ingresar numeros.")