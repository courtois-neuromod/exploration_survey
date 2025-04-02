from psychopy import visual, core, event, gui
import numpy as np

def check_response(mouse, buttons):
    return




def navigate_clips(keys, index_clip):
    if keys:
        if "right" in keys:
            return index_clip + 1
        elif "left" in keys and index_clip > 0:
            return index_clip -1
        elif "left" in keys and index_clip == 0:
            return index_clip
    else:
        return index_clip

def get_responds(responses, mouse, buttons, buttons_pressed):
    for idx, button in enumerate(buttons):
        if sum(buttons_pressed[idx][-15:]) > 0:
            buttons_pressed[idx].append(False)
            return buttons, responses
        else:
            if responses[idx] == 0 and mouse.isPressedIn(buttons[button]):
                buttons[button].fillColor = "white"
                responses[idx] = 1
                buttons_pressed[idx].append(True)
            elif responses[idx] == 1 and mouse.isPressedIn(buttons[button]):
                buttons[button].fillColor = "black"
                responses[idx] = 0
                buttons_pressed[idx].append(True)

    return buttons, responses

def draw_buttons(buttons, responses):
    for button in buttons:
        if responses[int(button[-1])-1] == 1:
            buttons[button].fillColor = "white"
        else:
            buttons[button].fillColor = "black"
        buttons[button].draw()

