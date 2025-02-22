class CPU:

    def process(self):
        return "Processing..."


class Memory:

    def __init__(self):
        self._used_memory = 2000
        self._total_memory = 2000

    def check_memory(self):
        available_memory = self._total_memory - self._used_memory
        if available_memory > 2000:
            return True
        else:
            return False

    def store(self):
        return "Storing Files..."


class Storage:

    def __init__(self):
        self._space = 5000

    def save(self):
        if self._space > 1000:
            return "Files can be stored"
        else:
            return "Not enough storage"


class Computer:

    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.storage = Storage()

    def run(self):
        processing = self.cpu.process()

        if self.memory.check_memory():
            storing = self.memory.store()
            saving = self.storage.save()
        else:
            storing = "Not enough memory to store files"
            saving = "Storage operation aborted"

        return f"{processing}\n{storing}\n{saving}"


if __name__ == '__main__':

    my_computer = Computer()
    print(my_computer.run())
