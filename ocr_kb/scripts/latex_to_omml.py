import sys
import os
import subprocess
import zipfile
import tempfile
import xml.etree.ElementTree as ET

def latex_to_omml(latex_string):
    """
    Converts a LaTeX math string into Microsoft Word OMML (Office Math Markup Language) XML.
    Uses pandoc as the conversion engine.
    """
    # Create a temporary directory to work in
    with tempfile.TemporaryDirectory() as tmpdir:
        md_file = os.path.join(tmpdir, "temp_math.md")
        docx_file = os.path.join(tmpdir, "temp_math.docx")
        
        # Wrap the latex in block math delimiters for pandoc
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(f"$$ {latex_string} $$")
            
        # Run pandoc to convert the markdown with math into a docx file
        # Pandoc natively converts LaTeX math into OMML in docx output
        try:
            subprocess.run(
                ["pandoc", md_file, "-o", docx_file], 
                check=True,
                capture_output=True
            )
        except subprocess.CalledProcessError as e:
            print("Error running pandoc. Ensure pandoc is installed.")
            print(e.stderr.decode("utf-8", errors="ignore"))
            return None
        except FileNotFoundError:
            print("Error: pandoc command not found. Please install pandoc.")
            return None

        # Extract the document.xml from the generated docx archive
        try:
            with zipfile.ZipFile(docx_file, 'r') as docx_zip:
                doc_xml_content = docx_zip.read('word/document.xml')
        except Exception as e:
            print(f"Error reading generated docx: {e}")
            return None

        # Parse the XML to extract the <m:oMathPara> or <m:oMath> element
        ET.register_namespace('w', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main')
        ET.register_namespace('m', 'http://schemas.openxmlformats.org/officeDocument/2006/math')
        
        root = ET.fromstring(doc_xml_content)
        
        # Word math elements namespace
        m_ns = '{http://schemas.openxmlformats.org/officeDocument/2006/math}'
        
        # Try to find paragraph-level math first (block equations)
        math_elements = root.findall(f'.//{m_ns}oMathPara')
        if not math_elements:
            # Fallback to inline math
            math_elements = root.findall(f'.//{m_ns}oMath')
            
        if math_elements:
            # We take the first math element found
            math_xml = ET.tostring(math_elements[0], encoding='unicode', method='xml')
            return math_xml
        else:
            print("Error: No math XML found in the generated document.")
            return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python latex_to_omml.py \"<latex_formula>\"")
        print("Example: python latex_to_omml.py \"E = mc^2\"")
        sys.exit(1)
        
    latex_input = sys.argv[1]
    omml_output = latex_to_omml(latex_input)
    
    if omml_output:
        print("--- OMML XML OUTPUT ---")
        print(omml_output)
        print("-----------------------")
