from data_analyzer import DataAnalyzer, IncorrectFileExtensionError
from datetime import time, datetime, date, timedelta

class UserInterface():
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        print("Seguimiento de los usuarios que se han conectado días feriados y no laborables (sábados y domingos).")
        print("Integrantes: \n\tBoldrini Matías, \n\tBourguet Tomás, \n\tChaves Ignacio")
        while True:
            try:
                path = input('Ingrese el path del archivo a analizar (.csv): ')
                data = DataAnalyzer(path)
                open(path)
                break
            except (FileNotFoundError, IsADirectoryError, IncorrectFileExtensionError):   
                print("Archivo no encontrado, intenelo de nuevo")
        print(f"\nVerificando el archivo, esto puede tardar unos segundos...")
        errors = data.validate()
        print(f"Se han encontrado [{len(errors)}] errores en el archivo original.")
        if errors:
            print("Generando csv filtrado..")
            while True:
                choice = input("Desea mostrar los errores por consola? (y/n) ")
                if choice == "y":
                    for error,detalles in errors.items():
                        print(f'{error}:  {detalles}\n')
                    break
                if choice == "n":
                    break
        data.generateFile(lines = tuple(errors.keys()))
        while True:
            while True:
                try:
                    fecha_inicio = input('Ingrese la fecha inicial: ')
                    if fecha_inicio == '':
                        startDate = date(2000, 1, 1) # Fecha antigua para incluir todos los resultados
                    else:
                        startDate = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
                    fecha_fin_input = input('Ingrese la fecha final: ')
                    if fecha_fin_input == '':
                        endDate = date.today()
                    else:
                        endDate = datetime.strptime(fecha_fin_input, "%Y-%m-%d").date()
                except ValueError as e:
                    print("Se debe ingresar la fecha en formato 'YYYY-mm-dd'. Intente de nuevo")
                else:
                    break
            print("Buscando entre los usuarios que se han conectado días feriados y fines de semana..")
            userData, startDate, endDate = data.filterUsers(startDate, endDate)
            print(self.strFormat(userData, startDate, endDate))
            while True:
                choice = input("Desesa exportar los datos a un archivo Excel ?(y,n) ")
                if choice.lower() == 'y':
                    path = input('Escriba el path de destino del archivo: ')
                    filename = f'reporte_{startDate}_{endDate}'
                    data.exportExcel(userData, path, filename)
                    break
                elif choice.lower() == 'n':
                    break
            while True:
                choice = input("Desesa filtrar con otro rango de fechas?(y,n): ")
                if choice.lower() == 'y':
                    break
                elif choice.lower() == 'n':
                    exit()

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
                    final_str += f"\n\t\t{mac}:"
                    final_str += f"\n\t\t\t Fecha de inicio:      {start_date} | Fecha de finalizacion: {end_date}"
                    final_str += f"\n\t\t\t Input Bytes:          {input_bytes:<10} | Output Bytes:     {output_bytes:<10} "
                    final_str += f"\n\t\t\t Cantidad de sesiones: {session_count:<10} | Tiempo total:   {session_time}"
        return final_str

if __name__ == '__main__':
    UserInterface().run()