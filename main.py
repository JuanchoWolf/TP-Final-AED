
from pprint import pprint
from modulo import cargar_generos, cargar_series, obtener_coincidentes_tiempo, validar_tiempo


def menu()->int:
    '''
    Interfaz Grafica Consola con retorno de opcion elejida.
    '''
    print(f'''
    {'='*40}
            MENU
    {'='*40}
        0) - Salir.
        1) - Cargar Generos.
        2) - Cargar Series.
        3) - Mostrar Series Segun Duracion.
    {'='*40}
    ''')
    opc = ''
    flag = False
    while not opc.isdigit() or (int(opc) < 0 or int(opc) > 3):

        if flag:
            print('Opcion Invalida...')
        else:
            flag = True

        opc = input('Ingrese opcion: ')

    return int(opc)


def  app():
    '''
    Ejecucion de App Principal.
    '''
    generos = []
    series = []
    while True:
        opc = menu()

        if opc == 1:
            generos = cargar_generos(generos)
            print('\nGeneros Cargados Correctamente')

        elif opc == 2:
            series, c = cargar_series(series, generos)
            if c != 0:
                print('\nSeries Cargados Correctamente')
                print(f"Se cargaron {len(series)} series, y {c-len(series)} fueron descartadas...")

            else:
                print("Cargue los 'Generos' antes de volver a intentar.\n")

        elif opc == 3:
            if len(series) != 0:
                desde = validar_tiempo("Indique el Inicio")
                hasta = validar_tiempo("Indique el Final")

                coincidentes, duracion = obtener_coincidentes_tiempo(desde, hasta, series)

                for i in range(len(coincidentes)):
                    print("\n", coincidentes[i].__str__())
                
                print(f"\nLa duracion promedio de las series coincidentes es {round(duracion/len(coincidentes), 2)} minutos.")

            else:
                print("Cargue las 'Series' antes de volver a intentar.\n")
            

        else:
            exit('Done!')


if __name__ == '__main__':
    app()