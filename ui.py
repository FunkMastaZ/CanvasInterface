import tkinter as tk
import helpers
import canvasapi as can
import os as os


# Home Screen
# Landing/Splash page for the interface
# home = Tk()
#
# topFrame = Frame(home).pack(side=TOP)
# bottomFrame = Frame(home).pack(side=BOTTOM)
# home_title = Label(topFrame, text="Welcome to the Canvas Interface!").pack(fill=X)
# begin_button = Button(topFrame, text="Click to begin", fg="black", bg="white").pack()
# home.mainloop()


########################################################################################################################
# Functions for UI
# TODO Clean these up
########################################################################################################################
def is_empty_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) == 0


def on_startup():
    global api_key_file
    global api_url_file
    global user_id7_file
    global api_key
    global api_url
    global user_id7

    # Read the configuration information from the files and update the entry variables
    print("Starting up...")
    # Get the API Key from storage
    print("Retrieving API KEY...")
    api_key.set(api_key_file.read())
    print("Done.")

    # Get the API URL from storage
    print("Retrieving API URL...")
    api_url.set(api_url_file.read())
    print("Done.")

    # Get this User's ID from storage
    print("Retrieving USER ID...")
    user_id7.set(user_id7_file.read())
    print("Done.")
    return


def login_press(event):
    global canvas_instance
    global status
    global api_key
    global api_url
    global this_user
    global user_id7

    # Create the account object which is very similar to logging in
    canvas_instance = can.Canvas(api_url.get(), api_key.get())

    # Get the user's account object which will be saved for later and serve as confirmation login was successful
    #  TODO implement a try-catch statement to catch login errors
    this_user = (canvas_instance.get_user(user_id7.get()))
    print("Logged in as:\t" + str(this_user))
    status.set("Connected")  # TODO not working/fix this

    # Write user info to files
    print("About to write user data to file...")
    if is_empty_file("api_key.txt"):
        api_key_file.write("%s" % api_key.get())
        print("Wrote API Key.")
        api_key_file.close()
    if is_empty_file("api_url.txt"):
        api_url_file.write("%s" % api_url.get())
        print("Wrote API URL.")
        api_url_file.close()
    if is_empty_file("user_id7.txt"):
        user_id7_file.write("%s" % user_id7.get())
        print("Wrote User ID7.")
        user_id7_file.close()
    print("Data writing is complete.")
    return  # Hopefully I don't need to return an object


def make_user_instructor(event):
    global canvas_instance
    global this_user
    global course_id7
    global user_id7

    # Create the course object for a given 7-digit course ID
    course_object = canvas_instance.get_course(course_id7.get())
    # Create an enrollment of the specified type for the specified user. The enrollment is returned as an object
    # TODO implement try-catch her to confirm the enrollment was succssefull
    enrollment = course_object.enroll_user(this_user, enrollment_type="TeacherEnrollment")
    print("Enrollment completed:\t" + str(enrollment))
    return


########################################################################################################################
# CanvasObject Screen
canvas_object_screen = tk.Tk()
########################################################################################################################

###########################################################
# Global Variable (Need to be instantiated after TK object)
###########################################################
status = tk.StringVar()
status.set("Not Connected")
api_key = tk.StringVar()
api_url = tk.StringVar()
canvas_instance = can.Canvas(api_url.get(), api_key.get(()))
this_user = None
course_id7 = tk.StringVar()
user_id7 = tk.StringVar()

api_key_file = open("api_key.txt", "r+")
api_url_file = open("api_url.txt", "r+")
user_id7_file = open("user_id7.txt", "r+")
file_list = {api_key_file, api_url_file, user_id7_file}

on_startup()  # Perform startup tasks
###########################################################

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

canvas_api_url_entry = tk.Entry(configuration_frame, textvariable=api_url)
canvas_api_url_entry.grid(row=0, column=1, columnspan=2)

# API Key
api_key_label = tk.Label(configuration_frame, text="Canvas API Key")
api_key_label.grid(row=1, column=0, sticky=tk.E)

api_key_entry = tk.Entry(configuration_frame, textvariable=api_key)
api_key_entry.grid(row=1, column=1, columnspan=2)

# Login Button
login_button = tk.Button(configuration_frame, text="Login!")
login_button.bind("<Button-1>", login_press)
login_button.grid(row=2, column=0)

# Login Status
login_status = tk.Label(configuration_frame, text=status.get())
login_status.grid(row=2, column=1, columnspan=2)

# Widgets for Functions Frame
# Canvas Course ID Entry (e.g. 1234567)
course_id_label = tk.Label(functions_frame, text="Canvas Course ID (e.g. 1234567)")
course_id_label.grid(row=0, column=0, sticky=tk.E)

course_id_entry = tk.Entry(functions_frame, textvariable=course_id7)
course_id_entry.grid(row=0, column=1)

# Canvas User ID Entry (e.g. 1234567)
user_id_label = tk.Label(functions_frame, text="Canvas User ID (e.g. 1234567)")
user_id_label.grid(row=1, column=0, sticky=tk.E)

user_id_entry = tk.Entry(functions_frame, textvariable=user_id7)
user_id_entry.grid(row=1, column=1)

# Make the specified user an instructor in the course
make_instructor_button = tk.Button(functions_frame, text="Make Me an Instructor")
make_instructor_button.bind("<Button-1>", make_user_instructor)
make_instructor_button.grid(row=2, column=0, columnspan=2, sticky=tk.EW)

# Get list of Turnitin Assignments
make_instructor_button = tk.Button(functions_frame, text="Make Me an Instructor")
make_instructor_button.bind("<Button-1>", make_user_instructor)
make_instructor_button.grid(row=2, column=0, columnspan=2, sticky=tk.EW)

canvas_object_screen.mainloop()
