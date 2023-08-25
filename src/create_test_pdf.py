from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import red, blue, green


def create_pdf(filename, text):
    '''Creates a PDF file'''
    c = canvas.Canvas(filename, pagesize=A4)
    c.setLineWidth(.3)
    c.setFont('Courier', 40)
    c.setFillColor(red)
    c.drawString(1 * cm, 27 * cm, text)
    c.setFillColor(blue)
    c.drawString(1 * cm, 25 * cm, text)
    c.setFillColor(green)
    c.drawString(1 * cm, 23 * cm, text)

    c.save()


def main():
    create_pdf('data/pdf/test1.pdf', 'This is test file ONE')
    create_pdf('data/pdf/test2.pdf', 'This is test file TWO')
    create_pdf('data/pdf/test3.pdf', 'This is test file THREE')


if __name__ == '__main__':
    main()
