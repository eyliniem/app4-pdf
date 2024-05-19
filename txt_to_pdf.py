from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob("Text_Files/*.txt")

pdf = FPDF(orientation='P', unit='in', format='letter')

for filepath in filepaths:
    section_header = Path(filepath).stem.title()
    pdf.add_page()
    pdf.set_font(family='Arial', size=16, style='B')
    pdf.cell(w=2, h=0.5, txt=section_header)
    print(section_header)

pdf.output(f"Text_Files/output_pdf.pdf")