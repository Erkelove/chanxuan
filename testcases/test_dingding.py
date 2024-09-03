import requests
import hmac
import hashlib
import base64
import time



from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler



class TestMyHandler():

    timestamp = str(int(time.time() * 1000))
    secret = 'SEC02c88c59f5e96afc802276ffeed61778f766d430d877d1b01b9d43203cd000b7'

    def send_to_dingding(self, message):
        # 生成签名
        generated_signature = self.generate_signature(self.secret, self.timestamp)
        print(generated_signature)
        # 钉钉机器人 Webhook 地址
        dingding_webhook = f'https://oapi.dingtalk.com/robot/send?access_token=33cd032971239149746f10b815ee2fd37648802e1efbc6372b889e9690d5b98e&timestamp={self.timestamp}&sign={generated_signature}'
        data = {
            "msgtype": "text",
            "text": {
                "content": message
            }
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(dingding_webhook, json=data, headers=headers)
        print(response.text)

    def generate_signature(self, secret, timestamp):
        secret_enc = secret.encode('utf-8')
        # timestamp_enc = timestamp.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        signature = hmac.new(secret_enc, string_to_sign_enc, hashlib.sha256).digest()
        signature_enc = base64.b64encode(signature).decode('utf-8')
        return signature_enc

    # def encrypt_message(self, secret, message):
    #     secret_enc = secret.encode('utf-8')
    #     message_enc = message.encode('utf-8')
    #     signature = hmac.new(secret_enc, message_enc, hashlib.sha256).digest()
    #     signature_enc = base64.b64encode(signature).decode('utf-8')
    #     return signature_enc
    def test_on_modified(self):
        secret = self.secret
        message = 'File has been modified'
        # message = self.encrypt_message(secret, message)
        self.send_to_dingding(message)

if __name__ == "__main__":
    event_handler = TestMyHandler()
    event_handler.test_on_modified()