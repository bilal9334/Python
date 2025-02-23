class Camera:

    def take_picture(self):
        return "Taking Picture..."


class Battery:

    def __init__(self):
        self.power = 50

    def check_battery(self):
        if self.power < 20:
            return "Low Battery! Please re-charge."
        return f"Battery is sufficient: {self.power}%"

    def charge_battery(self):
        if self.power < 100:
            self.power = 100
            return "Battery Fully Charged"
        return "Battery is already full"


class Screen:

    def __init__(self, battery):
        self.battery = battery

    def display_screen(self):
        if self.battery.power < 10:
            return "Low Battery! Can not open screen."
        return "Screen Visible"


class Phone:

    def __init__(self):
        self.camera = Camera()
        self.battery = Battery()
        self.screen = Screen(self.battery)

    def run(self):
        if self.battery.power < 10:
            return "Error! Battery low"

        self.battery.power -= 15

        open_screen = self.screen.display_screen()
        open_camera = self.camera.take_picture()
        return f"{open_screen} | {open_camera} | Picture Taken"


if __name__ == '__main__':
    phone = Phone()

    print(phone.battery.check_battery())
    print(phone.run())
    print(phone.battery.check_battery())
    print(phone.run())
    print(phone.battery.check_battery())
    print(phone.battery.charge_battery())
    print(phone.battery.check_battery())
    print(phone.run())
    print(phone.battery.check_battery())
    print(phone.run())
