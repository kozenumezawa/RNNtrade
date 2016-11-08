import numpy as np
import tensorflow as tf

def create_data(num_of_samples, sequence_len):
    X = np.zeros((num_of_samples, sequence_len))
    for row_idx in range(nb_of_samples):
        X[row_idx, :] = np.around(np.random.rand(sequence_len)).astype(int)
        t = np.sum(X, axis1)
        return X, t
    
