class Clase:
    def __init__(self, id, nombre, horario, salon, profesor):
        self.id = id
        self.nombre = nombre
        self.horario = horario
        self.salon = salon
        self.profesor = profesor
        self.alumnos = []

    def agregarAlumno(self, alumno):
        self.alumnos.append(alumno)

    def mostrarAlumnos(self):
        for alumno in self.alumnos:
            print(f"ID: {alumno.id}, Nombre: {alumno.nombre}, Fecha de nacimiento: {alumno.nacimiento}, Nota: {alumno.nota}")

    def cantidadAlumnos(self):
        return len(self.alumnos)

    def asignarNota(self, idAlumno, nota):
        for alumno in self.alumnos:
            if alumno.id == idAlumno:
                alumno.nota = nota
                print(f"Nota asignada correctamente al alumno {alumno.nombre}.")
                break
        else:
            print("El alumno no existe en esta clase")

    def mostrarEstudiantesConNotas(self):
        alumnos_ordenados = sorted(self.alumnos, key=lambda x: x.nota, reverse=True)
        for alumno in alumnos_ordenados:
            print(f"ID: {alumno.id}, Nombre: {alumno.nombre}, Nota: {alumno.nota}")

    def mostrarCursosConCantidadEstudiantes(self):
        clases_ordenadas = sorted(listaDeClases, key=lambda x: x.cantidadAlumnos(), reverse=True)
        for clase in clases_ordenadas:
            print(f"Curso: {clase.nombre}, Cantidad de estudiantes: {clase.cantidadAlumnos()}")

    def notaMedia(self):
        return sum([alumno.nota for alumno in self.alumnos]) / len(self.alumnos)

class Alumno:
    def __init__(self, id, nombre, fecha_nacimiento, nota=0):
        self.id = id
        self.nombre = nombre
        self.nacimiento = fecha_nacimiento
        self.nota = nota


def mostrarClases(listaDeClases):
    for clase in listaDeClases:
        print(f"ID: {clase.id}, Nombre: {clase.nombre}, Horario: {clase.horario}, Salon: {clase.salon}, Profesor: {clase.profesor}")

# INICIO DEL PROGRAMA
listaDeClases = []
listaDePromedios = []
opcion = 0

while opcion != 5:
    print("\n1. Agregar clase")
    print("2. Agregar alumno")
    print("3. Registro de Notas")
    print("4. Reportes")
    print("5. Salir")
    opcion = int(input("Opción: "))

    if opcion == 1:
        try:
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            horario = input("Horario: ")
            salon = input("Salon: ")
            profesor = input("Profesor: ")
            nuevaClase = Clase(id, nombre, horario, salon, profesor)
            listaDeClases.append(nuevaClase)
            print("Clase agregada exitosamente.")
        except:
            print("Error al agregar clase, alguno de los parametros no es valido.")

    elif opcion == 2:
        try:
            id = int(input("Carnet: "))
            nombre = input("Nombre: ")
            nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
            nuevoAlumno = Alumno(id, nombre, nacimiento)
            mostrarClases(listaDeClases)
            idClase = int(input("ID de la clase a asignar: "))

            for clase in listaDeClases:
                if clase.id == idClase:
                    alumno_ids = [alumno.id for alumno in clase.alumnos]
                    if nuevoAlumno.id not in alumno_ids:
                        clase.agregarAlumno(nuevoAlumno)
                        print(f"Alumno {nuevoAlumno.nombre} agregado a la clase {clase.nombre}.")
                    else:
                        print(f"El alumno con ID {nuevoAlumno.id} ya está en esta clase.")
        except:
            print("Error al agregar alumno, alguno de los parametros no es valido.")

    elif opcion == 3:
        try:
            mostrarClases(listaDeClases)
            print("Ingrese el ID de la clase en la que desea asignar nota: ")
            idClase = int(input())
            for clase in listaDeClases:
                if clase.id == idClase:
                    clase.mostrarAlumnos()
                    idAlumno = int(input("Carnet del alumno al que desea asignar nota: "))
                    nota = float(input("Nota: "))
                    clase.asignarNota(idAlumno, nota)
        except:
            print("Error al asignar nota, alguno de los parametros no es valido.")

    elif opcion == 4:


        opcionReporte = 0
        while(opcionReporte != 6):
            print("\n1. Listado de cursos con cantidad de estudiantes de mayor a menor")
            print("2. Listar estudiantes de un curso seleccionado junto con las notas de ese curso")
            print("3. Listar para un estudiante seleccionado sus nota")
            print("4. Reporte con la nota media por curso")
            print("5. Reporte con estudiante con mejor desempeño en general.")
            print("6. Regresar")
            opcionReporte = int(input("Opción: "))

            if opcionReporte == 1:
                clase.mostrarCursosConCantidadEstudiantes()
                break
            elif opcionReporte == 2:
                idClase = int(input("ID de la clase: "))
                for clase in listaDeClases:
                    if clase.id == idClase:
                        clase.mostrarEstudiantesConNotas()
                        break
            elif opcionReporte == 3:
                idAlumno = int(input("Carnet del alumno: "))
                for clase in listaDeClases:
                    for alumno in clase.alumnos:
                        if alumno.id == idAlumno:
                            print(f"Nombre: {alumno.nombre}, Curso: {clase.nombre}, Nota: {alumno.nota}")
                            continue
                break
            elif opcionReporte == 4:
                for clase in listaDeClases:
                    print(f"Curso: {clase.nombre}, Nota media: {str(clase.notaMedia())}")
                break

            elif opcionReporte == 5:
                # Coleccionar todas las notas de los estudiantes en todos los cursos
                notas_estudiantes = {}
                for clase in listaDeClases:
                    for alumno in clase.alumnos:
                        if alumno.id not in notas_estudiantes:
                            notas_estudiantes[alumno.id] = {'nombre': alumno.nombre, 'notas': []}
                        else:
                            notas_estudiantes[alumno.id]['notas'].append(alumno.nota)

                # Calcular el promedio general de notas
                mejor_estudiante = None
                mejor_promedio = 0
                for estudiante_id, data in notas_estudiantes.items():
                    promedio = sum(data['notas']) / len(data['notas']) if data['notas'] else 0
                    if promedio > mejor_promedio:
                        mejor_promedio = promedio
                        mejor_estudiante = data['nombre']

                if mejor_estudiante:
                    print(f"Nombre: {mejor_estudiante}, Promedio: {mejor_promedio}")
                else:
                    print("No hay estudiantes registrados.")
                break

            elif opcionReporte == 6:
                break
            else:
                print("Opción no válida.")

    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")
