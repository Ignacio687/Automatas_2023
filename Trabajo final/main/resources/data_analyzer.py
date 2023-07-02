import pathlib,csv, json
from datetime import datetime, timedelta, date
from collections import Counter
class IncorrectFileFormat(Exception):
    pass

class DataAnalyzer():
    def __init__(self, filePath: str) -> None:
        """Class capable of validating a specific format csv file and 
        returning filtered data.\n
        filePath: Absolute path of the file"""
        self.filePath = filePath
        startDate = datetime.strptime("2003-01-01", "%Y-%m-%d")
        endDate = datetime.strptime("2023-06-30", "%Y-%m-%d")
        self.filterUsers(startDate=startDate, endDate=endDate)

    def validate(self) -> dict[int, str|int]:
        """Method capable of validating the file format and all data within the lines. 
        Returns a dictionary with all the found errors '{line_index:[errors_list]}'."""
        pass

    def generateFile(self, path: str, lines: tuple[int]|None = None) -> str:
        """Method designed to copy the original file, with or without removing lines, 
        into a new directory. Returns the new file absolute path.\n
        path: Absolute path where the new file will be.\n
        lines: Indexes of lines willing to remove."""
        pass

    def filterUsers(self, 
                    filter: bool = True, 
                    startDate = None, 
                    endDate = None
                    ):
        """Method designed to filter the users that have accessed the system on Non-working days. 
        Returns a dictionary {user_name: [total_session_time, most_used_MAC_NWD, most_used_MAC_WD, 
            , total_output_octects]}  *NWD = Non-working days * WD = Working days\n
        filter: if set to False method returns complete list of users\n
        startDate/endDate: if either of them is set to None, the method will take the most old or 
        new date available respectively."""
        """
        ID,ID_Sesion,ID_Conexión_unico,Usuario,IP_NAS_AP,Tipo__conexión,Inicio_de_Conexión_Dia,Inicio_de_Conexión_Hora,FIN_de_Conexión_Dia,FIN_de_Conexión_Hora,
        Session_Time,Input_Octects,Output_Octects,MAC_AP,MAC_Cliente,Razon_de_Terminación_de_Sesión,,
        603877,5AA0184E-000001CA,d6104707df0cd315,invitado-deca,192.168.247.11,Wireless-802.11,2019-02-07,19:46:08,2019-03-13,11:27:57,25,39517,505219,DC-9F-DB-12-F3-EA:HCDD,DC-BF-E9-1A-B5-D0,User-Request,,
        """
        fecha_inicio = date(2020, 3, 22) ## Argumentos
        fecha_fin = date(2020, 3, 22)
        if fecha_inicio == None:
            fecha_inicio = date(2000, 3, 27) # Fecha antigua para incluir todos los resultados
        if fecha_fin == None:
            fecha_fin = date.today()
        if fecha_fin < fecha_inicio:
            fecha_fin, fecha_inicio = fecha_inicio, fecha_fin


        def is_weekend(fecha_inicio, fecha_fin):
            """Method designed to validate if a date range is has a weekend or holyday.
            Args:
                fecha_inicio (datetime.date): start date
                fecha_fin (datetime.date): end date
            Returns:
                bool: returns True if there is at least one weekend or holyday within the dates range.
            """
            with open(f"main/data/{fecha_inicio.year}.json") as json_file:
                fecha_actual = fecha_inicio
                data = json.load(json_file)
                delta = timedelta(days=1)
                fecha_actual = fecha_inicio
                while fecha_actual <= fecha_fin:
                    month = fecha_actual.month-1
                    day = fecha_actual.strftime("%d")
                    dia_semana = fecha_actual.weekday()
                    if fecha_actual.year != fecha_inicio.year:
                        # Json files are separated by years
                        # Open next year json and run the same procedure.
                        return is_weekend(fecha_actual, fecha_fin)
                    if dia_semana in [5, 6] or day in [i for i in data[month].keys()]: 
                        return True
                    fecha_actual += delta
                return False

        def print_data():
            for key in user_data.keys():
                print(f"\n{'-'*35} MOSTRANDO DATOS DESDE {fecha_inicio} HASTA {fecha_fin} {'-'*35}\n")
                print(f"{key}:")
                print(f"\tUsername: {user_data[key]['username']} ")
                mac_dict = user_data[key]['mac_cliente']
                connection_count = Counter(mac for mac in mac_dict for _ in mac_dict[mac])
                most_connected_mac = connection_count.most_common(1)[0][0]
                total_hours = {mac: sum(int(hour) for hour in mac_dict[mac]) for mac in mac_dict}
                mac_with_longest_duration = max(total_hours, key=total_hours.get)
                print(f"\tMost used mac adress: {most_connected_mac}")
                print(f"\tMost time connected mac {mac_with_longest_duration}")
                print(mac_dict)
                print(f"\tConexiones:")
                for i in user_data[key]['conexiones']:
                    print(f"\t\t{i}")
                    
        user_data = {}
        with open(self.filePath) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                inicio_conexion = datetime.strptime(row['Inicio_de_Conexión_Dia'], "%Y-%m-%d").date()
                fin_conexion = datetime.strptime(row['FIN_de_Conexión_Dia'], "%Y-%m-%d").date()
                session_time    = row['Session_Time']
                username        = row['Usuario']
                mac_cliente     = row['MAC_Cliente']
                input_octets    = row['Input_Octects']
                output_octects  = row['Output_Octects']

                if inicio_conexion <= fecha_fin and fin_conexion >= fecha_inicio and is_weekend(max(inicio_conexion, fecha_inicio), min(fin_conexion, fecha_fin)): 
                    if not user_data.get(username):
                        user_data[username] = {'username': username, 'mac_cliente': {}, 'conexiones': [] } 
                    if user_data[username]['mac_cliente'].get(mac_cliente):
                        user_data[username]['mac_cliente'][mac_cliente].append(row['Session_Time'])
                    else:
                        user_data[username]['mac_cliente'][mac_cliente] = [row['Session_Time']]
                    io_octets = f"input_octets: {row['Input_Octects']:<10} | output_octects: {row['Output_Octects']:<10}"
                    user_data[username]['conexiones'].append(f"{row['Inicio_de_Conexión_Dia']} -> {row['FIN_de_Conexión_Dia']} => Total time: {row['Session_Time']+' hs':<8} | {io_octets}")
        print_data()



                    
if __name__ == '__main__':
    d = DataAnalyzer('/Users/matiasboldrini/Facu/Automatas_2023/Trabajo final/main/data/test_files/test_mati2.csv')
    # d = DataAnalyzer('/Users/matiasboldrini/Facu/Automatas_2023/Trabajo final/archivo.csv')