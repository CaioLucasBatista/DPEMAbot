# coding: cp1252
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from conf.settings import TELEGRAM_TOKEN


def start(bot, update):
    response_message = "Olá! Sou um assistente virtual responsável por resolver problemas simples, caso tenha algum problema clique em /AJUDA."
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def ajuda(bot, update):
    response_message = "Qual o seu problema? Clique em uma das opções: Computador(/COMPUTADOR), Impressora(/IMPRESSORA), SGA(/SGA), PJE(/PJE), Ramais da SUINFO(/SUINFO), Meu problema não está listado(/SAIR)."
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def sga(bot, update):
    response_message = "Solução ainda não cadastrada! Clique em /AJUDA"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def pje(bot, update):
    response_message = "Solução ainda não cadastrada! Clique em /AJUDA"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def sair(bot, update):
    response_message = "Clique em /AJUDA para voltar ao menu ajuda."
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def impressora(bot, update):
    response_message = "Essa função ainda não foi implementada. Clique em /AJUDA"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def computador(bot, update):
    response_message = "Qual o problema no computador? Clique no comando correspondente ao seu problema: Computador lento(/LENTO), Computador não liga(/NAOLIGA), Computador reniciando(/REINICIANDO), Computador sem proxy(/proxy), Meu problema não está na lista(/SAIR)."
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def naoliga(bot, update):
    response_message = "É um simples problema de B.I.O.S."
    bot.send_message(
        
        chat_id=update.message.chat_id,
        text=response_message
    )


def lento(bot, update):
    response_message = "Muito simple! Pegue um balde com água e jogue sobre o computador. O seu problema estará resolvido."
    bot.send_message(
        
        chat_id=update.message.chat_id,
        text=response_message
    )

def reiniciando(bot, update):
    response_message = "Solução ainda não cadastrada! Clique em /AJUDA"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def suinfo(bot, update):
    response_message = "Estes são os ramais da SUINFO: 255, 265, 266"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def unknown(bot, update):
    response_message = "Não consegui entender, comando não cadastrado. Poderia repetir com um comando válido ou clicar em /AJUDA?"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('ajuda', ajuda)
    )
    dispatcher.add_handler(
        CommandHandler('impressora', impressora)
    )
    dispatcher.add_handler(
        CommandHandler('computador', computador)
    )
    dispatcher.add_handler(
        CommandHandler('lento', lento)
    )
    dispatcher.add_handler(
        CommandHandler('naoliga', naoliga)
    )
    dispatcher.add_handler(
        CommandHandler('sair', sair)
    )
    dispatcher.add_handler(
        CommandHandler('sga', sga)
    )
    dispatcher.add_handler(
        CommandHandler('pje', pje)
    )
    dispatcher.add_handler(
        CommandHandler('reiniciando', reiniciando)
    )
    dispatcher.add_handler(
        CommandHandler('suinfo', suinfo)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()