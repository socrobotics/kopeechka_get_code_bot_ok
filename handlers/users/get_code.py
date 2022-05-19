import re
import time

import requests


# Получаю новый id для почты


def get_code_kopeechka(email, token):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/100.0.4896.127 Safari/537.36 "
    }

    new_id = ""
    error = ""

    try:
        url = f'http://api.kopeechka.store/mailbox-reorder?site=facebook.com&email={email}&token={token}'
        while True:
            req_ = requests.get(url=url, headers=headers).text
            new_id = re.search(r'(?<=id":").*?(?=")', req_)[0]
            # if new_id.lower() == "error":
            #     raise StopIteration
            if new_id == "":
                new_id = re.findall(r'\d+.*?(?=")', req_)
            if new_id != "":
                break

        print(f'Получил ID - {new_id}')

        # Получаю код с почты

        url = f'https://api.kopeechka.store/mailbox-get-message?full=1&id={new_id}&token={token}'
        n = 0
        while True:
            if n > 30:
                return "Не приходит код на почту"
            r = requests.get(url=url, headers=headers).text
            status = re.search(r'(?<=status":").*?(?=")', r)[0].strip().lower()
            if status == "error" or status == "wait_link":
                n += 1
                print(f'{r} - #{n}')
                time.sleep(2)
                continue

            print(status)

            code = re.search(r'(?<=confirmcontact\.php\?c=).*?(?=&)', r)[0].strip()

            if code != "":
                print(f'Успешно получили код - {code}')
                return code
            else:
                time.sleep(5)
                n += 1
                continue

        # email.clear()
        return code

    except:
        # Отдаю пользователю уведомление
        print("Нe удалось получить КОД с почты")
        return "Нe удалось получить КОД с почты"
