from tkinter import *

# Home Screen
# Landing/Splash page for the interface
# home = Tk()
#
# topFrame = Frame(home).pack(side=TOP)
# bottomFrame = Frame(home).pack(side=BOTTOM)
# home_title = Label(topFrame, text="Welcome to the Canvas Interface!").pack(fill=X)
# begin_button = Button(topFrame, text="Click to begin", fg="black", bg="white").pack()
# home.mainloop()


# CanvasObject Screen
canvas_object_screen = Tk()
canvas_object_screen.title("CanvasObject Screen")
# canvas_object_screen.geometry("{}x{}".format(460, 350))

# Create the main containers (frames)
title_frame = Frame(canvas_object_screen, pady=3)  # Idk how the pady effect actually looks
configuration_frame = Frame(canvas_object_screen)
functions_frame = Frame(canvas_object_screen)
assignments_frame = Frame(canvas_object_screen)

# Layout the main containers
canvas_object_screen.grid_rowconfigure(1, weight=1)
canvas_object_screen.grid_columnconfigure(0, weight=1)

title_frame.grid(row=0, sticky=EW)
configuration_frame.grid(row=1, sticky=EW)
functions_frame.grid(row=3, sticky=EW)
assignments_frame.grid(row=4, sticky=NSEW)

# Widgets for Title Frame
welcome_label = Label(title_frame, text="CanvasObject")
welcome_label.grid(row=0, sticky=N)

# Widgets for Configuration Frame
# API URL
canvas_api_url_label = Label(configuration_frame, text="Canvas API URL")
canvas_api_url_label.grid(row=0, column=0, sticky=E)

canvas_api_url_entry = Entry(configuration_frame)
canvas_api_url_entry.grid(row=0, column=1)

# API Key
api_key_label = Label(configuration_frame, text="Canvas API Key")
api_key_label.grid(row=1, column=0, sticky=E)

api_key_entry = Entry(configuration_frame)
api_key_entry.grid(row=1, column=1)

# Login Button
login_button = Button(configuration_frame, text="Login!")
login_button.grid(row=2, column=0)

# Login Status
login_status = Label(configuration_frame, text="Connected/Not Connected will display here")
login_status.grid(row=2, column=1, columnspan=2)

# Widgets for Functions Frame


canvas_object_screen.mainloop()
