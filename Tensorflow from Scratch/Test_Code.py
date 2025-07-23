import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow logs
import tensorflow as tf

import time
start = time.time()
end = time.time()
print("Import took:", end - start, "seconds")   
print("TF version:", tf.__version__)