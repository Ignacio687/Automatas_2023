from data_analyzer import DataAnalyzer
from datetime import time, datetime

class UserInterface():
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        print("Seguimiento de los usuarios que se han conectado días feriados y no laborables (sábados y domingos).")
        print("Integrantes: \n\tBoldrini Matías, \n\tBourguet Tomás, \n\tChaves Ignacio")
        while True:
            try:
                #path = input('Ingrese el path del archivo a analizar (.csv): ')
                path = '/Users/matiasboldrini/Facu/Automatas_2023/Trabajo final/archivo.csv'
                data = DataAnalyzer(path)
                open(path)
                break
            except FileNotFoundError:   
                print("Archivo no encontrado, intenelo de nuevo")

        print(f"\nVerificando el archivo, esto puede tardar unos segundos...")
        errors = data.validate()
        print(f"Se han encontrado [{len(errors)}] errores en el archivo original. Generando csv filtrado..")
        data.generateFile(lines = tuple(errors.keys()))
        while True:
            try:
                fecha_inicio = input('Ingrese la fecha inicial: ')
                fecha_fin = input('Ingrese la fecha final: ')
                startDate = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
                endDate = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
                # startDate = datetime.strptime('2019-11-29', "%Y-%m-%d").date()
                # endDate = datetime.strptime('2019-11-19', "%Y-%m-%d").date()
                break
            except ValueError:
                if fecha_inicio == '' or fecha_fin == '':
                    startDate, endDate = fecha_inicio, fecha_fin
                    break
                print("Se debe ingresar la fecha en formate '%Y-%m-%d'. Intente de nuevo")
        print("Buscando entre los usuarios que se han conectado días feriados y fines de semana..")
        data.filterUsers(startDate, endDate)
        print(f"\n{data.__str__()}")
if __name__ == '__main__':
    UserInterface().run()