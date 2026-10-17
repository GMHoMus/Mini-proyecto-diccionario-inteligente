class Palabra:
    """Guarda una palabra y su significado."""

    def __init__(self, texto, definicion):
        self.texto = texto.strip()
        self.definicion = definicion.strip()

    def __str__(self):
        return f"{self.texto}: {self.definicion}"
