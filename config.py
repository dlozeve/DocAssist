import os

class config_path:
    def __init__(self):
        """
        All useful paths for the app
        """
        self.wd = os.path.abspath('')

        self.research_papers = os.path.join(self.wd,
                                            os.path.join('Medical_papers', 'full_paper_details.csv'))

        self.patient_id = '208e7a5f-5036-482b-ae1b-9e1ef12bb04b'

        self.speech2text_dir = os.path.join(self.wd, 'Transcripts')
        self.transcript_H = os.path.join(self.speech2text_dir, '')
        self.transcript_E = os.path.join(self.speech2text_dir, '')
        self.transcript_T = os.path.join(self.speech2text_dir, '')
        self.transcript_D = os.path.join(self.speech2text_dir, 'diagnosis_keyphrase.txt')
        self.transcript_P = os.path.join(self.speech2text_dir, '')
        self.transcript_S = os.path.join(self.speech2text_dir, '')

        self.patient_records = os.path.join(self.wd, 'Patients_records')
        self.patient_dict = os.path.join(self.patient_records, 'patient_dict.json')
        self.goals_dict = os.path.join(self.patient_records, 'goals_dict.json')
        self.diagnosis_codes = os.path.join(self.patient_records, '')

        self.diagnoses = os.path.join(self.wd, 'Diagnoses')
        self.diagnosis_dict = os.path.join(self.diagnoses, 'diagnosis_dict.json')
        self.diagnosis_network = os.path.join(self.diagnoses, 'clusters.gexf')
        self.clusters = os.path.join(self.diagnoses, 'df_clusters.csv')

        self.audio = os.path.join(self.wd, 'Audio_recordings')
        self.audio1 = os.path.join(self.audio, 'example1')

        # ES settings
        self.logs_dir = os.path.join(self.wd, 'logs')
        self.host = 'localhost'
        self.port = 9200
        self.index = "medical_papers"
        self.doc_type = "ref"
