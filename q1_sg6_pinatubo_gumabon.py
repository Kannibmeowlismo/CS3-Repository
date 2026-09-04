Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Lab:
...     def __init__(self, room_number):
...         self.room_number = room_number
... 
... 
... class Technician:
...     def __init__(self, name):
...         self.name = name
...         self.assigned_lab = None
... 
...     def assign_lab(self, lab_obj):
...         self.assigned_lab = lab_obj
... 
... 
... chem_lab = Lab("203")
... ms_suarez = Technician("Ms. Suarez")
... ms_suarez.assign_lab(chem_lab)
... 
... print(ms_suarez.assigned_lab.room_number)
