import subprocess

def compress_pdf(input_path, output_path):
    # Comando para usar o Ghostscript e comprimir o PDF
    gs_command = [
        'gs',
        '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.4',
        '-dPDFSETTINGS=/ebook',  # Pode ser /screen, /ebook, /printer, ou /prepress
        '-dNOPAUSE',
        '-dQUIET',
        '-dBATCH',
        f'-sOutputFile={output_path}',
        input_path
    ]

    # Executar o comando
    subprocess.run(gs_command)

# Caminhos dos arquivos PDF de entrada e saída
input_pdf_path = ""
output_pdf_path = ""

# Chamar a função para comprimir o PDF
compress_pdf(input_pdf_path, output_pdf_path)
