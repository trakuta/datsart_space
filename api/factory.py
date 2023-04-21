import requests
import json
import time


token = '642fed5a96d7e642fed5a96d81'


def generate_paint():
    '''
    Чтобы выбрать краски, надо сперва их сгенерировать на фабрике,
    на выбор дается 3 лота с разным количеством краски.
    За один такт генерится только один набор.
    '''
    url = 'http://api.datsart.dats.team/art/factory/generate'
    headers = {
            "Authorization": f"Bearer {token}",
            "Content-Length": '',
            "Content-Type": 'multipart/form-data; boundary='
            '----WebKitFormBoundary7MA4YWxkTrZu0gW'
    }
    body = '----WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
    headers['Content-Length'] = str(len(body))

    ans = requests.post(url, headers=headers, data=body)
    if ans.status_code == 200:
        ans = json.loads(ans.text)
    return ans


def pick_paint(paint_num: str, tick=''):
    '''
    После того, как краска сгенерирована, 
    вы можете выбрать один из цветов и забрать его к себе на "склад".
    Если Вы не укажете tick, то система будет действовать в рамках текущего тика. 
    А тики тикают каждый тик.

    Вся краска которая будет собрана доступна на любом из уровней
    за вычетом расхода на выстрелы.
    '''
    url = 'http://api.datsart.dats.team/art/factory/pick'
    headers = {
            "Authorization": f"Bearer {token}",
            "Content-Length": '',
            "Content-Type": 'multipart/form-data; boundary='
            '----WebKitFormBoundary7MA4YWxkTrZu0gW'
    }
    body = ('------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
            'Content-Disposition: form-data; name="num"\r\n'
            f'\r\n{paint_num}\r\n'
            '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
            'Content-Disposition: form-data; name="tick"\r\n'
            f'\r\n{tick}\r\n'
            '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
    )
    headers['Content-Length'] = str(len(body))

    ans = requests.post(url, headers=headers, data=body)
    if ans.status_code == 200:
        ans = json.loads(ans.text)
    else:
        print('err')
        print(ans)
        print(ans.text)
    return ans
