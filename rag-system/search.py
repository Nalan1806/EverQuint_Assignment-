"""
steps: 
1.load documents
2.Convert to vectors (TF-IDF)
3.Convert query to vector
4.Compute similarity
5.Return top-k docs

"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_documents(path="data/documents.txt"):
    """load and split documents from file"""

    with open(path,"r",encoding="utf-8") as f:
        content=f.read()

    #split by "Document X: "
    raw_docs=content.split("Document")
    documents=[]

    for doc in raw_docs:
            doc=doc.strip()
            if doc == "":
                continue

            #Remove "1: " etc
            parts=doc.split(":",1)
            if len(parts)>1:
                documents.append(parts[1].strip())

    return documents

def search(query,k=3):
     """
     return top-k relevant documents for a query
     """

     documents=load_documents()



     #convert documents to TF-IDF vectors
     vectorizer=TfidfVectorizer(stop_words='english',ngram_range=(1,2))
     doc_vectors=vectorizer.fit_transform(documents)

     #convert query to vector
     query_vector = vectorizer.transform([query])

     #compute cosine similarity
     similarities= cosine_similarity(query_vector,doc_vectors).flatten()

     #get top-k document indices
     top_indices = similarities.argsort()[-k:][::-1]

     #Return top documents
     top_docs=[documents[i] for i in top_indices]

     return top_docs
    



