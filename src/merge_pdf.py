import logging
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger


def get_input_files():
    '''Returns a list of file paths or raises an exception if no files are selected'''
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilenames(
        initialdir='/', title='Select PDF files to merge', filetypes=(('PDF files', '*.pdf'), ('all files', '*.*')))
    if not filename:
        raise ValueError('No files selected')
    return list(filename)


def get_output_file():
    '''Returns the output file path'''
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.asksaveasfilename(
        initialdir='/', title='Save merged PDF file as', filetypes=(('PDF files', '*.pdf'),))
    if not filename.endswith('.pdf'):
        logging.warning("Invalid file name. File name must end with '.pdf'.")
        filename += '.pdf'
    logging.debug(f'Saving merged PDF file as {filename}')
    return filename


def merge_files(input_files, output_file):
    '''Merges PDF files and saves the output file'''
    if not input_files:
        raise ValueError('No files selected')
    merger = PdfMerger()
    for pdf in input_files:
        merger.append(pdf)
    merger.write(output_file)
    logging.info('PDF files merged successfully')
    logging.info(f'Output file is located: {output_file}')


def main():
    '''Main function'''
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Program started')

    try:
        input_files = get_input_files()
        output_file = get_output_file()
        merge_files(input_files, output_file)
        logging.info('Program ended')
    except Exception as e:
        logging.error(str(e))


if __name__ == '__main__':
    main()
