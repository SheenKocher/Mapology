import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S STATES GAME ")
#building a way to access our image
image = "/Users/sheenkocher/Downloads/us-states-game-start/blank_states_img.gif"
# It adds the shape from the .gif file to the available shapes that can be used by the turtle.
screen.addshape(image)
#This line sets the shape of the turtle to the image specified by the image variable.
#By passing the image variable as the argument, the turtle's shape will be set to the image loaded from the .gif file.
turtle.shape(image)
guessed_state = []
while len(guessed_state) < 50:
    # taking input from user
    answer_state = screen.textinput(title = f"{len(guessed_state)} out of 50 states",prompt="What is the state's name?")
    answer_state = answer_state.title()
    print(answer_state)

    data = pandas.read_csv("/Users/sheenkocher/Downloads/us-states-game-start/50_states.csv")
    all_states = data.state.to_list()

    if answer_state=="Exit":
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        guessed_state.append(answer_state)
        t.hideturtle()
        t.penup()
        chosen_row = data[data["state"] == answer_state]
        t.goto(int(chosen_row.x),int(chosen_row.y))
        t.write(answer_state)


#generating a new file
need_to_retain = []
data = pandas.read_csv("/Users/sheenkocher/Downloads/us-states-game-start/50_states.csv")
for states in data["state"]:
    if states not in guessed_state:
        need_to_retain.append(states)

df = pandas.DataFrame(need_to_retain)
df.to_csv("need_to_retain.csv")

