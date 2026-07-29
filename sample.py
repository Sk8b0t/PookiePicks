import pickle
import numpy as np

similarity = pickle.load(open('similarity.pkl', 'rb'))
similarity_light = similarity.astype(np.float32)
np.save('similarity.npy', similarity_light)
