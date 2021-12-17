import secrets
from pathlib import Path
from fastapi import FastAPI
import qrcode

app = FastAPI()


def diretorio():
    """Método para pegar o diretório dos qr-codes gerados.

    Returns
    -------
    str
        Retorna a url do diretório qr-codes, onde será armazenado todos os qr-codes gerados.
    """
    # Obtem o caminho absoluto para o diretório home do usuário atual
    home = Path.home()
    path = Path(home, 'Documents', 'AGTEC',
                'Python', 'qr-code-fastapi', 'qr-codes')
    return path


@app.post('/v1/qrcode')
def qr_code_generation(text: str):
    """Método de geração de um qr-code

    Parameters
    ----------
    text : str
        Valor do qr-code

    Returns
    -------
    str
        Retorna a url do arquivo qr-code que acabou de ser gerado

    Raises
    ------
    exception
        Tratamento caso de algum erro durante a execução do método
    """
    try:
        qr_code = qrcode.make(text)
        file_name = secrets.token_hex(10)+'.png'
        qr_code.save('qr-codes/'+file_name)
        return f'{diretorio()}\{file_name}'
    except Exception as exception:
        raise exception
