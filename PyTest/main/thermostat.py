class SmartThermostat:

    def __init__(self, temperature):
        if 10 <= temperature <= 30:
            self.temperature = temperature
        else:
            raise ValueError("Temperature must be between 10 and 30 degrees")
        
    def set_temperature(self, temperature):
        if 10 <= temperature <= 30:
            self.temperature = temperature
        else:
            raise ValueError("Temperature must be between 10 and 30 degrees")
    
    def increase_temperature(self, value):
        new_temp = self.temperature + value
        if new_temp > 30:
            print("Temperatue cannot exceed 30 degrees")
        else:
            self.temperature = new_temp
    
    def decrese_temperature(self, value):
        new_temp = self.temperature - value
        if new_temp < 10:
            print("Temperature cannot go below 10 degrees")
        else:
            self.temperature = new_temp