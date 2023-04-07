from Crypto.PublicKey import RSA
from config import PASS


def gerar_cert(path):
    # Encriptando o arquivo privado
    
    with open(f"{path}private.pem", 'wb') as f:
        key = RSA.generate(2048)
        encrypted_key = key.export_key(passphrase=PASS, pkcs=1, protection='scryptAndAES256-CBC')
        f.write(encrypted_key)

    # Abrindo o arquivo privado
    with open(f"{path}private.pem", 'rb') as f:
        encrypted_key = f.read()
        key = RSA.import_key(encrypted_key, passphrase=PASS)
        public_key = key.publickey().export_key()
        decrypted_key = key.export_key()
    
        #gerando o arquivo publico
        with open(f"{path}public.pem", 'wb') as f:
            f.write(public_key)
            
        # Salve a chave privada descriptografada em um arquivo
        with open(f"{path}private-decrypt.pem", "wb") as f:
            f.write(decrypted_key)

