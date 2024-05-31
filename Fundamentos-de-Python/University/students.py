import db_processes as modulo

while True:
    print()
    print("=== Estudiantes ===")
    print("1. - Registrar a un alumno")
    print("2. - Listar Alumnos")
    print("3. - Buscar un Alumno")
    print("4. - Actualizar carrera del alumno")
    print("5. - Eliminar un Alumno")
    print("6. - Cerrar Sistema")
    print("=" * 10)

    opcion = int(input("Elige una opcion (1-6): ").strip())
    print("=" * 10)
    print()


    if opcion == 1:
        print("=== Datos del Alumno ===")
        nom = input("Nombre: ").strip().capitalize()
        ape = input("Apellido: ").strip().capitalize()
        car = input("Carrera: ").strip().capitalize()
        eda = int(input("Edad: ").strip())
        res = modulo.Registrar_Alumno(nom, ape, car, eda)
        if res == 1:
            print("=== Ocurrio un error al insertar ===")
        else:
            print("Alumno Registrado")

    elif opcion == 2:
        print("=== Lista de Alumnos ===")
        res = modulo.Listar_Alumnos()
        print(res)

    elif opcion == 3:
        print("=== Buscar un Alumno ===")
        est_id = int(input("Id del Alumno: ").strip())
        res = modulo.Obtener_Alumno_Id(est_id)
        if res == 1:
            print("== Error al buscar al alumno ==")
        elif res == ():
            print("== No existe alumno con ese Id ==")
        else:
            print(res)

    elif opcion == 4:
        print("=== Actualizar carrera del Alumno ===")
        est_id = int(input("Id del Alumno: ").strip())
        res = modulo.Obtener_Alumno_Id(est_id)
        if res == 1:
            print("== Error al buscar al alumno ==")
        elif res == ():
            print("== No existe alumno con ese Id ==")
        else:
            car = input("Ingresa la nueva carrera: ").strip().capitalize()
            res = modulo.Actualizar_Carrera_Alumno(car, est_id)
            if res == 1:
                print("== Error al Actualizar ==")
            else:
                print("== Carrera Cambiada ==")

    elif opcion == 5:
        print("=== Eliminar Alumno ===")
        est_id = int(input("Id del Alumno: ").strip())
        res = modulo.Obtener_Alumno_Id(est_id)
        if res == 1:
            print("== Error al buscar al alumno ==")
        elif res == ():
            print("== No existe alumno con ese Id ==")
        else:
            res = modulo.Eliminar_Alumno(est_id)
            if res == 1:
                print("== Error al Eliminar ==")
            else:
                print("== Alumno Eliminado ==")

    elif opcion == 6:
        print("==== Sistema Finalizado =====")
        break

    else:
        print("Error, Intentalo de nuevo")
