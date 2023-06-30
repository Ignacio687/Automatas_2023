from .data_analyzer import DataAnalyzer
import time

class UserInterface():
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        print("The function needs the location of the file to analyze.")
        while True:
            try:
                path = input('Path of the file: ')
                open(path)
                data = DataAnalyzer(path)
                break
            except FileNotFoundError:
                print("File not found. Try again.")

        while True:
            match input('''
What de you want to do?:
1. Search for errors in the file
2. Remove lines of the file
3. Filters Users that have accessed the system on Non-working Days}
'''):
                
                case '1':
                    errors = data.validate()
                    print(errors)
                
                case '2':
                    print(data.generateFile(path))
                    
                case '3':
                    pass

                case 'exit':
                    break

                case _:
                    print("Invalid Input. Be carefour, only write numbers for the options, or exit if you eant to leave")
                    time.sleep(3)
