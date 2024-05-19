from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit="in", format="letter")
pdf.set_auto_page_break(auto=False, margin=0)
footer_height = 0.75  # Height of the footer


df = pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()
    #set the header
    pdf.set_font(family="Arial", style="b", size=20)
    pdf.set_text_color(5,110,205)
    pdf.cell(w=0, h=.5, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.set_draw_color(5,110,205)
    pdf.line(0.4,0.8,8.1,0.8)    #pdf.line(x1,y1,x2,y2)
    #set the footer
    pdf.set_y(-footer_height)
    pdf.set_font(family="Arial", style='I',size=9)
    pdf.cell(w=0,h=footer_height,txt=row["Topic"], align="R")
    pdf.line(0.4,10.5,8.1,10.5) 
    for y in range(12,105,3):    #create lines for ruled paper
                pdf.line(0.4,y/10,8.1,y/10)


    for i in range(row["Pages"]-1):
        pdf.add_page()
        #set the footer
        pdf.set_y(-footer_height)
        pdf.set_font(family="Arial", style='I',size=9)
        pdf.cell(w=0,h=footer_height,txt=row["Topic"], align="R")
        pdf.line(0.4,10.5,8.1,10.5) 
        for y in range(6,105,3):
                pdf.line(0.4,y/10,8.1,y/10)

pdf.output("output.pdf")