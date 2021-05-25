from datetime import datetime
import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from pcg_ppg_analysis import data
from tqdm import tqdm

if ('darwin' in sys.platform):
    # BASE_PATH = Path('/') / 'Volumes' / 'Dati' / 'Users' / \
    #    'Data-out' / 'Dati_Bovio' / 'subjects_Mauri_Orlando'
    BASE_PATH = Path('/') / 'Volumes' / 'Storage' / 'Polimi' / \
        'HeartSounds' / 'subjects_Mauri_Orlando'
else:
    BASE_PATH = Path('..')

if (not BASE_PATH.exists()):
    print(f'{BASE_PATH} does not exist.')

force_rewrite = False
load_raw_data = False
if load_raw_data:
    for subject in tqdm(BASE_PATH.iterdir(), total=len(os.listdir(BASE_PATH))):
        if (subject.is_dir()):
            if (((subject / 'subject_data.csv').exists() and force_rewrite) or (not (subject / 'subject_data.csv').exists())):
                pcg = data.load_pcg(subject / 'pcg')
                ppg = data.load_ppg(subject / 'ppg')
                subject_df = pd.DataFrame(pcg, columns=['PCG'])
                subject_df.loc[:, 'PPG'] = ppg
                subject_df.to_csv(subject/'subject_data.csv', index=False)
                subject_info = data.load_recording_info(subject / 'note')
                # with open((subject / 'subject_info.json'), 'w') as f:
                #        json.dump(subject_info, f)
