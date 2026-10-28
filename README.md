# Word2Vec Word Embeddings

## 📌 Overview
This project explores pretrained Word2Vec word embeddings using Gensim and the Google News Word2Vec model. It demonstrates how words can be represented as numerical vectors and how these representations capture semantic relationships between words.

The project covers word similarity, nearest-word searches, word analogies, and visualization of word embeddings using heatmaps.

## 🎯 Objectives
- Load pretrained Word2Vec embeddings using Gensim.
- Explore numerical word representations and vector dimensions.
- Find semantically similar words.
- Calculate cosine similarity between words.
- Perform word analogy tasks using vector arithmetic.
- Identify outlier words in a group.
- Visualize embedding values and word similarities using heatmaps.

## 🛠️ Technologies Used
- Python
- Gensim
- NumPy
- Pandas
- Matplotlib
- Seaborn

## 🧠 Key Concepts

### 1. Word Embeddings
Represent words as dense numerical vectors. The pretrained Google News model uses 300-dimensional vectors.

### 2. Semantic Similarity
Use cosine similarity to measure the similarity between word vectors.

### 3. Word Analogies
Explore relationships using vector arithmetic, such as:

`king - man + woman ≈ queen`

### 4. Word Similarity and Outlier Detection
Retrieve similar words and identify words that differ semantically from a group.

### 5. Embedding Visualization
Use heatmaps to visualize selected embedding dimensions and cosine similarity scores between words.

## 📂 Project Structure

```text
Word2Vec/
├── main.py
├── README.md
└── .gitignore
```

The pretrained model is stored locally and excluded from GitHub because of its large file size.

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install gensim numpy pandas matplotlib seaborn
```

### 2. Download the pretrained model

Obtain the Google News Word2Vec model:

`GoogleNews-vectors-negative300.bin.gz`

Place the file in your local model directory. Update the file path in your Python script accordingly.

### 3. Run the project

```bash
main.py
```

**Note:** The full pretrained model is large and may require substantial RAM. The project uses `limit=100000` to load up to 100,000 word vectors.

## 📊 Expected Results
- Numerical vector representations for selected words.
- Lists of words with similar embeddings.
- Cosine similarity scores between words.
- Word analogy results.
- Heatmaps showing embedding values and pairwise word similarities.

## 📚 Learning Outcomes
This project strengthens practical understanding of word embeddings, vector operations, semantic similarity, and exploratory NLP visualization.

## 👤 Author
Vedline Ochieng

GitHub: [@Vedline2547](https://github.com/Vedline2547)

---

*This project is part of my ongoing journey in Machine Learning and Natural Language Processing.*
