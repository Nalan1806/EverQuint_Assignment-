"""
1.take user input
2.call search()
3.call summarize()
4.display output cleanly
"""

from search import search
from summarize import summarize

def run_rag():
    print("RAG system (type 'exit' to quit)\n")

    while True:
        query=input("Enter your query: ")

        if query.lower() == "exit":
            break

        #step 1: Retrieve documents
        top_docs=search(query)
        
        #step 2: Summarize
        summary = summarize(top_docs)

        #output 
        print("\n --- Retrieved Documents ---")
        for i,doc in enumerate(top_docs,1):
            print(f"\nDocument {i}:")
            print(doc[:200]) #preview

        print("\n ---Summary ---")
        print(summary)
        print("\n" + "="*50 +"\n")


if __name__=="__main__":
    run_rag()