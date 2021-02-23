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
    folios = args.folio_count

    # Get the URL for the designated Manuscript
    sefaria_imgs = sefaria_urls()
    mss_url = sefaria_imgs[mss]
    
    # Download Images
    
    # Since a Codex Has A and B sides, account for the sides
    folio_A = "A"
    folio_B = "B"

    # Download Folio Images for Manuscript
    for i in range(int(folios)):
        get_image(mss_url, mss, str("{:03}".format(i) + folio_A))
        get_image(mss_url, mss, str("{:03}".format(i) + folio_B))

    

def main(argv):
    """
    Download images of manuscript(s)
    :mss: specified manuscript (see manuscripts.ini)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("manuscript", help="See manuscripts.ini for available entries")
    parser.add_argument("folio_count", help="How many folios are they in the image set?")
    args = parser.parse_args()
    # B19A Folio count 492-1

    _download_imgs(args)


if __name__ == '__main__':
    main(sys.argv[1:])