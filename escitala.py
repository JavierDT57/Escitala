import os
# algoritmo de cifrado y descifrado escitala
from math import ceil
def cifrar(msg, n, file=False):
    # convert ascii string to bytes
    if type(msg)==str:
        msg = bytes(msg, encoding='ascii')
    n = int(n)
    if n == 1 or n == len(msg) or n > len(msg):
        raise ValueError("El numero de filas debe ser mayor que 1 y menor que la longitud del mensaje.")
    # length of each row
    l = int(ceil(len(msg) / float(n)))
    # padding message with ' ' to make it a multiple of n
    msg = msg.ljust(l * n, b' ')
    # take slices of l chars
    chunks = [msg[i:i+l] for i in range(0,len(msg),l)]
    transposed_codes = _transpose(chunks)
    # take each char and join them
    transposed_msg = list(map(lambda row: bytes(row), transposed_codes))
    msg =  b''.join(transposed_msg)
    # return bytes or ascii string
    if file:
        return msg
    return msg.decode(encoding='ascii')


def _transpose(matrix):
    return [bytes([row[i] for row in matrix]) for i in range(len(matrix[0]))]

def descifrar(msg, n, file=False):
    # convert ascii string to bytes
    n = int(n)
    if type(msg)==str:
        msg = bytes(msg, encoding='ascii')
    # take slices of n chars
    chunks = [msg[i:i+n] for i in range(0, len(msg), n)]
    transposed_codes = _transpose(chunks)
    # take each char and join them
    transposed_msg = list(map(lambda row: bytes(row), transposed_codes))
    msg = b''.join(transposed_msg)
    # return bytes or ascii string
    if file:
        return msg
    return msg.decode(encoding='ascii')

if __name__ == "__main__":
    while True:
        opt = input("1. Cifrar\n2. Descifrar\n3. Salir\nOpcion: ")
        if opt == "1":
            format = input("1. Imagen\n2. Texto\n3. Archivo\nOpcion:")
            if format == "1":
                img = input("Ingrese la ruta de la imagen: ")
                name = 'cifrado.' + img
                n = input("Ingrese el numero de filas: ")
                img = open(img, "rb").read()
                e_img = cifrar(img, n, file=True)
                open(name, 'wb').write(e_img)
                print(f"Imagen cifrada en {name}")
            elif format == "2":
                msg = input("Ingrese el mensaje: ")  # Solicita el mensaje de texto a cifrar
                n = int(input("Ingrese el numero de filas: "))  # Solicita el número de filas para el algoritmo de cifrado

                # Verifica si el número de filas es válido
                while True:
                    try:
                        e_msg = cifrar(msg, n)  # Llama a la función 'cifrar' para cifrar el mensaje de texto
                        print(f"'{e_msg}'")  # Muestra el mensaje cifrado
                        break
                    except ValueError as e:
                        print(f"Error: {e}")
                        n = int(input("Ingrese el numero de filas: "))
            elif format == "3":
                file = input("Ingrese la ruta del archivo: ")  # Solicita la ruta del archivo
                name = 'cifrado.' + file  # Crea el nombre del archivo cifrado
                n = input("Ingrese el numero de filas: ")  # Solicita el número de filas para el algoritmo de cifrado
                file = open(file, "rb").read()  # Abre y lee el contenido del archivo en formato binario
                e_file = cifrar(file, n, file=True)  # Llama a la función 'cifrar' para cifrar el contenido del archivo
                open(name, 'wb').write(e_file)  # Escribe el contenido cifrado en el nuevo archivo en formato binario
                print(f"Archivo cifrado en {name}")  # Informa al usuario que el archivo ha sido cifrado y guarda la ruta

        elif opt == "2":
            format = input("1. Imagen\n2. Texto\n3. Archivo\nOpcion: ")
            if format == "1":
                img = input("Ingrese la ruta de la imagen: ")
                name = 'descifrado.' + img
                n = input("Ingrese el numero de filas: ")
                img = open(img, "rb").read()
                d_img = descifrar(img, n, file=True)
                open(name, 'wb').write(d_img)
                print(f"Imagen descifrada en {name}")
            elif format == "2":
                msg = input("Ingrese el mensaje: ")
                n = input("Ingrese el numero de filas: ")
                d_msg = descifrar(msg, n)
                print(f"'{d_msg}'")
            elif format == "3":
                file = input("Ingrese la ruta del archivo: ")
                name = 'descifrado.' + file
                n = input("Ingrese el numero de filas: ")
                file = open(file, "rb").read()  # Abre y lee el contenido del archivo en formato binario
                d_file = descifrar(file, n, file=True)  # Llama a la función 'descifrar' para descifrar el contenido del archivo
                open(name, 'wb').write(d_file)  # Escribe el contenido descifrado en el nuevo archivo en formato binario
                print(f"Archivo descifrado en {name}")

            # clear the screen
        else:
            break
        input()
        os.system('cls' if os.name == 'nt' else 'clear')