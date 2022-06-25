import pickle
import numpy as np

with open('confidence_para.pkl', 'rb') as f:
    para_confidence = pickle.load(f) # 단 한줄씩 읽어옴

with open('confidence_non_para.pkl', 'rb') as f:
    non_para_confidence = pickle.load(f) # 단 한줄씩 읽어옴

indexes = [10, 6, 7, 3]
for index in indexes:
    print("index", index)
    print("para conf", para_confidence[index])
    print("non_para conf", non_para_confidence[index])
    print()

