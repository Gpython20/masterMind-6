import pygame
import random



#these are for whole board

class TurnBox:
    def __init__(self, display, rect, turn):
        self.display = display
        self.colors = {'black': (255, 255, 255), 'r': (255,0,0), 'y':(255,255,0), 'o':(255,150,0), 'g':(0,255,0), 'b':(0,0,255), 'p':(255,0,255)}
        self.rect = rect
        self.turn = turn
        self.selections = []

        #circles
        self.circles = []
        for i in range(4):
            x = 50*i
            y = self.turn + 45
            self.circles.append((x, y))


    def draw(self):
        pygame.draw.rect(self.display, self.colors['black'], self.rect)
        for circle in self.circles:
            #draw them
            pygame.draw.circle(self.display, (0,0,0), circle, 25) #color options needs to dynamically change
        counter = 0
        for i in self.selections:
            pygame.draw.circle(self.display, colors[i], self.circles[counter], 25)
            counter +=1


    def update_player_selections(self, playerSelection):
        self.selections.append(playerSelection)



class Game:

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((500, 1000))
        self.colors = ['r', 'y', 'o', 'g', 'b', 'p']
        self.turn = 0 #ten round, starting from zero
        self.board_turns = []
        self.is_game_true = True

    # 1. set initial combination
    def set_code(self):
        '''randomly selects secret code'''
        self.secret_code = []
        for i in range(4):
            a = random.choice(self.colors)
            self.secret_code.append(a)


    def draw_circle(self):
        pass

            # for turn in range(self.turn+1):
    # 3. draw new turn
    def draw_new_rect(self):
        #self.player_guess

        turnbox = TurnBox(self.display,  (0, self.turn*90, 500, 50), self.turn)

        self.board_turns.append(turnbox)
        for rectItem in self.board_turns:
            rectItem.draw()


    def player_guess_input(self):
        selections = []
        key = pygame.key.get_pressed()
        print(key)

    # 2. guessing function
    def guess_combo(self):
        #self.player_guess =[]
        self.draw_new_turn()
        self.player_guess_input()
        self.turn +=1

    def game_end(self):
        print('game over! you might have won, we havent coded that yet')
        self.is_game_true = False



    # 4. evaulate guess to initial combination

    def eval_guess(self):
        pass

    # 5. display update
    def update_board(self):
        pass

    def main_loop(self):
        # self.is_game_true = True
        while self.is_game_true:
            self.display.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.guess_combo()
            pygame.display.update()

            if self.turn == 9:
                self.game_end()




    def game_start(self):
        pygame.display.update()

        self.set_code()
        print(self.secret_code) #debug
        self.main_loop()


if __name__ =='__main__':
    master_mind = Game()
    master_mind.game_start()
