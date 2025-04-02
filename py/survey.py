import os
import time

import numpy as np
import random
import pandas as pd
from psychopy import visual, core, event, gui

import outils
import graphic
import mechanic


##########################
#Initialiser l'expérience#
##########################


seed = time.time() 
random.seed(int(seed))
id_participant = 1  

# Récupérer les vidéos
df_stim = outils.get_mario_scenes_dataframe()

# DataFrame pour choisir une série de clips au hazard
paths_stim = outils.get_random_serie_clips(df_stim)

# Création de la fenêtre PsychoPy
win = visual.Window(fullscr=True, color="black")

# Tableaux de résultats
result_responses = outils.creat_results_df(df_stim)

result_responses.at[0, "id"] = id_participant
result_responses.at[0, "sub"] = paths_stim.iloc[0].split('/')[-1].split('_')[0]
result_responses.at[0, "level"] = paths_stim.iloc[0].split('/')[-1].split('_')[3]
result_responses.at[0, "scene"] = paths_stim.iloc[0].split('/')[-1].split('_')[4]

result_responses.at[0, "clip_paths"] = paths_stim
index_clip = 0
start_time = time.time()

######################
#Page de présentation#
######################

text_stim = graphic.get_text(win)

text_stim['intro'].draw()
win.flip()
event.waitKeys(keyList= None)


#####################
# Boucle principale #
#####################

while index_clip <= len(paths_stim):
    
    if index_clip == len(paths_stim):
        #faire les remerciemnts
        break
    
    path = paths_stim[index_clip]

    # Afficher la vidéo
    movie = graphic.get_movie(win, path)
    result_responses.at[0, f'clip_duration_{index_clip}'] = movie.duration

    buttons = graphic.get_button(win)
    mouse = event.Mouse(win=win)
    start_anwser = time.time()
    keys = []
    responses = result_responses.at[0, f"clip_{index_clip+1}"]
    buttons_pressed = [[False]*15]*5

    # boucle pour afficher les frames
    while keys == []:

        movie.draw()

        mechanic.draw_buttons(buttons, responses)

        num_clip = visual.TextStim(win, text=f"Clip {index_clip+1}", color="white", pos=(-0.75 , 0.9))
        num_clip.draw()
        text_stim["consigne"].draw()
        text_stim["question1"].draw()
        text_stim["question2"].draw()
        text_stim["question3"].draw()
        text_stim["question4"].draw()
        text_stim["question5"].draw()

        win.flip()


        # Récupérer les réponses
        buttons, responses = mechanic.get_responds(responses, mouse, buttons, buttons_pressed)

        # stocker les réponses
        result_responses.at[0, f"clip_{index_clip+1}"] = responses

        keys =  event.getKeys(keyList=["left", "right", 'p'])
        index_clip = mechanic.navigate_clips(keys, index_clip)
    
    end_anwser = time.time()
    anwser_duration = end_anwser - start_anwser

    if anwser_duration > movie.duration:
        result_responses.at[0, f"anwser_duration_clip_{index_clip}"] = end_anwser - start_anwser
    else:
        pass
    
    if 'p' in keys:
        break

                
    # Afficher les questions

tot_duration = time.time() - start_time
result_responses.at[0, "total_duration"] = tot_duration
    
#sauvegarder dans fichier csv
path_resp = os.path.join(os.getcwd(),'survey_exploration', 'results', 'results_responses.csv')
outils.save_results(result_responses, path_resp)

# Fin de l'expérience
end_text = visual.TextStim(win, text="Merci pour votre participation !\n\nAppuyez sur ÉCHAP pour quitter.", color="white")
end_text.draw()
win.flip()
event.waitKeys(keyList=["escape"])
win.close()
core.quit()