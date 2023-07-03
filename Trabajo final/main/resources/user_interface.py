from data_analyzer import DataAnalyzer
from datetime import time, datetime, date, timedelta

class UserInterface():
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        print("Seguimiento de los usuarios que se han conectado días feriados y no laborables (sábados y domingos).")
        print("Integrantes: \n\tBoldrini Matías, \n\tBourguet Tomás, \n\tChaves Ignacio")
        while True:
            try:
                #path = input('Ingrese el path del archivo a analizar (.csv): ')
                path = '/home/ignaciochaves/code/python/Automatas_2023/Trabajo final/main/data/data_filtered.csv'
                data = DataAnalyzer(path)
                open(path)
                break
            except FileNotFoundError:   
                print("Archivo no encontrado, intenelo de nuevo")
        print(f"\nVerificando el archivo, esto puede tardar unos segundos...")
        #errors = data.validate()
        #print(f"Se han encontrado [{len(errors)}] errores en el archivo original. Generando csv filtrado..")
        #data.generateFile(lines = tuple(errors.keys()))
        while True:
            try:
                #fecha_inicio = input('Ingrese la fecha inicial: ')
                #fecha_fin = input('Ingrese la fecha final: ')
                # startDate = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
                # endDate = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
                startDate = datetime.strptime('2019-11-22', "%Y-%m-%d").date()
                endDate = datetime.strptime('2019-11-24', "%Y-%m-%d").date()
                break
            except ValueError:
                if fecha_inicio == '' or fecha_fin == '':
                    startDate, endDate = fecha_inicio, fecha_fin
                    break
                print("Se debe ingresar la fecha en formate '%Y-%m-%d'. Intente de nuevo")
        print("Buscando entre los usuarios que se han conectado días feriados y fines de semana..")
        userData, startDate, endDate = data.filterUsers(startDate, endDate)
        print(self.strFormat(userData, startDate, endDate))
        data.exportExcel(userData)


    def strFormat(self, userData: dict[str, str|dict[str, int]], startDate: str|date, endDate: str|date):
        def format_bytes(size):
            power = 2**10  # 2^10 = 1024
            units = ['bytes', 'kB', 'MB', 'GB', 'TB']
            exponent = (len(str(size)) - 1) // 3
            size /= power ** exponent
            size = round(size, 2)
            size_with_unit = str(size) + ' ' + units[exponent]
            return size_with_unit

        final_str = ''
        for username in userData.keys():
            final_str += f"\n\n{'-'*55} MOSTRANDO DATOS DESDE {startDate} HASTA {endDate} {'-'*55}\n"
            final_str += f"Username: {username} \n"
            final_str += f"\n\tDireccion MAC mas usada: {userData[username]['most_used_mac']}"
            final_str += f"\n\tDireccion MAC mas tiempo conectada: {userData[username]['mac_most_time']}\n"
            final_str += f"\n\tConexiones:"
            for index,mac in enumerate(userData[username].keys()):
                if index > 1:               
                    input_bytes     = format_bytes(userData[username][mac]['Input_Bytes'])
                    output_bytes    = format_bytes(userData[username][mac]['Output_Bytes'])
                    start_date      = userData[username][mac]['Session_dates'][0]
                    end_date        = userData[username][mac]['Session_dates'][1]
                    session_count   = userData[username][mac]['Session_count']
                    session_time = str(timedelta(seconds = userData[username][mac]['Session_Time']))
                    final_str += f"\n\t\t{mac}: Start date: {start_date}  | End date: {end_date}"
                    final_str += f"\n\t\t\t  Session time: {session_time:<18} | Input Bytes: {input_bytes:<10} | Output Bytes: {output_bytes:<10} | Session Count: {session_count} "
        return final_str

if __name__ == '__main__':
    UserInterface().run()