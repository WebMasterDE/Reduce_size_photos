#prima di procedere con l'avvio del programma, assicurarsi che  imagemagick (in versione AppImage) sia presente nella stessa cartella e allo stesso livello di questo programma python

import os
import glob
import sys
from PIL import Image

#funzione che comprime le immagini con una risoluzione superiore a 1920*1080 ad una risoluzione di 1920*1080
def compress_images(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith('.jpeg') or file.endswith(".png") or file.endswith(".JPG") or file.endswith('.JPEG') or file.endswith(".PNG"):
                print(os.listdir(root).index(file), " di ", os.listdir(root).__len__(), " -> ", file)
                image_path = os.path.join(root, file)
                img = Image.open(image_path)
                if img.width > 1920 or img.height > 1080:
                    img.thumbnail((1920, 1080))
                    #img.save(image_path, quality=70)
                    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.JPG') or file.endswith('.JPEG'):
                        img.save(os.path.join(root, 'compressed_' + file), 'JPEG', quality=70)
                    else:
                        img.save(os.path.join(root, 'compressed_' + file), 'PNG', quality=70)

# Funzione che conta il numero di immagini presenti nella cartella da analizzare
def count_image_files(directory):
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG'] #'*.gif', '*.bmp', '.heic' # Add more extensions if needed
    count = 0
    for extension in image_extensions:
        count += len(glob.glob(os.path.join(directory, '**', extension), recursive=True))
    return count


if __name__ == '__main__':
    # info for the final user
    print("This program reduce all photos with image resolution bigger than 1920x1080 (Full HD) to Full HD.")
    #directory_path = '/home/jeremy/Immagini/test_convert' # cartella da analizzare
    directory_path=input("Insert the folder where is contained the images (without the character \' or \" at the beginning or the end of the path): ")
    print("Counting...")

    # image count
    image_file_count = count_image_files(directory_path)  # richiamo la funzione che mi conta quante immagini sono presenti nella directory_path
    print('Number of image files:', image_file_count)

    if input("Press Enter to confirm: ") != "" :
        sys.exit("Program terminated as Enter key was not pressed to confirm")

    # call the function to reduce size > fullhd to fullhd
    compress_images(directory_path)




