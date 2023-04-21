import requests
import json


token = '642fed5a96d7e642fed5a96d81'


def get_next_level_info():
    '''
    Прежде чем начать уровень, вам необходимо запросить о нем информацию.
    '''
    url = 'http://api.datsart.dats.team/art/stage/next'
    headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"
        }
    ans = requests.post(url, headers=headers)
    if ans.status_code == 200:
        ans = json.loads(ans.text)
    return ans


def start_next_level(imageId):
    '''
    После того как вы определились с рисунком, необходимо указать id выбранной
    картинки и стартовать уровень. Вернуться и выбрать другую картинку после 
    старта уровня будет нельзя.
    '''
    url = 'http://api.datsart.dats.team/art/stage/next-start'
    headers = {
            "Authorization": f"Bearer {token}",
            "Content-Length": '',
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"
        }
    data = {'imageId': imageId}
    body = (f'------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
        f'Content-Disposition: form-data; name="imageId"\"\r\n'
        f'\r\n{imageId}\r\n'
        f'------WebKitFormBoundary7MA4YWxkTrZu0gW--\r\n')
    headers['Content-Length'] = str(len(body))
    ans = requests.post(url, headers=headers)
    if ans.status_code == 200:
        ans = json.loads(ans.text)
    return ans


def get_current_level_info():
    '''
    Здесь вы можете всегда увидеть информацию и статистику по текущему уровню,
    а также оригинал картинки и вашу картинку-результат:
    '''
    url = 'http://api.datsart.dats.team/art/stage/info'
    headers = {
            "Authorization": f"Bearer {token}",
            'Content-Length': '',
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"
        }
    body = '----WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
    headers['Content-Length'] = str(len(body))
    ans = requests.post(url, headers=headers)
    if ans.status_code == 200:
        ans = json.loads(ans.text)
    return ans


def finish_current_level():
    '''
    Если вы довольны своим результатом и оценкой Вашего шедевра, 
    можете завершить уровень.
    '''
    url = 'http://api.datsart.dats.team/art/stage/finish'
    headers = {
            "Authorization": f"Bearer {token}",
            'Content-Length': '',
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"
        }
    body = '----WebKitFormBoundary7MA4YWxkTrZu0gW\r\n'
    headers['Content-Length'] = str(len(body))
    ans = requests.post(url, headers=headers)
    if ans.status_code == 200:
        ans = json.loads(ans.text)
    return ans



print(get_current_level_info())
