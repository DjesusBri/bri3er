import csv

estudiantes = []

def validarFormatoRut(rut:str) -> bool:
    rut = rut.zfill(12)
    if len(rut) != 12:
        return False
    rut = rut.split(",")
    validacion_orden = len(rut[0]) == 2 and len(rut[1]) == 3
    if len(rut) == 3 and validacion_orden:
        for i in "".join(rut)[:-2]:
            if not i.isnumeric():
                break
        else:
            if rut [-1][-2] == "-" and rut [-1][-1].isnumeric() or rut[-1][-1] == "k":
                return True

def crear_estudiante():
    rut = input("Ingrese el rut del estudiante (12.123.123-1): ")
    assert validarFormatoRut(rut), "el rut ingresado es un formato incorrecto"
    if rut in estudiantes:
        print("EL rut del estudiante ya se encuentra en uso")
    else:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre not in estudiantes:
            n1 = float(input("Ingrese la primera nota: "))
            n2 = float(input("Ingrese la segunda nota: "))
            n3 = float(input("Ingrese la tercera nota: "))
            n4 = float(input("Ingrese la cuarta nota: "))
            
        sum_notas = n1 + n2 + n3 + n4
        pro_final = sum_notas // 4
        
        estudiante = {
            "nombre": nombre,
            "rut": rut,
            "1Nota": n1,
            "2Nota": n2,
            "3Nota": n3,
            "4Nota": n4,
            "promedio": pro_final   
        }
        estudiantes.append(estudiante)
        print("El estudiante ha sido creado excitosamente")

def ver_estudiantes():
    print(f"rut: {rut}, Nombre: {nombre}, Primera nota: {n1}, segunda nota: {n2}, tercera nota: {n3}, cuarta nota: {n4}")
            
   



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
        ver_estudiantes()
    elif opcion == '3':
        print("")
    elif opcion == '4':
        print("")
    elif opcion == '5':
        break
    else:
        print ("Opcion no valida intente de nuevo")
        
        
        
        
        
        
