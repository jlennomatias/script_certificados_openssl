import os
from gerar_certificados import gerar_cert

clientes = ["cli_teste"]
fapis = ['fapi1', 'fapi2', 'dcr']
certificados = ['brcac', 'enc', 'sig']


def criar_pasta():
    """Criando as pastas dos certificados e das certificações"""
    for cliente in clientes: 
        for fapi in fapis: 
            for certi in certificados:
                if not os.path.exists(f'{cliente}/{fapi}/{certi}'):
                    os.makedirs(f'{cliente}/{fapi}/{certi}')
                if certi == 'sig' or certi == 'enc':
                    gerar_cert(f'{cliente}/{fapi}/{certi}/')


