# # import json
# # from typing import Any, Text, Dict, List
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# # from rasa_sdk.events import SlotSet
# # import random
# # import re


# # class ActionGreetUser(Action):
# #     def name(self) -> Text:
# #         return "action_greet_user"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Menyapa pengguna dan meminta nama
# #         dispatcher.utter_message(response="utter_pembuka")

# #         return []

# # class ActionSaveNama(Action):

# #     def name(self) -> str:
# #         return "action_save_nama"

# #     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
# #         # Mengambil pesan terakhir dari pengguna
# #         user_message = tracker.latest_message.get('text')
        
# #         # Mengambil nama dari input (misalkan nama adalah kata terakhir dari input)
# #         # Ini bisa disesuaikan sesuai dengan cara kamu ingin mengambil nama
# #         nama_pengguna = user_message.split()[-1]

# #         # Memberikan respons ke pengguna
# #         dispatcher.utter_message(response=f"utter_sapa_pengguna")
        
# #         # Mengembalikan SlotSet untuk menyimpan nama pengguna
# #         return [SlotSet("nama_pengguna", nama_pengguna)]

# # class ActionLaptop(Action):
    
# #     def name(self) -> Text:
# #         return "action_laptop"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Mengambil data produk dari file JSON
# #         with open('C:/rasa chatbot/capstone-v1.0.4/actions/produk.json', 'r') as file:
# #             produk_data = json.load(file)

# #         # Mengacak dan memilih 5 produk
# #         produk_acak = random.sample(produk_data, min(5, len(produk_data)))

# #         # Menyiapkan tombol produk
# #         buttons = []
# #         for produk in produk_acak:
# #             produk_id = produk.get("ID")
# #             nama = produk.get("nama")
# #             harga = produk.get("harga")

# #             # Menambahkan tombol untuk setiap produk
# #             buttons.append({
# #                 "title": f"{nama} - {harga}",
# #                 "payload": f'/pilih_produk{{"produk_id":"{produk_id}"}}'
# #             })

# #         # Mengirimkan pesan dengan tombol produk
# #         dispatcher.utter_message(text="Berikut 5 produk {merk} di toko kami:", buttons=buttons)

# #         return []

# # class ActionLaptopLenovo(Action):
    
# #     def name(self) -> Text:
# #         return "action_laptop_lenovo"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Mengambil data produk dari file JSON
# #         with open('C:/rasa chatbot/capstone-v1.0.3/actions/produk_lenovo.json', 'r') as file:
# #             produk_data = json.load(file)

# #         # Mengacak dan memilih 5 produk
# #         produk_acak = random.sample(produk_data, min(5, len(produk_data)))

# #         # Menyiapkan tombol produk
# #         buttons = []
# #         for produk in produk_acak:
# #             produk_id = produk.get("ID")
# #             nama = produk.get("nama")
# #             harga = produk.get("harga")

# #             # Menambahkan tombol untuk setiap produk
# #             buttons.append({
# #                 "title": f"{nama} - {harga}",
# #                 "payload": f'/pilih_produk{{"produk_id":"{produk_id}"}}'
# #             })

# #         # Mengirimkan pesan dengan tombol produk
# #         dispatcher.utter_message(text="Berikut 5 produk Lenovo di toko kami:", buttons=buttons)

# #         return []

# # class ActionLaptopLenovoNama(Action):
    
# #     def name(self) -> Text:
# #         return "action_laptop_lenovo_nama"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Mengambil nama pengguna dari slot
# #         nama_pengguna = tracker.get_slot("nama_pengguna")

# #         # Membaca data produk dari file JSON
# #         with open('C:/rasa chatbot/capstone-v1.0.3/actions/produk_lenovo.json', 'r') as file:
# #             produk_data = json.load(file)

# #         # Mengacak dan memilih 5 produk
# #         produk_acak = random.sample(produk_data, min(5, len(produk_data)))

# #         # Menyiapkan tombol produk
# #         buttons = []
# #         for produk in produk_acak:
# #             produk_id = produk.get("ID")
# #             nama = produk.get("nama")
# #             harga = produk.get("harga")

# #             # Menambahkan tombol untuk setiap produk
# #             buttons.append({
# #                 "title": f"{nama} - {harga}",
# #                 "payload": f'/pilih_produk_lenovo_nama{{"produk_id":"{produk_id}"}}'
# #             })

# #         # Mengirimkan pesan dengan tombol produk
# #         dispatcher.utter_message(
# #             text=f"Hai kak {nama_pengguna}. Berikut 5 produk Lenovo di toko kami:",
# #             buttons=buttons
# #         )

# #         return []

# # class ActionPilihProduk(Action):
    
# #     def name(self) -> Text:
# #         return "action_pilih_produk"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Mendapatkan produk_id dari slot
# #         produk_id = tracker.get_slot("produk_id")

# #         # Memuat data produk dari file JSON
# #         with open('C:/rasa chatbot/capstone-v1.0.3/actions/produk.json', 'r') as file:
# #             produk_data = json.load(file)

# #         # Mencari produk berdasarkan produk_id
# #         produk_terpilih = next((produk for produk in produk_data if produk.get("ID") == produk_id), None)

# #         if produk_terpilih:
# #             nama_produk = produk_terpilih.get("nama")
# #             dispatcher.utter_message(text=f"Kamu memilih produk: {nama_produk}")
# #         else:
# #             dispatcher.utter_message(text="Produk tidak ditemukan.")

# #         return [SlotSet("produk_id", produk_id)]

# # class ActionPilihProdukLenovo(Action):

# #     def name(self) -> Text:
# #         return "action_pilih_produk_lenovo"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Mendapatkan produk_id dari slot
# #         produk_id = tracker.get_slot("produk_id")

# #         # Memuat data produk dari file JSON
# #         with open('C:/rasa chatbot/capstone-v1.0.3/actions/produk_lenovo.json', 'r') as file:
# #             produk_data = json.load(file)

# #         # Mencari produk berdasarkan produk_id
# #         produk_terpilih = next((produk for produk in produk_data if produk.get("ID") == produk_id), None)

# #         if produk_terpilih:
# #             nama_produk = produk_terpilih.get("nama")
# #             dispatcher.utter_message(text=f"Kamu memilih produk: {nama_produk}")
# #         else:
# #             dispatcher.utter_message(text="Produk tidak ditemukan.")

# #         return [SlotSet("produk_id", produk_id)]

# # class ActionPilihProdukLenovoNama(Action):
    
# #     def name(self) -> Text:
# #         return "action_pilih_produk_lenovo_nama"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Mendapatkan nama pengguna dan produk_id dari slot
# #         nama_pengguna = tracker.get_slot("nama_pengguna")
# #         produk_id = tracker.get_slot("produk_id")

# #         # Memuat data produk dari file JSON
# #         with open('C:/rasa chatbot/capstone-v1.0.3/actions/produk_lenovo.json', 'r') as file:
# #             produk_data = json.load(file)

# #         # Mencari produk berdasarkan produk_id
# #         produk_terpilih = next((produk for produk in produk_data if produk.get("ID") == produk_id), None)

# #         if produk_terpilih:
# #             nama_produk = produk_terpilih.get("nama")
# #             dispatcher.utter_message(text=f"Hai kak {nama_pengguna}. Kamu memilih produk: {nama_produk}")
# #         else:
# #             dispatcher.utter_message(text=f"Hai kak {nama_pengguna}. Produk tidak ditemukan.")

# #         return [SlotSet("produk_id", produk_id)]

# # class ActionDeskripsi(Action):
    
# #     def name(self) -> Text:
# #         return "action_deskripsi"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Mendapatkan produk_id dari slot
# #         produk_id = tracker.get_slot("produk_id")

# #         # Memuat data produk dari file JSON
# #         with open('C:/rasa chatbot/capstone-v1.0.3/actions/produk.json', 'r') as file:
# #             produk_data = json.load(file)

# #         # Mencari produk berdasarkan produk_id
# #         produk_terpilih = next((produk for produk in produk_data if produk.get("ID") == produk_id), None)

# #         if produk_terpilih:
# #             nama_produk = produk_terpilih.get("nama")
# #             deskripsi = produk_terpilih.get("deskripsi")
# #             dispatcher.utter_message(text=f"Berikut deskripsi produk {nama_produk}:\n{deskripsi}")
# #         else:
# #             dispatcher.utter_message(text="Deskripsi untuk produk ini tidak ditemukan.")

# #         return []

# # class ActionDeskripsiLenovo(Action):
    
# #     def name(self) -> Text:
# #         return "action_deskripsi_lenovo"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Mendapatkan produk_id dari slot
# #         produk_id = tracker.get_slot("produk_id")

# #         # Memuat data produk dari file JSON
# #         with open('C:/rasa chatbot/capstone-v1.0.3/actions/produk_lenovo.json', 'r') as file:
# #             produk_data = json.load(file)

# #         # Mencari produk berdasarkan produk_id
# #         produk_terpilih = next((produk for produk in produk_data if produk.get("ID") == produk_id), None)

# #         if produk_terpilih:
# #             nama_produk = produk_terpilih.get("nama")
# #             deskripsi = produk_terpilih.get("deskripsi")
# #             dispatcher.utter_message(text=f"Berikut deskripsi produk {nama_produk}:\n{deskripsi}")
# #         else:
# #             dispatcher.utter_message(text="Deskripsi untuk produk ini tidak ditemukan.")

# #         return []

    
# # class ActionDeskripsiLenovoNama(Action):
    
# #     def name(self) -> Text:
# #         return "action_deskripsi_lenovo_nama"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Mendapatkan produk_id dan nama pengguna dari slot
# #         produk_id = tracker.get_slot("produk_id")
# #         nama_pengguna = tracker.get_slot("nama_pengguna")

# #         # Memuat data produk dari file JSON
# #         with open('C:/rasa chatbot/capstone-v1.0.3/actions/produk_lenovo.json', 'r') as file:
# #             produk_data = json.load(file)

# #         # Mencari produk berdasarkan produk_id
# #         produk_terpilih = next((produk for produk in produk_data if produk.get("ID") == produk_id), None)

# #         if produk_terpilih:
# #             nama_produk = produk_terpilih.get("nama")
# #             deskripsi = produk_terpilih.get("deskripsi")
# #             dispatcher.utter_message(text=f"Hai kak {nama_pengguna}, berikut deskripsi produk {nama_produk}:\n{deskripsi}")
# #         else:
# #             dispatcher.utter_message(text="Deskripsi untuk produk ini tidak ditemukan.")

# #         return []


# # class ActionLaptopAsus(Action):
    
# #     def name(self) -> Text:
# #         return "action_laptop_asus"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Mengambil data produk dari file JSON
# #         with open('C:/rasa chatbot/capstone-v1.0.3/actions/produk_asus.json', 'r') as file:
# #             produk_data = json.load(file)

# #         # Mengacak dan memilih 5 produk
# #         produk_acak = random.sample(produk_data, min(5, len(produk_data)))

# #         # Menyiapkan tombol produk
# #         buttons = []
# #         for produk in produk_acak:
# #             produk_id = produk.get("ID")
# #             nama = produk.get("nama")
# #             harga = produk.get("harga")

# #             # Menambahkan tombol untuk setiap produk
# #             buttons.append({
# #                 "title": f"{nama} - {harga}",
# #                 "payload": f'/pilih_produk{{"produk_id":"{produk_id}"}}'
# #             })

# #         # Mengirimkan pesan dengan tombol produk
# #         dispatcher.utter_message(text="Berikut 5 produk Asus di toko kami:", buttons=buttons)

# #         return []

# # class ActionPilihProdukAsus(Action):

# #     def name(self) -> Text:
# #         return "action_pilih_produk_asus"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Mendapatkan produk_id dari slot
# #         produk_id = tracker.get_slot("produk_id")

# #         # Memuat data produk dari file JSON
# #         with open('C:/rasa chatbot/capstone-v1.0.3/actions/produk_asus.json', 'r') as file:
# #             produk_data = json.load(file)

# #         # Mencari produk berdasarkan produk_id
# #         produk_terpilih = next((produk for produk in produk_data if produk.get("ID") == produk_id), None)

# #         if produk_terpilih:
# #             nama_produk = produk_terpilih.get("nama")
# #             dispatcher.utter_message(text=f"Kamu memilih produk: {nama_produk}")
# #         else:
# #             dispatcher.utter_message(text="Produk tidak ditemukan.")

# #         return [SlotSet("produk_id", produk_id)]

# # class ActionDeskripsiAsus(Action):
    
# #     def name(self) -> Text:
# #         return "action_deskripsi_asus"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Mendapatkan produk_id dari slot
# #         produk_id = tracker.get_slot("produk_id")

# #         # Memuat data produk dari file JSON
# #         with open('C:/rasa chatbot/capstone-v1.0.3/actions/produk_asus.json', 'r') as file:
# #             produk_data = json.load(file)

# #         # Mencari produk berdasarkan produk_id
# #         produk_terpilih = next((produk for produk in produk_data if produk.get("ID") == produk_id), None)

# #         if produk_terpilih:
# #             deskripsi = produk_terpilih.get("deskripsi")
# #             dispatcher.utter_message(text=f"Deskripsi produk:\n{deskripsi}")
# #         else:
# #             dispatcher.utter_message(text="Deskripsi untuk produk ini tidak ditemukan.")

# #         return []

# # #Sentiment Analysis##
# # from datetime import datetime

# # class ActionRespondBasedOnSentiment(Action):
# #     def name(self) -> Text:
# #         return "action_respond_based_on_sentiment"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Mendapatkan intent terbaru
# #         latest_intent = tracker.latest_message['intent'].get('name')

# #         # Mendapatkan waktu saat ini
# #         current_hour = datetime.now().hour

# #         # Menentukan ucapan waktu sesuai waktu saat ini
# #         if 5 <= current_hour < 12:
# #             time_response = "utter_pagi"
# #         elif 12 <= current_hour < 15:
# #             time_response = "utter_siang"
# #         elif 15 <= current_hour < 19:
# #             time_response = "utter_greet_evening"
# #         else:
# #             time_response = "utter_sore"

# #         # Memberikan respons sesuai intent dan waktu
# #         if latest_intent == "marah":
# #             dispatcher.utter_message(response="utter_marah")
# #         elif latest_intent == "bahagia":
# #             dispatcher.utter_message(response="utter_bahagia")
# #         elif latest_intent == "sedih":
# #             dispatcher.utter_message(response="utter_sedih")
# #         else:
# #             dispatcher.utter_message(response=time_response)
        
# #         return []

# # class ActionLaptopAsusByBudget(Action):
    
# #     def name(self) -> Text:
# #         return "action_laptopAsus_by_budget"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Ambil slot budget dan periksa formatnya
# #         budget_text = tracker.get_slot("budget")
# #         budget = 0  # Default jika budget tidak ditemukan

# #         if budget_text:
# #             # Menghapus karakter non-digit dan mengonversi
# #             budget = re.sub(r'[^\d]', '', budget_text)
# #             # Jika teks berisi 'juta', konversi ke angka jutaan
# #             budget = int(budget) * 1000000 if 'juta' in tracker.latest_message['text'].lower() else int(budget)
        
# #         # Definisikan rentang harga dengan margin 1 juta
# #         range_bawah = budget - 1000000
# #         range_atas = budget + 1000000

# #         # Memuat data produk
# #         with open('C:/rasa chatbot/capstone-v1.0.3/actions/produk_asus.json', 'r') as file:
# #             produk_data = json.load(file)

# #         # Filter produk dalam rentang harga yang ditentukan
# #         produk_in_budget = [
# #             produk for produk in produk_data
# #             if range_bawah <= int(re.sub(r'[^\d]', '', produk["harga"])) <= range_atas
# #         ]

# #         # Menyiapkan tombol produk jika ada produk yang sesuai dengan budget
# #         if produk_in_budget:
# #             buttons = []
# #             for produk in produk_in_budget:  # Menghilangkan batasan jumlah produk
# #                 produk_id = produk.get("ID")
# #                 nama = produk.get("nama")
# #                 harga = produk.get("harga")
                
# #                 # Menambahkan tombol untuk setiap produk
# #                 buttons.append({
# #                     "title": f"{nama} - {harga}",
# #                     "payload": f'/pilih_produk{{"produk_id":"{produk_id}"}}'
# #                 })
            
# #             # Mengirimkan pesan dengan tombol produk
# #             dispatcher.utter_message(text="Berikut daftar produk yang sesuai dengan budget Anda:", buttons=buttons)
# #         else:
# #             dispatcher.utter_message(text="Maaf, tidak ada produk yang cocok dengan budget Anda.")

# #         return []
    
# # class ActionLaptopLenovoByBudget(Action):
    
# #     def name(self) -> Text:
# #         return "action_laptopLenovo_by_budget"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         # Ambil slot budget dan periksa formatnya
# #         budget_text = tracker.get_slot("budget")
# #         budget = 0  # Default jika budget tidak ditemukan

# #         if budget_text:
# #             # Menghapus karakter non-digit dan mengonversi
# #             budget = re.sub(r'[^\d]', '', budget_text)
# #             # Jika teks berisi 'juta', konversi ke angka jutaan
# #             budget = int(budget) * 1000000 if 'juta' in tracker.latest_message['text'].lower() else int(budget)
        
# #         # Definisikan rentang harga dengan margin 1 juta
# #         range_bawah = budget - 1000000
# #         range_atas = budget + 1000000

# #         # Memuat data produk
# #         with open('C:/rasa chatbot/capstone-v1.0.3/actions/produk_lenovo.json', 'r') as file:
# #             produk_data = json.load(file)

# #         # Filter produk dalam rentang harga yang ditentukan
# #         produk_in_budget = [
# #             produk for produk in produk_data
# #             if range_bawah <= int(re.sub(r'[^\d]', '', produk["harga"])) <= range_atas
# #         ]

# #         # Menyiapkan tombol produk jika ada produk yang sesuai dengan budget
# #         if produk_in_budget:
# #             buttons = []
# #             for produk in produk_in_budget:  # Menghilangkan batasan jumlah produk
# #                 produk_id = produk.get("ID")
# #                 nama = produk.get("nama")
# #                 harga = produk.get("harga")
                
# #                 # Menambahkan tombol untuk setiap produk
# #                 buttons.append({
# #                     "title": f"{nama} - {harga}",
# #                     "payload": f'/pilih_produk{{"produk_id":"{produk_id}"}}'
# #                 })
            
# #             # Mengirimkan pesan dengan tombol produk
# #             dispatcher.utter_message(text="Berikut daftar produk yang sesuai dengan budget Anda:", buttons=buttons)
# #         else:
# #             dispatcher.utter_message(text="Maaf, tidak ada produk yang cocok dengan budget Anda.")

# #         return []





# class ActionLaptop(Action):
#     def name(self) -> Text:
#         return "action_laptop"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         json_path = current_dir / "produk_laptop.json"
#         with open(json_path, "r", encoding="utf-8") as file:
#             produk_data = json.load(file) 
#         produk_acak = random.sample(produk_data, min(5, len(produk_data)))
#         buttons = []
#         for produk in produk_acak:
#             produk_id = produk.get("ID")
#             nama = produk.get("nama")
#             harga = produk.get("harga")
#             buttons.append({
#                 "title": f"{nama} - {harga}",
#                 "payload": f'/pilih_produk{{"produk_id":"{produk_id}"}}'
#             })
#         dispatcher.utter_message(text="Berikut 5 produk laptop dengan merk {merk} di toko kami:", buttons=buttons)
#         return []