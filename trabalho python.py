import tkinter
import PyPDF2
import requests

url = "https://date.nager.at/api/v3/PublicHolidays/2024/BR"

payload = {}
headers = {
  'accept': 'application/json',
  'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJz'
  }

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

url = "https://date.nager.at/api/v3/PublicHolidays/2025/BR"

payload = {}
headers = {
  'accept': 'application/json',
  'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJz'
  }

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

url = "https://date.nager.at/api/v3/PublicHolidays/2026/BR"

payload = {}
headers = {
  'accept': 'application/json',
  'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJz'
  }

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


def Get_text_from_PDFfiles_usingPyPDF2(in_PdfFile):
    reader = PyPDF2.PdfReader(in_PdfFile) 
    print(reader.pages[0].extract_text())

def Exemplo():
    root = tkinter.Tk()
    root.title("Leitor de PDF")
    root.resizable(True, True)
    
    test = tkinter.Button(root, text="Ler PDF", command=LerPDF)
    test.pack()

    
    root.mainloop()

def LerPDF():
    Get_text_from_PDFfiles_usingPyPDF2(r"C:\Users\202502304706\Documents\Lista de datas.pdf")

Exemplo()
LerPDF()
