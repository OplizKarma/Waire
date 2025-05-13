import os
import requests
from hashlib import md5
from dotenv import load_dotenv
from PIL import Image, ImageEnhance, ImageOps
import io
import random

# === Charger la clé API depuis le fichier .env ===
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))  # Charger le .env depuis la racine du projet
API_KEY = os.getenv("SERPAPI_KEY")

# === Vérification que la clé est bien chargée ===
if not API_KEY:
    print("Erreur : La clé API n'a pas été trouvée dans le fichier .env")
    exit(1)

# === Configuration ===
SEARCH_ENGINE = "google"
IMAGES_TO_DOWNLOAD = 100               # Nombre d'images originales à récupérer
AUGMENTATIONS_PER_IMAGE = 5            # Nombre de variantes par image

# === Entrée utilisateur ===
connector_name = input("Nom du connecteur à rechercher (ex: hdmi, usb-c): ").strip().lower()
output_dir = os.path.join("dataset", connector_name)

# === Création du dossier ===
os.makedirs(output_dir, exist_ok=True)
print(f"Dossier de destination : {output_dir}")

# === Récupération des images via SerpAPI ===
params = {
    "engine": SEARCH_ENGINE,
    "q": connector_name,
    "tbm": "isch",
    "api_key": API_KEY,
    "ijn": 0
}

downloaded_urls = set()
original_image_count = 0
total_image_count = 0
page = 0

# === Fonction de Data Augmentation ===
def augment_image(image, base_name, variant_index):
    transformations = []

    # Rotation
    if random.random() > 0.5:
        angle = random.choice([90, 180, 270])
        image = image.rotate(angle)
        transformations.append(f"rot{angle}")

    # Flip
    if random.random() > 0.5:
        image = ImageOps.mirror(image)
        transformations.append("flip")

    # Brightness
    if random.random() > 0.5:
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(random.uniform(0.5, 1.5))
        transformations.append("bright")

    # Zoom (crop puis resize)
    if random.random() > 0.5:
        width, height = image.size
        left = random.randint(0, width // 4)
        top = random.randint(0, height // 4)
        right = width - random.randint(0, width // 4)
        bottom = height - random.randint(0, height // 4)
        image = image.crop((left, top, right, bottom))
        image = image.resize((width, height))
        transformations.append("zoom")

    suffix = "_".join(transformations) if transformations else "original"
    file_name = f"{base_name}_{variant_index+1}_{suffix}.jpg"
    return image, file_name

while original_image_count < IMAGES_TO_DOWNLOAD:
    print(f"🔎 Récupération page {page + 1}...")
    params["ijn"] = page
    response = requests.get("https://serpapi.com/search.json", params=params)
    data = response.json()

    if "images_results" not in data:
        print("Aucune image trouvée ou erreur API.")
        break

    for img in data["images_results"]:
        img_url = img.get("original")
        if not img_url or img_url in downloaded_urls:
            continue

        try:
            img_data = requests.get(img_url, timeout=5).content
            image = Image.open(io.BytesIO(img_data)).convert("RGB")

            downloaded_urls.add(img_url)
            original_image_count += 1

            base_name = f"{connector_name}_{original_image_count}"

            for i in range(AUGMENTATIONS_PER_IMAGE):
                total_image_count += 1
                aug_image, aug_filename = augment_image(image.copy(), base_name, i)
                file_path = os.path.join(output_dir, aug_filename)
                aug_image.save(file_path)
                print(f"✅ {aug_filename}")

            if original_image_count >= IMAGES_TO_DOWNLOAD:
                break

        except Exception as e:
            print(f"❌ Erreur pour {img_url[:60]}... : {e}")
            continue

    page += 1

print(f"\n🎉 {total_image_count} images augmentées enregistrées dans '{output_dir}'")
