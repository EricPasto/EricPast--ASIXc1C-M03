class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.velocity = 1

    def move_up(self):
        self.y += self.velocity

    def move_down(self):
        self.y -= self.velocity

    def move_right(self):
        self.x += self.velocity

    def move_left(self):
        self.x -= self.velocity

    def accelerate(self):
        if self.velocity < 10:
            self.velocity += 0.5

    def decelerate(self):
        if self.velocity > 0:
            self.velocity -= 0.5

    def position(self):
        print(f"La posició del robot és ({self.x}, {self.y})")

    def show_velocity(self):
        print(f"La velocitat del robot és {self.velocity}")

def main():
    robot = Robot()
    actions = {
        'DALT': robot.move_up,
        'BAIX': robot.move_down,
        'DRETA': robot.move_right,
        'ESQUERRA': robot.move_left,
        'ACCELERAR': robot.accelerate,
        'DISMINUIR': robot.decelerate,
        'POSICIO': robot.position,
        'VELOCITAT': robot.show_velocity,
        'END': lambda: None  # Funció lambda buida per indicar finalització
    }

    print("Benvingut al programa del robot!\n")
    ended = False
    while not ended:
        action = input("> ").strip().upper()
        if action in actions:
            actions[action]()
            if action == 'END':
                ended = True
        else:
            print("Acció no vàlida. Intenta-ho de nou.")

if __name__ == "__main__":
    main()

