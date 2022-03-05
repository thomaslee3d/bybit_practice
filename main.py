from pybit import WebSocket
import pandas as pd
import time
import json
import ccxt



subs = [
    'orderBookL2_25.BTCUSD',
    'instrument_info.100ms.BTCUSD',
    'instrument_info.100ms.ETHUSD'
]

ws = WebSocket(
    "wss://stream-testnet.bybit.com/realtime",
    api_key="mMiNZltEy0ZXB9PBE9", api_secret="RdbCACnsB4wfispOGPAVMjkP75HVJTQQgppV",
    subscriptions=subs
)

while True:
    data = ws.fetch(subs[0])
    if data:
        df = pd.DataFrame(data)
        print(df)


# Authenticate with API.

