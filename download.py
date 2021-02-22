# encoding: utf-8

import os
import sys
import argparse
from config import sefaria_urls
from downloader import get_image

def _download_imgs(args):
    """
    Download the image to local directory
    """
    # From Arg Parse Get Manuscript Siglum
    mss = args.manuscript

    # Get the URL for the designated Manuscript
    sefaria_imgs = sefaria_urls()
    mss_url = sefaria_imgs[mss]

    # Download Images
    # TODO writer the iterator to download

    # TODO format mss_url (url + \d+ + ".jpg") where \d+ has an upper limit of ca. 600
    # img = get_image(mss_url)

    

def main(argv):
    """
    Download images of manuscript(s)
    :mss: specified manuscript (see manuscripts.ini)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("manuscript", help="See manuscripts.ini for available entries")
    args = parser.parse_args()

    _download_imgs(args)


if __name__ == '__main__':
    main(sys.argv[1:])