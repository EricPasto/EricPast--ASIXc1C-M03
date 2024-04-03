class MechanicalArm:
    def __init__(self):
        self.openAngle = 0.0
        self.altitude = 0.0
        self.turnedOn = False

    def toggle(self):
        self.turnedOn = not self.turnedOn

    def updateAltitude(self, increment):
        if self.turnedOn:
            self.altitude = max(0, self.altitude + increment)

    def updateAngle(self, increment):
        if self.turnedOn:
            self.openAngle = (self.openAngle + increment) % 360

    def __str__(self):
        return f"MechanicalArm{{openAngle={self.openAngle}, altitude={self.altitude}, turnedOn={self.turnedOn}}}"

def main():
    arm = MechanicalArm()
    print(arm)

    arm.toggle()
    arm.updateAltitude(3)
    print(arm)

    arm.updateAngle(180)
    print(arm)

    arm.updateAltitude(-3)
    print(arm)

    arm.updateAngle(-180)
    print(arm)

    arm.updateAltitude(6)
    print(arm)

    arm.toggle()
    print(arm)

if __name__ == "__main__":
    main()
