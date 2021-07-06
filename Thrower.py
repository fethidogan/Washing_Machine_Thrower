import pygame, sys, math, random
clock = pygame.time.Clock()
#Screen
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load("background.png")

class Player:
    def __init__(self):
        self.playerimg = pygame.image.load("idle.png")
        self.playerimg = pygame.transform.scale(self.playerimg,(150,150))
        self.player_x = 50
        self.player_y = 400
        self.player_velocity = 3
        self.is_jump = False
        self.jump_count = 10

    # Move player and limit boundry
    def move_player_in_screen(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.player_x < 720:
            self.player_x += 3
        if keys[pygame.K_LEFT] and self.player_x > 0:
            self.player_x -= 3

    # Jump
    def player_jump(self):
        keys = pygame.key.get_pressed()
        if not self.is_jump:
            if keys[pygame.K_SPACE]:
                self.is_jump = True
        else:
            if self.jump_count >= -10:
                # jump formula
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.player_y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 10

class Alien:
    def __init__(self):
        self.alienimg = []
        self.alien_pos_x = []
        self.alien_pos_y = []
        self.num_of_aliens = 3
        self.alien_pos = 450
        self.alien_velocity = 1
        self.score = 0
        self.gameover = False

    def generate_aliens(self):
        for i in range(self.num_of_aliens):
            self.alienimg.append(pygame.image.load("alien.png"))
            self.alien_pos_x.append(random.randint(750, 900))
            self.alien_pos_y.append(self.alien_pos)
            self.alien_pos -= 90

        for i in range(alien.num_of_aliens):
            alien.alien_pos_x[i] -= alien.alien_velocity
            screen.blit(alien.alienimg[i], (alien.alien_pos_x[i], alien.alien_pos_y[i]))

        for i in range(alien.num_of_aliens):
            # 2D distance formula --> square root ( (x2-x1)**2 + (y2-y1)**2 )
            distance = math.sqrt((alien.alien_pos_x[i] - machine.washing_machine_x) ** 2 + (alien.alien_pos_y[i] - machine.washing_machine_y) ** 2)
            player_distance = math.sqrt((alien.alien_pos_x[i] - player.player_x) ** 2 + (alien.alien_pos_y[i] - player.player_y) ** 2)

            # if player's position and washing machine position is lesser than 55
            if player_distance < 55:
                self.gameover = True

            # if machine throw is True than kill aliens
            if machine.throw is True:
                if distance < 40:
                    alien.alien_pos_y[i] = -500
                    screen.blit(alien.alienimg[i],(alien.alien_pos_x[i],alien.alien_pos_y[i]))
                    self.score += 1

    # if score hits 3 regenerate aliens at random position between 750-900
    def regenerate_aliens(self):
        if alien.score // 3 == 1:
            self.score = 0
            self.alien_velocity += 0.4
            self.alienimg = []
            self.alien_pos_x = []
            self.alien_pos_y = []
            self.alien_pos = 450
            for i in range(self.num_of_aliens):
                self.alienimg.append(pygame.image.load("alien.png"))
                self.alien_pos_x.append(random.randint(750, 900))
                self.alien_pos_y.append(self.alien_pos)
                self.alien_pos -= 90

    # if alien's position is lesser than 20
    def alien_wins(self):
        for i in range(self.num_of_aliens):
            if self.alien_pos_x[i] < 20:
                pygame.quit()
                sys.exit()
# Objects
player = Player()
alien = Alien()
class Machine:
    def __init__(self):
        self.washing_machine = pygame.image.load("machine.png")
        self.washing_machine_x = player.player_x + 40
        self.washing_machine_y = player.player_y + 50
        self.throw = False

    # throw machine
    def throw_machine(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.throw = True

        # if machine is not thrown stick with the player
        if not self.throw:
            self.washing_machine_x = player.player_x + 40
            self.washing_machine_y = player.player_y + 50

        # if machine is thrown move the machine on x axis
        else:
            self.washing_machine_x += 20
            if self.washing_machine_x > 850:
                self.washing_machine_x = player.player_x + 40
                self.washing_machine_y = player.player_y + 50
                self.throw = False

machine = Machine()
def main_loop():
    # Main game loop
    while not alien.gameover:
        # Fps
        clock.tick(80)

        # Handling Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # screen blits
        screen.blit(background, (0, 0))
        screen.blit(machine.washing_machine, (machine.washing_machine_x, machine.washing_machine_y))
        screen.blit(player.playerimg, (player.player_x, player.player_y))

        # Class functions
        player.move_player_in_screen()
        player.player_jump()
        alien.generate_aliens()
        machine.throw_machine()
        alien.regenerate_aliens()
        alien.alien_wins()

        # refresh window
        pygame.display.update()

main_loop()
