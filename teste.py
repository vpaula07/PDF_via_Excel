from pathlib import Path

from formatcao_de_dados import pegar_template_renderizado

config = {
     'mes_referencia': '2023-01',
     'pasta_dados': Path('dados'),
     'arquivo_excel': 'dados.xlsx',
     'pasta_assets': Path('assets'),
     'arquivo_template':'template.jinja',
     'arquivo_css':'style.css',
}

html = pegar_template_renderizado(**config)

#with open('tabelas.html', 'w', encoding='utf-8') as arquivo:
     #arquivo.write(html)

# HTML para PDF

pasta_output = Path('output')
pasta_output.mkdir(exist_ok=True, parents=True)

import pdfkit

mes_referencia = config['mes_referencia']

nome_relatorio = f'Relatório Mensal - {mes_referencia}.pdf'
caminho_relatorio = pasta_output / nome_relatorio

caminho_exec = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
pdfkit_config = pdfkit.configuration(wkhtmltopdf=caminho_exec)

pdfkit.from_string(html, output_path=str(caminho_relatorio), configuration=pdfkit_config)