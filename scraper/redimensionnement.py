from PIL import Image
import os

SIZE = (224, 224)

def resize_images_in_folder(folder_path, size=SIZE):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):
            file_path = os.path.join(folder_path, filename)
            try:
                with Image.open(file_path) as img:
                    img = img.convert("RGB")
                    img = img.resize(size)
                    img.save(file_path)
                    print(f"Redimensionné : {filename}")
            except Exception as e:
                print(f"Erreur avec {filename} : {e}")

connecteur = input("nom du dossier : ")

folder_path = f"./dataset/{connecteur}/"

resize_images_in_folder(folder_path)