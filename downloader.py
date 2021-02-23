import os
import urllib3.request
from config import dirs

def save_image(image, d, fname):
    """
    Save image to directory
    """
    img_PATH = os.path.join(d, fname + ".jpg")
    
    # TODO Save Image Files to Directory

def get_image(url, mss, folio):
    """
    Download image
    """
    http = urllib3.PoolManager()
    app_dirs = dirs()
    mss_dir = app_dirs[mss]

    # Attempt to download the image
    if not os.path.exists(mss_dir):
            os.makedirs(mss_dir)
    try:
        img = http.request('GET', url + folio + '.jpg', retries=False)
        if img.status == 404:
            next #TODO import reporting and print report on status 404
        else:
            print(img.status)
        # save_image(img, mss_dir, folio)
    except urllib3.exceptions.NewConnectionError:
        print('Connection failed')
    return img
