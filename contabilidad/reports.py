from fpdf import FPDF

from .models import Compras


class ReporteDeCompras(FPDF):
    def add_page(self, empresa, año, mes):
        self.empresa = empresa
        self.año = año
        self.mes = mes
        super().add_page()

    def header(self):
        empresa = self.empresa
        año = self.año
        mes = self.mes
        self.set_font(family="helvetica", style="", size=10)
        # Los márgenes son ajustados para tener un área de 267 mm de uso horizontal
        # Y 195.9 mm vertical, estando la página en formato horizontal.
        self.set_margins(left=6.2, top=10, right=6.2)
        self.set_auto_page_break(auto=True, margin=10)
        self.cell(w=30, text="REGISTRO Nº", align="L")
        self.cell(w=59, text=empresa.nrc, align="L")
        self.cell(w=89, text="LIBRO DE COMPRAS", align="C")
        self.cell(w=89)
        self.ln(5)
        self.cell(w=30, text="MES", align="L")
        self.cell(w=59, text=f"{mes}", align="L")
        self.cell(w=89, text="", align="C")
        self.cell(w=89)
        self.ln(5)
        self.cell(w=30, text="AÑO", align="L")
        self.cell(w=59, text=f"{año}", align="L")
        self.cell(w=89, text=empresa.nombre, align="C")
        self.cell(w=89, text=f"FOLIO {self.page_no()}", align="R")
        self.ln(8)
        self.set_font(family="helvetica", style="", size=7)
        # TOP da la siguiente celda a la par.

    def insertar_encabezado_de_tabla(self):
        # Encabezado de tabla
        self.multi_cell(text="\nCorre-\nlativo", w=9, border=1, new_y="TOP", align="C")
        self.multi_cell(text="\nFecha\nEmisión", w=11, border=1, new_y="TOP", align="C")
        self.multi_cell(
            text="\nNº del\nComprobante", w=20, border=1, new_y="TOP", align="C"
        )
        self.multi_cell(
            text="\nNº de\nRegistro", w=18, border=1, new_y="TOP", align="C"
        )
        self.multi_cell(
            text="\n\nNombre de Proveedor", w=54, border=1, new_y="TOP", align="C"
        )

        self.multi_cell(
            text="\nCompras Exentas",
            w=40,
            border=1,
            new_x="LEFT",
            new_y="NEXT",
            align="C",
        )
        self.multi_cell(text="Internas", w=20, border=1, new_y="TOP", align="C")
        self.multi_cell(text="Importaciones", w=20, border=1, new_y="TOP", align="C")
        # Configuro las posición actual para que no baje
        self.set_xy(158.2, 28.0)
        self.multi_cell(
            text="\nCompras Gravadas",
            w=55,
            border=1,
            new_x="LEFT",
            new_y="NEXT",
            align="C",
        )
        self.multi_cell(text="Internas", w=20, border=1, new_y="TOP", align="C")
        self.multi_cell(text="Importaciones", w=20, border=1, new_y="TOP", align="C")
        self.multi_cell(text="IVA", w=15, border=1, new_y="TOP", align="C")
        self.set_xy(213.2, 28.0)
        self.multi_cell(text="\nTotal\ncompras", w=22, border=1, new_y="TOP", align="C")
        self.multi_cell(
            text="\nRetención\na terceros", w=19, border=1, new_y="TOP", align="C"
        )
        self.multi_cell(
            text="Anticipo a\ncuenta 1%\nIVA Reten.",
            w=18,
            border=1,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )


def crear_reporte_de_compras(empresa, año, mes):
    """
    Función para crear un reporte de compras de la empresa en mes y año
    de los argumentos que se pasan
    """
    compras = Compras.objects.filter(empresa=empresa, fecha__month=mes, fecha__year=año)
    reporte_de_compras = ReporteDeCompras(
        format="Letter", unit="mm", orientation="landscape"
    )
    reporte_de_compras.add_page(empresa=empresa, año=año, mes=mes)
    reporte_de_compras.set_author("ECONTA S.A. de C.V.")
    reporte_de_compras.set_creator("Pacamara Dev")
    reporte_de_compras.set_font(family="helvetica", style="", size=7)
    reporte_de_compras.insertar_encabezado_de_tabla()

    correlativo = 1
    total_compras_exentas_internas = 0
    total_compras_exentas_importaciones = 0
    total_compras_gravadas_internas = 0
    total_compras_gravadas_importaciones = 0
    total_iva = 0
    total_compras = 0
    for compra in compras:
        if reporte_de_compras.will_page_break(14.8):
            reporte_de_compras.add_page(empresa=empresa, año=año, mes=mes)
            reporte_de_compras.insertar_encabezado_de_tabla()

        reporte_de_compras.multi_cell(
            text="", w=20, new_x="LMARGIN", new_y="NEXT", align="C"
        )
        reporte_de_compras.multi_cell(
            text=f"{correlativo}", w=9, new_y="TOP", align="L"
        )
        reporte_de_compras.multi_cell(
            text=f"{compra.fecha.day}/{compra.fecha.month}",
            w=11,
            new_y="TOP",
            align="L",
        )
        reporte_de_compras.multi_cell(
            text=f"{compra.numero_de_comprobante}",
            w=21,
            new_y="TOP",
            align="L",
        )
        reporte_de_compras.multi_cell(
            text=f"{compra.proveedor.nrc}", w=18, new_y="TOP", align="L"
        )
        reporte_de_compras.multi_cell(
            text=f"{compra.proveedor.nombre}", w=54, new_y="TOP", align="L"
        )
        if compra.compra_excenta:
            if compra.tipo_de_compra == "INT":
                reporte_de_compras.multi_cell(
                    text=f"{compra.compra_excenta}", w=20, new_y="TOP", align="R"
                )
                reporte_de_compras.multi_cell(text="", w=20, new_y="TOP", align="R")
                total_compras_exentas_internas += compra.compra_excenta
            else:
                reporte_de_compras.multi_cell(text="", w=20, new_y="TOP", align="R")
                reporte_de_compras.multi_cell(
                    text=f"{compra.compra_excenta}", w=20, new_y="TOP", align="R"
                )
                total_compras_exentas_importaciones += compra.compra_excenta
        else:
            reporte_de_compras.multi_cell(text="", w=20, new_y="TOP", align="R")
            reporte_de_compras.multi_cell(text="", w=20, new_y="TOP", align="R")
        if compra.compra_neta:
            if compra.tipo_de_compra == "INT":
                reporte_de_compras.multi_cell(
                    text=f"{compra.compra_neta}", w=20, new_y="TOP", align="R"
                )
                reporte_de_compras.multi_cell(text="", w=20, new_y="TOP", align="R")
                total_compras_gravadas_internas += compra.compra_excenta
            else:
                reporte_de_compras.multi_cell(text="", w=20, new_y="TOP", align="R")
                reporte_de_compras.multi_cell(
                    text=f"{compra.compra_neta}", w=20, new_y="TOP", align="R"
                )
                total_compras_gravadas_importaciones += compra.compra_excenta
        else:
            reporte_de_compras.multi_cell(text="", w=20, new_y="TOP", align="R")
            reporte_de_compras.multi_cell(text="", w=20, new_y="TOP", align="R")
        reporte_de_compras.multi_cell(
            text=f"{compra.iva}", w=15, new_y="TOP", align="R"
        )
        total_iva += compra.iva
        reporte_de_compras.multi_cell(
            text=f"{compra.total}", w=22, new_y="TOP", align="R"
        )
        total_compras += compra.total
        reporte_de_compras.multi_cell(text=f"", w=19, new_y="TOP", align="R")
        reporte_de_compras.multi_cell(
            text=f"{compra.percepcion_iva}",
            w=18,
            align="R",
        )
        correlativo += 1

    reporte_de_compras.ln(15)
    reporte_de_compras.multi_cell(text="\n\n", w=25, new_y="TOP", align="C")
    reporte_de_compras.multi_cell(
        text="Compras exentas\n\n    Internas                   Importaciones",
        w=50,
        new_y="TOP",
        align="C",
        border=1,
    )
    reporte_de_compras.multi_cell(
        text="Compras gravadas\n\nInternas                Importaciones                       Iva  ",
        w=75,
        new_y="TOP",
        align="C",
        border=1,
    )
    reporte_de_compras.multi_cell(
        text="\nTotal\ncompras", w=25, new_y="TOP", align="C", border=1
    )
    reporte_de_compras.multi_cell(
        text="\nRetención\na terceros", w=25, new_y="TOP", align="C", border=1
    )
    reporte_de_compras.multi_cell(
        text="Anticipo a\ncuenta 1%\nIVA Retenido",
        w=25,
        new_x="LMARGIN",
        new_y="NEXT",
        align="C",
        border=1,
    )
    reporte_de_compras.multi_cell(text="\nTotales", w=25, new_y="TOP", align="R")
    reporte_de_compras.multi_cell(
        text=f"\n{total_compras_exentas_internas}",
        w=25,
        new_y="TOP",
        align="R",
        border=1,
    )
    reporte_de_compras.multi_cell(
        text=f"\n{total_compras_exentas_importaciones}",
        w=25,
        new_y="TOP",
        align="R",
        border=1,
    )
    reporte_de_compras.multi_cell(
        text=f"\n{total_compras_exentas_internas}",
        w=25,
        new_y="TOP",
        align="R",
        border=1,
    )
    reporte_de_compras.multi_cell(
        text=f"\n{total_compras_gravadas_importaciones}",
        w=25,
        new_y="TOP",
        align="R",
        border=1,
    )
    reporte_de_compras.multi_cell(
        text=f"\n{total_iva}", w=25, new_y="TOP", align="R", border=1
    )
    reporte_de_compras.multi_cell(
        text=f"\n{total_compras}", w=25, new_y="TOP", align="R", border=1
    )
    reporte_de_compras.multi_cell(text="\n0.00", w=25, new_y="TOP", align="R", border=1)
    reporte_de_compras.multi_cell(
        text="\n0.00", w=25, new_x="LMARGIN", new_y="NEXT", align="R", border=1
    )

    if reporte_de_compras.will_page_break(50):
        reporte_de_compras.add_page(empresa=empresa, año=año, mes=mes)
    reporte_de_compras.ln(15)
    reporte_de_compras.set_font(family="times", style="b", size=12)
    reporte_de_compras.multi_cell(
        text="Nombre de Contador o Crontribuyente:", w=133.5, align="C", new_y="TOP"
    )
    reporte_de_compras.multi_cell(
        text="Firma de Contador o Crontribuyente:", w=133.5, align="C"
    )
    return reporte_de_compras


class ReporteDeVentasAContribuyentes(FPDF):
    def header(self):
        self.set_font(family="helvetica", style="", size=10)
        # Los márgenes son ajustados para tener un área de 267 mm de uso horizontal
        # Y 195.9 mm vertical, estando la página en formato horizontal.
        self.set_margins(left=6.2, top=10, right=6.2)
        self.set_auto_page_break(auto=True, margin=10)
        self.cell(w=30, text="REGISTRO Nº", align="L")
        self.cell(w=59, text="172014-0", align="L")
        self.cell(w=89, text="LIBRO DE VENTAS A CONTRIBUYENTES", align="C")
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

    def insertar_encabezado_de_tabla(self):
        # Encabezado de tabla
        self.multi_cell(text="\nCorre-\nlativo", w=10, border=1, new_y="TOP", align="C")
        self.multi_cell(text="\nFecha\nEmisión", w=12, border=1, new_y="TOP", align="C")
        self.multi_cell(
            text="\nNº del\nComprobante", w=25, border=1, new_y="TOP", align="C"
        )
        self.multi_cell(
            text="\nNº de\nRegistro", w=20, border=1, new_y="TOP", align="C"
        )
        self.multi_cell(
            text="\n\nNombre de Proveedor", w=65, border=1, new_y="TOP", align="C"
        )

        self.multi_cell(
            text="Ventas Internas",
            w=60,
            border=1,
            new_x="LEFT",
            new_y="NEXT",
            align="C",
        )
        self.multi_cell(text="\nExentas", w=30, border=1, new_y="TOP", align="C")
        self.multi_cell(text="\nGrabadas", w=30, border=1, new_y="TOP", align="C")
        # Configuro las posición actual para que no baje
        self.set_xy(198.2, 28.0)
        self.multi_cell(
            text="\nIVA\n(Débito Fiscal)", w=25, border=1, new_y="TOP", align="C"
        )
        self.multi_cell(
            text="Anticipo a\ncuenta IVA\nretenido",
            w=22,
            border=1,
            new_y="TOP",
            align="C",
        )
        self.multi_cell(
            text="\nTotal\n ",
            w=27,
            border=1,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )


def crear_reporte_de_ventas_a_contribuyentes():
    """
    Función para crear un reporte de compras
    """
    reporte_de_ventas_ccf = ReporteDeVentasAContribuyentes(
        format="Letter", unit="mm", orientation="landscape"
    )
    reporte_de_ventas_ccf.add_page()
    reporte_de_ventas_ccf.set_author("ECONTA S.A. de C.V.")
    reporte_de_ventas_ccf.set_creator("Pacamara Dev")
    reporte_de_ventas_ccf.set_font(family="helvetica", style="", size=7)
    reporte_de_ventas_ccf.insertar_encabezado_de_tabla()

    for i in range(100):
        if reporte_de_ventas_ccf.will_page_break(14.8):
            reporte_de_ventas_ccf.add_page()
            reporte_de_ventas_ccf.insertar_encabezado_de_tabla()

        reporte_de_ventas_ccf.multi_cell(
            text="", w=20, new_x="LMARGIN", new_y="NEXT", align="C"
        )
        reporte_de_ventas_ccf.multi_cell(text=f"{i+1}", w=10, new_y="TOP", align="L")
        reporte_de_ventas_ccf.multi_cell(text="23/03", w=12, new_y="TOP", align="L")
        reporte_de_ventas_ccf.multi_cell(
            text="E0123456789123456789123456",
            w=25,
            new_y="TOP",
            align="L",
        )
        reporte_de_ventas_ccf.multi_cell(text="1234567-8", w=20, new_y="TOP", align="L")
        reporte_de_ventas_ccf.multi_cell(
            text="CORPORACION GILTON, S.A. DE C.V.", w=65, new_y="TOP", align="L"
        )
        reporte_de_ventas_ccf.multi_cell(text="", w=30, new_y="TOP", align="R")
        reporte_de_ventas_ccf.multi_cell(
            text="5,999,999.00", w=30, new_y="TOP", align="R"
        )
        reporte_de_ventas_ccf.multi_cell(
            text="505,326.58", w=25, new_y="TOP", align="R"
        )
        reporte_de_ventas_ccf.multi_cell(text="9,999.87", w=22, new_y="TOP", align="R")
        reporte_de_ventas_ccf.multi_cell(
            text="6,779,998.87", w=27, new_x="LMARGIN", new_y="NEXT", align="R"
        )

    # Agrego la fila de totales del final:

    reporte_de_ventas_ccf.multi_cell(
        text="", w=20, new_x="LMARGIN", new_y="NEXT", align="C"
    )
    reporte_de_ventas_ccf.multi_cell(
        text="", w=20, new_x="LMARGIN", new_y="NEXT", align="C"
    )
    reporte_de_ventas_ccf.multi_cell(text="\nTOTALES", w=132, new_y="TOP", align="R")

    reporte_de_ventas_ccf.multi_cell(
        text="\n0.00", w=30, new_y="TOP", align="R", border=1
    )
    reporte_de_ventas_ccf.multi_cell(
        text="\n5,999,999.00", w=30, new_y="TOP", align="R", border=1
    )
    reporte_de_ventas_ccf.multi_cell(
        text="\n505,326.58", w=25, new_y="TOP", align="R", border=1
    )
    reporte_de_ventas_ccf.multi_cell(
        text="\n9,999.87", w=22, new_y="TOP", align="R", border=1
    )
    reporte_de_ventas_ccf.multi_cell(
        text="\n6,779,998.87", w=27, new_y="TOP", align="R", border=1
    )

    # Espacio para firmas, si no hay suficiente espacio se hace un quiebre
    if reporte_de_ventas_ccf.will_page_break(50):
        reporte_de_ventas_ccf.add_page()
    reporte_de_ventas_ccf.ln(15)
    reporte_de_ventas_ccf.set_font(family="times", style="b", size=12)
    reporte_de_ventas_ccf.multi_cell(
        text="Firma de contribuyente:", w=133.5, align="C", new_y="TOP"
    )
    reporte_de_ventas_ccf.multi_cell(text="Firma de Contador:", w=133.5, align="C")
    reporte_de_ventas_ccf.output(name="Libro_de_ventas_ccf.pdf")


class ReporteDeVentasAConsumidorFinal(FPDF):
    def header(self):
        self.set_font(family="helvetica", style="", size=10)
        # Los márgenes son ajustados para tener un área de 260 mm de uso horizontal
        # Y 195.9 mm vertical, estando la página en formato horizontal.
        # Por lo tanto para hacer uso de mediciones exactas hay que empezar a
        # contar en 9.7 mm a la izquierda e ir sumando
        self.set_margins(left=9.7, top=10, right=9.7)
        self.set_auto_page_break(auto=True, margin=10)
        self.cell(w=29, text="REGISTRO Nº", align="L")
        self.cell(w=57, text="172014-0", align="L")
        self.cell(w=87, text="LIBRO DE VENTAS A CONSUMIDOR FINAL", align="C")
        self.cell(w=87)
        self.ln(5)
        self.cell(w=29, text="MES", align="L")
        self.cell(w=57, text="Febrero", align="L")
        self.cell(w=87, text="", align="C")
        self.cell(w=87)
        self.ln(5)
        self.cell(w=29, text="AÑO", align="L")
        self.cell(w=57, text="2024", align="L")
        self.cell(w=87, text="COMERCIALIZADORA GILTON, S.A. DE C.V.", align="C")
        self.cell(w=87, text=f"FOLIO {self.page_no()}", align="R")
        self.ln(8)
        self.set_font(family="helvetica", style="", size=7)
        # TOP da la siguiente celda a la par.

    def insertar_encabezado_de_tabla(self):
        # Encabezado de tabla
        self.multi_cell(
            text="\nFecha de\nEmisión", w=15, border=1, new_y="TOP", align="C"
        )

        self.multi_cell(
            text="Facturas",
            w=90,
            border=1,
            new_x="LEFT",
            new_y="NEXT",
            align="C",
        )
        self.multi_cell(text="\nDel Nº", w=45, border=1, new_y="TOP", align="C")
        self.multi_cell(text="\nAl Nº", w=45, border=1, new_y="TOP", align="C")
        # Configuro las posición actual para que no baje
        self.set_xy(114.7, 28.0)
        self.multi_cell(text="\n\nSucursal", w=35, border=1, new_y="TOP", align="C")
        self.multi_cell(
            text="Ventas",
            w=90,
            border=1,
            new_x="LEFT",
            new_y="NEXT",
            align="C",
        )
        self.multi_cell(text="\nExcentas", w=30, border=1, new_y="TOP", align="C")
        self.multi_cell(
            text="Gravadas\n Locales", w=30, border=1, new_y="TOP", align="C"
        )
        self.multi_cell(
            text="Gravadas\nExportaciones", w=30, border=1, new_y="TOP", align="C"
        )
        # Configuro las posición actual para que no baje
        self.set_xy(239.7, 28.0)
        self.multi_cell(
            text="\nVentas\nTotales",
            w=29,
            border=1,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )


def crear_reporte_de_ventas_a_consumidor_final():

    reporte_de_ventas_a_consumidor_final = ReporteDeVentasAConsumidorFinal(
        format="Letter", unit="mm", orientation="landscape"
    )
    reporte_de_ventas_a_consumidor_final.add_page()
    reporte_de_ventas_a_consumidor_final.set_author("ECONTA S.A. de C.V.")
    reporte_de_ventas_a_consumidor_final.set_creator("Pacamara Dev")
    reporte_de_ventas_a_consumidor_final.set_font(family="helvetica", style="", size=7)
    reporte_de_ventas_a_consumidor_final.insertar_encabezado_de_tabla()

    for i in range(100):
        if reporte_de_ventas_a_consumidor_final.will_page_break(14.8):
            reporte_de_ventas_a_consumidor_final.add_page()
            reporte_de_ventas_a_consumidor_final.insertar_encabezado_de_tabla()

        reporte_de_ventas_a_consumidor_final.multi_cell(
            text="", w=20, new_x="LMARGIN", new_y="NEXT", align="C"
        )
        reporte_de_ventas_a_consumidor_final.multi_cell(
            text="23/03", w=15, new_y="TOP", align="L"
        )
        reporte_de_ventas_a_consumidor_final.multi_cell(
            text="E0123456789123456789123456",
            w=45,
            new_y="TOP",
            align="L",
        )
        reporte_de_ventas_a_consumidor_final.multi_cell(
            text="E0123456789123456789123477",
            w=45,
            new_y="TOP",
            align="L",
        )
        reporte_de_ventas_a_consumidor_final.multi_cell(
            text="Centro 1", w=35, new_y="TOP", align="L"
        )
        reporte_de_ventas_a_consumidor_final.multi_cell(
            text="", w=30, new_y="TOP", align="L"
        )
        reporte_de_ventas_a_consumidor_final.multi_cell(
            text="", w=30, new_y="TOP", align="R"
        )
        reporte_de_ventas_a_consumidor_final.multi_cell(
            text="9,999.00", w=30, new_y="TOP", align="R"
        )
        reporte_de_ventas_a_consumidor_final.multi_cell(
            text="9,999.00", w=29, new_y="TOP", align="R"
        )
        reporte_de_ventas_a_consumidor_final.multi_cell(
            text="", w=20, new_x="LMARGIN", new_y="NEXT", align="C"
        )
    if reporte_de_ventas_a_consumidor_final.will_page_break(14.8):
        reporte_de_ventas_a_consumidor_final.add_page()

    reporte_de_ventas_a_consumidor_final.multi_cell(
        text="", w=20, new_x="LMARGIN", new_y="NEXT", align="C"
    )
    reporte_de_ventas_a_consumidor_final.multi_cell(
        text="", w=20, new_x="LMARGIN", new_y="NEXT", align="C"
    )
    reporte_de_ventas_a_consumidor_final.multi_cell(
        text="", w=20, new_x="LMARGIN", new_y="NEXT", align="C"
    )
    reporte_de_ventas_a_consumidor_final.multi_cell(
        text="\nTOTALES", w=140, new_y="TOP", align="R"
    )
    reporte_de_ventas_a_consumidor_final.multi_cell(
        text="\n$0.00", w=30, new_y="TOP", align="R", border=1
    )
    reporte_de_ventas_a_consumidor_final.multi_cell(
        text="\n$0.00", w=30, new_y="TOP", align="R", border=1
    )
    reporte_de_ventas_a_consumidor_final.multi_cell(
        text="\n9,999,999.00", w=30, new_y="TOP", align="R", border=1
    )
    reporte_de_ventas_a_consumidor_final.multi_cell(
        text="\n9,999,999.00", w=29, new_y="TOP", align="R", border=1
    )
    if reporte_de_ventas_a_consumidor_final.will_page_break(50):
        reporte_de_ventas_a_consumidor_final.add_page()
    reporte_de_ventas_a_consumidor_final.ln(15)
    reporte_de_ventas_a_consumidor_final.set_font(family="times", style="b", size=12)
    reporte_de_ventas_a_consumidor_final.multi_cell(
        text="Firma de contribuyente:", w=133.5, align="C", new_y="TOP"
    )
    reporte_de_ventas_a_consumidor_final.multi_cell(
        text="Firma de Contador:", w=133.5, align="C"
    )
    reporte_de_ventas_a_consumidor_final.output(
        name="Libro_de_ventas_consumidor_final.pdf"
    )
    return reporte_de_ventas_a_consumidor_final
