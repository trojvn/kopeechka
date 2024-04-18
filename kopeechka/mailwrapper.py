import contextlib
from typing import Literal

import httpx

SITES = Literal["telegram.org", "tiktok.com"]
MAIL_TYPES = [
    "gmail.com",
    "outlook.com",
    "rambler.ru",
    "yahoo.com",
    "hotmail.com",
    "lenta.ru",
    "ya.ru",
    "icloud.com",
]


class KopeechkaMailWrapper:
    def __init__(self, token: str):
        self.__base_url, self.__token = "https://api.kopeechka.store", token

    def get_mail(
        self,
        site: SITES,
        mail_type: str,
        regex: str = "",
    ) -> str:
        url = f"{self.__base_url}/mailbox-get-email"
        params = {
            "token": self.__token,
            "site": site,
            "mail_type": mail_type,
            "regex": regex,
        }
        with contextlib.suppress(Exception):
            json_data = httpx.get(url, params=params).json()
            return f"{json_data['mail']}|{json_data['id']}"
        return "ERROR"

    # noinspection PyShadowingBuiltins
    def get_message(self, id: str) -> str:
        url = f"{self.__base_url}/mailbox-get-message"
        params = {"token": self.__token, "id": id}
        with contextlib.suppress(Exception):
            json_data = httpx.get(url, params=params).json()
            return str(json_data["value"])
        return "WAIT_LINK"
