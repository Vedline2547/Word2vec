import gensim
from gensim.models import Word2Vec,KeyedVectors
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
model = KeyedVectors.load_word2vec_format(r'C:\Users\HP\Desktop\New ML\Word2vec\GoogleNews-vectors-negative300.bin.gz',binary=True,limit=100000)
print(model['man'])
print(model['man'].shape)
print(model['glass'].shape)
print(model.most_similar('man'))
print(model.most_similar('cricket'))
print(model.most_similar('facebook'))
print(model.most_similar('woman'))
print(model.similarity('man','woman'))
print(model.similarity('Python','man'))
print(model.doesnt_match(['JAVA','Python','Elephant']))
vec = model['king'] - model['man'] + model['woman']
print(model.most_similar(vec))

words = ['queen','woman','girl','boy','man','water','king']
embeddings = np.array([
    model['queen'][0:50],
    model['woman'][0:50],
    model['girl'][0:50],
    model['boy'][0:50],
    model['man'][0:50],
    model['water'][0:50],
    model['king'][0:50],
])

df = pd.DataFrame(embeddings,index=words)
plt.figure(figsize=(18,6))
heatmap = sns.heatmap(df,cmap='crest')
plt.show()