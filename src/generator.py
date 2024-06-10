import csv
import os

from fill_in_pdf import create_pdf_from_member_data
from pdf_merge import merge_files


def clear_output_folder(output_folder):
    # remove all files in the output folder
    for file in os.listdir(output_folder):
        os.remove(f"{output_folder}/{file}")


def generate_pdfs(
        date,
        document_template_filepath,
        member_data_csv_filepath,
        zuwendungen_csv_filepath,
        output_pdf_filename,
        output_folder="./../output",
):
    # member_data
    with open(member_data_csv_filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        member_data = [row for row in reader]

    # zuwendungs daten
    with open(zuwendungen_csv_filepath, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        zuwendungs_data = [row for row in reader]

    join_data = []
    missing_data = []

    # join both data arrays on the first (id) column
    for i in range(len(zuwendungs_data)):
        added = False
        for j in range(len(member_data)):
            if zuwendungs_data[i][0] == member_data[j][0]:
                # append the joined data without the second id column
                join_data.append(member_data[j][:] + zuwendungs_data[i][1:])
                added = True
                continue
        if not added:
            missing_data.append(zuwendungs_data[i])

    # check if data is available
    if join_data is None or len(join_data) == 0:
        print("No data found in the CSV file")
        exit()

    print("Anzahl der Mitglieder: ", len(member_data))
    print("Anzahl der Zuwendungsdaten: ", len(zuwendungs_data))
    print("Anzahl nicht gefundener mgl_daten, die aber in zuwendungsdaten enthalten sind: ", len(missing_data))
    print("Fehlende daten von mitgliedern mit IDs: ", [row[0] for row in missing_data])
    print("Resultierende anzahl an zuwendungsbescheinigungen: ", len(join_data))

    print("Generating PDFs...")

    # create output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        clear_output_folder(output_folder)

    # create a pdf for each member
    for row in join_data:
        create_pdf_from_member_data(
            name=row[1],
            address=row[2],
            location=row[3] + " " + row[4],
            value=int(row[5]),
            date=date,
            template_filename=document_template_filepath,
            output_filename=f"{output_folder}/mitglied_{row[0]}.pdf"
        )

    # merge all pdfs into one
    pdfs = [f"{output_folder}/{pdf}" for pdf in os.listdir(output_folder)]
    merge_files(pdfs, output_pdf_filename)

    # remove all files in the output folder
    clear_output_folder(output_folder)

    print("Zuwendungsbescheinigungen wurden erfolgreich erstellt und zusammengeführt: ",
          os.path.abspath(output_pdf_filename))
