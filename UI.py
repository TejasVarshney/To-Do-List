from button import Button
from graphics import *
import time as t
import listMaker as lM

def Update_panel(obj) :
    obj.__del__()
    obj.show()

def error(msg) :
    win = GraphWin("ERROR", 300, 120)
    ok_button = Button("OK", 115, 70, 185, 100, "yellow", win)
    Txt = Text(Point(win.getWidth()/2, 20), str(msg))
    Txt.draw(win)
    ok_button.show()

    while True :
        mouseP = win.getMouse()
        if(ok_button.isClicked(mouseP)) :
            win.close()
            break

def showMenu(win, panel, done_button, back_button) :
    height = win.getHeight() - 100
    width = win.getWidth() - 100

    back_button.show()

    for i in range(0, 5) :
        if lM.getTask(i) == "Nothing":
            panel[i].setColour("yellow")
            done_button[i].setColour(color_rgb(205, 92, 92))
        else :
            panel[i].setColour("pink")
            done_button[i].setColour(color_rgb(144,238,144))

    for i in range(0, 5) :
        panel[i].setText(lM.getTask(i))
        panel[i].show()
        done_button[i].show()

    while True :
        mousePos = win.getMouse()

        if(back_button.isClicked(mousePos)) :
            break

        for i in range(0, 5) :
            if(done_button[i].isClicked(mousePos)) :
                if(lM.Done(i)) :
                    error("No task in the selected panel")
                else :
                    panel[i].setText("DONE")
                    lM.setTask(i, "DONE")


    for i in range(0, 5) :
        panel[i].__del__()
        done_button[i].__del__()

    back_button.__del__()
    return

def addMenu(win, txt, Back, Submit, input_box) :
    win.setBackground('White')

    Back.show()
    Submit.show()
    input_box.draw(win)
    txt.draw(win)

    while (True) :
        mousePos = win.getMouse()
        if(mousePos != None) :
            if (Back.isClicked(mousePos)) :
                break

            if (Submit.isClicked(mousePos) and input_box.getText() != "" and not input_box.getText().isspace()) :
                if (lM.totalTask() >= 5) :
                    error("You have reached your maximum task")
                else :
                    for i in range(0, 5) :
                        if(lM.getTask(i) == "Nothing" or lM.getTask(i) == "DONE") :
                            lM.setTask(i, input_box.getText())
                            input_box.setText("")
                            break
                    break

    txt.undraw()
    Back.__del__()
    Submit.__del__()
    input_box.undraw()
    return

def mainMenu_disableUI(Add, Show, Exit, toDO_list, creator) :
    Add.__del__()
    Show.__del__()
    Exit.__del__()
    toDO_list.undraw()
    creator.undraw()

def mainMenu(win, Add, Show, Exit, to_do_list, creator) :
    win.setBackground("White")

    Add.show()
    Show.show()
    Exit.show()

    to_do_list.draw(win)
    creator.draw(win)

    while True :

        mouse_clickedPos = win.getMouse()

        if(Exit.isClicked(mouse_clickedPos)) :
            mainMenu_disableUI(Add, Show, Exit, to_do_list, creator)
            return "exit"

        if(Add.isClicked(mouse_clickedPos)) :
            mainMenu_disableUI(Add, Show, Exit, to_do_list, creator)
            return "add"

        if(Show.isClicked(mouse_clickedPos)) :
            mainMenu_disableUI(Add, Show, Exit, to_do_list, creator)
            return "show"
