import arcade
import random
import os


char1 = arcade.load_texture("goku.png")
char2 = arcade.load_texture("vegeta.png")
back = arcade.load_texture("BACKGROUNG.jpeg")

vs = arcade.load_texture("are-you.jpg")
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
MARGIN = 5
boxSize = SCREEN_HEIGHT // 10

class Game(arcade.View):
    def __init__(self):
        super().__init__()
        self.board = []
        self.player1 = 1
        self.player2 = 2
        self.turn = "player1"
        self.win = "0"
        self.state = "GameMenu"
        self.player2Score = 0
        self.player1Score = 0
        self.initilizeBoard(10, 10)
        self.Score_Checker = 0
        self.Human_Sore_Record = 0
        self.player2_Score_Record = 0


    def initilizeBoard(self, rows, cols):
        for i in range(cols):
            tempBoard = []
            for i in range(0, rows):
                tempBoard.append(0)
            self.board.append(tempBoard)
        self.board[0][9] = 2
        self.board[9][0] = 1


    def on_key_press(self, key, modifiers):
        if self.state == "GameMenu":
            if key:
                self.player1 = 1
                self.player2 = 2
                self.state = "GameOn"

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        

    def draw_horizental(self, grid_size, box_size, pixel):
        temp = box_size
        for i in range(1, grid_size):
            arcade.draw_line(0, box_size, (box_size*grid_size), box_size,  arcade.color.WHITE, pixel)
            box_size = box_size + temp 


    def draw_vertical(self, grid_size, box_size, pixel):
        temp = box_size
        for i in range(1, grid_size):
            arcade.draw_line(box_size, 0, box_size, (box_size*grid_size),  arcade.color.WHITE, pixel)
            box_size = box_size + temp 
 
    def reset(self):
            self.board = []
            self.player1 = 1
            self.player2 = 2
            self.turn = "player1"
            self.win = "0"
            self.state = "GameMenu"
            self.player2Score = 0
            self.player1Score = 0
            self.initilizeBoard(10, 10) 

    def on_draw(self):
        arcade.start_render()
        if self.state == "GameMenu":
            arcade.draw_text("Welcome to Wandering in the woods game", 100, 300, arcade.color.RED,font_name="Algerian", font_size=28)
            arcade.draw_text("Select any mode to enter the game", 480, 250, arcade.color.RED,font_name="Algerian", font_size=30, anchor_x="center")

            arcade.draw_text("K-2 Grades", 500, 400, arcade.color.RED,font_name="Algerian", font_size=28, anchor_x="center")           
            arcade.draw_text("3-5 Grades", 500, 450, arcade.color.RED,font_name="Algerian", font_size=28, anchor_x="center")           
            arcade.draw_text("6-8 Grades", 500, 500, arcade.color.RED,font_name="Algerian", font_size=28, anchor_x="center")
            self.__init__()

        elif self.state == "GameOn":
            arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,back)

            
            
            self.draw_horizental(10, boxSize, 4)
            self.draw_vertical(10, boxSize, 4)
            arcade.draw_lrwh_rectangle_textured(600, 0,1000, SCREEN_HEIGHT,back)
            arcade.draw_text("Wandering in the woods", 630, 515, arcade.color.YELLOW,font_name="Broadway",font_size=18)
            arcade.draw_text(" player1 Score = " + str(self.player1Score), 690, 450,arcade.color.LIME,font_name="Broadway",font_size=18)
            arcade.draw_text(" player2 Score = " + str(self.player2Score), 690, 400,arcade.color.LIME,font_name="Broadway", font_size=18)
            arcade.draw_lrwh_rectangle_textured(600,80, 400, 300, vs)
            Y = boxSize
            temp = 0
            #print(self.board)
            for row in range (0, len(self.board)):
                X = 0
                for col in range (0, len(self.board)):
                    if self.board[row][col] == 1 : 
                        arcade.draw_lrwh_rectangle_textured( X+MARGIN, SCREEN_HEIGHT-Y, boxSize-MARGIN, boxSize-MARGIN, char1)
                    
                    elif self.board[row][col] == 2 : 
                        arcade.draw_lrwh_rectangle_textured( X+MARGIN, SCREEN_HEIGHT-Y, boxSize-MARGIN, boxSize-MARGIN, char2)
                    
            
                    
                    X += boxSize
                temp += 1
                Y += boxSize
                

        elif self.state == "GameOver":
            if self.player1Score > self.player2Score:
                self.win = "player1"
            elif self.player1Score < self.player2Score:
                self.win = "player2"
            elif self.player1Score == self.player2Score:
                self.win = "draw"

            if self.win == "player1":
                arcade.draw_text("Congratulations, Human has Won !", 100, 300, arcade.color.RED,font_name="Algerian", font_size=35)
                arcade.draw_text("Click to continue", 480, 250, arcade.color.RED,font_name="Algerian", font_size=30, anchor_x="center")
              

            elif self.win == "player2":
                arcade.draw_text("Congratulation player2 has Won :)", 100, 300, arcade.color.RED,font_name="Algerian",font_size=35)
                arcade.draw_text("Click to continue", 480, 250, arcade.color.RED,font_name="Algerian", font_size=20, anchor_x="center")
            

            elif self.win == "draw":
                arcade.draw_text("It's a draw..", 350, 300, arcade.color.RED,font_name="Algerian", font_size=35)
                arcade.draw_text("Click to continue", 480, 250, arcade.color.RED,font_name="Algerian", font_size=30, anchor_x="center")
            

    def move_player(self, player, dx, dy):
        x, y = self.getplayerPosition(player)
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < 10 and 0 <= new_y < 10 and self.board[new_x][new_y] in [0, 22, player]:
            self.board[x][y] = 11 if player == 2 else 22
            self.board[new_x][new_y] = player
            if player == 1:
                self.player1Score += 1
            else:
                self.player2Score += 1

    def LSlip(self, Player):
        self.move_player(Player, 0, -1)

    def RSlip(self, Player):
        self.move_player(Player, 0, 1)

    def DownSlip(self, Player):
        self.move_player(Player, 1, 0)

    def UPSlip(self, Player):
        self.move_player(Player, -1, 0)

    def getplayerPosition(self, player):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if self.board[i][j] == player:
                    return i, j
        

    #Function to check if we are stuck
    def StuckCondition(self):
        if self.Human_Sore_Record == self.player1Score or self.player2_Score_Record == self.player2Score:
            self.Score_Checker += 1
        else:
            self.Human_Sore_Record , self.player2_Score_Record, self.Score_Checker = self.player1Score , self.player2Score , 0
        if self.Score_Checker == 5:
            self.state = "GameOver"

    def calcRowCol(self, x, y):
        x1 = y // boxSize
        y1 = x // boxSize
        return 9-x1, y1

    #To check the validity of the click
    def checkValidClick(self, x, y):
        if 0 <= x <= SCREEN_WIDTH and 0 <= y <= SCREEN_HEIGHT:
            return True
        elif 0 > x > SCREEN_WIDTH and 0 > y > SCREEN_HEIGHT:
            return False
    #To find the points where we are currently standing
    def getplayer1Position(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if self.board[i][j] == 2:
                    return i,j


    def getplayer2Position(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                if self.board[i][j] == 1:
                    return i,j

    #Heurestic Funtion which causes the ai agent to move intelligently
    def player2Turn(self):
        self.MoveRightChance = 0
        self.MoveLeftChance = 0
        self.MoveDownChance = 0
        self.MoveUpChance = 0
        self.NoOfOnes = []
        x, y = self.getplayer2Position()
        for a in range(0,10):
            if y+a <= 9:
                if self.board[x][y+a] == 22:
                    break
                if self.board[x][y+a] == 0:
                    self.MoveRightChance += 1 
            else:
                break
        self.NoOfOnes.append(self.MoveRightChance)
        for b in range(0,10): 
            if y-b>=0:
                if self.board[x][y-b] == 22:
                    break
                if self.board[x][y-b] == 0:
                    self.MoveLeftChance += 1
            else:
                break
        self.NoOfOnes.append(self.MoveLeftChance)
        for c in range(0,10):
            if x+c<=9:
                if self.board[x+c][y] == 22:
                    break
                if self.board[x+c][y] == 0:
                    self.MoveDownChance += 1
            else:
                break
        self.NoOfOnes.append(self.MoveDownChance)
        for d in range(0,10):   
            if x-d>=0:
                if self.board[x-d][y] == 22:
                    break
                if self.board[x-d][y] == 0:
                    self.MoveUpChance += 1
            else:
                break
        self.NoOfOnes.append(self.MoveUpChance)

        self.NoOfOnes.sort()

        self.maxVal = self.NoOfOnes[3]  

        if x != 9 and y != 9:
            if self.board[x][y+1] != 11 and self.board[x][y-1] != 11 and self.board[x+1][y] != 11 and self.board[x-1][y] != 11:
                if self.maxVal == self.MoveRightChance and y != 9 and self.board[x][y+1] == 11:
                    self.maxVal = self.NoOfOnes[2]
                elif self.maxVal == self.MoveLeftChance and y != 0 and self.board[x][y-1] == 11:
                    self.maxVal = self.NoOfOnes[2]
                elif self.maxVal == self.MoveDownChance and x != 9 and self.board[x+1][y] == 11:
                    self.maxVal = self.NoOfOnes[2]
                elif self.maxVal == self.MoveUpChance and x != 0 and self.board[x-1][y] == 11:
                    self.maxVal = self.NoOfOnes[2]

        if self.maxVal == self.MoveRightChance and y != 9:
            # print("self.MoveRightChance")
            if  self.board[x][y+1] == 11:
                self.RSlip(2)
            else:
                if  self.board[x][y+1] == 22 or self.board[x][y+1] == 2:
                    return
                else:
                    self.board[x][y+1], self.board[x][y] = 1, 11
                    self.player2Score += 1

        elif self.maxVal == self.MoveLeftChance and y != 0:
            # print("self.MoveLeftChance")
            if  self.board[x][y-1] == 11:
                self.LSlip(2)
            else:
                if self.board[x][y-1] == 22 or self.board[x][y-1] == 2:
                    return
                else:
                    self.board[x][y-1], self.board[x][y] = 1, 11
                    self.player2Score += 1

        elif self.maxVal == self.MoveDownChance and x != 9:
            # print("MoveDownChance")
            if  self.board[x+1][y] == 11:
                self.DownSlip(2)
            else:
                if self.board[x+1][y] == 22 or self.board[x+1][y] == 2:
                    return
                else:
                    self.board[x+1][y], self.board[x][y] = 1, 11
                    self.player2Score += 1

        elif self.maxVal == self.MoveUpChance and x != 0:
            # print("self.MoveUpChance")
            if  self.board[x-1][y] == 11:
                self.UPSlip(2)
            else:
                if self.board[x-1][y] == 22 or self.board[x-1][y] == 2:
                    return
                else:
                    self.board[x-1][y], self.board[x][y] = 1, 11
                    self.player2Score += 1
        self.turn = "player1"

    def on_mouse_press(self, x, y, _button, _modifiers):
        if self.state == "GameOn":
            row, col = self.calcRowCol(x,y)
            if self.checkValidClick(x, y):
                # Now check weather the clicked space is next to the Position of player
                if self.turn == "player1":
                    x,y = self.getplayer1Position()
                    if   row==x and y+1==col and self.board[row][col]==0 or self.board[row][col] == 22 and row==x and y+1==col: #Right Move
                        if self.board[row][col] == 22:
                            self.RSlip(1)
                        else:
                            self.board[row][col], self.board[x][y] = 2, 22
                          #  self.turn = "player2"
                            self.player1Score += 1
                        
                    elif row==x and y-1==col and self.board[row][col]==0 or self.board[row][col] == 22 and row==x and y-1==col: #Left Move
                        if self.board[row][col] == 22:
                            self.LSlip(1)
                        else:
                            self.board[row][col], self.board[x][y] = 2, 22
                          #  self.turn = "player2"
                            self.player1Score += 1
                    elif x+1==row and y==col and self.board[row][col]==0 or self.board[row][col] == 22 and x+1==row and y==col: #down Move
                        if self.board[row][col]==22:
                            self.DownSlip(1)
                        else:
                            self.board[row][col], self.board[x][y] = 2, 22
                        #    self.turn = "player2"
                            self.player1Score += 1
                    elif x-1==row and y==col and self.board[row][col]==0 or self.board[row][col]==22 and x-1==row and y==col: #Up Move
                        if self.board[row][col]==22:
                            self.UPSlip(1)
                        else:
                            self.board[row][col], self.board[x][y] = 2, 22
                         #   self.turn = "player2"
                            self.player1Score += 1
                    else:
                     #   self.turn = "player2"
                        print("INVALID CLICK, player1 TURN LOST !!!!")
                self.player2Turn()
                self.StuckCondition()
                self.score()
            

        elif self.state == "GameOver":
            self.board = []
            self.player1 = 1
            self.player2 = 2
            self.turn = "player1"
            self.win = "0"
            self.state = "GameMenu"

    def score(self):

        if self.player1Score > 49 or self.player2Score > 49:
            self.state = "GameOver"
            if self.player1Score > self.player2Score:
                self.win = "player1"
            elif self.player1Score < self.player2Score:
                self.win = "player2"
        elif  self.player1Score == 49 and self.player2Score == 49:
            self.state = "GameOver"
            self.win = "draw"

         
        

if __name__ == "__main__":
    window = arcade.Window(SCREEN_HEIGHT+400, SCREEN_WIDTH, "wandering in the woods game")
    game_view = Game()
    window.center_window()
    window.show_view(game_view)
    arcade.run()