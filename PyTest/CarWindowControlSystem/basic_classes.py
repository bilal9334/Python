class Window:
    def __init__(self, name: str):
        self.name = name
        self.state = "Closed"
    
    def set_state(self, state: str):
        self.state = state
    
    def __repr__(self):
        return f"Window({self.name}, State: {self.state})"


class Car:
    def __init__(self):
        self.windows = {
            "Front Left": Window("Front Left"),
            "Front Right": Window("Front Right"),
            "Rear Left": Window("Rear Left"),
            "Rear Right": Window("Rear Right"),
        }
    
    def get_window(self, name: str) -> Window:
        return self.windows.get(name)


class WindowController:
    def __init__(self, car: Car):
        self.car = car
    
    def open_window(self, name: str):
        window = self.car.get_window(name)
        if window:
            window.set_state("Open")
    
    def close_window(self, name: str):
        window = self.car.get_window(name)
        if window:
            window.set_state("Closed")


class CarWindowTestCase:
    def __init__(self):
        self.test_steps = []
    
    def append(self, step_name: str, args: list):
        self.test_steps.append((step_name, args))
    
    def run(self):
        print("Running Test Case: ")
        for step, args in self.test_steps:
            print(f"Step: {step} - Args: {args}")


def create_test_cases(car: Car, controller: WindowController) -> list[CarWindowTestCase]:
    test_cases = []

    # Define test steps for each window
    for window_name in car.windows.keys():
        test_case = CarWindowTestCase()
    
        # Reset All windows
        test_case.append("Reset Windows", [])

        # Open Windows
        test_case.append("Open Window", [window_name])
        controller.open_window(window_name)

        # Close Windows
        test_case.append("Close Window", [window_name])
        controller.close_window(window_name)

        test_cases.append(test_case)
    return test_cases

# Running the test case
car = Car()
controller = WindowController(car)
test_cases = create_test_cases(car, controller)

for tc in test_cases:
    tc.run()