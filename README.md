# Diccionario de Programacion

## Descripcion
Proyecto de consola hecho en Python para practicar clases, objetos, arboles binarios de busqueda, recursividad y recorridos.

## Requisitos
- Python 3 instalado.
- No requiere instalar librerias externas.

## Archivos
- `modelos.py`: clase `Palabra`.
- `arbol.py`: nodos, insercion, busqueda, recorrido inorden y prefijos.
- `main.py`: carga de 50 terminos y menu de usuario.

## Como ejecutarlo en Windows
1. Descargue y extraiga la carpeta del proyecto.
2. Abra la carpeta en Visual Studio Code.
3. Abra Terminal > Nueva terminal.
4. Ejecute:
   ```powershell
   python main.py
   ```
   Si ese comando no funciona, pruebe:
   ```powershell
   py main.py
   ```

## Pruebas recomendadas
1. Opcion 1, buscar `Python`: debe mostrar su definicion.
2. Opcion 1, buscar `Java`: debe mostrar su definicion.
3. Opcion 1, buscar `Minecraft`: debe indicar que no existe.
4. Opcion 2, escribir `pro`: debe mostrar `Programacion` no esta incluida como termino; pruebe `pro` para verificar las coincidencias disponibles como `Repositorio` no coincidira. Para un resultado claro, pruebe `a`, `ar` o `so`.
5. Opcion 3: muestra las 50 palabras en orden alfabetico.
6. Opcion 4: debe indicar 50 palabras.
7. Opcion 5: termina el programa.

## Como funciona el arbol
Cada palabra se guarda en un nodo. Las palabras alfabeticamente menores se colocan a la izquierda y las mayores a la derecha. La busqueda compara el termino solicitado con el nodo actual. El recorrido inorden visita izquierda, nodo y derecha, por eso el diccionario se muestra ordenado.

La busqueda por prefijo recorre el listado ordenado y conserva los terminos que comienzan con las letras escritas.
