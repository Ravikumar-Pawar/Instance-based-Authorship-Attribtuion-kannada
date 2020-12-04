import numpy as np
import nltk
import glob
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from scipy.cluster.vq import whiten
import os
#data reading mutilple files
#hrudayashiva-instance-->01-12
#ravi beligeri-isntance-->13-25
#somashaker-isntance-->26-36

data_folder = "C://Users/RAVIKUMAR/PycharmProjects/Authorship_Attribution_Instance/Data_2"
files = sorted(glob.glob(os.path.join(data_folder, "instance*.txt")))
chapters = []
for fn in files:
    with open(fn, encoding="utf-8") as f:
        chapters.append(f.read().replace('\n', ' '))
        all_text = ' '.join(chapters)
print(chapters)
# print(all_text)
#feature vector
