#prima di procedere con l'avvio del programma, assicurarsi che  imagemagick (in versione AppImage) sia presente nella stessa cartella e allo stesso livello di questo programma python

import os
import glob
from PIL import Image

#funzione che comprime le immagini con una risoluzione superiore a 1920*1080 ad una risoluzione di 1920*1080
def compress_images(path):
    for item in os.listdir(path):

        if item.endswith('.jpg') or item.endswith('.jpeg') or item.endswith('.png'):
            print(os.listdir(path).index(item), " di ", os.listdir(path).__len__(), " -> ", item)
            im = Image.open(os.path.join(path, item))
            if im.size[0] > 1920 or im.size[1] > 1080:
                im.thumbnail((1920, 1080))
                if item.endswith('.jpg') or item.endswith('.jpeg'):
                    im.save(os.path.join(path, 'compressed_' + item), 'JPEG', quality=70)
                else:
                    im.save(os.path.join(path, 'compressed_' + item), 'PNG', quality=70)

# Funzione che conta il numero di immagini presenti nella cartella da analizzare
def count_image_files(directory):
    image_extensions = ['*.jpg', '*.jpeg', '*.png'] #'*.gif', '*.bmp', '.heic' # Add more extensions if needed
    count = 0
    for extension in image_extensions:
        count += len(glob.glob(os.path.join(directory, '**', extension), recursive=True))
    return count


if __name__ == '__main__':
    directory_path = '/home/jeremy/Immagini/test_convert' # cartella da analizzare

    # image count
    image_file_count = count_image_files(directory_path)  # richiamo la funzione che mi conta quante immagini sono presenti nella directory_path
    print('Number of image files:', image_file_count)

    # info for the final user
    print("This program reduce all photos with image resolution bigger than 1920x1080 (Full HD) to Full HD.")
    confirmation = input("Press Enter to confirm: ")

    # call the function to reduce size > fullhd to fullhd
    compress_images(directory_path)




