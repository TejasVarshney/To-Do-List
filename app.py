from graphics import *
from button import Button
import UI
import listMaker as lM

lM.reset()

win = GraphWin("To-Do List", 500, 420)

#MAIN MENU UI INITIALIZATION
mainMenu_to_do_listTxt = Text(Point(int(win.getWidth()/2), int(win.getHeight()/6)), "TO-DO LIST")
mainMenu_creator = Text(Point(win.getWidth()/2, mainMenu_to_do_listTxt.getAnchor().y + 50), "Created by Tejas Varshney")
mainMenu_to_do_listTxt.setSize(36)

mainMenu_add = Button("ADD", int((win.getWidth()/3)-(win.getWidth()/30)), 200, int(2*win.getWidth()/3+win.getWidth()/30), 250, "blue", win)
mainMenu_show = Button("SHOW", mainMenu_add.startP().x, mainMenu_add.startP().y + 65, mainMenu_add.endP().x, mainMenu_add.endP().y + 65, "yellow", win)
mainMenu_exit = Button("EXIT", mainMenu_show.startP().x, mainMenu_show.startP().y + 65, mainMenu_show.endP().x, mainMenu_show.endP().y + 65, "red", win)

#ADD MENU UI INITIALIZATION
addMenu_txt = Text(Point(int(win.getWidth()/2), int(win.getHeight()/6)), "Enter Your task")
addMenu_input_box = Entry(Point(win.getWidth()/2, addMenu_txt.getAnchor().y+30), 50)
addMenu_Submit = Button("SUBMIT", int(win.getWidth()/4), int(1.5*win.getHeight()/3), int(3*win.getWidth()/4), int(4*win.getHeight()/6), "yellow", win)
addMenu_Back = Button("BACK", addMenu_Submit.startP().x + 15, int(win.getHeight()/1.4), addMenu_Submit.endP().x - 15, win.getHeight()/1.2, "red", win)

#SHOW MENU UI INITIALIZATION
showMenu_height = int(win.getHeight()/1.4)
showMenu_width = int(win.getWidth()/1.25)
pColour = "pink"
dColour = "yellow"
panel = []
done_button = []
showMenu_Back = Button("Back", 0, showMenu_height, win.getWidth(), win.getHeight(), "red", win)

for i in range(0, 5) :
    panel.append(Button(lM.getTask(i), 0, int(i*(showMenu_height)/5), showMenu_width, int((i+1)*(showMenu_height)/5), pColour, win))
    done_button.append(Button("Done", showMenu_width, int(i*(showMenu_height)/5), win.getWidth(), int((i+1)*(showMenu_height)/5), dColour, win))

while True :
    lM.Saving()
    menu = UI.mainMenu(win, mainMenu_add, mainMenu_show, mainMenu_exit, mainMenu_to_do_listTxt, mainMenu_creator)

    if menu == "exit" :
        win.close()
        break

    if menu == "show" :
        UI.showMenu(win, panel, done_button, showMenu_Back)

    if menu == "add" :
        UI.addMenu(win, addMenu_txt, addMenu_Back, addMenu_Submit, addMenu_input_box)
    lM.Saving()
