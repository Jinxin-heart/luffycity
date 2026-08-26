import base64, json, time, hashlib
from datetime import datetime

if __name__ == '__main__':


    # header
    header_data = {'typ': 'jwt', 'alg': 'HS256'}
    header = base64.b64encode(json.dumps(header_data).encode()).decode()
    # print(header)
    # eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9

    # payload
    iat = int(datetime.now().timestamp())
    payload_data = {
        'sub': 'root',
        'exp': iat + 60 * 60,
        "iat": iat,
        "name": "jinx",
        "user_id": 1,
        "admin": True,
        "acc_pwd": "QiLCJhbGciOiJIUzI1NiJ9QiLCJhbGciOiJIUzI1NiJ9QiLCJhbGciOiJIUzI1NiJ9",
    }
    payload = base64.b64encode(json.dumps(payload_data).encode()).decode()
    # print(payload)
    # eyJzdWIiOiAicm9vdCIsICJleHAiOiAxNzg3NzMzOTQ4LCAiaWF0IjogMTc4NzczMDM0OCwgIm5hbWUiOiAiamlueCIsICJhdmF0YXIiOiAiMS5wbmciLCAidXNlcl9pZCI6IDEsICJhZG1pbiI6IHRydWUsICJhY2NfcHdkIjogIlFpTENKaGJHY2lPaUpJVXpJMU5pSjlRaUxDSmhiR2NpT2lKSVV6STFOaUo5UWlMQ0poYkdjaU9pSklVekkxTmlKOSJ9

    secret = 'jinx'
    data = header + payload + secret  # 秘钥绝对不能提供给客户端。
    HS256 = hashlib.sha256()
    HS256.update(data.encode('utf-8'))
    signature = HS256.hexdigest()
    # print(signature)
    # 5cdbd0a624bbfba80123cf37d0a95c3a85d28e8dc6ab0f4c67b97df700b39b3e

    # jwt 最终的生成
    token = f"{header}.{payload}.{signature}"
    # print(token)
    # eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9.eyJzdWIiOiAicm9vdCIsICJleHAiOiAxNzg3NzM0MTc0LCAiaWF0IjogMTc4NzczMDU3NCwgIm5hbWUiOiAiamlueCIsICJhdmF0YXIiOiAiMS5wbmciLCAidXNlcl9pZCI6IDEsICJhZG1pbiI6IHRydWUsICJhY2NfcHdkIjogIlFpTENKaGJHY2lPaUpJVXpJMU5pSjlRaUxDSmhiR2NpT2lKSVV6STFOaUo5UWlMQ0poYkdjaU9pSklVekkxTmlKOSJ9.aa5fdeed89f73608feb3ba90e61be9a73eb26390fcdd04155115e965be724ba8


    token = 'eyJ0eXAiOiAiand0IiwgImFsZyI6ICJIUzI1NiJ9.eyJzdWIiOiAicm9vdCIsICJleHAiOiAxNzg3NzM0MTc0LCAiaWF0IjogMTc4NzczMDU3NCwgIm5hbWUiOiAiamlueCIsICJhdmF0YXIiOiAiMS5wbmciLCAidXNlcl9pZCI6IDEsICJhZG1pbiI6IHRydWUsICJhY2NfcHdkIjogIlFpTENKaGJHY2lPaUpJVXpJMU5pSjlRaUxDSmhiR2NpT2lKSVV6STFOaUo5UWlMQ0poYkdjaU9pSklVekkxTmlKOSJ9.aa5fdeed89f73608feb3ba90e61be9a73eb26390fcdd04155115e965be724ba8'
    header, payload, signature = token.split(".")

    # 验证是否过期了
    # 先基于base64，接着使用json解码
    payload_data = json.loads( base64.b64decode(payload.encode()) )
    print(payload_data)
    exp = payload_data.get("exp", None)
    if exp is not None and int(exp) < int(datetime.now().timestamp()):
        print("token过期！！！")
    else:
        print("没有过期")

    # 验证token是否有效，是否被篡改
    # from django.conf import settings
    # secret = settings.SECRET_KEY
    secret = 'jinx'
    data = header + payload + secret  # 秘钥绝对不能提供给客户端。
    HS256 = hashlib.sha256()
    HS256.update(data.encode('utf-8'))
    new_signature = HS256.hexdigest()

    if new_signature != signature:
        print("认证失败")
    else:
        print("认证通过")


