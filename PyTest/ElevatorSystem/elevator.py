class Elevator:
    def __init__(self, elevator_id: str, current_floor=0):
        self.elevator_id = elevator_id 
        self.current_floor = current_floor
    
    def move_up(self):
        self.current_floor += 1
        return self.current_floor

    def move_down(self):
        self.current_floor -= 1
        return self.current_floor
                
    def stop_at_floor(self):
            print(f"Elevator_{self.elevator_id} stopped at Floor_{self.current_floor}")


class ElevatorSystem:
    def __init__(self):
        self.elevators = []
    
    def add_elevators(self, elevator):
        self.elevators.append(elevator)
    
    def handle_request(self, requested_floor):
        elevator = min(self.elevators, key=lambda e: abs(e.current_floor - requested_floor))

        print(f"Request recevied for floor {requested_floor}.")
        print(f"Assigning {elevator.elevator_id} to the request.")


        while elevator.current_floor != requested_floor:
            if elevator.current_floor < requested_floor:
                elevator.move_up()
            elif elevator.current_floor > requested_floor:
                elevator.move_down()
        
        elevator.stop_at_floor()


system = ElevatorSystem()

system.add_elevators(Elevator("1", 0))
system.add_elevators(Elevator("2", 3))

system.handle_request(2)
system.handle_request(5)