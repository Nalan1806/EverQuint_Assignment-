"""
evaluates the retrieval accuracy and summarization quality. 

Purpose: 
-define test cases (query + expected keyword)
-check if retrieved docs contain expected content
- Print simple accuracy results

Note: This is a lightweight evaluation, not production metrics. 
"""

from search import search 
from summarize import summarize


# Test Cases: query + expected keywords
test_cases=[
    ("What is machine learning?", ["machine", "learning"]),
    ("Explain deep learning", ["deep", "learning"]),
    ("What are transformers?", ["transformers", "attention"]),
    ("What is reinforcement learning?", ["reinforcement", "learning"]),
    ("Explain natural language processing", ["language", "processing"]),
]


def jaccard_similarity(text, keywords):
    text_words = set(text.lower().split())
    keyword_words = set(keywords)

    intersection = text_words.intersection(keyword_words)
    union = text_words.union(keyword_words)

    if len(union) == 0:
        return 0

    return len(intersection) / len(union)


def evaluate():
    retrieval_correct = 0

    print("Running Evaluation... \n")

    for i,(query,keywords) in enumerate(test_cases,1):
        print(f"Test Case {i}")
        print(f"Query: {query}")

        docs = search(query)
        summary = summarize(docs)

        retrieved_text = " ".join(docs).lower()
        summary_text = summary.lower()

        # Retrieval Check
        if any(k in retrieved_text for k in keywords):
            print("Retrieval: Correct")
            retrieval_correct += 1
        else: 
             print("Retrieval: Incorrect")

        # Summary Semantic Check
        if any(k in summary_text for k in keywords):
            print("Summary Relevance: Good")
        else:
            print("Summary Relevance: Weak")

        # JACCARD SCORE
        score = jaccard_similarity(summary_text, keywords)
        print(f"Jaccard Score: {score:.2f}")

        print("\nSummary:")
        print(summary)

        print("\n"+"-"*60+"\n")

    accuracy = retrieval_correct / len(test_cases)
    print(f"Final Retrieval Accuracy: {accuracy:.2f}")


if __name__=="__main__":
    evaluate()