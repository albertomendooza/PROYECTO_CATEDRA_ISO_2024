from fpdf import FPDF

reporte_de_compras = FPDF(format="Letter", unit="mm", orientation="landscape")
reporte_de_compras.add_page()
reporte_de_compras.set_author("ECONTA S.A. de C.V.")
reporte_de_compras.set_creator("Pacamara Dev")
reporte_de_compras.set_font(family="helvetica", style="", size=10)
# Los márgenes son ajustados para tener un área de 267 mm de uso horizontal
# Y 195.9 mm vertical, estando la página en formato horizontal.
reporte_de_compras.set_margins(left=6.2, top=10, right=6.2)
reporte_de_compras.set_auto_page_break(auto=True, margin=10)
reporte_de_compras.cell(w=30, text="REGISTRO Nº", align="L")
reporte_de_compras.cell(w=59, text="172014-0", align="L")
reporte_de_compras.cell(w=89, text="LIBRO DE COMPRAS", align="C")
reporte_de_compras.cell(w=89)
reporte_de_compras.ln(5)
reporte_de_compras.cell(w=30, text="MES", align="L")
reporte_de_compras.cell(w=59, text="Febrero", align="L")
reporte_de_compras.cell(w=89, text="", align="C")
reporte_de_compras.cell(w=89)
reporte_de_compras.ln(5)
reporte_de_compras.cell(w=30, text="AÑO", align="L")
reporte_de_compras.cell(w=59, text="2024", align="L")
reporte_de_compras.cell(w=89, text="COMERCIALIZADORA GILTON, S.A. DE C.V.", align="C")
reporte_de_compras.cell(w=89, text="FOLIO 15", align="R")
reporte_de_compras.ln(8)
reporte_de_compras.set_font(family="helvetica", style="", size=7)
# TOP da la siguiente celda a la par.
reporte_de_compras.multi_cell(
    text="\nCorre-\nlativo", w=9, border=1, padding=0, new_y="TOP", align="C"
)
reporte_de_compras.multi_cell(
    text="\nFecha\nEmisión", w=11, border=1, padding=0, new_y="TOP", align="C"
)
reporte_de_compras.multi_cell(
    text="\nNº del\nComprobante", w=20, border=1, padding=0, new_y="TOP", align="C"
)
reporte_de_compras.multi_cell(
    text="\nNº de\nRegistro", w=18, border=1, padding=0, new_x="LMARGIN", new_y="NEXT", align="C"
)

reporte_de_compras.multi_cell(
    text="", w=20, padding=0, new_x="LMARGIN", new_y="NEXT", align="C"
)

reporte_de_compras.multi_cell(
    text="1234", w=9, padding=0, new_y="TOP", align="L"
)
reporte_de_compras.multi_cell(
    text="23/03", w=11, padding=0, new_y="TOP", align="L"
)
reporte_de_compras.multi_cell(
    text="E0123456789123456789123456", w=21, padding=0, new_y="TOP", align="L"
)
reporte_de_compras.multi_cell(
    text="1234567-8", w=18, padding=0, new_y="TOP", align="L"
)
reporte_de_compras.output(name="Libro_de_compras.pdf")
