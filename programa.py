import json

# Ruta para los JSON
ruta_estudiantes = "estudiantes.json"
ruta_materias = "materias.json"
ruta_notas = "notas.json"

# Funciones para leer y escribir en los JSON
def leer_archivo_json(ruta):
    try:
        with open(ruta, "r") as archivo:
            datos_json = json.load(archivo)
        return datos_json
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def escribir_archivo_json(ruta, datos_json):
    with open(ruta, "w") as archivo:
        json.dump(datos_json, archivo, indent=4)

# Para mostrar el menú del principal
def mostrar_menu():
    print("\nMenú de principal:")
    print("1. Gestion de estudiantes")
    print("2. Gestion de materias")
    print("3. Gestion de notas")
    print("4. Salir")

    opcion = input("Ingrese la opción deseada: ")
    return opcion

# Función para gestionar estudiantes
def gestionar_estudiantes():
    while True:
        opcion_estudiante = input("\nOpciones de estudiantes:\n1. Agregar un estudiante a la lista\n2. Ver la lista de estudiantes\n3. Eliminar los datos de un estudiante de la lista\n4. Volver al menú principal\nIngrese la opción deseada: ")

        if opcion_estudiante == "1":
            # Podemos agregar un nuevo estudiante a la lista
            nuevo_estudiante = {
                "dni": input("Ingrese el DNI: "),
                "nombre": input("Ingrese el nombre: "),
                "apellido": input("Ingrese el apellido: "),
            }
            estudiantes_json = leer_archivo_json(ruta_estudiantes)
            estudiantes_json.append(nuevo_estudiante)
            escribir_archivo_json(ruta_estudiantes, estudiantes_json)
            print("Estudiante agregado correctamente.")
        elif opcion_estudiante == "2":
            # Ver lista de los estudiantes registrados
            estudiantes_json = leer_archivo_json(ruta_estudiantes)
            if estudiantes_json:
                print("\nLista de estudiantes registrados:")
                for estudiante in estudiantes_json:
                    print(f"- {estudiante['dni']}: {estudiante['nombre']} {estudiante['apellido']}")
            else:
                print("No hay estudiantes registrados.")
        elif opcion_estudiante == "3":

            # Eliminar los datos de un estudiante de la lista
            dni_estudiante = input("Ingrese el DNI del estudiante a eliminar: ")

            estudiantes_json = leer_archivo_json(ruta_estudiantes)
            estudiantes_actualizados = [estudiante for estudiante in estudiantes_json if estudiante["dni"] != dni_estudiante]

            if estudiantes_actualizados != estudiantes_json:
                escribir_archivo_json(ruta_estudiantes, estudiantes_actualizados)
                print(f"Estudiante con DNI {dni_estudiante} eliminado correctamente.")
            else:
                print(f"El estudiante con DNI {dni_estudiante} no está registrado.")
        elif opcion_estudiante == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Función para gestionar materias
def gestionar_materias():
    while True:
        opcion_materia = input("\nOpciones de materias:\n1. Agregar materia\n2. Ver lista de materias\n3. Volver al menú principal\nIngrese la opción deseada: ")

        if opcion_materia == "1":
            # Agregar nueva materia
            nueva_materia = {
                "codigo": input("Ingrese el código de la materia: "),
                "materia": input("Ingrese el nombre de la materia: "),
                "uc": input("Ingrese las unidades de crédito de la materia: "),
            }
            materias_json = leer_archivo_json(ruta_materias)
            materias_json.append(nueva_materia)
            escribir_archivo_json(ruta_materias, materias_json)
            print("Materia agregada correctamente.")
        elif opcion_materia == "2":
            # Ver lista de materias
            materias_json = leer_archivo_json(ruta_materias)
            if materias_json:
                print("\nLista de materias:")
                for materia in materias_json:
                    print(f"- {materia['codigo']}: {materia['materia']} ({materia['uc']} UC)")
            else:
                print("No hay materias registradas.")
        elif opcion_materia == "3":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Gention de notas
def gestionar_notas():
    while True:
        opcion_nota = input("\nOpciones de notas:\n1. Agregar nota\n2. Ver notas de un estudiante\n3. Modificar nota\n4. Promediar nota\n5. Volver al menú principal\nIngrese la opción deseada: ")

        if opcion_nota == "1":
            # Agregar nueva nota
            dni_estudiante = input("Ingrese el DNI del estudiante: ")
            codigo_materia = input("Ingrese el código de la materia: ")
            nota = float(input("Ingrese la nota (entre 0 y 10): "))
            periodo = input("Ingrese el periodo evaluado (formato 1-2024, 2-2023, etc.): ")

            nueva_nota = {
                "dni": dni_estudiante,
                "codigo": codigo_materia,
                "nota": nota,
                "periodo": periodo,
            }

            notas_json = leer_archivo_json(ruta_notas)
            notas_json.append(nueva_nota)
            escribir_archivo_json(ruta_notas, notas_json)
            print("Nota agregada correctamente.")

        elif opcion_nota == "2":
            # Ver notas de un estudiante
            dni_estudiante = input("Ingrese el DNI del estudiante: ")

            notas_estudiante = []
            for nota in leer_archivo_json(ruta_notas):
                if nota["dni"] == dni_estudiante:
                    notas_estudiante.append(nota)

            if notas_estudiante:
                print("\nNotas del estudiante:")
                for nota in notas_estudiante:
                    print(f"- {nota['codigo']}: {nota['nota']} ({nota['periodo']})")
            else:
                print(f"El estudiante con DNI {dni_estudiante} no tiene notas registradas.")

        elif opcion_nota == "3":
            # Modificar nota
            dni_estudiante = input("Ingrese el DNI del estudiante: ")
            codigo_materia = input("Ingrese el código de la materia: ")
            periodo = input("Ingrese el periodo evaluado (formato 1-2024, 2-2023, etc.): ")

            notas_json = leer_archivo_json(ruta_notas)

            nota_encontrada = False
            for i, nota in enumerate(notas_json):
                if nota["dni"] == dni_estudiante and nota["codigo"] == codigo_materia and nota["periodo"] == periodo:
                    nota_encontrada = True
                    nueva_nota = float(input("Ingrese la nueva nota (entre 0 y 20): "))
                    notas_json[i]["nota"] = nueva_nota
                    break

            if nota_encontrada:
                escribir_archivo_json(ruta_notas, notas_json)
                print("Nota modificada correctamente.")
            else:
                print(f"No se encontró la nota para el estudiante con DNI {dni_estudiante}, materia {codigo_materia} y periodo {periodo}.")

 
        elif opcion_nota == "4":
       #Promediar notas
            dni_estudiante = input("Ingrese el DNI del estudiante: ")
            periodo = input("Ingrese el periodo evaluado (formato 1-2024, 2-2023, etc.): ")

            notas_json = leer_archivo_json(ruta_notas)
            materias_json = leer_archivo_json(ruta_materias)
                
            nota_encontrada = False
            for i, nota in enumerate(notas_json):
                if nota["dni"] == dni_estudiante and nota["periodo"] == periodo:
                    nota_encontrada = True
                    nuevo_promedio = float(input("Ingrese la nueva nota (entre 0 y 10): "))
                    notas_json[i]["nota"] = nuevo_promedio
                    break

            for estudiante in sorted(set([nota["dni"] for nota in           opcion_nota])):
                promediar_nota = [nota["nota"] for nota in opcion_nota if nota["dni"] == estudiante]
                promedio = sum(promediar_nota) / len(promediar_nota)
            print(f"\nEstudiante: {estudiante} - Promedio: {promedio:.2f}")

    
            notas_json = leer_archivo_json(ruta_notas)
            notas_json.append(promediar_nota)
            escribir_archivo_json(ruta_notas, notas_json)
            print("Promedio agregado correctamente.")

        else:
            print("No hay notas registradas.")

# Función principal del programa
def main():
    while True:
        opcion_menu = mostrar_menu()

        if opcion_menu == "1":
            gestionar_estudiantes()
        elif opcion_menu == "2":
            gestionar_materias()
        elif opcion_menu == "3":
            gestionar_notas()
        #elif opcion_menu == "4":
            #promediar_notas()
        elif opcion_menu == "5":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
