# PookiePicks
A fast, self-contained movie recommendation engine deployed with Flask, Pandas, and Scikit-Learn. Uses memory-mapped vector similarity to deliver instant recommendations without external API dependencies.
## 🛠️ Tech Stack

## 🛠️ Tech Stack

### **Backend & Core Logic**
* ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) **Python** – Primary programming language.
* ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) **Flask** – Lightweight web framework for handling routes and request processing.
* ![NLTK](https://img.shields.io/badge/NLTK-154360?style=for-the-badge&logo=python&logoColor=white) **NLTK** – Natural language processing for keyword stemming and tokenization.
* ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) **NumPy** – Memory-mapped array processing (`.npy`) for ultra-fast, low-RAM vector reads.
* ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) **Pandas** – Data manipulation and movie metadata mapping.
* ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) **Scikit-Learn** – Text vectorization (CountVectorizer) & Cosine similarity matrix computations.

---

### **Frontend & User Interface**
* ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) **HTML5 / Jinja2** – Templating engine for rendering dynamic search results.
* ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) **CSS3** – Custom responsive styling.

  ### ⚡ Performance Highlights
* **Zero External APIs:** Runs completely self-contained without rate limits or API key dependencies.
* **Low Memory Footprint:** Uses precision-optimized NumPy matrix files to handle thousands of similarity vectors on minimal RAM.
### 🎯 Step-by-Step Breakdown

1. **Data Cleaning & Tag Extraction:** Extracted genres, keywords, top cast, and director from the dataset, combining them into a unified `tags` string for each movie.
2. **Text Normalization (NLTK):** Applied stemming using `nltk.stem.porter.PorterStemmer` to convert words to their root forms (e.g., `"actions"` $\rightarrow$ `"action"`).
3. **Feature Extraction:** Converted text tags into numeric feature vectors using `CountVectorizer`.
4. **Similarity Computation:** Generated a pairwise Cosine Similarity matrix using Scikit-Learn to evaluate relative movie proximity.
5. **Memory-Mapped Inference:** Saved the similarity matrix as a `.npy` file to enable low-RAM, lightning-fast row lookups inside the Flask app.
