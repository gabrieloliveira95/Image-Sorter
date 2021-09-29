from PIL import Image
import os
import argparse


def image_sorter(path_name):
    for path, subdirs, files in os.walk(path_name):
        for name in files:
            if ".jpg" in name or ".png" in name or ".PNG" in name or ".JPG" in name or ".JPEG" in name or ".jpeg":
                file_name_full = os.path.join(path, name)
                if not os.path.isfile(file_name_full):
                    continue
                try:
                    date = Image.open(file_name_full)._getexif()[36867][:7]
                    year = date[0:4]
                    month = date[5:7]
                except:
                    print(f"Cannot Convert {file_name_full}")
                    continue
                file_full = os.path.join(path_name, year, month)
                if not os.path.exists(file_full):
                    os.makedirs(file_full)
                os.rename(file_name_full, os.path.join(file_full, name))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required=True,
                    help="Folder Path")
    args = vars(ap.parse_args())
    image_sorter(args['path'])
    print("Process Complete")
