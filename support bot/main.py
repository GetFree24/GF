


# import re
# from telegram.ext import Updater, CallbackContext, MessageHandler, CallbackQueryHandler, Filters, CommandHandler
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# import os
#
# def start_handler(update: Update, context:CallbackContext):
#     context.bot.send_message(update.message.chat_id, 'Здраствуйте!\n'
#                              'Мы сервис помошников, ...')
#     context.bot.send_message()

import json
import os
import sqlite3
import telebot
from telebot import types

bot =telebot.TeleBot(token='5234888949:AAFLY_2uCZ1Z9B8MPvHWkdsUrt6rubuFhnA')

global conn
conn = sqlite3.connect('user_data.db', check_same_thread=False)


def db_table(conn, user_id:int, user_name:str, tasks):
    cursor = conn.cursor
    cursor.execute('INSERT INTO tasks (user_id, user_name, tasks) VALUES (?,?,?,?)', (user_id, user_name, tasks))
    conn.commit()

@bot.message_handler(commands=['start'])
def startpg(message):

    startmenu = types.ReplyKeyboardMarkup(True, True)
    startmenu.row('Начать')
    bot.send_message(message.chat.id, 'Здраствуйте!\nМы сервис помощников, ...', reply_markup=startmenu)

@bot.message_handler(content_types=['text'])
def general(message):
     if message.text == 'Начать':
         # send = bot.send_message(message.chat.id)
         # bot.register_next_step_handler(send, menu)
         menu(message)
     elif message.text == 'Поставить задачу':
         bot.send_message(message.chat.id, 'Опишите свою задачу, укажите ответственного(-ых), укажите сроки выполнения задачи, укажите какой доступ к ресурсам предоставить - бюджет(?)')
     elif message.text == 'Список задач':
         num = 1
         for task in get_tasks(message.chat.id):
             bot.send_message(message.chat.id, f'{num}. {task}')
             num += 1
     else:
         write_json(message.text, message.from_user.id)

def menu(message):
    bot.send_message(message.chat.id, 'Выберите один из пунктов')


    change = types.ReplyKeyboardMarkup(True, False)
    change.row_width = 4
    change.row('Поставить задачу')
    change.row('Список задач')
    change.row('Профиль')
    change.row('Настройки')
    # change.add(types.KeyboardButton('Поставить задачу', callback_data='cb_take_task'),
    #            types.InlineKeyboardButton('Список задач', callback_data='cb_task_list'),
    #            types.InlineKeyboardButton('Профиль', callback_data='cb_profile'),
    #            types.InlineKeyboardButton('Настройки', callback_data='cb_settings'))
    # bot.send_message(message.chat.id, 'Меню:', reply_markup=change)
    # return change

# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     if call.data == 'cb_take_task':
#         bot.ca(call.id, 'Опишите свою задачу, укажите ответственного(-ых), укажите сроки выполнения задачи, укажите какой доступ к ресурсам предоставить - бюджет(?)')
#     elif call.data == 'cb_task_list':
#         bot.send_message(chat_id, get_tasks())
#         # list_menu = types.ReplyKeyboardMarkup(True, False)
#         # list_menu.row('Изменить')
#         # list_menu.row('Удалить')

def add_task_list(message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    tasks = []
    tasks.append(message.text)
    db_table(conn, user_id, user_name, 'C:\\Users\\AdminPycharmProjects\\supportBot\\tasks.json')

def write_json(new_tasks, user_id, filename='tasks.json'):
    filesize = os.path.getsize('tasks.json')
    with open(filename) as file:
        id_existing = json.load(file)
        if filesize == 0:
            with open(filename) as file:
                file_data = json.load(file)
            file_data[str(user_id)] = []
            file_data[str(user_id)].append(new_tasks)
            with open(filename, 'w') as file:
                json.dump(file_data, file)
        elif str(user_id) in id_existing:
            with open(filename, 'r+') as file:
                file_data = json.load(file)
                file_data[str(user_id)].append(new_tasks)
                file.seek(0)
                json.dump(file_data, file, indent=4)
        else:
            with open(filename) as file:
                file_data = json.load(file)
            file_data[str(user_id)] = []
            file_data[str(user_id)].append(new_tasks)
            with open(filename, 'w') as file:
                json.dump(file_data, file)

def get_tasks(user_id, filename='tasks.json'):
    with open(filename) as file:
        tasks_json = json.load(file)
        tasks = tasks_json[str(user_id)]
    return tasks

if __name__ == '__main__':
    bot.remove_webhook()
    bot.polling(none_stop=True)