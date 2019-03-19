"""
This program saves crops chromatogram images from the PDF files provided in the pdf-files folder.
"""

import os
import os.path
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes


PDF_DIR = 'pdf-files'  # input directory, PDF files
IMG_DIR = 'images'  # output directory, image files


def create_folders(dir_name):
    """Checks if output folder exists. If not, creates the folder.
    
    Parameters: 
        img: Image object
        filename (str): Final image filename without the extension    
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def get_chromatogram(img, filename):
    """Crop the chromatogram from the full page image
    
    Parameters: 
        img: Image object
        filename (str): Final image filename without the extension    
    """

    image = img.crop((64, 1270, 1594, 1972))
    image.save(f'{IMG_DIR}/{filename}.jpg')
    print(f'Image "{filename}" saved.')


def main():
    create_folders(IMG_DIR)
    pdf_files = os.listdir(PDF_DIR)

    for pdf_file in pdf_files:
        image = convert_from_path(PDF_DIR + '/' + pdf_file)[0]
        name = pdf_file.split('.')[0]

        get_chromatogram(image, name)

    print(f'\nDone.{len(pdf_files)} files processed.')


if __name__ == '__main__':
    main()
