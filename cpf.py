from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Documento Inválido!!')


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = str(documento)
        else:
            raise ValueError('CPF inválido')

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def fatiamento(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.fatiamento()


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = str(documento)
        else:
            raise ValueError('CNPJ inválido')

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def fatiamento(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.fatiamento()
