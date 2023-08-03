from tkinter import filedialog
import logging
from pypdf import PdfWriter


PDF_FILE_TYPE = ("PDF files", "*.pdf")
ALL_FILE_TYPE = ("all files", "*.*")
merger = PdfWriter()


class FileDialog:
    def __init__(self, root):
        self.root = root

    def get_input_files(self):
        '''Returns a list of file paths'''
        self.root.withdraw()
        self.root.filename = filedialog.askopenfilenames(
            initialdir="/", title="Select PDF files for merging", filetypes=(PDF_FILE_TYPE, ALL_FILE_TYPE))
        nr_of_files = len(self.root.filename)
        logging.info(f'{nr_of_files} files selected')
        if nr_of_files == 0:
            raise ValueError('No files selected')
        else:
            return self.root.filename

    def get_output_file(self):
        '''Returns the output file path'''
        self.root.withdraw()
        self.root.filename = filedialog.asksaveasfilename(
            initialdir="/", title="Save merged PDF file as", filetypes=(PDF_FILE_TYPE,))
        if not self.root.filename.endswith('.pdf'):
            self.root.filename += '.pdf'
        logging.info(f'Saving merged PDF file as {self.root.filename}')
        return self.root.filename


class PDFMerger:
    def __init__(self, merger):
        self.merger = merger

    def merge_files(self, input_files, output_file):
        '''Merges PDF files and saves the output file'''
        if input_files is None:
            raise ValueError('No files selected')
        else:
            for pdf in input_files:
                self.merger.append(pdf)

            self.merger.write(output_file)
            logging.info('PDF files merged successfully')
            logging.info(f'Output file is located: {output_file}')
            self.merger.close()


def merge_pdf(file_dialog, merger):
    '''Merges the input files and saves the output file'''
    input_files = file_dialog.get_input_files()
    output_file = file_dialog.get_output_file()
    merger.merge_files(input_files, output_file)
