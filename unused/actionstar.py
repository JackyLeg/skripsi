# import pandas as pd
from charset_normalizer import from_path
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
import json
from pathlib import Path
import random
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sentence_transformers import SentenceTransformer, util

#direktori awal
current_dir = Path(__file__).parent

class ActionGreetUser(Action):
    def name(self) -> Text:
        return "action_menyapa"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_sapa")
        return []


class ActionSaveNama(Action):
    def name(self) -> str:
        return "action_save_nama"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get('text')
        nama_pengguna = user_message.split()[-1]
        dispatcher.utter_message(response=f"utter_sapa_nama")
        return [SlotSet(key = "nama_pengguna", value = nama_pengguna)]


class ActionTampilkanProduk(Action):
    def name(self) -> Text:
        return "action_tampilkan_produk"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Ambil jenis produk dari entity
        jenis_produk = next(tracker.get_latest_entity_values("jenis_produk"), None)

        if not jenis_produk:
            dispatcher.utter_message(text="Maaf, saya tidak tahu jenis produk apa yang Anda cari.")
            return []

        json_path = current_dir / f"produk_{jenis_produk.lower()}.json"

        if not json_path.exists():
            dispatcher.utter_message(text=f"Maaf, kami belum punya data untuk produk {jenis_produk}.")
            return []

        # Baca file JSON
        with open(json_path, "r", encoding="utf-8") as file:
            produk_data = json.load(file)

        # Pilih 5 produk secara acak
        produk_acak = random.sample(produk_data, min(5, len(produk_data)))
        buttons = []
        for produk in produk_acak:
            produk_id = produk.get("ID")
            nama = produk.get("nama")
            harga = produk.get("harga")
            buttons.append({
                "title": f"{nama} - {harga}",
                "payload": f'/pilih_produk{{"produk_id":"{produk_id}"}}'
            })

        dispatcher.utter_message(
            text=f"Berikut 5 produk {jenis_produk} pilihan kami:",
            buttons=buttons
        )

        return []



class ActionFaqSemantic(Action):
    def name(self) -> Text:
        return "action_faq_semantic"

    def __init__(self):
        # Load model dan FAQ saat inisialisasi (sekali saja)
        self.model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")  # Bisa ganti ke model lain
        faq_path = current_dir / "faq_combined.json"

        with open(faq_path, "r", encoding="utf-8") as f:
            self.faq_data = json.load(f)
        
        self.questions = [item["question"].lstrip("- ").strip() for item in self.faq_data]
        self.answers = [item["answer"] for item in self.faq_data]
        self.embeddings = self.model.encode(self.questions, convert_to_tensor=True)

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message.get("text")
        if not user_message:
            dispatcher.utter_message(text="Maaf, saya tidak mengerti pertanyaan Anda.")
            return []

        query_embedding = self.model.encode(user_message, convert_to_tensor=True)
        cosine_scores = util.pytorch_cos_sim(query_embedding, self.embeddings)[0]

        best_match_idx = int(np.argmax(cosine_scores))
        best_score = float(cosine_scores[best_match_idx])

        if best_score < 0.60:
            dispatcher.utter_message(text="Maaf, saya belum bisa menemukan jawaban yang sesuai.")
        else:
            best_answer = self.answers[best_match_idx]
            dispatcher.utter_message(text=best_answer)

        return []





# # Load dataset once when the action server starts
# encoding = from_path("data/flipkart_com-ecommerce_sample.csv").best().encoding
# PRODUCT_DATA = pd.read_csv("data/flipkart_com-ecommerce_sample.csv", encoding=encoding)



# class ActionSearchProduct(Action):

#     def name(self) -> Text:
#         return "action_search_product"

#     def run(self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: DomainDict) -> List[Dict[Text, Any]]:

#         # Get slots/entities from the user message
#         brand = tracker.get_slot("brand")
#         product_type = tracker.get_slot("product_type")
#         user_message = tracker.latest_message.get("text")

#         # Filter logic
#         df = PRODUCT_DATA

#         if brand:
#             df = df[df["brand"].str.contains(brand, case=False, na=False)]
#         if product_type:
#             df = df[df["product_name"].str.contains(product_type, case=False, na=False)]

#         # Optional fallback to raw text
#         if df.empty and not (brand or product_type):
#             df = PRODUCT_DATA[PRODUCT_DATA["product_name"].str.contains(user_message, case=False, na=False)]

#         # Handle responses
#         if df.empty:
#             dispatcher.utter_message(text="Maaf, saya tidak menemukan produk yang sesuai.")
#             return []

#         # Show top 3 products
#         top_matches = df.head(3)
#         response = "Berikut produk yang saya temukan:\n\n"

#         for _, row in top_matches.iterrows():
#             name = row.get("product_name", "Tidak diketahui")
#             price = row.get("discounted_price", "N/A")
#             url = row.get("product_url", "#")
#             brand = row.get("brand", "-")
#             category = row.get("product_category_tree", "-")

#             response += f"🛍️ *{name}*\n"
#             response += f"🏷️ Merek: {brand}\n"
#             response += f"💸 Harga: Rp {price}\n"
#             response += f"📦 Kategori: {category}\n"
#             response += f"🔗 [Lihat Produk]({url})\n\n"

#         dispatcher.utter_message(text=response)
#         return []
