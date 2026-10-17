from modelos import Palabra
from arbol import ArbolDiccionario


def cargar_palabras(arbol):
    """Carga 50 terminos iniciales del diccionario."""
    datos = [
        ("Algoritmo", "Conjunto de pasos para resolver un problema."),
        ("Almacenamiento", "Lugar o medio donde se guardan datos."),
        ("API", "Interfaz que permite comunicarse a dos programas."),
        ("Archivo", "Conjunto de datos guardados con un nombre."),
        ("Arreglo", "Estructura que almacena varios elementos."),
        ("Atributo", "Dato o propiedad que pertenece a un objeto."),
        ("Base de datos", "Conjunto organizado de informacion."),
        ("Bucle", "Instruccion que repite un bloque de codigo."),
        ("Byte", "Unidad de informacion formada por ocho bits."),
        ("Clase", "Modelo usado para crear objetos."),
        ("Codigo", "Instrucciones escritas para una computadora."),
        ("Compilador", "Programa que traduce codigo a otro lenguaje."),
        ("Condicional", "Estructura que ejecuta codigo segun una condicion."),
        ("Constante", "Valor que no se espera cambiar durante la ejecucion."),
        ("Dato", "Representacion de un hecho o valor."),
        ("Depuracion", "Proceso de encontrar y corregir errores."),
        ("Diccionario", "Estructura que relaciona claves con valores."),
        ("Ejecucion", "Proceso de poner un programa en funcionamiento."),
        ("Encapsulamiento", "Proteccion y organizacion de datos dentro de una clase."),
        ("Error", "Problema que impide o altera el funcionamiento esperado."),
        ("Estructura de datos", "Forma de organizar y almacenar informacion."),
        ("Excepcion", "Situacion que interrumpe el flujo normal del programa."),
        ("Funcion", "Bloque reutilizable que realiza una tarea."),
        ("Hardware", "Componentes fisicos de una computadora."),
        ("Herencia", "Mecanismo para crear una clase basada en otra."),
        ("HTML", "Lenguaje de marcado usado para estructurar paginas web."),
        ("IDE", "Entorno que reúne herramientas para programar."),
        ("Indice", "Posicion de un elemento dentro de una secuencia."),
        ("Instruccion", "Orden que el programa puede ejecutar."),
        ("Interfaz", "Medio por el que una persona o programa interactua con otro."),
        ("Iteracion", "Una repeticion de un proceso o ciclo."),
        ("Java", "Lenguaje de programacion de proposito general."),
        ("Lista", "Coleccion ordenada de elementos."),
        ("Metodo", "Funcion definida dentro de una clase."),
        ("Modulo", "Archivo que contiene codigo reutilizable."),
        ("Nodo", "Elemento que guarda un dato y referencias a otros elementos."),
        ("Objeto", "Instancia creada a partir de una clase."),
        ("Parametro", "Dato que una funcion recibe para trabajar."),
        ("Python", "Lenguaje de programacion conocido por su sintaxis clara."),
        ("Recursividad", "Tecnica en la que una funcion se llama a si misma."),
        ("Red", "Conjunto de dispositivos conectados para compartir informacion."),
        ("Repositorio", "Lugar donde se guarda y controla el codigo de un proyecto."),
        ("Salida", "Informacion que un programa entrega como resultado."),
        ("Servidor", "Sistema que ofrece servicios o recursos a otros equipos."),
        ("Sistema operativo", "Software que administra el equipo y sus recursos."),
        ("Software", "Programas e instrucciones que usa una computadora."),
        ("SQL", "Lenguaje usado para consultar y administrar bases de datos."),
        ("Variable", "Espacio con nombre que guarda un valor."),
        ("Versión", "Estado identificado de un programa o archivo."),
        ("Web", "Sistema de paginas y recursos accesibles por internet."),
    ]

    for texto, definicion in datos:
        arbol.insertar(Palabra(texto, definicion))


def mostrar_menu():
    print("\n" + "=" * 42)
    print("       DICCIONARIO DE PROGRAMACION")
    print("=" * 42)
    print("1. Buscar una palabra")
    print("2. Buscar por prefijo (autocompletar)")
    print("3. Mostrar diccionario completo")
    print("4. Ver cantidad de palabras")
    print("5. Salir")
    print("=" * 42)


def buscar_palabra(arbol):
    texto = input("Escriba la palabra que desea buscar: ").strip()
    if not texto:
        print("No escribio ninguna palabra.")
        return

    palabra = arbol.buscar(texto)
    if palabra:
        print(f"\nPalabra: {palabra.texto}")
        print(f"Definicion: {palabra.definicion}")
    else:
        print("La palabra no se encuentra en el diccionario.")


def buscar_prefijo(arbol):
    prefijo = input("Escriba el inicio de la palabra: ").strip()
    if not prefijo:
        print("Escriba al menos una letra.")
        return

    resultados = arbol.buscar_por_prefijo(prefijo)
    if resultados:
        print("\nPalabras encontradas:")
        for palabra in resultados:
            print(f"- {palabra.texto}: {palabra.definicion}")
    else:
        print("No hay palabras que comiencen con ese prefijo.")


def mostrar_diccionario(arbol):
    palabras = arbol.listar_ordenado()
    print(f"\nDICCIONARIO ({len(palabras)} palabras)")
    print("-" * 42)
    for palabra in palabras:
        print(f"{palabra.texto}: {palabra.definicion}")


def main():
    arbol = ArbolDiccionario()
    cargar_palabras(arbol)
    print(f"Se cargaron {arbol.contar()} palabras.")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            buscar_palabra(arbol)
        elif opcion == "2":
            buscar_prefijo(arbol)
        elif opcion == "3":
            mostrar_diccionario(arbol)
        elif opcion == "4":
            print(f"El diccionario tiene {arbol.contar()} palabras.")
        elif opcion == "5":
            print("Gracias por usar el diccionario. Hasta luego.")
            break
        else:
            print("Opcion no valida. Seleccione del 1 al 5.")


if __name__ == "__main__":
    main()
