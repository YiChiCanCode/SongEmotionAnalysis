import pickle

import librosa
import numpy as np
from Feature_Extraction import extract_feature

MODEL_PATH = "knn_model.sav"
SONG_PATH = "Linkin Park - Easier to run.mp3"

kNN = pickle.load(open(MODEL_PATH, 'rb'))

song_df = extract_feature(SONG_PATH)
prediction_prob = kNN.predict_proba(song_df)
prediction = kNN.predict(song_df)
# print(prediction)
# # print(prediction_prob)

for i, e in enumerate(prediction_prob[0]):
    if e != 0:
        if i == 0:
            print(f"angry: {e}")
        elif i == 1:
            print(f"happy: {e}")
        elif i == 2:
            print(f"relaxed: {e}")
        elif i == 3:
            print(f"sad: {e}")

