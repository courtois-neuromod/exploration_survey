from psychopy import visual, core, event, gui
import numpy as np
import os


def get_screen_info(win):
    info = {
        "screen_width": win.size[0],
        "screen_height": win.size[1],
        "min_size": np.min(win.size),
        "max_size": np.max(win.size),
        "screen_ratio": np.max(win.size) / np.min(win.size)
    }
    return info

print("Screen information:")

def get_text(win):
    screen_info = get_screen_info(win)
    screen_ratio = screen_info["screen_ratio"]
    texts = {
        "intro": visual.TextStim(win, text="Bienvenue dans l'étude.\n\nAppuyez sur ESPACE pour commencer.", color="white"),
        "consigne": visual.TextStim(win, height=0.032*screen_ratio,  text="Select the affirmations that you agree with:", color="white", pos=(0 , -0.1),  wrapWidth=2),
        "question1": visual.TextStim(win, height=0.032*screen_ratio, text="The player explores a new path or interacts with a game element for the first time.", color="white", pos=(0 , -0.3), wrapWidth=2),
        "question2": visual.TextStim(win, height=0.032*screen_ratio, text="The player tries out a movement pattern or gameplay strategy they haven't used before.", color="white", pos=(0 , -0.4), wrapWidth=2),
        "question3": visual.TextStim(win, height=0.032*screen_ratio, text="The player chooses a more difficult route than in their previous attempts, requiring greater skill or precision.", color="white", pos=(0 , -0.5), wrapWidth=2),
        "question4": visual.TextStim(win, height=0.032*screen_ratio, text="The player use the same solution as in previous attempts", color="white", pos=(0 , -0.6), wrapWidth=2),
        "question5": visual.TextStim(win, height=0.032*screen_ratio, text="The player's movements are becoming more efficient and smooth.", color="white", pos=(0 , -0.7), wrapWidth=2),
        "fin": visual.TextStim(win, text="Merci d'avoir participé à l'étude.", color="white")
    }
    return texts

def get_button(win):
    screen_info = get_screen_info(win)
    screen_ratio = screen_info["screen_ratio"]
    buttons = {
        "button1": visual.Rect(win, width=0.05, height=0.05*screen_ratio, pos=(-0.9, -0.3), fillColor="black", lineColor="white"),
        "button2": visual.Rect(win, width=0.05, height=0.05*screen_ratio, pos=(-0.9, -0.4), fillColor="black", lineColor="white"),
        "button3": visual.Rect(win, width=0.05, height=0.05*screen_ratio, pos=(-0.9, -0.5), fillColor="black", lineColor="white"),
        "button4": visual.Rect(win, width=0.05, height=0.05*screen_ratio, pos=(-0.9, -0.6), fillColor="black", lineColor="white"),
        "button5": visual.Rect(win, width=0.05, height=0.05*screen_ratio, pos=(-0.9, -0.7), fillColor="black", lineColor="white"),
    }
    return buttons

def get_movie(win, path):
    screen_info = get_screen_info(win)
    min_size = screen_info["min_size"]
    movie_size = np.array([min_size, min_size])/2.1
    movie = visual.MovieStim(win, 
                             os.path.join(os.getcwd(), path), 
                             loop = True, 
                             size = movie_size,
                             pos = (0, movie_size[1]/2))
    return movie


