from tkinter import filedialog
from tkinter import Tk
import logging
from pypdf import PdfWriter
import subprocess
import os


merger = PdfWriter()
root = Tk()

PDF_FILE_TYPE = ("PDF files", "*.pdf")
ALL_FILE_TYPE = ("all files", "*.*")


def get_input_files():
    '''Returns a list of file paths'''
    root.withdraw()
    root.filename = filedialog.askopenfilenames(
        initialdir="/", title="Select PDF files for merging", filetypes=(PDF_FILE_TYPE, ALL_FILE_TYPE))
    nr_of_files = len(root.filename)
    print(f'{nr_of_files} files selected')
    if nr_of_files == 0:
        logging.info(f'{nr_of_files} files selected')
        raise SystemExit(1)
    else:
        return root.filename


def get_output_file():
    '''Returns a file path'''
    root.withdraw()
    root.filename = filedialog.asksaveasfilename(
        initialdir="/", title="Input file name and choose destination", filetypes=(PDF_FILE_TYPE, ALL_FILE_TYPE))
    return root.filename


def merge_pdf():
    '''Merges PDF files and saves the output file'''
    files = get_input_files()
    if files is None:
        logging.info('No files selected')
        raise SystemExit(1)
    else:
        for pdf in files:
            merger.append(pdf)

        output_file = get_output_file()
        merger.write(output_file)
        print('PDF files merged successfully')
        print(f'Output file is located: {output_file}')
        merger.close()
        root.destroy()


def clear():
    '''Clears the terminal screen.'''
    subprocess.call("cls" if os.name == "nt" else "clear", shell=False)


def main():
    clear()
    merge_pdf()


if __name__ == "__main__":
    main()
