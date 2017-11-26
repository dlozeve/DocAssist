#!/usr/bin/env python3

# Record audio with:
# rec -c 1 -e unsigned -r 16000 speech.wav

import os
import requests
import glob
import json
import difflib
import pandas as pd

import api_keys

# Define the data directories.
audio_dir = 'Audio_recordings/example1'
transcripts_dir = 'Transcripts'

# Set up the parameters for the Speech API requests.
url = 'https://speech.platform.bing.com/speech/recognition/'\
      'conversation/cognitiveservices/v1?language=en-US&format=detailed'

headers = {'Ocp-Apim-Subscription-Key': api_keys.SPEECH_API_KEY,
           'Transfer-Encoding': 'chunked',
           'Content-type': 'audio/wav; codec=audio/pcm; samplerate=16000'}

# For each step of the consultation, we transcribe the recordings.
# Each step has to be recorded in several files because of the API's
# limitation to 15s.
# We write the transcribed text to a file.

history_txt = ''
for filename in glob.glob(os.path.join(audio_dir, 'history*.wav')):
    with open(filename, 'rb') as payload:
        r = requests.post(url, params=headers, data=payload)
        interpretation = r.json().get('NBest')[0]
        history_txt += interpretation.get('Display')
with open(os.path.join(transcripts_dir, 'history.txt'), 'w') as f:
    f.write(history_txt)

examination_txt = ''
for filename in glob.glob(os.path.join(audio_dir, 'examination*.wav')):
    with open(filename, 'rb') as payload:
        r = requests.post(url, params=headers, data=payload)
        interpretation = r.json().get('NBest')[0]
        examination_txt += interpretation.get('Display')
with open(os.path.join(transcripts_dir, 'examination.txt'), 'w') as f:
    f.write(examination_txt)

tests_txt = ''
for filename in glob.glob(os.path.join(audio_dir, 'tests*.wav')):
    with open(filename, 'rb') as payload:
        r = requests.post(url, params=headers, data=payload)
        interpretation = r.json().get('NBest')[0]
        tests_txt += interpretation.get('Display')
with open(os.path.join(transcripts_dir, 'tests.txt'), 'w') as f:
    f.write(tests_txt)

diagnosis_txt = ''
for filename in glob.glob(os.path.join(audio_dir, 'diagnosis*.wav')):
    with open(filename, 'rb') as payload:
        r = requests.post(url, params=headers, data=payload)
        interpretation = r.json().get('NBest')[0]
        diagnosis_txt += interpretation.get('Display')
with open(os.path.join(transcripts_dir, 'diagnosis.txt'), 'w') as f:
    f.write(diagnosis_txt)

treatment_txt = ''
for filename in glob.glob(os.path.join(audio_dir, 'treatment*.wav')):
    with open(filename, 'rb') as payload:
        r = requests.post(url, params=headers, data=payload)
        interpretation = r.json().get('NBest')[0]
        treatment_txt += interpretation.get('Display')
with open(os.path.join(transcripts_dir, 'treatment.txt'), 'w') as f:
    f.write(treatment_txt)

summary_txt = ''
for filename in glob.glob(os.path.join(audio_dir, 'summary*.wav')):
    with open(filename, 'rb') as payload:
        r = requests.post(url, params=headers, data=payload)
        interpretation = r.json().get('NBest')[0]
        summary_txt += interpretation.get('Display')
with open(os.path.join(transcripts_dir, 'summary.txt'), 'w') as f:
    f.write(summary_txt)


# Parameters for the keyPhrases API

payload = {"documents":
           [
               {
                   "language": "en",
                   "id": 1,
                   "text": diagnosis_txt
               }
           ]}

url = 'https://westeurope.api.cognitive.microsoft.com/'\
      'text/analytics/v2.0/keyPhrases'

headers = {'Ocp-Apim-Subscription-Key': api_keys.KEYPHRASES_API_KEY,
           'Content-Type': 'application/json',
           'Accept': 'application/json'}

r = requests.post(url, headers=headers, data=json.dumps(payload))

diagnosis = r.json().get('documents')[0].get('keyPhrases')

df_clusters = pd.read_csv("Diagnoses/df_clusters.csv")
del df_clusters["Unnamed: 0"]

diagnosis = ["diabetes"]

# Look up the current diagnosis in the list of known diagnoses
current_diagnoses = [s for s in df_clusters["display"]
                     for d in diagnosis if d in s]
# If we can't find an exact match, we look at the closest candidates
if len(current_diagnoses) == 0:
    current_diagnoses = difflib.get_close_matches(diagnosis,
                                                  df_clusters["display"], n=2)

# Write the diagnosis to a file
print(current_diagnoses.join('\n'))
with open(os.path.join(transcripts_dir, 'diagnosis_keyphrase.txt'), 'w') as f:
    f.write(str(current_diagnoses))
