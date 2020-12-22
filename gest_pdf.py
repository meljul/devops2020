from fpdf import FPDF
import purchase
import webbrowser

def createPDF(purchase_to_print):

       pdf = FPDF()
       pdf.add_page()
       pdf.set_font('Arial', 'B', 12)
       purchase_number = purchase_to_print.purchase_id
       purchase_employe = purchase_to_print.employee_name
       datedisplay = purchase_to_print.formated_date

       purchase_lines = purchase_to_print.purchase_details

       pdf.cell(35,5, txt = "ABC inc.", ln = 1, align='L')
       pdf.cell(35,5, txt = "Waterloo street", ln = 2, align='L')
       pdf.cell(35,5, txt = "1000 Brussels", ln=3, align='L' )
       pdf.cell(35,5, txt = f"Purchase number : {purchase_number}", ln=6, align='L' )
       pdf.cell(40,5, txt = f"Employee : {purchase_employe}", ln=6, align='L' )
       VAT = 6

       inclVAT = purchase_to_print.total
       exVAT = (inclVAT/100)*6
       VATdiff = inclVAT - exVAT
       print(purchase_lines)

       for menu in purchase_lines:
           print(menu)
           pdf.cell(40,8, txt = f'Menu: {menu[1]} - {menu[2]}', ln = 7, align='L')

       pdf.cell(40,5, txt = f"----------------------------------------------------------", ln=10, align='C' )
       pdf.cell(40,6, txt = f"                     excl.VAT     VAT      incl. VAT", ln=11, align='C' )
       pdf.cell(45,6, txt = f"  VAT {VAT}%    {round(VATdiff, 2)}     {round(exVAT, 2)}       {inclVAT}", ln=11, align='C' )
       pdf.cell(40,6, txt = f"----------------------------------------------------------", ln=10, align='C' )
       pdf.cell(40,6, txt = f"TOTAL                        {inclVAT}", ln=15, align='L' )
       pdf.cell(42,8, txt = f"Date          {datedisplay}", ln=18, align='L' )
       pdf.cell(42,8, txt = f"VAT number    BE 0123 4567 890", ln=18, align='L' )

       filepath = f"order_{datedisplay}h.pdf"
       pdf.output(filepath, 'F')

       webbrowser.open(filepath)



       return pdf
