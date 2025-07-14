import json

# Baca dua file txt
with open("faq_examples_id.txt", "r", encoding="utf-8") as f:
    questions = [line.strip() for line in f if line.strip()]

with open("faq_answers_id.txt", "r", encoding="utf-8") as f:
    answers = [line.strip() for line in f if line.strip()]

# Gabungkan jadi list of dict
faq_data = []
for q, a in zip(questions, answers):
    faq_data.append({
        "question": q,
        "answer": a
    })

# Simpan sebagai JSON
with open("faq_combined.json", "w", encoding="utf-8") as f:
    json.dump(faq_data, f, indent=2, ensure_ascii=False)

print("Selesai membuat faq_combined_id.json")
