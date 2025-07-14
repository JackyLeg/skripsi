import json
import random
from typing import Any, Dict, List, Text, Union, Set
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import EventType

PATH_JSON = "data/produk_flipkart.json"

def baca_data_produk():
    try:
        with open(PATH_JSON, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error: {e}")
        return []

class ActionTampilkan10ProdukRandom(Action):
    def name(self) -> Text:
        return "action_tampilkan_10_produk_random"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data = baca_data_produk()
        if not data:
            dispatcher.utter_message(text="Maaf, tidak dapat membaca data produk.")
            return []

        random_produk = random.sample(data, 10)
        pesan = "\n".join([f"{p['id']}: {p['nama']}" for p in random_produk])
        dispatcher.utter_message(text="Berikut 10 produk acak:\n" + pesan)
        return []

class ActionPilihProduk(Action):
    def name(self) -> Text:
        return "action_pilih_produk"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        produk_id = tracker.get_slot("produk_id")
        data = baca_data_produk()
        produk = next((p for p in data if str(p["id"]) == str(produk_id)), None)

        if not produk:
            dispatcher.utter_message(text="Produk tidak ditemukan.")
            return []

        dispatcher.utter_message(text=f"Produk '{produk['nama']}' telah dipilih.")
        return [
            SlotSet("produk_id", produk["id"]),
            SlotSet("nama", produk["nama"]),
            SlotSet("kategori", produk.get("kategori")),
            SlotSet("harga", produk.get("harga")),
            SlotSet("harga_awal", produk.get("harga_awal")),
            SlotSet("deskripsi", produk.get("deskripsi")),
            SlotSet("gambar", produk.get("gambar")),
            SlotSet("url", produk.get("url")),
            SlotSet("brand", produk.get("brand")),
        ]
        

class ActionMultiInfoProduk(Action):
    def name(self) -> Text:
        return "action_multi_info_produk"

    # cache kandidat internal per session
    intent_kandidat: List[Set[str]] = []

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[EventType]:

        user_input = tracker.latest_message.get("text", "").strip().replace(" ", "")
        user_intents = set(user_input.split("+"))

        # Cek apakah input user cocok dengan kandidat sebelumnya
        for kandidat in self.intent_kandidat:
            if user_intents == kandidat:
                self.intent_kandidat = []  # reset
                return self._jawab_intents(list(user_intents), tracker, dispatcher)

        # Ambil intent ranking dari fallback
        ranking = tracker.latest_message.get("intent_ranking", [])
        kandidat_names = [r["name"] for r in ranking if r["name"] != "nlu_fallback"][:2]

        if len(kandidat_names) >= 2:
            kandidat_sets = [set(name.split("+")) for name in kandidat_names]
            self.intent_kandidat = kandidat_sets

            dispatcher.utter_message(
                text="Apa maksud Anda?",
                buttons=[
                    {"title": name.replace("+", " + "), "payload": name}
                    for name in kandidat_names
                ]
            )
        else:
            dispatcher.utter_message(text="Maaf, saya tidak yakin dengan maksud Anda.")

        return []

    def _jawab_intents(self, intents: List[str], tracker: Tracker,
                        dispatcher: CollectingDispatcher) -> List[EventType]:

        # Ambil semua slot produk
        harga = tracker.get_slot("harga")
        harga_awal = tracker.get_slot("harga_awal")
        kategori = tracker.get_slot("kategori")
        deskripsi = tracker.get_slot("deskripsi")
        gambar = tracker.get_slot("gambar")
        url = tracker.get_slot("url")
        brand = tracker.get_slot("brand")

        for i in intents:
            if i == "tanya_harga":
                if harga_awal and harga_awal != harga:
                    dispatcher.utter_message(
                        text=f"Harga produk ini adalah Rp {harga} (diskon dari Rp {harga_awal}).\n"
                    )
                else:
                    dispatcher.utter_message(text=f"Harga produk ini adalah Rp {harga}.")
            elif i == "tanya_diskon":
                if harga_awal and harga_awal != harga:
                    potongan = int(harga_awal) - int(harga)
                    dispatcher.utter_message(text=f"Produk ini sedang diskon sebesar Rp {potongan}.")
                else:
                    dispatcher.utter_message(text="Produk ini tidak sedang diskon.")
            elif i == "tanya_kategori":
                dispatcher.utter_message(text=f"Produk ini termasuk dalam kategori: {kategori}.")
            elif i == "tanya_deskripsi":
                dispatcher.utter_message(text=f"Deskripsi produk: {deskripsi}")
            elif i == "tanya_gambar":
                if gambar:
                    dispatcher.utter_message(text="Ini gambar produk yang tersedia:")
                    for g in gambar[:2]:
                        dispatcher.utter_message(image=g)
                else:
                    dispatcher.utter_message(text="Maaf, gambar produk tidak tersedia.")
            elif i == "tanya_url":
                dispatcher.utter_message(text=f"Kamu bisa melihat detail produk di sini: {url}")
            elif i == "tanya_brand":
                dispatcher.utter_message(text=f"Brand dari produk ini adalah: {brand}")
            else:
                dispatcher.utter_message(text=f"Maaf, belum ada jawaban untuk '{i}'.")

        return []
