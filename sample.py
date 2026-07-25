import pickle
import numpy as np

# Load your big pkl file
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Convert precision to float32 (reduces size by 50%) and save as numpy array
similarity_light = similarity.astype(np.float32)
np.save('similarity.npy', similarity_light)

print("Saved compressed matrix as similarity.npy!")