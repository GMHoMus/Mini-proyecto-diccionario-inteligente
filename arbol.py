class Nodo:
    """Nodo del arbol binario de busqueda."""

    def __init__(self, palabra):
        self.palabra = palabra
        self.izquierdo = None
        self.derecho = None


class ArbolDiccionario:
    """Guarda palabras en orden alfabetico usando un BST."""

    def __init__(self):
        self.raiz = None

    def insertar(self, palabra):
        if self.raiz is None:
            self.raiz = Nodo(palabra)
        else:
            self._insertar_recursivo(self.raiz, palabra)

    def _insertar_recursivo(self, nodo, palabra):
        actual = palabra.texto.casefold()
        guardada = nodo.palabra.texto.casefold()

        if actual < guardada:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(palabra)
            else:
                self._insertar_recursivo(nodo.izquierdo, palabra)
        elif actual > guardada:
            if nodo.derecho is None:
                nodo.derecho = Nodo(palabra)
            else:
                self._insertar_recursivo(nodo.derecho, palabra)
        # Si el termino ya existe, no se agrega otra vez.

    def buscar(self, texto):
        return self._buscar_recursivo(self.raiz, texto.strip().casefold())

    def _buscar_recursivo(self, nodo, texto):
        if nodo is None:
            return None

        actual = nodo.palabra.texto.casefold()
        if texto == actual:
            return nodo.palabra
        if texto < actual:
            return self._buscar_recursivo(nodo.izquierdo, texto)
        return self._buscar_recursivo(nodo.derecho, texto)

    def _inorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.palabra)
            self._inorden_recursivo(nodo.derecho, resultado)

    def listar_ordenado(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def buscar_por_prefijo(self, prefijo):
        prefijo = prefijo.strip().casefold()
        if not prefijo:
            return []

        coincidencias = []
        for palabra in self.listar_ordenado():
            if palabra.texto.casefold().startswith(prefijo):
                coincidencias.append(palabra)
        return coincidencias

    def contar(self):
        return len(self.listar_ordenado())
