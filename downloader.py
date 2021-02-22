import urllib3.request

def get_image(file):
    """
    Download image
    """
    http = urllib3.PoolManager()

    # Attempt to download the image
    try:
        img = http.request('GET', 'https://manuscripts.sefaria.org/leningrad-color/BIB_LENCDX_F073B.jpg', retries=False)
    except urllib3.exceptions.NewConnectionError:
        print('Connection failed')
    return img
