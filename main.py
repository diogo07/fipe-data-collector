import requests
from consts import Veiculo


def get_marcas(tipo_veiculo):
    for i in range(1, 284):
        data = {
            "codigoTabelaReferencia": i,
            "codigoTipoVeiculo": tipo_veiculo
        }

        r = requests.post(url="https://veiculos.fipe.org.br/api/veiculos//ConsultarMarcas", data=data)
        print(r.text)


def get_modelos(tipo_veiculo):
    for i in range(1, 284):
        data = {
            "codigoTabelaReferencia": i,
            "codigoTipoVeiculo": tipo_veiculo
        }

        r = requests.post(url="https://veiculos.fipe.org.br/api/veiculos//ConsultarMarcas", data=data)
        print(r.text)


get_marcas(Veiculo.CARRO.value)