from datasets import load_dataset
import json

# Load dataset dari Hugging Face
dataset = load_dataset("Andyrasika/Ecommerce_FAQ")
faq_data = dataset['train']  # gunakan bagian 'train'

# Format ulang agar sesuai dengan Rasa
formatted_data = []
for item in faq_data:
    formatted_data.append({
        "intent": "faq",
        "examples": f"- {item['question']}",
        "answer": item['answer']
    })

# Simpan ke file JSON (opsional)
with open("faq_data.json", "w", encoding="utf-8") as f:
    json.dump(formatted_data, f, indent=4, ensure_ascii=False)
