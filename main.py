from pathlib import Path
from pcg_ppg_analysis import data

MAIN_FILE_PATH = Path('/') / 'Volumes' / 'Dati' / 'Users' / 'Data-out' / 'Dati_Bovio'
MAIN_DATA_PATH = MAIN_FILE_PATH / 'subjects_Mauri_Orlando'

for subject_folder in MAIN_DATA_PATH.iterdir():
    if (subject_folder.is_dir()):
        recording_info = data.load_recording_info(subject_folder / 'note')  
        pcg = data.load_pcg(subject_folder / 'PCG')
        ppg = data.load_ppg(subject_folder / 'PPG')
        