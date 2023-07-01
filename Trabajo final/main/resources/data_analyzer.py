import pathlib,csv
from datetime import datetime, timedelta

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
        # Alternativa:
        # {user_name: [total_session_time, MAC, days and total hours connected}
        """
        ID,ID_Sesion,ID_Conexión_unico,Usuario,IP_NAS_AP,Tipo__conexión,Inicio_de_Conexión_Dia,Inicio_de_Conexión_Hora,FIN_de_Conexión_Dia,FIN_de_Conexión_Hora,
        Session_Time,Input_Octects,Output_Octects,MAC_AP,MAC_Cliente,Razon_de_Terminación_de_Sesión,,
        603877,5AA0184E-000001CA,d6104707df0cd315,invitado-deca,192.168.247.11,Wireless-802.11,2019-02-07,19:46:08,2019-03-13,11:27:57,25,39517,505219,DC-9F-DB-12-F3-EA:HCDD,DC-BF-E9-1A-B5-D0,User-Request,,
        """
        def get_dates_range(fecha_inicio, fecha_fin):
            fechas_set = set()
            fecha_actual = fecha_inicio
            while fecha_actual <= fecha_fin:
                fechas_set.add(fecha_actual)
                fecha_actual += timedelta(days=1)
            return sorted(fechas_set)

        fecha_inicio = datetime(2023, 1, 20)
        fecha_fin = datetime(2023, 1, 30)
        fechas = get_dates_range(fecha_inicio, fecha_fin)
        print(fechas)

        def is_weekend(fecha_inicio, fecha_fin):
            delta = timedelta(days=1)
            fecha_actual = fecha_inicio
            while fecha_actual <= fecha_fin:
                dia_semana = fecha_actual.weekday()
                if dia_semana in [5, 6]:  # 5 representa sábado y 6 representa domingo
                    return True
                fecha_actual += delta
            return False
        metadata = {}
        fecha_creacion = datetime.strptime("2023-01-30", "%Y-%m-%d")
        with open(self.filePath) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                inicio_conexion = datetime.strptime('2023-01-20', "%Y-%m-%d")
                fin_conexion = datetime.strptime('2023-01-30', "%Y-%m-%d")
                session_time = row['Session_Time']
                username = row['Usuario']
                mac_cliente = row['MAC_Cliente']
                if not metadata.get(username):
                    metadata[username] = {'username': username, 'mac_cliente': mac_cliente, 'conexiones': []} 
                metadata[username]['conexiones'].append(f"{row['Inicio_de_Conexión_Dia']} -> {row['FIN_de_Conexión_Dia']}")
        for key in metadata.keys():
            print(f'{metadata[key]}\n')

if __name__ == '__main__':
    d = DataAnalyzer('/Users/matiasboldrini/Facu/Automatas_2023/Trabajo final/main/data/test_files/test_mati.csv')