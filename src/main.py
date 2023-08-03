from merge import FileDialog, PDFMerger, merger, merge_pdf

from tkinter import Tk


def main():
    file_dialog = FileDialog(Tk())
    pdf_merger = PDFMerger(merger)
    merge_pdf(file_dialog, pdf_merger)


if __name__ == '__main__':
    main()
