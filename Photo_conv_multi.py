import subprocess
import os
from multiprocessing import Pool


current_dir = os.path.dirname(os.path.abspath(__file__))
Source_dir = os.path.join(current_dir, "Source")
Result_dir = os.path.join(current_dir, "Result")

def get_images(folder):
   photos = []
   for f in os.listdir(folder):
      if ".jpg" in f:
         photos.append(f)
   return photos

def make_result_dir(folder_name):
    if not os.path.exists(folder_name):
      os.mkdir(folder_name)

def pic_compression(photo):
    subprocess.call("convert {0}\\{1} -resize 200 {2}\\{1}".format(Source_dir, photo, Result_dir))


if __name__ == '__main__':
    make_result_dir("Result")
    photos = get_images(Source_dir)
    pool = Pool(4)
    pool.map(pic_compression, photos)
    pool.close()
    pool.join()
