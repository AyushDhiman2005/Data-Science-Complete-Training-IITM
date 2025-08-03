from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self,speed):
        super().__init__()
        self.top_Speed = speed

    @abstractmethod
    def move(self):
        print(f"moving.... with speed: {self.top_Speed}")

class LandTransport(Transport):
    def __init__(self, speed):
        super().__init__(speed)

    def move(self):
        print(f"Car is moving with speed {self.top_Speed}")

class WaterTransport(Transport):
    def __init__(self, speed):
        super().__init__(speed)

    def move(self):
        print(f"Ship is moving with speed {self.top_Speed}")

class AirTransport(Transport):
    def __init__(self, speed):
        super().__init__(speed)

    def move(self):
        print(f"Aircraft is moving with speed {self.top_Speed}")

class Ampihbious(Transport):
    def __init__(self, speed):
        super().__init__(speed)

    def move(self):
        print(f"Amphibious ship is moving with speed {self.top_Speed}")

tata_Nexon = LandTransport(200)
tata_Nexon.move()

INS_Vishakhapatnam = WaterTransport(120)
INS_Vishakhapatnam.move()

GlobeMaster= AirTransport(1120)
GlobeMaster.move()

INS_Jalashwa=Ampihbious(220)
INS_Jalashwa.move()
