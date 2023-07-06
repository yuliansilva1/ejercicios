import os


lista_ruts = []
lista_nombres = []
lista_direcciones = []
lista_comunas = []
lista_correos = []
lista_edades = []
lista_generos = []
lista_celulares = []
lista_tipos = []
lista_suscripcion = []

#menu
def ver_menu():
    os.system('cls')
    print("""Juan Maestro App
        1. Registrar Cliente
        2. Suscripcion
        3. Consultar Datos Cliente
        4. Eliminar Cliente
        5. Salir""")
       
def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion in(1,2,3,4,5):
                return opcion
            else:
                print("Opcion invalida")
        except:
            print("Debe ingresar un numero entero")
   
def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("Nombre invalido debe tener almenos 3 caracteres")
                   
def validar_rut():
    while True:
            try:
                rut = int(input("Ingrese rut(sin puntos ni digito verificador): "))
                if rut >= 10000000 and rut <= 99999999:
                    return rut
                else:
                    print("Rut fuera de rango")
            except:
                print("Debe ingresar un numero entero")
            
def validar_direccion():
    while True:
        direccion = input("Ingrese direccion: ")
        return direccion
 
def validar_comuna():
    while True:
        comuna = input("Ingrese comuna: ")
        return comuna 
  
def validar_correo():
    while True:
        correo = input("Ingrese correo: ")
        if "@" in correo:
            return correo
        else:
            print("Correo invalido")

def validar_edad():
    while True:
        try:
            edad = int(input("Ingrese edad: "))
            if edad >= 0 and edad <=110:
                return edad
            else:
                print("error edad fuera de rango")
        except:
            print("erro debe ongresar un numero entero")

def validar_genero():
    while True:
        genero = input("Ingrese genero(F:femnino M:masculino O:otro): ")
        if genero.upper() in("F","M","O"):
            return genero
        else:
            print("genero invalido debe ser F,M,O")       

def validar_celular():
    while True:
        try:
            celular = int(input("Ingrese celular: "))
            if celular >= 00000000 and celular <= 99999999:
                return celular
            else:
                print("error numero de telefono incorecto")
        except:
            print("error debe ingresar un numero entero")    

def validar_tipo():
    while True:
        tipo = input("Ingrese tipo(premium,gold,silver): ")
        if tipo.upper() in("PREMIUM","GOLD","SILVER"):
            return tipo
        else:
            print("error opcion incorecta")
                  
def registrar_cliente():    
    print("\tREGISTRO DE DATOS CLIENTE\n")
    rut = validar_rut()
    nombre = validar_nombre()
    direccion = validar_direccion()
    comuna = validar_comuna()
    correo = validar_correo()
    edad = validar_edad()
    genero = validar_genero()
    celular = validar_celular()
    tipo = validar_tipo()
    
    lista_ruts.append(rut)
    lista_nombres.append(nombre)
    lista_direcciones.append(direccion)
    lista_comunas.append(comuna)
    lista_correos.append(correo)
    lista_edades.append(edad)
    lista_generos.append(genero)
    lista_celulares.append(celular)
    lista_tipos.append(tipo)
    lista_suscripcion.append("suscripcion")
    
    print("Cliente Registrado con exito")

def validar_fecha():
    while True:
            try:
                fecha = int(input("Ingrese fecha de suscripcion: "))
                return fecha
            except:
                print("error fecha invalida")
                
def suscripcion():
    rut = int(input("Ingrese rut: "))
    if rut in lista_ruts:
        for x in range(len(lista_ruts)):
            if rut == lista_ruts[x]:
                posicion_encontrada = x
            fecha = validar_fecha()
            lista_suscripcion[posicion_encontrada] = lista_suscripcion[posicion_encontrada] + " " + fecha
    else:
        print("Rut no encontrado")
        
def consultar_datos_cliente():
    rut = int(input("Ingrese rut: "))
    if rut in lista_ruts:
        for x in range(len(lista_ruts)):
            if rut == lista_ruts[x]:
                posicion_encontrada = x
            print(lista_nombres[posicion_encontrada])
            print(lista_direcciones[posicion_encontrada])
            print(lista_comunas[posicion_encontrada])
            print(lista_correos[posicion_encontrada])
            print(lista_edades[posicion_encontrada])
            print(lista_generos[posicion_encontrada])
            print(lista_celulares[posicion_encontrada])
            print(lista_tipos[posicion_encontrada])
            print(lista_suscripcion[posicion_encontrada])
        else:
            print("El rut del cliente no se encunetra registrado")
   
def eliminar_cliente():
    rut =int(input("Ingrese rut(sin puntos ni digito verificador): "))
    if rut in lista_ruts:
        for x in range(len(lista_ruts)):
            if rut == lista_ruts[x]:
                posicion = x
                return
            lista_ruts.pop(posicion)
            lista_nombres.pop(posicion)
            lista_direcciones.pop(posicion)
            lista_comunas.pop(posicion)
            lista_correos.pop(posicion)
            lista_edades.pop(posicion)
            lista_generos.pop(posicion)
            lista_celulares.pop(posicion)
            lista_tipos.pop(posicion)
            lista_suscripcion.pop(posicion)
            
            print("Cliente Eliminado con exito")
        else:
            print("el rut del cliente no se encunetra registrado")
            
def salir():
    print("gracias por suscribirse a la app de juan maestro")         