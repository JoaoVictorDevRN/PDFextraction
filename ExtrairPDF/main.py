import PyPDF2

pdf = open('Teste.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdf)
pagina = reader.getPage(0)  # Use getPage para obter a página

print(pagina.extractText())

pdf.close()  # Não se esqueça de fechar o arquivo PDF após a leitura
