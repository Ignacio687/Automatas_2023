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
        self.user_data = {}
        #startDate = datetime.strptime("2003-01-01", "%Y-%m-%d")
        #endDate = datetime.strptime("2023-06-30", "%Y-%m-%d")
        #self.filterUsers(startDate=startDate, endDate=endDate)
    def __str__(self):
        user_data = self.user_data
        final_str = ''
        for key in user_data.keys():
            final_str += f"\n\n{'-'*35} MOSTRANDO DATOS DESDE {self.fecha_inicio} HASTA {self.fecha_fin} {'-'*35}\n"
            final_str += f"\n{key}:"
            final_str += f"\n\tUsername: {user_data[key]['username']} "
            mac_dict = user_data[key]['mac_cliente']
            connection_count = Counter(mac for mac in mac_dict for _ in mac_dict[mac])
            most_connected_mac = connection_count.most_common(1)[0][0]
            total_hours = {mac: sum(int(hour) for hour in mac_dict[mac]) for mac in mac_dict}
            mac_with_longest_duration = max(total_hours, key=total_hours.get)
            final_str += f"\n\tMost used mac adress: {most_connected_mac}"
            final_str += f"\n\tMost time connected mac {mac_with_longest_duration}"
            mac_keys = [i for i in mac_dict.keys()]
            # Dividir la lista en sublistas de 4 elementos
            sublists = [mac_keys[i:i+4] for i in range(0, len(mac_keys), 4)]
            # Unir cada sublista utilizando tabulaciones
            formatted_keys = '\n\t\t'.join(['\t'.join(sublist) for sublist in sublists])
            final_str += f'\n\tTotal Mac adress:\n\t\t{formatted_keys}'
            final_str += f"\n\tConexiones:"
            for i in user_data[key]['conexiones']:
                final_str += f"\n\t\t{i}"
        return final_str
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
                    startDate = None, 
                    endDate = None,
                    filter: bool = True, 
                    ):
        """Method designed to filter the users that have accessed the system on Non-working days. 
        Returns a dictionary {user_name: [total_session_time, most_used_MAC_NWD, most_used_MAC_WD, 
            , total_output_octects]}  *NWD = Non-working days * WD = Working days\n
        filter: if set to False method returns complete list of users\n
        startDate/endDate: if either of them is set to None, the method will take the most old or 
        new date available respectively."""

        if startDate == '':
            fecha_inicio = date(2000, 3, 27) # Fecha antigua para incluir todos los resultados
        else:
            fecha_inicio = startDate

        if endDate == '':
            fecha_fin = date.today()
        else:
            fecha_fin = endDate
    
        if fecha_fin < fecha_inicio:
            fecha_fin, fecha_inicio = fecha_inicio, fecha_fin
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin


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
            self.user_data = user_data

        #print_data()

if __name__ == '__main__':
    d = DataAnalyzer('/Users/matiasboldrini/Facu/Automatas_2023/Trabajo final/main/data/test_files/test_mati2.csv')
    # d = DataAnalyzer('/Users/matiasboldrini/Facu/Automatas_2023/Trabajo final/archivo.csv')