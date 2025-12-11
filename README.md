progress_message = bot.sendMessage("𝘴т𝘳𝓲тєиg⚡...")

steps = [
    "??",
    " ????",
    "!!!!!",
    "σи тнє ᥴꪮммєи∂🟢",
    "ρℓєαѕє ωαιт 1 ѕєᥴ",
] 

for step in steps:
    time.sleep(1)  # wait 1 second between updates
    bot.editMessageText(
        step,
        chat_id=message.chat.id,
        message_id=progress_message["message_id"]
    )

# wait 2 seconds after completion, then delete
time.sleep(1)
bot.deleteMessage(chat_id=message.chat.id, message_id=progress_message["message_id"])

# Miracle-file-store-bot
Our file store bot is 24/7 working
