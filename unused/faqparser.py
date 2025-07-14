import json

# Buka file JSON
with open("faq_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Ambil semua pertanyaan dan jawaban
examples = [item["examples"].strip() for item in data]
answers = [item["answer"].strip() for item in data]

# Simpan ke dua file terpisah
with open("faq_examples.txt", "w", encoding="utf-8") as f1:
    f1.write("\n".join(examples))

with open("faq_answers.txt", "w", encoding="utf-8") as f2:
    f2.write("\n".join(answers))
