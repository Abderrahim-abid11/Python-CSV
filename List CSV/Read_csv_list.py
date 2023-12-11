import csv

class Csv:
    data = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Csv.data.append(self)
    @classmethod
    def read_csv(cls, filename):
        with open(filename, newline='') as file:
            reade = csv.DictReader(file)
            items = list(reade)
        for row in items:
            Csv(
                    name=row.get('name'),
                    age=int(row.get('age'))
                    )
    def __repr__(self):
        return f"'{self.name}', '{self.age}'"

filename = str(input("Enter File Name : "))
Csv.read_csv(filename)
infos = Csv.data
for info in infos:
    print(info)

