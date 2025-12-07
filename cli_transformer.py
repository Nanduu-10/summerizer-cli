import argparse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def summarize_text(text, model_name="t5-small"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    if "t5" in model_name:
        text = "summarize: " + text

    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    ids = model.generate(
        inputs["input_ids"],
        max_length=120,
        min_length=20,
        num_beams=4
    )
    return tokenizer.decode(ids[0], skip_special_tokens=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--model", default="t5-small")
    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as f:
        data = f.read()

    print("Loaded text length:", len(data))
    print("\nGenerating summary...\n")
    print(summarize_text(data, args.model))

if __name__ == "__main__":
    main()
