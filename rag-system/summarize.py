"""
Approach:
1. Combine retrieved documents
2. Use local transformer model for summarization
"""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# load once (global)
tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")

def summarize(documents, max_sentences=3):
    text = " ".join(documents)

    # truncate to avoid overflow
    inputs = tokenizer(text[:1000], return_tensors="pt", truncation=True)

    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=120,
        min_length=30,
        do_sample=False
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary