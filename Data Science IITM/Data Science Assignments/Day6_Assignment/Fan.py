

class Fan():

    #Speed variable
    def __init__(self):
        self.__fan_speed =0

    def get_current_Speed(self):
        print(f"Current Fan speed Level = {self.__fan_speed}\n")

    def turn_on(self):
        __fan_speed=1
        print(f"\nFan is running at speed Level= {__fan_speed}")
    def turn_off(self):
        self.__fan_speed=0
        print("\nFan is turned off!")
        print(f"Current Fan speed Level = {self.__fan_speed}\n")
    def increase_speed(self,rate):
        if self.__fan_speed >=0 and self.__fan_speed<5 and self.__fan_speed+rate<6:
            self.__fan_speed = self.__fan_speed+rate
            print(f"\nIncreasing fan speed level from {self.__fan_speed} to {self.__fan_speed+rate}")
        elif self.__fan_speed<5 and self.__fan_speed+rate>5:
            print(f"Cannot increase speed from {self.__fan_speed} to {self.__fan_speed+rate}")
        else:
            print("Speed Level, not available!")
        print(f"Current Fan speed Level = {self.__fan_speed}\n")
    def decrease_speed(self,rate):
        if self.__fan_speed==0:
            print(f"Fan is at lowest speed ={self.__fan_speed}")
        elif self.__fan_speed>0 and self.__fan_speed-rate<0:
            print(f"Cannot decrease speed from {self.__fan_speed} to {self.__fan_speed-rate}")
        elif self.__fan_speed>0 and self.__fan_speed<6 and self.__fan_speed-rate>0:
            print(f"\nDeccreasing fan speed level from {self.__fan_speed} to {self.__fan_speed-rate}")
            self.__fan_speed = self.__fan_speed-rate
        print(f"Current Fan speed Level = {self.__fan_speed}\n")
a=Fan()
a.turn_on()
a.increase_speed(3)
a.decrease_speed(2)
a.increase_speed(5)
a.decrease_speed(6)
a.turn_off()