from googletrans import Translator  # pip install googletrans==4.0.0-rc1

# 1. Baca file jawaban FAQ dalam bahasa Inggris
with open("faq_answers.txt", "r", encoding="utf-8") as f:
    english_answers = [line.strip() for line in f if line.strip()]

# 2. Inisialisasi translator
translator = Translator()

# 3. Terjemahkan semua jawaban
translated_answers = [translator.translate(a, src='en', dest='id').text for a in english_answers]

# 4. Simpan ke file baru
with open("faq_answers_id.txt", "w", encoding="utf-8") as f:
    for a in translated_answers:
        f.write(a + "\n")

print("✅ Selesai! Jawaban telah diterjemahkan ke 'faq_answers_id.txt'")
