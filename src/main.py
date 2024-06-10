from generator import generate_pdfs

# pdf file
document_template_filepath = \
    "C:\\Users\\JP\\Nextcloud\\can carmina\\Finanzen\\Spendenverwaltung\\Zuwendungsbescheinigung_Vorlage_2023.pdf"
# csv with columns: [id, name and surname, address, plz, location]
member_data_csv_filepath = "C:\\Users\\JP\\Documents\\tmp cc\\mgl_daten.csv"
# csv with columns: [id, value (in EUR)]
zuwendungen_csv_filepath = "C:\\Users\\JP\\Documents\\tmp cc\\zuwendungs_daten_2023_2.csv"
output_filepath = "./../zuwendungsbescheinigungen_2023_2.pdf"

date = "02.10.2023"

generate_pdfs(
    date=date,
    document_template_filepath=document_template_filepath,
    member_data_csv_filepath=member_data_csv_filepath,
    zuwendungen_csv_filepath=zuwendungen_csv_filepath,
    output_pdf_filename=output_filepath
)
