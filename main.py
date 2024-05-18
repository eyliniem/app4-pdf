from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit="in", format="letter")

df = pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Arial", style="b", size=20)
    pdf.set_text_color(5,110,205)
    pdf.cell(w=0, h=.5, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.set_draw_color(5,110,205)
    pdf.line(0.4,0.8,8.1,0.8)    #pdf.line(x1,y1,x2,y2)

pdf.output("output.pdf")