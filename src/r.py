import pandas as pd
import numpy as np
import os
from constants import DATA_DIR

users_dict = np.load(os.path.join(DATA_DIR,'user_dict_final.npy'), allow_pickle=True)
users_history_lens = np.load(os.path.join(DATA_DIR,'users_history_lens_dict_final.npy'), allow_pickle=True)
