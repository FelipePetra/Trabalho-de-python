import tkinter
import PyPDF2
import requests



url = "https://date.nager.at/api/v3/PublicHolidays/2025/BR"

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
    lista_de_datas = reader.pages[0].extract_text().split("\n")
    print (lista_de_datas)
    for data in lista_de_datas:
        if data.strip() in response.text:
            print (data)
        

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
