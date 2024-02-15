# Never ending Dice Game
from tkinter import *
from PIL import ImageTk, Image
'''Python image library is used to add images to ur platform'''
'''Image is used to open the image file'''
'''ImageTk is used to add the picture file to root window'''

root = Tk()
root.title('Endless Dice Game')
root.geometry("600x400")
root.configure(background = "IndianRed3")

img = ImageTk.PhotoImage(Image.open("Ball.png"))

player1 = Label(root, text = "Player 1", bg = "coral2", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(root, text = "Player 2", bg = 'coral2', fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player_1_score_label = Label(root, bg = "SpringGreen2", fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(root, bg = "SpringGreen2", fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_dice_label = Label(root, bg = "VioletRed4", fg = "white")
random_dice_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

btn_player_1 = Button(root, image = img)
btn_player_1.place(relx = 0.2, rely = 0.7, anchor = CENTER)

btn_player_2 = Button(root, image = img)
btn_player_2.place(relx = 0.8, rely = 0.7, anchor = CENTER)

root.mainloop()