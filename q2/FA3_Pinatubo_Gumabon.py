from abc import ABC, abstractmethod

class Sensor(ABC) :
    @abstractmethod
    def get_reading(self):
        pass
    
class PHSensor(Sensor):
    def get_reading(self):
        return "7.2 pH"
        
class TempSensor(Sensor):
    def get_reading(self):
        return "24.5°C" 

my_phsensor = PHSensor()
my_tempsensor = TempSensor()

print("--- Lab Inventory System ---")
print("[pH Sensor] Reading:", my_phsensor.get_reading(), "(neutral)")
print("[Temperature Sensor] Reading:", my_tempsensor.get_reading())
print("----------------------------")

