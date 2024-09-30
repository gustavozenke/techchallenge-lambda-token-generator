import json
from exceptions.cliente_nao_encontrado_exception import ClienteNaoEncontradoException
from service.cliente_service import ClienteService
from service.token_service import TokenService
from utils.utils import payload_encode_token, payload_response_gateway


class AutenticacaoService:

    def __init__(self):
        self.cliente_sem_identificacao = "00000000000"

    def processar(self, event):

        cpf_cliente = event.get('pathParameters', {}).get("cpf") if event.get('pathParameters') is not None else {}

        if cpf_cliente:
            try:
                cliente_service = ClienteService()
                response = cliente_service.buscar_cliente(cpf_cliente)
            except ClienteNaoEncontradoException as error:
                status_code = error.args[0]
                body = error.args[1]
                return payload_response_gateway(status_code, body)
        else:
            response = {
                "cpf": self.cliente_sem_identificacao,
                "nome": "Cliente sem identificacao",
                "email": None,
                "marketing": False
            }

        payload = payload_encode_token(response)
        token_service = TokenService()
        token = token_service.encode_jwt_token(payload)

        body = {
            "access_token": token
        }

        return payload_response_gateway(200, json.dumps(body))
