class Lights:

    def turn_on(self):
        return "Lights Turn On"

    def turn_off(self):
        return "Lights Turn Off"


class Thermostat:

    def increase_temp(self):
        return "Temperature increased"

    def decrease_temp(self):
        return "Temperature decreased"


class SecurityCamera:

    def __init__(self):
        self.intruder = False
        self.alarm = None

    def alert(self, alarm):
        if alarm == "Warning":
            self.intruder = True
            return "Intruder Alert! Alarm Triggered"
        return "No Activity Detected"

    def record(self):
        if self.intruder:
            return "Recording Suspicious Activity"
        return "Everything is normal"


class SmartHome:

    def __init__(self):
        self.lights = Lights()
        self.temperature = Thermostat()
        self.security_camera = SecurityCamera()


if __name__ == '__main__':

    home = SmartHome()
    print(home.lights.turn_on())
    print(home.lights.turn_off())

    print(home.temperature.increase_temp())
    print(home.temperature.decrease_temp())

    print(home.security_camera.record())

    print(home.security_camera.alert("Warning"))
    print(home.security_camera.record())
