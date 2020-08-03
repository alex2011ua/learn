from bs4 import BeautifulSoup
from decimal import Decimal



def convert(amount, cur_from, cur_to, date, requests):
    def curse(val):
        nominal = int(soup.valcurs.find(string =val).parent.parent.nominal.string)
        value = (soup.valcurs.find(string =val).parent.parent.value.string)
        val_float = value.replace(',', '.')
        return nominal, float(val_float)

    payload = {'date_req':date}

    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp', params=payload)  # Использовать переданный requests
    soup = BeautifulSoup(response.text, "lxml")

    def v_RUR(valute, amount):
        nom, val = curse(valute)
        result = (amount * Decimal(val)) / Decimal(nom)
        return result

    def iz_RUR(valute, amount):
        nom, val = curse(valute)
        result = (amount * Decimal(nom)) / Decimal(val)
        return result

    if cur_from == 'RUR':
        result = iz_RUR(cur_to, amount)
    elif cur_to == 'RUR':
        result = v_RUR(cur_from, amount)
    else:
        perevod_v_RUR = v_RUR(cur_from, amount)
        result = iz_RUR(cur_to, perevod_v_RUR)
    result = result.quantize(Decimal("1.0000"))
    return result  # не забыть про округление до 4х знаков после запятой
