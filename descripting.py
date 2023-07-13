from pypdf import PdfReader, PdfWriter
from os import chdir, getcwd, listdir


path = chdir('D:\Documentos\cursos_projetos\projetos\Projeto_Python\lendo_pdf\contas')
print(getcwd())

def descripting(reader):
    if reader.is_encrypted:
        reader.decrypt('37119')

def extrair_vencimento(string):

    inicio = string.find('Vencimento')
    return print(string[inicio + 10 : inicio + 21])


def ler_arquivo():
    teste = PdfReader('D:\Documentos\cursos_projetos\projetos\Projeto_Python\lendo_pdf\contas\SuaContaClaro_Abr-2023.pdf')
    page_teste = teste.pages

    page_teste[0].extract_text()

    print(page_teste)

for arquivo in listdir():
    print(arquivo)
    reader = PdfReader(arquivo)
    
    descripting(reader)
    page = reader.pages
    string = page[0].extract_text()
    extrair_vencimento(string)


ler_arquivo()


