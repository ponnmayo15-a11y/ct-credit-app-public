"""Google API群共通のOAuth2アクセストークン取得(リフレッシュトークン方式)

GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET / GOOGLE_REFRESH_TOKEN の3つの環境変数を使う。
リフレッシュトークンに付与されたスコープの範囲内であれば、Calendar APIなど
どのGoogle APIへのアクセスにも同じ関数でアクセストークンを取得できる。
"""
import os

import requests

TOKEN_URL = "https://oauth2.googleapis.com/token"


def get_access_token() -> str:
    resp = requests.post(
        TOKEN_URL,
        data={
            "client_id": os.environ["GOOGLE_CLIENT_ID"],
            "client_secret": os.environ["GOOGLE_CLIENT_SECRET"],
            "refresh_token": os.environ["GOOGLE_REFRESH_TOKEN"],
            "grant_type": "refresh_token",
        },
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]
