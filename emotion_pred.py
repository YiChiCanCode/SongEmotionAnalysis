import pickle

import librosa
import numpy as np
from Feature_Extraction import extract_feature
import random

def convert_emojis(emotion):
    # 0: angry 1: happy 2: relaxed 3: sad
    happy = ["&#128515", "&#128516", "&#128518", "&#128522", "&#128513", "&#128512"]
    angry = ["&#128530", "&#128544", "&#128545", "&#128547"]
    relaxed = ["&#128521", "&#128578"]
    sad = ["&#128532", "&#128534", "&#128542", "&#128546"]
    if emotion == 0:
        return random.choice(angry)
    elif emotion == 1:
        return random.choice(happy)
    elif emotion == 2:
        return random.choice(relaxed)
    else:
        return random.choice(sad)


MODEL_PATH = "knn_model.sav"
SONG_PATH = "Linkin Park - Easier to run.mp3"

kNN = pickle.load(open(MODEL_PATH, 'rb'))

song_df = extract_feature(SONG_PATH)
prediction_prob = kNN.predict_proba(song_df)
prediction = kNN.predict(song_df)
# print(prediction)
# # print(prediction_prob)


prominent = 0
prominent_idx = -1
second_prominent = 0
for i, e in enumerate(prediction_prob[0]):
    if e != 0:
        if e > prominent:
            prominent_idx = i
            prominent = max(e, prominent)
res = np.delete(prediction_prob[0], prominent_idx)
for e in res:
    second_prominent = max(e, second_prominent)

second_prominent_idx = np.where(prediction_prob[0] == second_prominent)[0][0]

print(f"prominent: {convert_emojis(prominent_idx)}, second: {convert_emojis(second_prominent_idx)}")
