from PyPDF2 import PdfMerger
import os

dir_path = r"D:\BITS_WILP_MTech_Automotive_Electronics\Semester 1\Embedded System Design\Regular contents\OneDrive_1_9-16-2022"
pdfs = []
for path in os.scandir(dir_path):
    if path.is_file() and '.pdf' in path.name:
        pdfs.append(dir_path+'\\'+path.name)


# pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']
#
merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()