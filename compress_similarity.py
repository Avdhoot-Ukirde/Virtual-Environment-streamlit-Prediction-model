import pickle
import joblib
import os

# Load original similarity file
with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# Save compressed version
joblib.dump(similarity, "similarity_compressed.pkl", compress=3)

# Show file sizes
print("Original size:", os.path.getsize("similarity.pkl") / (1024 * 1024), "MB")
print("Compressed size:", os.path.getsize("similarity_compressed.pkl") / (1024 * 1024), "MB")
