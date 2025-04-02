# library with outils functions

import os
import numpy as np
import pandas as pd
import random

import time

def get_mp4_path():
    """Return the path to the mp4 file"""
    root = os.path.join(os.path.dirname(__file__), 'data', 'mario_scenes')
    all_map4_path = []
    for root, dirs, files in os.walk('survey_exploration/data'):
        for file in files:
            if file.endswith('.mp4'):
                all_map4_path.append(os.path.join(root, file))

    return all_map4_path


def get_mario_scenes_dataframe():
    """Return the dataframe with all the mp4 files in it"""

    all_mp4_path = get_mp4_path()
    df = pd.DataFrame(all_mp4_path, columns=['mp4_path'])
    df['mp4_name'] = df['mp4_path'].apply(lambda x: x.split('/')[-1])
    df['sub'] = df['mp4_name'].apply(lambda x: x.split('_')[0])
    df['ses'] = df['mp4_name'].apply(lambda x: x.split('_')[1])
    df['run'] = df['mp4_name'].apply(lambda x: x.split('_')[2])
    df['level'] = df['mp4_name'].apply(lambda x: x.split('_')[3])
    df['scene'] = df['mp4_name'].apply(lambda x: x.split('_')[4])
    df['clip'] = df['mp4_name'].apply(lambda x: x.split('_')[5])

    return df


a = get_mario_scenes_dataframe()
b = a[(a['sub'] == 'sub-01') & (a['level'] == 'level-w1l1') & (a['scene'] == 'scene-1')]['mp4_name'].sort_values()
#print(b)



def get_random_serie_clips(df):
    """Return  random serie of clips, based on the sub, level and scene"""

    sub = random.choice(df['sub'].unique())
    level = random.choice(df['level'].unique())
    scene = random.choice(df[df['level'] == level]['scene'].unique())
    paths_stim = df[(df['sub'] == sub) & (df['level'] == level) & (df['scene'] == scene)]['mp4_path'].sort_values()
    return paths_stim.reset_index(drop=True)

a = get_random_serie_clips(a)

def get_max_series_length(df):
    # Grouper par sub, level et scene, puis compter le nombre de clips par groupe
    series_length = df.groupby(['sub', 'level', 'scene']).size()

    # Boucle sur les groupes et affichage des infos
    for (sub, level, scene), count in series_length.items():
        #print(f"Groupe: sub={sub}, level={level}, scene={scene} -> Nombre de clips: {count}")
        pass

    # Trouver la longueur maximale d'une série de clips
    max_length = series_length.max()

    return max_length

def creat_results_df(df, num_button = 5):
    """Return the results dataframe"""

    num_clip_max = get_max_series_length(df)
    columns = ['id'] + [f'clip_{i}' for i in range(1, num_clip_max + 1)] + [f'clip_duration_{i}' for i in range(1, num_clip_max + 1)] + [f'anwser_duration_clip_{i}' for i in range(1, num_clip_max + 1)] + ['sub', 'level', 'scene','clip_paths'] + ['total_duration']
    results_df = pd.DataFrame([{col: None for col in columns}])
    for i in range(1, num_clip_max + 1):
        results_df.at[0, f'clip_{i}'] = [0]*num_button
    #rsults_df.loc[0] = [None] * len(df.columns)
    #results_df = results_df.append(df.iloc[0], ignore_index=True)
    
    return results_df

def save_results(df, path):
    """Save the results dataframe to a CSV file"""
    print(path)
    # Ensure path is a valid file path, not a directory
    dir_path = os.path.dirname(path)
    print(dir_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)  # Create the directory if it doesn't exist
    
    if not os.path.exists(path):  # If the file doesn't exist, create an empty one
        df_old = pd.DataFrame(columns=df.columns)
    else:  # If the file exists, read it
        df_old = pd.read_csv(path)
    
    # Concatenate old and new dataframes
    df_combined = pd.concat([df_old, df], ignore_index=True)
    
    # Save the combined dataframe to CSV
    df_combined.to_csv(path, index=False) # Sauvegarder le fichier mis à jour