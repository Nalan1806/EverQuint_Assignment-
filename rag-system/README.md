# Document Search and Summarization using LLM

## 1. Project Overview

In this project, I built a Retrieval-Augmented Generation (RAG) system that can search through a corpus of documents and generate concise summaries based on user queries.

The system takes a user query as input, retrieves the most relevant documents using a search mechanism, and then summarizes the retrieved content using a transformer-based model.

---

## 2. Data Preparation

I created a corpus of AI and technology-related documents (Artificial Intelligence, Machine Learning, Transformers, etc.) stored in a structured text file.

### Steps taken:

* Organized content into clearly separated documents (`Document 1`, `Document 2`, etc.)
* Removed unnecessary formatting
* Ensured consistent structure for parsing

This made it easier to:

* Load documents efficiently
* Convert them into vectors for search
* Feed them into the summarization model

---

## 3. Document Search Methodology

For document retrieval, I implemented a **TF-IDF-based search system**.

### Steps:

1. Load documents from the dataset
2. Convert documents into TF-IDF vectors
3. Convert the user query into a vector
4. Compute cosine similarity between query and documents
5. Return top-k most relevant documents

### Improvements:

* Used `stop_words='english'` to remove noise
* Used `ngram_range=(1,2)` to improve phrase matching

This approach provides efficient and fast retrieval of relevant documents.

---

## 4. Summarization Approach

For summarization, I used a **transformer-based model (DistilBART)** from HuggingFace.

### Steps:

1. Combine retrieved documents
2. Tokenize input using a pretrained tokenizer
3. Generate summary using the transformer model
4. Decode and return the summary

### Why this approach:

* Produces **abstractive summaries** (not just copying sentences)
* Captures context and meaning better than rule-based methods
* Works locally without requiring API access

---

## 5. Evaluation

I implemented a basic evaluation framework to assess both retrieval and summarization quality.

### Metrics used:

* **Retrieval Accuracy** → checks if relevant keywords appear in retrieved documents
* **Summary Relevance Check** → verifies if summary captures key concepts
* **Jaccard Similarity** → measures overlap between summary and expected keywords

### Observations:

* Retrieval accuracy was high due to TF-IDF effectiveness on structured data
* Summaries were coherent and context-aware due to transformer model

---

## 6. Challenges Faced and Solutions

### 1. API Limitations

Initially, I attempted to use OpenAI APIs for summarization, but faced quota and billing issues.

**Solution:**

* Switched to HuggingFace transformer models (DistilBART)
* Enabled fully local execution without API dependency

---

### 2. Dependency Issues (Transformers)

Faced multiple issues with:

* incompatible transformer versions
* pipeline errors
* Python environment conflicts

**Solution:**

* Used compatible versions of `transformers`, `tokenizers`, and `huggingface_hub`
* Avoided unstable pipeline usage and directly used model + tokenizer

---

### 3. Dataset Design

Initially used very small/simple documents which led to weak retrieval results.

**Solution:**

* Expanded dataset with richer, more descriptive documents
* Improved diversity of topics



---

## 7. How to Run the Project

### Step 1: Install dependencies

```bash
pip install scikit-learn transformers torch
```

### Step 2: Run the system

```bash
python main.py
```

### Step 3: Enter queries

Example:

```
What are transformers?
Explain machine learning
```

---

## 8. Future Improvements

* Use **embedding-based search** instead of TF-IDF for better semantic understanding
* Integrate **API-based LLMs (GPT)** for higher-quality summaries
* Implement **ROUGE score evaluation**
* Add a **web interface** for better user experience

---


