# Importa a biblioteca PyPDF2 para trabalhar com arquivos PDF
import PyPDF2

# Abre o arquivo PDF no modo de leitura binária ('rb')
pdf = open('Teste.pdf', 'rb')

# Cria um objeto PdfFileReader para ler o arquivo PDF
reader = PyPDF2.PdfFileReader(pdf)

# Usa o método getPage para obter a primeira página do PDF
pagina = reader.getPage(0)

# Imprime o texto extraído da primeira página
print(pagina.extractText())

# Fecha o arquivo PDF após a leitura
pdf.close()

