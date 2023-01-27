import fitz
def pdf_to_jpg(pdf_path, jpg_path, dpi=300):
    # Open the PDF
    pdf_doc = fitz.open(pdf_path)
    # Get the first page
    page = pdf_doc[0]
    # Render the page at a high DPI
    pix = page.get_pixmap(dpi=dpi, alpha=False)
    # Save the image as a JPEG
    pix.save(jpg_path, "JPEG")
    print("PDF converted to JPEG successfully!")
# Usage example
pdf_to_jpg("example.pdf", "example.jpg", dpi=300)


