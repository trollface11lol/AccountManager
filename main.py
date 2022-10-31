import telebot
from anticaptchaofficial.recaptchav2proxyless import *
from telebot import types  # для указание типов
import time
import requests
import re

from test import LolzteamApi
import accountsmanager_v1_pb2
import accountsmanager_v1_pb2_grpc
import grpc
import logging


bot = telebot.TeleBot("5743367920:AAFBpEHIlQ_0O-RuR9e67yhcNoEK1Y28-xw")


def run(message):
    with grpc.insecure_channel('localhost:50011') as channel:
        stub = accountsmanager_v1_pb2_grpc.AccountsManagerStub(channel)
        response = stub.GetAccounts(accountsmanager_v1_pb2.GetAccountsRequest())
    if response.count < 1000:
        bot.send_message(message.chat.id, "Количество аккаунтов < 1000")
        time.sleep(10)
        proxy(message)
    else:
        time.sleep(10)
        proxy(message)


def capcha(message):
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key("00d45aaf78b9bdd9a1616474b226b357")
    if (int(solver.get_balance()) < 2):
        bot.send_message(message.chat.id, "Остаток на балансе Antyicapcha меньше 2-х долларов")
        time.sleep(10)
        lolz(message)
    else:
        time.sleep(10)
        lolz(message)

def proxy(message):
    balanceProxy = requests.get('https://proxy-store.com/api/2fb95edfe2215b3cd5093e190d4cd82d/getbalance') # на сайте прокси установить свой ip, и если изменят ключ, то поменять его тут тоже
    example = balanceProxy.text.split(',')
    money = example[1].split('"')
    if ((float(money[3])) < 1000):
        bot.send_message(message.chat.id, "Остаток на балансе Proxy-store меньше 1000 рублей")
        time.sleep(10)
        capcha(message)
    else:
        time.sleep(10)
        capcha(message)


def lolz(message):
    api = LolzteamApi('5d24abb68490642eec8fd1cff175342db0012d1d', 6083779) # поменять токен и id на рабочий
    datas = api.market_payments(type_='income')
    balanceLolz = datas['payments']['71576103']['incoming_sum'] - datas['payments']['71576103']['outgoing_sum']
    if balanceLolz < 1000:
        bot.send_message(message.chat.id, "Остаток на балансе Lolzteam меньше 1000 рублей")
        time.sleep(3600)
        run(message)
    else:
        time.sleep(3600)
        run(message)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Баланс anticapcha💵")
    btn2 = types.KeyboardButton("Баланс Proxy-store💰")
    btn3 = types.KeyboardButton("Баланс Lolzteam💲")
    btn4 = types.KeyboardButton("Количество аккаунтов🔢")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)
    if __name__ == "__main__":
        logging.basicConfig()
        run(message)




@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Баланс anticapcha💵"):
        solver = recaptchaV2Proxyless()
        solver.set_verbose(1)
        solver.set_key("00d45aaf78b9bdd9a1616474b226b357")
        bot.send_message(message.chat.id, "Остаток на балансе " + str(solver.get_balance()) + " долларов")


    if (message.text == "Баланс Proxy-store💰"):
        balance = requests.get('https://proxy-store.com/api/2fb95edfe2215b3cd5093e190d4cd82d/getbalance')
        example = balance.text.split(',')
        money = example[1].split('"')
        bot.send_message(message.chat.id, "Остаток на балансе " + str(money[3]) + " рублей")


    if (message.text == "Баланс Lolzteam💲"):
        api = LolzteamApi('5d24abb68490642eec8fd1cff175342db0012d1d', 6083779)
        datas = api.market_payments(type_='income')
        balanceLolz = datas['payments']['71576103']['incoming_sum'] - datas['payments']['71576103']['outgoing_sum']
        bot.send_message(message.chat.id, "Остаток на балансе " + str(balanceLolz) + " рублей")

    if (message.text == "Количество аккаунтов🔢"):
        with grpc.insecure_channel('localhost:50011') as channel:
            stub = accountsmanager_v1_pb2_grpc.AccountsManagerStub(channel)
            response = stub.GetAccounts(accountsmanager_v1_pb2.GetAccountsRequest())
            bot.send_message(message.chat.id, "Количество аккаунтов " + str(response.count))


bot.polling(none_stop=True)

