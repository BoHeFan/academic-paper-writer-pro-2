import sys
import os

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: PyMuPDF is not installed. Please run: pip install PyMuPDF")
    sys.exit(1)

def convert_pdf_to_images(pdf_path, output_dir, dpi=200):
    """
    Converts a PDF file into a sequence of PNG images, one for each page.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: Original PDF not found at {pdf_path}")
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    
    print(f"Starting conversion of {len(doc)} pages...")
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        # 200 DPI is generally a good balance between file size and OCR clarity
        pix = page.get_pixmap(dpi=dpi)
        output_filename = f"page_{page_num + 1:03d}.png"
        output_path = os.path.join(output_dir, output_filename)
        
        pix.save(output_path)
        print(f"[{page_num + 1}/{len(doc)}] Saved {output_path}")
        
    print(f"Successfully converted all pages into {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python page_to_image.py <pdf_path> <output_dir>")
        sys.exit(1)
        
    pdf_input = sys.argv[1]
    dir_output = sys.argv[2]
    
    convert_pdf_to_images(pdf_input, dir_output)
