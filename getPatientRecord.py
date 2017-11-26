from config import config_path
import json

def get_past_diagnosis(patient_id):
    config = config_path()

    patients_files = json.loads(open(config.patient_dict).read())
    history = patients_files[patient_id]

    return(history)

def get_current_goals(patient_id)
    config = config_path()

    goals_file = json.loads(open(config.goals_dict).read())
    goals = goals_file[patient_id]

    return (goals)


