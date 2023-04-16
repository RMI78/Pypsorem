import httpx
from bs4 import BeautifulSoup

class Lorem():
    def __init__(self, dataFormat: str, amount: int, startLorem: bool) -> None:
        self.dataFormat = dataFormat
        self.amount = amount 
        self.startLorem = startLorem
        self.__req()
        self.__parse()

    def __req(self) -> None:
        booleanStart = 'yes' if self.startLorem else 'no'
        try:
            self._request = httpx.get(f'https://www.lipsum.com/feed/html?amount={self.amount}&what={self.dataFormat}&start={booleanStart}&generate=Generate+lorem+Ipsum')
            self._request.raise_for_status()
        except httpx.RequestError as err:
            print(f"An error occurred while making the request: {err}")
        except httpx.HTTPStatusError as err:
            print(f"HTTP status error: {err}")

    def __parse(self) -> None:
        self._htmlParsing = BeautifulSoup(self._request.text, 'html.parser').find(id="lipsum").get_text()
        if self.dataFormat == "lists":
            self._htmlParsing = self._htmlParsing.replace('\n\n\n\n', '\n').replace('.\n', '. ')[3:-1]
        elif self.dataFormat == "words":
            self._htmlParsing = self._htmlParsing[2:-1]
        elif self.dataFormat == "bytes":
            self._htmlParsing = self._htmlParsing[2:-1]
        elif self.dataFormat == "paras":
            self._htmlParsing = self._htmlParsing.replace('\n\n', '')[:-1]

    def __str__(self) -> str:
        return self._htmlParsing