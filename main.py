import turtle
import pandas
import tkinter as tk


def usa():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    guessed_states = []

    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What's another state's name?").title()
        if answer_state == "Exit":
            missing_states = []
            for state in all_states:
                if state not in guessed_states:
                    missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break
        if answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)


def india ():
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "india.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = pandas.read_csv("indiastates.csv")
    all_states = data.state.to_list()
    guessed_states = []

    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/36 States Correct",
                                        prompt="What's another state's name?").title()
        if answer_state == "Exit":
            missing_states = []
            for state in all_states:
                if state not in guessed_states:
                    missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break
        if answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)




# Create a new window
window = tk.Tk()

# Set the window title
window.title("State Scavenger")

# Create a label with the question
question_label = tk.Label(window, text="Choose a Map")

# Create two buttons with styles
button1 = tk.Button(window, text="INDIA MAP", command=india, bg="black", fg="yellow", padx=10, pady=5)
button2 = tk.Button(window, text="USA MAP ", command=usa, bg="black", fg="green", padx=10, pady=5)

# Add the label and buttons to the window
question_label.pack(pady=10)
button1.pack(pady=5)
button2.pack(pady=5)

# Start the main event loop
window.mainloop()

