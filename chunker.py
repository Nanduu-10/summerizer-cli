import re
def split_into_chunks(text, max_tokens=800, overlap=100):
    words = re.findall(r"\S+", text)
    chunks = []
    i = 0
    while i < len(words):
        end = min(i + max_tokens, len(words))
        chunk = " ".join(words[i:end])
        chunks.append(chunk)
        i = max(0, end - overlap)
    return chunks