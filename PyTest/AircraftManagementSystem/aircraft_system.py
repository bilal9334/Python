class Aircraft:
    def __init__(self, aircraft_id: str, altitude=0):
        self.aircraft_id = aircraft_id
        self.status = "on ground"
        self.altitude = altitude
    
    def take_off(self, target_altitude: int):
        if self.status == "on ground" and target_altitude > 0:
            self.status = "ascending"
            print(f"Aircraft_{self.aircraft_id} is taking off and ascending to {target_altitude} feet.")
            self.altitude = target_altitude

        elif self.status == "ascending" and target_altitude > self.altitude:
            self.altitude = target_altitude
            self.status = "cruising"
            print(f"Aircraft_{self.aircraft_id} has reached cruising altitude: {self.altitude} feet.")

        else:
            print(f"Aircraft_{self.aircraft_id} cannot take off in its current status: {self.status}.")
    
    def descend(self, target_altitude: int):
        if self.status == "cruising":
            self.status = "descending"
            print(f"Aircraft_{self.aircraft_id} has started to descend and has reached an altitude: {target_altitude} feet.")

            if target_altitude == 0:
                self.status = "on ground"   
                print(f"Aircraft_{self.aircraft_id} has landed successfully.")
            else:
                self.altitude = target_altitude
                print(f"Aircraft_{self.aircraft_id} is now at {self.altitude} feet.")

        elif self.status == "on ground":
            print(f"Aircraft_{self.aircraft_id} is already on the ground. Cannot descend further.")
        
        elif self.status == "ascending":
            print(f"Aircraft_{self.aircraft_id} cannot descend while ascending")
        else:
            print(f"Aircraft_{self.aircraft_id} is still descending.")
    
    def get_status(self):
        return self.status


# class AircraftTestCase:
#     def __init__(self):
#         self.test_steps = []
    
#     def append(self, step_name: str, args: list):
#         self.test_steps.append((step_name, args))
    
#     def run(self):
#         print("Running Test Case: ")
#         for step, args in self.test_steps:
#             print(f"Step: {step} - Args: {args}")


# def create_test_cases(aircraft: Aircraft) -> list[AircraftTestCase]:
#     test_cases = []

#     # Define test steps
#     test_case = AircraftTestCase()

#     # Take Off
#     aircraft_name = aircraft.aircraft_id
#     test_case.append("Take Off", [aircraft_name])
#     aircraft.take_off(40000)

#     # Descend
#     test_case.append("Descend", [aircraft_name])
#     aircraft.descend(30000)

#     test_cases.append(test_case)

#     return test_case



# # Checking the program
# aircraft = Aircraft("A320-001")
# test_cases = create_test_cases(aircraft)

# test_cases.run()