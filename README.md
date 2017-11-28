# DocAssist

This is a project made for [OxfordHack](http://oxfordhack.com/) 2017.

DocAssist is an application facilitating consultations for
doctors. Medical practitioners are faced with an increasing amount of
bureaucracy, and find it hard to keep records on every consultation,
to follow each patient's diagnoses, and to keep up-to-date with recent
developments in medical research.

DocAssist works in four stages:

- The entire consultation is recorded, as a dialogue between the
  doctor and the patient. The consultation is conveniently subdivided
  into six separate steps (history, examination, tests, diagnosis,
  treatment, and summary).
- A speech recognition service
  [(Microsoft Cognitive Services API)](https://azure.microsoft.com/en-us/services/cognitive-services/speech/)
  is run on the recordings, extracting meaningful data and generating
  automatically a record of the consultation for regulatory purposes.
- A recommendation system, based on clusters of common diagnoses
  extracted from a database of patient records, presents the doctor
  with an ordered list of diagnoses commonly associated with the
  current one. For instance, gall stones are commonly associated with
  diabetes, and thus DocAssist might encourage the doctor to look into
  tests for diabetes.
- The final diagnosis is used to match relevant papers in the medical
  literature. We use
  [MedLine's](https://www.nlm.nih.gov/bsd/pmresources.html) API and
  ElasticSearch on a local database.

Instructions to run:

- speech2text.py will launch speech recognition on the files in the
  Audio_recordings folder.
- graph_suggestion.py will use the graph with its communities in
  Diagnoses/ to return suggestions of potential diagnoses based on the
  current diagnosis and the patient's history.
- mainSearch.py will launch a medical research papers search based on
  a local database (with ElasticSearch) and on Medline's API.
