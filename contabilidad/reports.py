from fpdf import FPDF


class ReporteDeCompras(FPDF):
    def header(self):
        self.set_font(family="helvetica", style="", size=10)
        # Los márgenes son ajustados para tener un área de 267 mm de uso horizontal
        # Y 195.9 mm vertical, estando la página en formato horizontal.
        self.set_margins(left=6.2, top=10, right=6.2)
        self.set_auto_page_break(auto=True, margin=10)
        self.cell(w=30, text="REGISTRO Nº", align="L")
        self.cell(w=59, text="172014-0", align="L")
        self.cell(w=89, text="LIBRO DE COMPRAS", align="C")
        self.cell(w=89)
        self.ln(5)
        self.cell(w=30, text="MES", align="L")
        self.cell(w=59, text="Febrero", align="L")
        self.cell(w=89, text="", align="C")
        self.cell(w=89)
        self.ln(5)
        self.cell(w=30, text="AÑO", align="L")
        self.cell(w=59, text="2024", align="L")
        self.cell(w=89, text="COMERCIALIZADORA GILTON, S.A. DE C.V.", align="C")
        self.cell(w=89, text=f"FOLIO {self.page_no()}", align="R")
        self.ln(8)
        self.set_font(family="helvetica", style="", size=7)
        # TOP da la siguiente celda a la par.
        


reporte_de_compras = ReporteDeCompras(
    format="Letter", unit="mm", orientation="landscape"
)
reporte_de_compras.add_page()
reporte_de_compras.set_author("ECONTA S.A. de C.V.")
reporte_de_compras.set_creator("Pacamara Dev")
reporte_de_compras.set_font(family="helvetica", style="", size=7)

for i in range(75):
    if reporte_de_compras.will_page_break(14.8):
        reporte_de_compras.add_page()
        reporte_de_compras.multi_cell(text="\nCorre-\nlativo", w=9, border=1, new_y="TOP", align="C")
        reporte_de_compras.multi_cell(text="\nFecha\nEmisión", w=11, border=1, new_y="TOP", align="C")
        reporte_de_compras.multi_cell(
            text="\nNº del\nComprobante", w=20, border=1, new_y="TOP", align="C"
        )
        reporte_de_compras.multi_cell(
            text="\nNº de\nRegistro", w=18, border=1, new_y="TOP", align="C"
        )
        reporte_de_compras.multi_cell(
            text="\n\nNombre de Proveedor", w=54, border=1, new_y="TOP", align="C"
        )

        reporte_de_compras.multi_cell(
            text="\nCompras Exentas",
            w=40,
            border=1,
            new_x="LEFT",
            new_y="NEXT",
            align="C",
        )
        reporte_de_compras.multi_cell(text="Internas", w=20, border=1, new_y="TOP", align="C")
        reporte_de_compras.multi_cell(text="Importaciones", w=20, border=1, new_y="TOP", align="C")
        # Configuro las posición actual para que no baje
        reporte_de_compras.set_xy(158.2, 28.0)
        reporte_de_compras.multi_cell(
            text="\nCompras Gravadas",
            w=55,
            border=1,
            new_x="LEFT",
            new_y="NEXT",
            align="C",
        )
        reporte_de_compras.multi_cell(text="Internas", w=20, border=1, new_y="TOP", align="C")
        reporte_de_compras.multi_cell(text="Importaciones", w=20, border=1, new_y="TOP", align="C")
        reporte_de_compras.multi_cell(text="IVA", w=15, border=1, new_y="TOP", align="C")
        reporte_de_compras.set_xy(213.2, 28.0)
        reporte_de_compras.multi_cell(text="\nTotal\ncompras", w=22, border=1, new_y="TOP", align="C")
        reporte_de_compras.multi_cell(
            text="\nRetención\na terceros", w=19, border=1, new_y="TOP", align="C"
        )
        reporte_de_compras.multi_cell(
            text="Anticipo a\ncuenta 1%\nIVA Reten.",
            w=18,
            border=1,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )

    reporte_de_compras.multi_cell(
        text="", w=20, new_x="LMARGIN", new_y="NEXT", align="C"
    )
    reporte_de_compras.multi_cell(
        text="", w=20, new_x="LMARGIN", new_y="NEXT", align="C"
    )

    reporte_de_compras.multi_cell(text=f"{i}", w=9, new_y="TOP", align="L")
    reporte_de_compras.multi_cell(text="23/03", w=11, new_y="TOP", align="L")
    reporte_de_compras.multi_cell(
        text="E0123456789123456789123456",
        w=21,
        new_y="TOP",
        align="L",
    )
    reporte_de_compras.multi_cell(text="1234567-8", w=18, new_y="TOP", align="L")
    reporte_de_compras.multi_cell(
        text="CORPORACION GILTON, S.A. DE C.V.", w=54, new_y="TOP", align="L"
    )
    reporte_de_compras.multi_cell(text="", w=19, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(text="", w=20, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(text="5,999,999.00", w=20, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(text="", w=20, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(text="779,999.87", w=15, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(text="6,779,998.87", w=22, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(text="6,779,998.87", w=19, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(
        text="59,999.99", w=18, new_x="LMARGIN", new_y="NEXT", align="R"
    )


for i in range(25):
    if reporte_de_compras.will_page_break(14.8):
        reporte_de_compras.add_page()

    reporte_de_compras.multi_cell(
        text="", w=20, new_x="LMARGIN", new_y="NEXT", align="C"
    )
    reporte_de_compras.multi_cell(
        text="", w=20, new_x="LMARGIN", new_y="NEXT", align="C"
    )

    reporte_de_compras.multi_cell(text=f"{i + 100}", w=9, new_y="TOP", align="L")
    reporte_de_compras.multi_cell(text="23/03", w=11, new_y="TOP", align="L")
    reporte_de_compras.multi_cell(
        text="DSC00-2566",
        w=21,
        new_y="TOP",
        align="L",
    )
    reporte_de_compras.multi_cell(text="1234567-8", w=18, new_y="TOP", align="L")
    reporte_de_compras.multi_cell(
        text="Importadora diversa S.A. de C.V.", w=54, new_y="TOP", align="L"
    )
    reporte_de_compras.multi_cell(text="", w=19, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(text="36,000.57", w=20, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(text="", w=20, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(text="", w=20, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(text="4,680.07", w=15, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(text="4,068.64", w=22, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(text="0.00", w=19, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(
        text="0.00", w=18, new_x="LMARGIN", new_y="NEXT", align="R"
    )


reporte_de_compras.ln(15)
reporte_de_compras.multi_cell(text="\n\n", w=25, new_y="TOP", align="C")
reporte_de_compras.multi_cell(text="Compras exentas\n\n    Internas                   Importaciones", w=50, new_y="TOP", align="C", border=1)
reporte_de_compras.multi_cell(text="Compras gravadas\n\nInternas                Importaciones                       Iva  ", w=75, new_y="TOP", align="C", border=1)
reporte_de_compras.multi_cell(text="\nTotal\ncompras", w=25, new_y="TOP", align="C", border=1)
reporte_de_compras.multi_cell(text="\nRetención\na terceros", w=25, new_y="TOP", align="C", border=1)
reporte_de_compras.multi_cell(text="Anticipo a\ncuenta 1%\nIVA Retenido", w=25, new_x="LMARGIN", new_y="NEXT", align="C", border=1)
reporte_de_compras.multi_cell(text="\nTotales", w=25, new_y="TOP", align="R")
reporte_de_compras.multi_cell(text="\n0.00", w=25, new_y="TOP", align="R", border=1)
reporte_de_compras.multi_cell(text="\n0.00", w=25, new_y="TOP", align="R", border=1)
reporte_de_compras.multi_cell(text="\n0.00", w=25, new_y="TOP", align="R", border=1)
reporte_de_compras.multi_cell(text="\n0.00", w=25, new_y="TOP", align="R", border=1)
reporte_de_compras.multi_cell(text="\n0.00", w=25, new_y="TOP", align="R", border=1)
reporte_de_compras.multi_cell(text="\n0.00", w=25, new_y="TOP", align="R", border=1)
reporte_de_compras.multi_cell(text="\n0.00", w=25, new_y="TOP", align="R", border=1)
reporte_de_compras.multi_cell(text="\n0.00", w=25, new_x="LMARGIN", new_y="NEXT", align="R", border=1)


if reporte_de_compras.will_page_break(50):
        reporte_de_compras.add_page() 
reporte_de_compras.ln(15)
reporte_de_compras.set_font(family="times", style="b", size=12)
reporte_de_compras.multi_cell(text="Nombre de Contador o Crontribuyente:", w=133.5, align="C", new_y="TOP")
reporte_de_compras.multi_cell(text="Firma de Contador o Crontribuyente:", w=133.5, align="C")
reporte_de_compras.output(name="Libro_de_compras.pdf")
