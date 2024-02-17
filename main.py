
import pyodbc


class Calendar:
    def __init__(self, file_path='baza.txt'):
        self.file_path = file_path
        self.whole_dict = {}
        self.emptiness = -99

        with open(self.file_path, 'r') as file:
            instance = file.read()

        if not(instance):
            self.emptiness = 1

        for i in instance.split("\n"):
            one = i.split("&&&!&&&")
            if len(one) > 1:
                key, values = one[0], one[1]
                lists = values.split("%/end/%")
                self.whole_dict[key] = lists

        input_start = '0'
        while input_start != '99':
            input_start = input("Read/add/del/exit (1,2,99): ")
            if input_start == '1':
                self.read_calendar()
            elif input_start == '2':
                self.add_to_calendar()
            elif input_start == '777':
                self.delete_calendar()
            elif input_start == '99':
                print("Exiting calendar...")
            else:
                print("Invalid choice.")


    def read_calendar(self):
        print("\n\n")

        if self.emptiness == 1:
            print("Calendar is empty :)")
        else:
            for day, value in self.whole_dict.items():
                print(day, value)
    
        print("\n\n")
        
    def add_to_calendar(self):
        day = input("Input day:")
        desc = input("Description:")
        
        old_desc = self.whole_dict[day] if (day in self.whole_dict) else []
        old_desc.append(desc)
        self.whole_dict[day] = old_desc

        self.save_calendar()
        
        self.read_calendar()

    def save_calendar(self):
        with open(self.file_path, 'w') as file:
            for key, value in self.whole_dict.items():
                file.write(f"{key}&&&!&&&{value}\n")

        with open(self.file_path, 'w') as file:
            for key, values in self.whole_dict.items():
                file.write(f"{key}&&&!&&&{values[0]}")
                for value in values[1:]:
                    file.write(f"%/end/%{value}")  # Write subsequent values with separator
                file.write("\n")
        self.emptiness = 0


    def delete_calendar(self):
        self.whole_dict = {}
        with open(self.file_path, 'w') as file:
            file.write("")
        self.emptiness = 1

# Example usage:

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=your_server_name;'
    'DATABASE=your_database_name;'
    'UID=your_username;'
    'PWD=your_password;'
)


#calendar_instance = Calendar(file_path='baza.txt')
