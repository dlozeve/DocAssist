from config import config_path
import json

def get_past_diagnosis(patient_id):
    config = config_path()

    patients_files = json.loads(open(config.patient_dict).read())
    history = patients_files[patient_id]

    return(history)

def get_current_goals():
    config = config_path()

    goals_file = json.loads(open(config.goals_dict).read())
    goals = goals_file[config.patient_id]

    if len(goals) == 0:
        return(('goals: example: Hba1c level < 7;'))
    else:
        return(('goals:' + '\n'.join(goals) + ';'))

# print(get_current_goals())


