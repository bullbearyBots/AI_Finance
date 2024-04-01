import time

import MetaTrader5 as mt5
import os

SERVER_INDEX = 2
LOGIN_INDEX = 3
PASSWORD_INDEX = 4

SERVER = None
LOGIN = None
PASSWORD = None

os.chdir("C:\\Users\\mpran\\Desktop")
key = open("mt5_demo.txt", "r")

# Name, Type, Server, Login, Password
while True:
    line = key.readline()
    if not line:
        break

    prop_value = line.split(":")

    if prop_value[0].strip() == "Server":
        SERVER = prop_value[1].strip()
    elif prop_value[0].strip() == "Login":
        LOGIN = int(prop_value[1].strip())
    elif prop_value[0].strip() == "Password":
        PASSWORD = prop_value[1].strip()

terminal_path = "C:\\Program Files\\MetaTrader 5\\terminal64.exe"

if mt5.initialize(path=terminal_path, login=LOGIN, password=PASSWORD, server=SERVER):
    print(f"Connection to {mt5.account_info().name} established.")


symbols = mt5.symbols_get("USD*")

for symbol in symbols:
    print(f"{symbol.name}: {symbol.bidhigh} {symbol.askhigh}")

symbol = mt5.symbol_info("EURUSD")

while True:
    print(mt5.symbol_info_tick("EURUSD"))
    time.sleep(1)