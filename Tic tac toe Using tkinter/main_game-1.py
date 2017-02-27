from tkinter import Frame, Canvas, Label, Button, LEFT,RIGHT, ALL, Tk
from random import randint
from tkinter import messagebox
import sqlite3

class Player:
    """Player class to store players information"""


    def __init__(self,data,id):
        """Constructor to initialize the values """
        #fetch the data from the database and store in variable then store in respective variables.
        data1 = data.get_player_data(id)
        self.name = data1[1]
        self.playing_symbol = data1[2]
        self.id = data1[0]
        self.stats = {'win':0,'lose':0,'draw':0}
        self.stats['win'] = data1[3]
        self.stats['lose'] = data1[5]
        self.stats['draw'] = data1[4]

    def set_stats(self,x,y,z,data):
        """function to update the statistics of the games that are played"""
        self.stats['win'] += x
        self.stats['lose'] += y
        self.stats['draw'] += z
        #call functtion to update database
        data.save_player_data(self.id,self.stats['win'],self.stats['lose'],self.stats['draw'])

    def get_score(self):
        """function to calculate the score on the basis of win, lose and draw"""
        return (self.stats['win'] * 2 + self.stats['draw'] - self.stats['lose'])

    def __lt__(self,other):
        """functin to check whose score is greater or less"""
        if self.get_score() < other.get_score():
            return True
        else:
            return False

class Deck:
    """This class is to maintan the game board information"""
    board = ['0','1','2','3','4','5','6','7','8']               # list that contains the values on the board. Initially all values are set to be the position number
    player1choices = []                                 #list to keep track of players inputs
    player2choices = []

    def __init__(self,canvas):
        """Creates the board"""
        canvas.create_rectangle(0,0,300,300, outline="black")
        canvas.create_rectangle(100,300,200,0, outline="black")
        canvas.create_rectangle(0,100,300,200, outline="black")

class TicTacToe:

    def __init__(self,root):
        """constructor to initialise variables and create board"""

        self.root = root
        self.data = DataAccessLayer()
        self.player1 = Player(self.data,2)
        self.player2 = Player(self.data,1)
        self.counter = 0
         #master frame
        self.frame = Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        #frame to contain the labels
        self.framea=Frame(self.frame)
        self.framea.pack(fill="both", expand=True, )
        msg1 = self.player1.name + "\n" + "  " +str(self.player1.get_score())
        self.lbl_player1_score=Label(self.framea, text=msg1, height=3, bg='black', fg='blue')
        self.lbl_player1_score.pack(fill="both", expand=True, side = LEFT)
        msg2 = "Game Number \n" + str(self.counter)
        self.lbl_game_counter=Label(self.framea, text=msg2, height=3, bg='black', fg='blue')
        self.lbl_game_counter.pack(fill="both", expand=True, side = LEFT)
        msg3 = self.player2.name + "\n" + "  " +str(self.player2.get_score())
        self.lbl_player2_score=Label(self.framea, text=msg3, height=3, bg='black', fg='blue')
        self.lbl_player2_score.pack(fill="both", expand=True, side = LEFT)

        #canvas where the game is played on
        self.canvas = Canvas(self.frame, width=300, height=300)
        self.canvas.pack(fill="both", expand=True)

        #Shows status of game
        self.lbl_message=Label(self.frame, text='Tic Tac Toe Game', height=2, bg='black', fg='blue')
        self.lbl_message.pack(fill="both", expand=True)

        #canvas board drawing function call
        Deck(self.canvas)
        self.start()

    def start(self):
        #Starts the game

        #refresh canvas
        self.canvas.delete(ALL)
        self.lbl_message['text']=('Player 1 turn')

        #function call on click
        self.canvas.bind("<ButtonPress-1>", self.get_user_input)
        Deck(self.canvas)

        #Starts the matrix to do calculations
        #of the positions of circles and crosses.
        self.TTT=[[0,0,0],[0,0,0],[0,0,0]]

        #counter of turns
        self.i=0

        #trigger to end game
        self.j=False

    def get_user_input(self,event):
        #game loop
        for k in range(0,300,100):
            for j in range(0,300,100):
                #checks if the mouse input is in a bounding box
                if event.x in range(k,k+100) and event.y in range(j,j+100):
                    #checks if there is nothing in the bounding box
                    if self.canvas.find_enclosed(k,j,k+100,j+100)==():
                        self.lbl_message['text']=('Tic Tac Toe Game')
                        #checks the turn
                        if self.i%2==0:
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            if self.player1.playing_symbol == 'O':
                                self.canvas.create_oval( X+25, Y+25, X-25, Y-25, width=4, outline="black")
                            elif self.player1.playing_symbol == 'X':
                                self.canvas. create_line( X+20, Y+20, X-20, Y-20, width=4, fill="black")
                                self.canvas. create_line( X-20, Y+20, X+20, Y-20, width=4, fill="black")
                            self.TTT[Y1][X1]+=1
                            self.i+=1
                            self.lbl_message['text']=('Player 2 turn')
                            self.lbl_message['fg'] = ('blue')
                            Deck.player1choices.append((X1)+(Y1*3))
                        else:
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            if self.player2.playing_symbol == 'O':
                                self.canvas.create_oval( X+25, Y+25, X-25, Y-25, width=4, outline="black")
                            elif self.player2.playing_symbol == 'X':
                                self.canvas. create_line( X+20, Y+20, X-20, Y-20, width=4, fill="black")
                                self.canvas. create_line( X-20, Y+20, X+20, Y-20, width=4, fill="black")

                            self.TTT[Y1][X1]+=9
                            self.i+=1
                            self.lbl_message['text']=('Player 1 turn')
                            self.lbl_message['fg'] = ('blue')
                            Deck.player2choices.append((X1)+(Y1*3))
                    else:
                        self.lbl_message['text']=('Position already selected')
                        self.lbl_message['fg'] = ('red')
        #After everything, remember to check for wins/losts/draws
        self.is_game_over()

    def is_game_over(self):
        """checks the conditions if any player wins or its a draw"""
        #horizontal check
        for i in range(0,3):
            if sum(self.TTT[i])==27:
                self.player2.set_stats(1,0,0,self.data)
                self.player1.set_stats(0,1,0,self.data)
                self.lbl_message['text']=(self.player2.name +" wins!")
                msg = self.player2.name + " wins. Do You want to play another game??"
                res = messagebox.askquestion("Game Over",msg)
                if res == 'yes':
                    self.restart()
                else:
                    self.end()

            if sum(self.TTT[i])==3:
                self.player1.set_stats(1,0,0,self.data)
                self.player2.set_stats(0,1,0,self.data)
                self.lbl_message['text']=(self.player1.name +" wins!")
                msg = self.player1.name + " wins. Do You want to play another game??"
                res = messagebox.askquestion("Game Over",msg)
                if res == 'yes':
                    self.restart()
                else:
                    self.end()
        #vertical check
        #the matrix below transposes self.TTT so that it could use the sum function again
        #for vertical rows
        self.ttt=[[row[i] for row in self.TTT] for i in range(3)]
        for i in range(0,3):
            if sum(self.ttt[i])==27:
                self.player2.set_stats(1,0,0,self.data)
                self.player1.set_stats(0,1,0,self.data)
                self.lbl_message['text']=(self.player2.name +" wins!")
                msg = self.player2.name + " wins. Do You want to play another game??"
                res = messagebox.askquestion("Game Over",msg)
                if res == 'yes':
                    self.restart()
                else:
                    self.end()
            if sum(self.ttt[i])==3:
                self.player1.set_stats(1,0,0,self.data)
                self.player2.set_stats(0,1,0,self.data)
                self.lbl_message['text']=(self.player1.name +" wins!")
                msg = self.player1.name + " wins. Do You want to play another game??"
                res = messagebox.askquestion("Game Over",msg)
                if res == 'yes':
                    self.restart()
                else:
                    self.end()
        #check for diagonal wins
        if self.TTT[1][1]==9:
            if self.TTT[0][0]==self.TTT[1][1] and self.TTT[2][2]==self.TTT[1][1] :
                self.player2.set_stats(1,0,0,self.data)
                self.player1.set_stats(0,1,0,self.data)
                self.lbl_message['text']=(self.player2.name +" wins!")
                msg = self.player2.name + " wins. Do You want to play another game??"
                res = messagebox.askquestion("Game Over",msg)
                if res == 'yes':
                    self.restart()
                else:
                    self.end()
            elif self.TTT[0][2]==self.TTT[1][1] and self.TTT[2][0]==self.TTT[1][1] :
                self.player2.set_stats(1,0,0,self.data)
                self.player1.set_stats(0,1,0,self.data)
                self.lbl_message['text']=(self.player2.name +" wins!")
                msg = self.player2.name + " wins. Do You want to play another game??"
                res = messagebox.askquestion("Game Over",msg)
                if res == 'yes':
                    self.restart()
                else:
                    self.end()
        if self.TTT[1][1]==1:
            if self.TTT[0][0]==self.TTT[1][1] and self.TTT[2][2]==self.TTT[1][1] :
                self.player1.set_stats(1,0,0,self.data)
                self.player2.set_stats(0,1,0,self.data)
                self.lbl_message['text']=(self.player1.name +" wins!")
                msg = self.player1.name + " wins. Do You want to play another game??"
                res = messagebox.askquestion("Game Over",msg)
                if res == 'yes':
                    self.restart()
                else:
                    self.end()
            elif self.TTT[0][2]==self.TTT[1][1] and self.TTT[2][0]==self.TTT[1][1] :
                self.player1.set_stats(1,0,0,self.data)
                self.player2.set_stats(0,1,0,self.data)
                self.lbl_message['text']=(self.player1.name +" wins!")
                msg = self.player1.name + " wins. Do You want to play another game??"
                res = messagebox.askquestion("Game Over",msg)
                if res == 'yes':
                    self.restart()
                else:
                    self.end()
        #check for draws
        if self.j==False:
            a=0
            for i in range(0,3):
                a+= sum(self.TTT[i])
            if a==41:
                self.player2.set_stats(0,0,1,self.data)
                self.player1.set_stats(0,0,1,self.data)
                self.lbl_message['text']=("It's a Draw!")
                msg = "Its a draw"
                res = messagebox.askquestion("Game Over",msg)
                if res == 'yes':
                    self.restart()
                else:
                    self.end()

    def restart(self):
        """function to restart the game"""
        #increment the game counter and update the scores
        self.counter += 1
        msg1 = "Player 1 \n" + "  " + str(self.player1.get_score())
        self.lbl_player1_score['text'] =msg1
        msg2 = "Player 1 \n" + "  " + str(self.player2.get_score())
        self.lbl_player2_score['text'] =msg2
        msg3 = "Game Number \n" + str(self.counter)
        self.lbl_game_counter['text'] =msg3

        self.start()

    def end(self):
        """Ends the game"""
        self.canvas.unbind("<ButtonPress-1>")
        self.j=True
        quit(self.root)

class DataAccessLayer:
    """Class to access database"""
    def __init__(self):
        """function to establish connection and cursor"""
        self.conn = sqlite3.connect('tic_tac_toe.db')   #Create connection
        self.cur = self.conn.cursor()                   #create cursor

    def get_player_data(self,id):
        """function to read data from database"""
        self.cur.execute("SELECT * FROM Player where PlayerId = '%d'"%id)
        data = self.cur.fetchone()
        return(data)

    def save_player_data(self,id,win,lose,draw):
        """Function to update the database"""
        self.cur.execute("UPDATE Player SET Won =%d,Drawn=%d, Lost =%d WHERE PlayerId=%d"%(win,draw,lose,id))
        self.conn.commit()      #save the changes
    def __del__(self):
        """destructor to close the connection"""
        self.conn.close()


root = Tk()
app = TicTacToe(root)
root.mainloop()