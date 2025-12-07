from transformers import pipeline

# Load the lightweight model
summarizer = pipeline("summarization", model="sshleifer/tiny-t5")

# Your long text to summarize
long_text = """
Paste any long article, notes, or document content here. This can be a paragraph from a textbook, a blog post, or any document you want to shorten.
"""

# Run the summarizer
summary = summarizer(long_text, max_length=130, min_length=30, do_sample=False)

# Show the result
print("Summary:\n", summary[0]['summary_text'])