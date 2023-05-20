import telegram
from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup

def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Привет! Я бот расписания пар группы.")

def get_schedule(update, context):
    chat_id = update.effective_chat.id
    group = context.args[0]  # Get the argument with the group number
    url = f"https://schedule.kpi.kharkov.ua/?group={group}"  # Form the URL with the group number
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the necessary information from the HTML page using BeautifulSoup
    subjects = soup.find_all("div", class_="subject-name")
    schedule = ""
    for subject in subjects:
        schedule += subject.text + "\n"

    context.bot.send_message(chat_id=chat_id, text=schedule)

def get_teacher_schedule(update, context):
    chat_id = update.effective_chat.id
    teacher_name = " ".join(context.args)  # Get the argument with the teacher's name
    url = f"https://schedule.kpi.kharkov.ua/?teacher={teacher_name}"  # Form the URL with the teacher's name
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the necessary information from the HTML page using BeautifulSoup
    subjects = soup.find_all("div", class_="subject-name")
    schedule = ""
    for subject in subjects:
        schedule += subject.text + "\n"

    context.bot.send_message(chat_id=chat_id, text=schedule)

def main():
    token = "YOUR_BOT_TOKEN"  # Replace with your bot's token
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("schedule", get_schedule))
    dp.add_handler(CommandHandler("teacher", get_teacher_schedule))  # Add a command handler for getting the teacher's schedule
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
