from transformers import pipeline

# Load the tiny model (fast and demo-friendly)
summarizer = pipeline("summarization", model="t5-small")

def summarize_chunk(chunk, style="concise"):
    prompt = "summarize: " + chunk
    result = summarizer(prompt, max_length=100, min_length=30, do_sample=False)
    return result[0]["summary_text"]

def consolidate_summaries(summaries, style="concise"):
    mega_text = " ".join(summaries)
    prompt = "summarize: " + mega_text
    result = summarizer(prompt, max_length=120, min_length=40, do_sample=False)
    return result[0]["summary_text"]