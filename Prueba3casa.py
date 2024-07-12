import csv

estudiantes = []

def verificadorRut(rut, num_verificador):
    vuelta_rut = rut[::-1]
    multi=2
    rut_sumado = 0
    for num in vuelta_rut:
        rut_sumado += int(num) * multi
        multi+=1
        if multi > 7:
            multi=2
    rut_div=rut_sumado % 11
    verificador = 11 - rut_div
    if verificador == 10:
        verificador = "k"
    elif verificador == 11:
        verificador = 0   
    return str(verificador)==str(num_verificador)

def crear_estudiante():
    rut_ingresado = input("Ingrese el rut del estudiante (12345678-1): ")
    if "-" not in rut_ingresado:
        print("El rut ingresado no es válido")
        return
    rut, num_verificador = rut_ingresado.split("-")
    
    if not verificadorRut(rut, num_verificador):
        print("Rut ingresado incorrecto. Por favor ingrese de nuevo")
        return
    
    nombre = input("Ingrese el nombre del estudiante: ")
    if not nombre.isalpha():
        print("El nombre ingresado solo debe contener letras")
        return

    try:
        n1 = float(input("Ingrese la primera nota: "))
        n2 = float(input("Ingrese la segunda nota: "))
        n3 = float(input("Ingrese la tercera nota: "))
        n4 = float(input("Ingrese la cuarta nota: "))
    except ValueError:
        print("Para las notas solamente colocar valores numéricos")
        return

    nota_presentacion = (n1 + n2 + n3) * 0.3 + n4 * 0.1
    promedio = (n1 + n2 + n3 + n4) / 4
    
    estado = "Aprobado" if promedio >= 4.0 else "Reprobado"
            
    estudiante = {
        "rut": rut,
        "nombre": nombre,
        "1Nota": n1,
        "2Nota": n2,
        "3Nota": n3,
        "4Nota": n4,
        "presentacion": nota_presentacion,
        "promedio": promedio,
        "estado": estado
    }
    estudiantes.append(estudiante)
    print("El estudiante ha sido creado exitosamente")

    
def ListaEstudiantes(lista_estudiantes):
    if len(lista_estudiantes) > 0:
        Campos = ("N°", "RUT", "Nombre", "Nota N°1", "Nota N°2", "Nota N°3", "Nota N°4", "Nota Presentación", "Promedio", "Estado")
        print(f"\n{Campos[0].center(5)}{Campos[1].center(15)}{Campos[2].center(16)}{Campos[3].center(13)}{Campos[4].center(15)}{Campos[5].center(15)}{Campos[6].center(15)}{Campos[7].center(20)}{Campos[8].center(15)}{Campos[9].center(10)}")
        k = 1
        for estudiante in lista_estudiantes:
            print(f"{str(k).center(5)}{estudiante['rut'].center(15)}{estudiante['nombre'].center(16)}{str(estudiante['1Nota']).center(13)}{str(estudiante['2Nota']).center(15)}{str(estudiante['3Nota']).center(15)}{str(estudiante['4Nota']).center(15)}{str(estudiante['presentacion']).center(20)}{str(estudiante['promedio']).center(15)}{estudiante['estado'].center(10)}")
            k += 1
    else:
        print("No se han registrado estudiantes.")

def buscar_estudiante_por_rut(rut_buscar):
    encontrado = False
    for estudiante in estudiantes:
        if estudiante['rut'] == rut_buscar:
            encontrado = True
            estado = "Aprobado" if estudiante['promedio'] >= 4.0 else "Reprobado"
            print("\nInformación del Estudiante:")
            print(f"{'RUT'.center(15)}{'Nombre'.center(16)}{'Nota N1'.center(13)}{'Nota N2'.center(15)}{'Nota N3'.center(15)}{'Nota N4'.center(15)}{'Promedio'.center(15)}{'Estado'.center(15)}")
            print(f"{estudiante['rut'].center(15)}{estudiante['nombre'].center(16)}{str(estudiante['1Nota']).center(13)}{str(estudiante['2Nota']).center(15)}{str(estudiante['3Nota']).center(15)}{str(estudiante['4Nota']).center(15)}{str(estudiante['promedio']).center(15)}{estado.center(15)}")
            break

    if not encontrado:
        print("No se encontró ningún estudiante con el RUT especificado.")

def exportar_csv(nombre_archivo, lista_alumnos):
    with open(nombre_archivo, "w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(["RUT", "Nombre", "Nota N1", "Nota N2", "Nota N3", "Nota N4", "Nota Presentacion", "Promedio", "Estado"])
        
        for alumno in lista_alumnos:
            rut = alumno['rut']
            nombre = alumno['nombre']
            nota1 = alumno['1Nota']
            nota2 = alumno['2Nota']
            nota3 = alumno['3Nota']
            nota4 = alumno['4Nota']
            nota_presentacion = alumno['presentacion']
            promedio = alumno['promedio']
            estado = alumno['estado']
            
            escritor_csv.writerow([rut, nombre, nota1, nota2, nota3, nota4, nota_presentacion, promedio, estado])
    
    print(f"Se ha exportado correctamente la lista de alumnos en '{nombre_archivo}'.")

while True:
    print ("calcular notas de estudiantes")
    print ("1. Registrao de estudiantes")
    print ("2. Visualización de todos los estudiantes")
    print ("3. buscar estudiante por rut")
    print ("4. exportar archivo a CSV")
    print ("5. salir")
 
 
    opcion = input("ingrese una opcion: ")
 
 
    if opcion == '1':
        crear_estudiante()  
    elif opcion == '2':
        ListaEstudiantes(estudiantes)
    elif opcion == '3':
        rut_buscar = input("Ingrese el RUT del estudiante a buscar: ")
        buscar_estudiante_por_rut(rut_buscar)
    elif opcion == '4':
        print("Elija una opción:")
        print("1. Todos los estudiantes")
        print("2. Estudiantes aprobados")
        print("3. Estudiantes reprobados")
        segunda_opcion = input("Ingrese una opción: ")
        
        if segunda_opcion == "1":
            nombre_archivo = input("Ingrese el nombre del archivo CSV para exportar: ")
            exportar_csv(nombre_archivo, estudiantes)
        elif segunda_opcion == "2":
            aprobados = [alumno for alumno in estudiantes if alumno["promedio"] >= 4.0]
            nombre_archivo = input("Ingrese el nombre del archivo CSV para exportar: ")
            exportar_csv(nombre_archivo, aprobados)
        elif segunda_opcion == "3":
            reprobados = [alumno for alumno in estudiantes if alumno["promedio"] < 4.0]
            nombre_archivo = input("Ingrese el nombre del archivo CSV para exportar: ")
            exportar_csv(nombre_archivo, reprobados)
        else:
            print("Opción no válida. Intente de nuevo.")
    elif opcion == '5':
        break
    else:
        print ("Opcion no valida intente de nuevo")
