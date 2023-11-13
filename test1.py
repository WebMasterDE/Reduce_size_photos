import os
from PIL import Image

path = '/home/jeremy/Immagini/test_convert'

def compress_images():
    for item in os.listdir(path):
        if item.endswith('.jpg'):
            print(os.listdir(path).index(item) , " di " , os.listdir(path).__len__() , " -> " , item)
            im = Image.open(os.path.join(path, item))
            if im.size[0] > 1920 or im.size[1] > 1080:
                im.thumbnail((1920, 1080))
                #img.save(os.path.join(folder_path, 'compressed_' + filename), optimize=True, quality=quality)
                im.save(os.path.join(path, 'compressed_'+item), 'JPEG', quality=70)

if __name__ == '__main__':
    compress_images()
    print("Fatto")
