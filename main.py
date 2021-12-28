from cpf import Documento
from telefonebr import Telefonebr
from datasbr import DatasBr

doc1 = Documento.cria_documento('08189769000292')
doc2 = Documento.cria_documento('31687330832')
tel1 = Telefonebr('13991128595')
date1 = DatasBr()
print(doc1)
print(doc2)
print(tel1)
print(date1.mes_cadastro())
print(date1.dias_semana())
print(date1)
print(date1.tempo_cadastro())
