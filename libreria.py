from random import randint
import json

class Libro:
    def __init__(self, id='', titulo='', autor='', publicado=2000, editorial='') -> None:
        self.id = randint(0, 1000) if id == '' else id # comparacion ? true : false
        self.__titulo = titulo
        self.__autor = autor
        self.__publicado = publicado
        self.__editorial = editorial

    # @property
    # def titulo(self):
    #     return self.__titulo

    # @property
    # def autor(self):
    #     return self.__autor

    # dict() list()
    def to_dict(self):
        return {"id": self.id, 
                "titulo": self.__titulo, 
                "autor": self.__autor, 
                "publicado": self.__publicado, 
                "editorial": self.__editorial} 

    def __str__(self) -> str:
        return f'id: {self.id}\nTítulo: {self.__titulo}\nAutor: {self.__autor}\nPublicado: {self.__publicado}\nEditorial: {self.__editorial}\n'

class Libreria:
    def __init__(self) -> None:
        self.__libros = []

    def abrir(self, ubicacion: str):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__libros = [Libro(**dicc) for dicc in lista]
                return True
        except:
            return False

    def guardar(self, ubicacion: str):
        try:
            with open(ubicacion, 'w') as archivo:
                #archivo.write(str(self.__libros[0].to_dict()))
                lista = [libro.to_dict() for libro in self.__libros]
                json.dump(lista, archivo, indent=5)
                return True
        except:
            return False
    
    def agregar_final(self, libro: Libro):
        self.__libros.append(libro)

    def agregar_inicio(self, libro: Libro):
        self.__libros.insert(0, libro)

    def eliminar(self, id) -> bool:
        for libro in self.__libros:
            if libro.id == id:
                self.__libros.remove(libro)
                return True
        return False

    def modificar(self, id, libro: Libro) -> bool:
        i = 0
        while i < len(self.__libros):
            if self.__libros[i].id == id:
                self.__libros[i] = libro
                return True
            i = i + 1
        return False

    def mostrar(self):
        for libro in self.__libros:
            print(libro)

    def __str__(self) -> str:
        return "".join(str(libro) + '\n' for libro in self.__libros)

    