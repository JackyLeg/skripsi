import csv
import json
import ast

def clean_text(text):
    return text.replace("\u0000", "").strip() if text else ""

def parse_images(images_str):
    try:
        return ast.literal_eval(images_str)
    except Exception:
        return []

def simplify_category(cat_str):
    try:
        cats = ast.literal_eval(cat_str)
        if cats:
            return cats[0].replace(">>", ">").strip()
    except Exception:
        return ""
    return ""

input_csv = "flipkart_com-ecommerce_sample.csv"
output_json = "produk_flipkart.json"

produk_list = []

with open(input_csv, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        produk = {
            "id": clean_text(row["uniq_id"]),
            "nama": clean_text(row["product_name"]),
            "kategori": simplify_category(row["product_category_tree"]),
            "harga": clean_text(row["discounted_price"]),
            "harga_awal": clean_text(row["retail_price"]),
            "deskripsi": clean_text(row["description"]),
            "gambar": parse_images(row["image"]),
            "url": clean_text(row["product_url"]),
            "brand": clean_text(row["brand"])
        }
        produk_list.append(produk)

with open(output_json, "w", encoding="utf-8") as f:
    json.dump(produk_list, f, ensure_ascii=False, indent=2)

print(f"Sukses mengubah {len(produk_list)} produk ke {output_json}")
