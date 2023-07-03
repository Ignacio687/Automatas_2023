from data_analyzer import DataAnalyzer
from datetime import time, datetime, date

class UserInterface():
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        print("Seguimiento de los usuarios que se han conectado días feriados y no laborables (sábados y domingos).")
        print("Integrantes: \n\tBoldrini Matías, \n\tBourguet Tomás, \n\tChaves Ignacio")
        while True:
            try:
                #path = input('Ingrese el path del archivo a analizar (.csv): ')
                path = '/home/ignaciochaves/code/python/Automatas_2023/Trabajo final/data.csv'
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
        userData, startDate, endDate = data.filterUsers(startDate, endDate)
        print(userData)
        #self.strFormat(userData, startDate, endDate)


    def strFormat(self, userData: dict[str, dict[str, dict[str, int]]], startDate: str|date, endDate: str|date):
        final_str = ''
        for username in userData.keys():
            final_str += f"\n{'-'*55} MOSTRANDO DATOS DESDE {startDate} HASTA {endDate} {'-'*55}\n"
            final_str += f"Username: {username} "
            final_str += f"\n\tDireccion MAC mas usada: {userData[username][most_used_mac]}"
            final_str += f"\n\tDireccion MAC mas tiempo conectada: {userData[username][mac_most_time]}\n"
            final_str += f"\n\tConexiones:"
            
            for mac in userData[username].keys():               
                final_str += f""" \n\t{mac}: Session time: {datetime.strptime(str(userData[username][mac]['Session_time']),"%H:%M:%S"):<10} 
                                | Input Bytes: {userData[username][mac]['Input_Bytes']:<10} | Output Bytes: {userData[username][mac]['Output_Bytes']:<10} 
                                | Session Count: {userData[username][mac]['Session_count']} """
            
        return final_str

if __name__ == '__main__':
    UserInterface().run()