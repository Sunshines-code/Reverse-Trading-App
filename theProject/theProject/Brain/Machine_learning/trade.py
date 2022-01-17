from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import json
import pprint as pprint
import pandas as pd
from joblib import dump, load
import requests
import math
from time import sleep
model = load('V2Model.joblib')
X_scaler = load('V2X_scaler.joblib')
y_scaler = load('V2y_scaler.joblib')
import alpaca_trade_api as tradeapi
from twilio.rest import Client
account_sid = 'AC4ab3ece33d5bb0b0a6d617086b40ae98'
auth_token = '285a6c2756f288274702c9e3de20003c'
client = Client(account_sid, auth_token)
import os


def check():
    api_key = 'AKHME2093RBNAQYHPUAV'
    base_url = 'https://api.alpaca.markets'
    secret_key = 'bEWXQSpd8FHvzZgH5LFZGv0s1iPYJjOYHF5nX3LI'
    api = tradeapi.REST(api_key, secret_key)
    positions = api.list_positions()
    account = api.get_account()
    global pp
    pp = math.floor((round(float(account.cash),1)/3)*.97)
    c = 0
    if len(positions) > 0:
        for i in positions:
            api.submit_order(
            symbol=positions[c].symbol,
            qty=positions[c].qty,
            side='sell',
            type='market',
            time_in_force='gtc',
            )
            message = client.messages \
                        .create(
                         body=f"{i} sold",
                             from_='+19703153376',
                             to='+13033044215'
                         )
        c+=1
    else:
        print("0 sold")
        pass

def learn():
    price_info= []
    count = 0

    lf = pd.read_csv('./V2List.csv')
    tckr = lf['Ticker'].tolist()
    for i in tckr:
        api_key = 'PKU2SKNAWU76OBUNS88G'
        APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'
        secret_key = 'RUjuIk7HvPQ9Kt6FVzBaF6RiAM3KdrtLxVg5w0VH'
        api = tradeapi.REST(api_key, secret_key)
        try:
            barset = api.get_barset(i, 'day', limit=2)         
            openingY = barset[i][0].o
            closingY = barset[i][0].c
            highY = barset[i][0].h
            lowY = barset[i][0].l
            openingT = barset[i][1].o
            closingT = barset[i][1].c
            highT = barset[i][1].h
            lowT = barset[i][1].l
            info = {'Ticker':f'{i}',
                    'openingY':openingY,
                    'closingY':closingY,
                    'highY':highY,
                    'lowY':lowY,
                    'openingT':openingT,
                    'closingT':closingT,
                    'highT':highT,
                    'lowT':lowT}
            pprint(i)
            count+=1
            price_info.append(info)
    #         pprint(price_info)
            
            

        except:
            
            count+=1

            print(f'result error{i}')
            pass
    
    global df
    df = pd.DataFrame(price_info)

def trade():
    X = df[['openingY', 'closingY', 'highY', 'lowY']]
    y = df["highT"].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)
    dump(X_scaler, 'V2X_scaler.joblib') 
    dump(y_scaler, 'V2y_scaler.joblib') 
    model = LinearRegression()
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    y_train_scaled = y_scaler.transform(y_train)
    y_test_scaled = y_scaler.transform(y_test)
    model.fit(X_train_scaled, y_train_scaled)
    predictions = model.predict(X_test_scaled)
    r2 = model.score(X_test_scaled, y_test_scaled)
    dump(model, 'V2Model.joblib') 
    ldf = df[['openingT', 'closingT', 'highT', 'lowT']]
    sc_new_in = X_scaler.transform(ldf)
    new_out = model.predict(sc_new_in)
    new_out = y_scaler.inverse_transform(new_out)
    df["next_high"]= new_out
    df["change"]= df['next_high']/df["closingT"]*100-100
    rdf = df.sort_values(by=['change'], axis=0, ignore_index=True, inplace=False, ascending = False)
    purchase_list = rdf.head(3)
    purchase_list
    api_key = 'AKHME2093RBNAQYHPUAV'
    base_url = 'https://api.alpaca.markets'
    secret_key = 'bEWXQSpd8FHvzZgH5LFZGv0s1iPYJjOYHF5nX3LI'
    api = tradeapi.REST(api_key, secret_key)
    c = 0
    message_list = []
    for i in purchase_list.Ticker:
        message_list.append(purchase_list.Ticker[c])
        message_list.append(math.floor(pp/purchase_list.highT[c]))
        message_list.append(purchase_list.change[c])
        api.submit_order(
            symbol=i,
            qty=math.floor(pp/buy_list.high[c]),
            side='buy',
            type='market',
            time_in_force='day'
        )
        c+=1
    message = client.messages \
                .create(
                    body=f"Model accuracy rating of {r2}. "
        f"{message_list[1]} Shares of {message_list[0]} projected with {message_list[2]}change. "
        f"{message_list[4]} Shares of {message_list[3]} projected with {message_list[5]}change. "
        f"{message_list[7]} Shares of {message_list[6]} projected with {message_list[8]}change. ",
                    from_='+19703153376',
                    to='+13033044215'
                )

def setSell():
    api_key = 'AKHME2093RBNAQYHPUAV'
    base_url = 'https://api.alpaca.markets'
    secret_key = 'bEWXQSpd8FHvzZgH5LFZGv0s1iPYJjOYHF5nX3LI'
    api = tradeapi.REST(api_key, secret_key)
    positions = api.list_positions()
    c = 0
    for i in positions:
        api.submit_order(
        symbol=positions[c].symbol,
        qty=positions[c].qty,
        side='sell',
        type='trailing_stop',
        trail_percent=0.3,
        time_in_force='gtc',
        )
        message = client.messages \
                    .create(
                         body=f"{i} set to sell",
                         from_='+19703153376',
                         to='+13033044215'
                     )
        c+=1

def RunAll():
    price_info= []
    df =[]
    count = 0
    check()
    learn()
    sleep(2)
    trade()
    sleep(15)
    setSell()
RunAll()