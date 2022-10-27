
class Series:
    def __init__(self, poster:str, title:str, runtime:str, certificate:str, episodes:int, genre:int, rating:float, overwiew:str, votes:int) -> None:
        self.poster_link = poster
        self.series_title = title
        self.runtime_series = runtime
        self.certificate = certificate
        self.runtime_episodes = episodes
        self.genre = genre
        self.rating = rating
        self.overwiew = overwiew
        self.no_vote = votes


    def __str__(self) -> str:
        return f' Serie: {self.series_title} Poster: {self.poster_link} Runtime: {self.runtime_series} Cerificacion: {self.certificate} Tiempo Prom de Episodios: {self.runtime_episodes} Genero: {self.genre} Rating: {self.rating} Resumen: {self.overwiew} Votos: {self.no_vote} '


class Generos:
    def __init__(self, index:int, nombre:str, cantidad:int) -> None:
        self.indice = index
        self.nombre = nombre
        self.cantidad = cantidad


    def __str__(self) -> str:
        return f" Indice de Codigo: {self.indice} Genero: {self.nombre} Cantidad Listado: {self.cantidad} "


def cargar_generos(vector: list)->list:
    from os.path import getsize
    LOCATE = '.\\generos.txt'

    file = open(LOCATE, 'rt')
    SIZE = getsize(LOCATE)
    
    # tell() position actual|| seek() move pointer
    while file.tell() < SIZE:
        obj = file.readline()
        vector.append(obj[:-1])

    file.close()
    return vector


def cargar_series(vector: list, codigos: list)->list:
    from os.path import getsize
    LOCATE = '.\\series_aed.csv'

    file = open(LOCATE, 'rt')
    SIZE = getsize(LOCATE)
    
    if not codigos == []:
        flag = False
        cont = 0
        # tell() position actual|| seek() move pointer
        while file.tell() < SIZE:
            cont += 1
            line = file.readline()
            
            if flag:
                obj = process_line(line[:-1])

                flag_cumple, obj = cumple_duracion(obj)
                if not flag_cumple:
                    continue

                obj = formatear_genero(obj, codigos)

                pos = buscar_posicion(obj.no_vote, vector)

                vector.insert(pos, obj)

            else:
                flag = True


        file.close()
        return vector, cont
    
    else:
        file.close()
        print('\nNo Han sido cargados los Codigos...')
        return [], 0


def process_line(line: str)->Series:
    sec = line.split('|')

    flt = sec[6].replace(',', '.')
    #epi = sec[4].replace("min", "")

    obj = Series(
        sec[0],
        sec[1],
        sec[2],
        sec[3],
        sec[4], # int(epi),
        sec[5],
        float(flt),
        sec[7],
        int(sec[12])
    )
    return obj


def buscar_posicion(votos: int, registro: list)-> int:
    izq = 0
    der = len(registro) - 1

    while izq <= der:
        cen = (izq + der) // 2

        if registro[cen].no_vote == votos:
            return cen + 1

        elif registro[cen].no_vote > votos:
            izq = cen + 1

        else:
            der = cen - 1

    return izq


def cumple_duracion(registro: Series)->Series:

    if registro.runtime_episodes == "":
        t = False

    else:
        t = True
        dur:str = registro.runtime_episodes
        dur = dur.replace("min", "")
        registro.runtime_episodes = int(dur)

    return t, registro
    


def formatear_genero(objeto: Series, generos: list)->Series:
    genre = objeto.genre
    index = generos.index(genre)
    objeto.genre = index

    return objeto


