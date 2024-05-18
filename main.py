from fpdf import FPDF

pdf = FPDF(orientation='P', unit="mm", format="letter")

pdf.add_page()

pdf.set_font(family="Arial", style="b", size=12)
pdf.cell(w=0, h=12, txt="Hello There!", align="L", ln=1, border=0)
pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=10, txt="Hi There!", align="C", ln=1, border=0)

pdf.output("output.pdf")