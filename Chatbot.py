import  tkinter



# GUI

root = tkinter()

root.title("SamBot")



BG_GRAY = "#ABB2B9"

BG_COLOR = "#17202A"

TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"

FONT_BOLD = "Helvetica 13 bold"



# Send function

def send():

    send = "You -> " + e.get()

    txt.insert(end "\n" + send)

    user = e.get().lower()

    

    if user == "hello":

        txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")

    elif user in ["hi", "hii", "hiiii"]:

        txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")

    elif user == "how are you":

        txt.insert(END, "\n" + "Bot -> Fine! And you?")

    elif user in ["fine", "i am good", "i am doing good"]:

        txt.insert(END, "\n" + "Bot -> Great! How can I help you?")

    elif user in ["thanks", "thank you", "now its my time"]:

        txt.insert(END, "\n" + "Bot -> My pleasure!")

    elif user in ["what do you sell", "what kinds of items are there", "have you something"]:

        txt.insert(END, "\n" + "Bot -> We have coffee and tea")

    elif user in ["tell me a joke", "tell me something funny", "crack a funny line"]:

        txt.insert(END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison!")

    elif user in ["goodbye", "see you later", "see yaa"]:

        txt.insert(END, "\n" + "Bot -> Have a nice day!")

    else:

        txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")

    

    e.delete(0, END)



label1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)

txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)

scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)

e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send).grid(row=2, column=1)

