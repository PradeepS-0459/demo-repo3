import pandas as pd 
import numpy as np

embeddings_1=[1,2,3]
embeddings_2=[1,2,3]


similarity=np.dot(embeddings_1,embeddings_2)/(np.linalg.norm(embeddings_1)*np.linalg.norm(embeddings_2))


print("Cosine similarity : ", similarity)