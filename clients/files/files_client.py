from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class File(TypedDict):
    """
    Описание структуры файла.
    """
    id: str
    url: str
    filename: str
    directory: str

class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла
    """
    filename: str
    directory: str
    upload_file: str

class CreateFileResponseDict(TypedDict):
    """
    Описание структуры ответа создания файла.
    """
    file: File

class FileClient(APIClient):
    """
       Клиент для работы с /api/v1/files
    """


    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файда.
        :return: Ответ от сервера в виде ответа httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file
        :return: Ответ от сервера в виде ответа httpx.Response
        """
        return self.post(
            f"/api/v1/files",
            data=request,
            files={"upload_file": open(request['upload_file'], 'rb')},
        )

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файда.
        :return: Ответ от сервера в виде ответа httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        response = self.create_file_api(request)
        return response.json()

def get_files_client(user: AuthenticationUserDict) -> FileClient:
    """
    Функция создает экземпляр FileClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FileClient
    """
    return FileClient(client=get_private_http_client(user))