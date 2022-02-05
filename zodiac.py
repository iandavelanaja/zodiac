from calendar import month
from cgitb import text
from curses.panel import top_panel
from logging import root
from tkinter import *
from tkcalendar import *
from PIL import ImageTk,Image


root = Tk()
root.title("Zodiac Identifier")
root.geometry("400x200")


## Functions ##
def pickButton():

    def grab_date():
        global aquarius_img
        global pisces_img
        global aries_img
        global aquarius_img
        global leo_img
        global taurus_img
        global gemini_img
        global cancer_img
        global virgo_img
        global scorpio_img
        global sagittarius_img
        global capricorn_img
        
        zodiacWindow = Toplevel()
        zodiacWindow.title("Your zodiac sign is....")
        #zodiacWindow.geometry("600x400")
        
        bday = str(cal.get_date())                                     # getting the birtday stroign in bday variable

        trimmed = bday.split("/")                               # removing the slash sign for easy conversion
        trimmed = trimmed[0] + trimmed[1]                       # trimming out the year, we don't need those

        rawBirt = int(trimmed)                                  # casting string to int for iterations later
        
        ## functions
        
        def zodiac(start, end):
            
            zodiac_list = []

            for i in range(start, end+1):
                 zodiac_list.append(i)

            return zodiac_list

        def capri():
            capricorn = []
            for i in range(1222,1231):
                capricorn.append(i)

            for j in range(101,120):
                capricorn.append(j)
    
            return capricorn
        
        aquarius = zodiac(120, 218)
        pisces = zodiac(219, 320)
        aries = zodiac(321, 419)
        taurus = zodiac(420, 520)
        gemini = zodiac(521, 621)
        cancer = zodiac(622, 722)
        leo = zodiac(723, 822)
        virgo = zodiac(823, 922)
        libra = zodiac(921, 1023)
        scorpio = zodiac(1024, 1121)
        sagittarius = zodiac(1122, 1221)
        capricorn = capri()

        if rawBirt in aquarius:
            aquarius_img = ImageTk.PhotoImage(Image.open("images/aquarius.jpg"))
            aquarius_label = Label(zodiacWindow, image=aquarius_img).pack()
            #print("You are a Aquarius")
        elif rawBirt in pisces:
            pisces_img = ImageTk.PhotoImage(Image.open("images/pisces.jpg"))
            pisces_label = Label(zodiacWindow, image=pisces_img).pack()
            #print("You are a Pisces")
        elif rawBirt in aries:
            aries_img = ImageTk.PhotoImage(Image.open("images/aries.jpg"))
            aries_label = Label(zodiacWindow, image=aries_img).pack()
            #print("You are a Aries")
        elif rawBirt in taurus:
            taurus_img = ImageTk.PhotoImage(Image.open("images/taurus.jpg"))
            taurus_label = Label(zodiacWindow, image=taurus_img).pack()
            #print("You are a Taurus")
        elif rawBirt in gemini:
            gemini_img = ImageTk.PhotoImage(Image.open("images/gemini.jpg"))
            gemini_label = Label(zodiacWindow, image=gemini_img).pack()
            #print("You are a Gemini")
        elif rawBirt in cancer:
            cancer_img = ImageTk.PhotoImage(Image.open("images/cancer.jpg"))
            cancer_label = Label(zodiacWindow, image=cancer_img).pack()
            #print("You are a Cancer")
        elif rawBirt in leo:
            leo_img = ImageTk.PhotoImage(Image.open("images/leo.jpg"))
            leo_label = Label(zodiacWindow, image=leo_img).pack()
            #print("You are a Leo")
        elif rawBirt in virgo:
            virgo_img = ImageTk.PhotoImage(Image.open("images/virgo.jpg"))
            virgo_label = Label(zodiacWindow, image=virgo_img).pack()
            #print("You are a Virgo")
        elif rawBirt in libra:
            libra_img = ImageTk.PhotoImage(Image.open("images/libra.jpg"))
            libra_label = Label(zodiacWindow, image=libra_img).pack()
            #print("You are a Libra")
        elif rawBirt in scorpio:
            scorpio_img = ImageTk.PhotoImage(Image.open("images/scorpio.jpg"))
            scorpio_label = Label(zodiacWindow, image=scorpio_img).pack()
            #print("You are a Scorpio")
        elif rawBirt in sagittarius:
            sagittarius_img = ImageTk.PhotoImage(Image.open("images/sagi.jpg"))
            sagittarius_label = Label(zodiacWindow, image=sagittarius_img).pack()
            #print("You are a Sagittarius")
        elif rawBirt in capricorn:
            capricorn_img = ImageTk.PhotoImage(Image.open("images/capricorn.jpg"))
            capricorn_label = Label(zodiacWindow, image=capricorn_img).pack()
            #print("You are a Capricorn")
        else:
            print("Please use a valid birthday format: m/d/yy")

        def exitProgram():
            root.quit()

        quitButton = Button(zodiacWindow, text="Quit Program", command=exitProgram)
        quitButton.pack(pady=20)



    
    # TopLevel Window 
    calendarWindow = Toplevel()
    calendarWindow.title("Pick Your Birthday")
    calendarWindow.geometry("600x400")

    # Adding The Calendar in the Window once the buton is clicked. 
    
    cal = Calendar(calendarWindow, selectmode="day", year=2022, month=1, day=1)
    cal.pack(pady= 20)

    submitButton = Button(calendarWindow, text="That's my Birthday!", command=grab_date)
    submitButton.pack()



## Create Widget Here  ##
## Note: Widget in the Main Window #

pickButton = Button(root, text="Select Your Birthday",padx=40,pady=20, command=pickButton)

## Display the Widget Here ##
pickButton.pack(pady=50)



root.mainloop()