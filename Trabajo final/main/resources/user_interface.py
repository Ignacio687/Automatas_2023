from data_analyzer import DataAnalyzer
from datetime import time, datetime

class UserInterface():
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        print("Seguimiento de los usuarios que se han conectado días feriados y no laborables (sábados y domingos).")
        print("Integrantes: \n\tBourguet Tomás, \n\tChaves Ignacio, \n\tGotusso Emiliano, \n\tBoldrini Matías")
        while True:
            try:
                path = input('Ingrese el path del archivo a analizar (.csv): ')
                #path = '/Users/matiasboldrini/Facu/Automatas_2023/Trabajo final/main/data/test_files/test_mati.csv'
                open(path)
                data = DataAnalyzer(path)
                break
            except FileNotFoundError:   
                print("Archivo no encontrado, intenelo de nuevo")

        print(f"\nVerificando el archivo, esto puede tardar unos segundos...")
        print("Buscando entre los usuarios que se han conectado días feriados y fines de semana..")
        while True:
            #errors = data.validate()
            #print(f"Se han encontrado [{len(errors)}] errores en el archivo original. Generando csv filtrado..")
            try:
                #startDate = datetime.strptime(input('Ingrese la fecha inicial: '), "%Y-%m-%d").date()
                #endDate = datetime.strptime(input('Ingrese la fecha final: '), "%Y-%m-%d").date()
                startDate = datetime.strptime('2020-01-01', "%Y-%m-%d").date()
                endDate = datetime.strptime('2020-02-02', "%Y-%m-%d").date()
                break
            except ValueError:
                    print("Se debe ingresar la fecha en formate '%Y-%m-%d'. Intente de nuevo")
        data.filterUsers(startDate, endDate)
        print(f"\n{data.__str__()}")
if __name__ == '__main__':
    UserInterface().run()