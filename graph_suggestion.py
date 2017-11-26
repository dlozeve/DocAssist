#!/usr/bin/env python3

import json
import numpy as np
import pandas as pd
import networkx as nx
import difflib

from speech2text import diagnosis


def neighbours_suggestions(graph, current_diagnoses, past_diagnoses):
    # Neighbours of the current diagnosis
    try:
        first = sum(
            [list(nx.all_neighbors(graph, v)) for v in current_diagnoses],
            [])
    except nx.exception.NetworkXError:
        first = []
    # give weight 1
    first = list(zip(first, np.repeat(1, len(first))))
    # Neighbours of the past diagnoses
    try:
        second = sum(
            [list(nx.all_neighbors(graph, v)) for v in past_diagnoses],
            [])
    except nx.exception.NetworkXError:
        second = []
    # give weight 0.5
    second = list(zip(second, np.repeat(0.5, len(second))))
    # Add all the weights in case a diagnosis appears several times
    res = {}
    for code, coef in first + second:
        if code in res:
            res[code] += coef
        else:
            res[code] = coef
    return(res)


g = nx.read_gexf("Diagnoses/clusters.gexf")

df_clusters = pd.read_csv("Diagnoses/df_clusters.csv")
del df_clusters["Unnamed: 0"]

# Look up the current diagnosis in the list of known diagnoses
current_diagnoses = [s for s in df_clusters["display"]
                     for d in diagnosis if d in s]
# If we can't find an exact match, we look at the closest candidates
if len(current_diagnoses) == 0:
    current_diagnoses = difflib.get_close_matches(diagnosis,
                                                  df_clusters["display"], n=2)

# Extract the past diagnoses for our patient
# TODO extract from JSON
patient_file = "Patients_records/fhir/"\
               "Williamson863_Livia674_80.json"
past_diagnoses = []
with open(patient_file, "r") as f:
    parsed_json = json.loads(f.read())
    for entry in parsed_json.get("entry"):
        subentry = entry.get("resource")
        if subentry.get("resourceType") == "Condition":
            past_diagnoses.append(
                subentry.get("code").get("coding")[0].get("code"))

# Generate suggestions by analyzing graph neighbours
suggestions = neighbours_suggestions(g, current_diagnoses, past_diagnoses)
# Sort suggestions by score
suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)

# df_suggestions = []
# for code, weight in suggestions:
#     df_suggestions.append(
#         (code,
#          df_clusters[df_clusters.code == int(code)]["display"],
#          weight))

df_suggestions = pd.DataFrame.from_records(suggestions,
                                           columns=["code", "weight"])
df_suggestions.code = pd.to_numeric(df_suggestions.code)

df_suggestions = pd.merge(df_clusters, df_suggestions, on="code")

# Output our list of suggestions
print(df_suggestions[["display", "weight"]])