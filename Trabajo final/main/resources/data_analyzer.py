import pathlib, datetime

class IncorrectFileFormat(Exception):
    pass

class DataAnalyzer():
    def __init__(self, filePath: str) -> None:
        """Class capable of validating a specific format csv file and 
        returning filtered data.\n
        filePath: Absolute path of the file"""
        self.filePath = filePath

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
                    startDate: datetime.datetime|None = None, 
                    endDate: datetime.datetime|None = None
                    ) -> dict[str, tuple[datetime.datetime, str, str, int, int]]:
        """Method designed to filter the users that have accessed the system on Non-working days. 
        Returns a dictionary {user_name: [total_session_time, most_used_MAC_NWD, most_used_MAC_WD, 
        total_input_octects, total_output_octects]}  *NWD = Non-working days * WD = Working days\n
        filter: if set to False method returns complete list of users\n
        startDate/endDate: if either of them is set to None, the method will take the most old or 
        new date available respectively."""
        pass