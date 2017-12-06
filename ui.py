import tkinter as tk
import helpers
import canvasapi as can

# Home Screen
# Landing/Splash page for the interface
# home = Tk()
#
# topFrame = Frame(home).pack(side=TOP)
# bottomFrame = Frame(home).pack(side=BOTTOM)
# home_title = Label(topFrame, text="Welcome to the Canvas Interface!").pack(fill=X)
# begin_button = Button(topFrame, text="Click to begin", fg="black", bg="white").pack()
# home.mainloop()

canvas_instance = None  # Global Variable
status = "Not connected"


# Functions for UI
# TODO Clean these up
def login_press(event):
    global canvas_instance, status
    canvas_instance = can.Canvas(str(canvas_api_url_entry), str(api_key_entry))
    status = "Connected"
    return canvas_instance  # Hopefully I don't need to return an object


def make_user_instructor(event):
    global canvas_instance
    course_object = canvas_instance.get_course(str(course_id_entry))
    print(course_object.id)
    course_object.enroll_user(user=str(user_id_entry), enrollment_type="Instructor")
    return course_object
########################################################################################################################
# CanvasObject Screen
canvas_object_screen = tk.Tk()
canvas_object_screen.title("CanvasObject Screen")
# canvas_object_screen.geometry("{}x{}".format(460, 350))

# Create the main containers (frames)
title_frame = tk.Frame(canvas_object_screen, pady=3)  # Idk how the pady effect actually looks
configuration_frame = tk.Frame(canvas_object_screen)  # Configuration options for the program including API and URL
functions_frame = tk.Frame(canvas_object_screen)  # Functionality the page has to perform.
assignments_frame = tk.Frame(canvas_object_screen)

# Layout the main containers
canvas_object_screen.grid_rowconfigure(1, weight=1)
canvas_object_screen.grid_columnconfigure(0, weight=1)

title_frame.grid(row=0, sticky=tk.EW)
configuration_frame.grid(row=1, sticky=tk.EW)
functions_frame.grid(row=3, sticky=tk.EW)
assignments_frame.grid(row=4, sticky=tk.NSEW)

# Widgets for Title Frame
welcome_label = tk.Label(title_frame, text="Create the Canvas Account Object")
welcome_label.grid(row=0, sticky=tk.N)

# Widgets for Configuration Frame
# API URL
canvas_api_url_label = tk.Label(configuration_frame, text="Canvas API URL")
canvas_api_url_label.grid(row=0, column=0, sticky=tk.E)

canvas_api_url_entry = tk.Entry(configuration_frame)
canvas_api_url_entry.grid(row=0, column=1, columnspan=2)

# API Key
api_key_label = tk.Label(configuration_frame, text="Canvas API Key")
api_key_label.grid(row=1, column=0, sticky=tk.E)

api_key_entry = tk.Entry(configuration_frame)
api_key_entry.grid(row=1, column=1, columnspan=2)

# Login Button
login_button = tk.Button(configuration_frame, text="Login!")
login_button.bind("<Button-1>", login_press)
login_button.grid(row=2, column=0)

# Login Status
login_status = tk.Label(configuration_frame, text=str(status))
login_status.grid(row=2, column=1, columnspan=2)

# Widgets for Functions Frame
# Canvas Course ID Entry (e.g. 1234567)
course_id_label = tk.Label(functions_frame, text="Canvas Course ID (e.g. 1234567)")
course_id_label.grid(row=0, column=0, sticky=tk.E)

course_id_entry = tk.Entry(functions_frame)
course_id_entry.grid(row=0, column=1)

# Canvas User ID Entry (e.g. 1234567)
user_id_label = tk.Label(functions_frame, text="Canvas User ID (e.g. 1234567)")
user_id_label.grid(row=1, column=0, sticky=tk.E)

user_id_entry = tk.Entry(functions_frame)
user_id_entry.grid(row=1, column=1)

# Make the specified user an instructor in the course
make_instructor_button = tk.Button(functions_frame, text="Make Me an Instructor")
make_instructor_button.bind("<Button-1>", make_user_instructor)
make_instructor_button.grid(row=2, column=0, columnspan=2, sticky=tk.EW)

canvas_object_screen.mainloop()
########################################################################################################################
