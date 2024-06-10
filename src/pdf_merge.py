from pypdf import PdfMerger


def merge_files(pdfs, output_filepath):
    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(output_filepath)
    merger.close()
