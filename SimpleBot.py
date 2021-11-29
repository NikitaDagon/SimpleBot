
import telebot
from telebot import types
token = "2120405290:AAGAGHqEXJ488IFdSqp13zcz_vHErUeOql8"
bot = telebot.TeleBot(token)

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("как дела?", "считать умеешь?", "легко быть ботом?", "/help")
    bot.send_message(message.chat.id, 'Привет,я имею не очень много функций,но помогу чем смогу', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:\n /Anic-рассказать анекдот \n /MTUCI-показать последние новости вуза \n /Picture-отправить смешную пикчу \n')


@bot.message_handler(commands=['MTUCI'])
def start_message(message):
    bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')

    @bot.message_handler(commands=['Picture'])
    def start_message(message):
        bot.send_message(message.chat.id, "Вот пикча!")
        picture = open('D:\\papizi.jpg')
        bot.send_picture(message.chat.id, picture)
        picture.close()


@bot.message_handler(commands=['Anic'])
def start_message(message):
    bot.send_message(message.chat.id, "Попали как-то в ад бабник, алкоголик и наркоман. Сатана им и говорит:"
                                      "Я могу дать вам ещё один шанс вернуться в мир живых. Вам всего лишь нужно провести сотню лет в"
                                      "комнате с вашими самыми откровенными желаниями, и тогда я вас отпущу.Бабнику достались хоромы, полные роскошных девиц, жаждущих соития с ним, к чему он сразу же и приступил."
                                      "Алкоголику досталась комната, полная самого изысканного бухла, которое только можно было сыскать во всём мире. Не чуя подвоха, он с радостью принял испытание."
                                      "Ну а наркоману конечно же досталась каморка, набитая бесконечным количеством отборнейшего курева всех сортов, способного вштырить не по-детски."
                                      "Через 80 лет Сатана решил проверить, как идут дела у  заключённых. "
                                      "Начал он с комнаты алкоголика. Его взгляду предстал измученный мужик, умоляющий выпустить его. Он в первый же день выпил всё бухло и теперь страдал от бесконечного похмелья в течение восьмидесяти лет."
                                      " Сатана с удовлетворением выпустил его, забрав душу алкоголика себе.Открыв комнату бабника, Сатане предстало мерзкое зрелище: за теперь вечномолодым парнем бегала толпа состарившихся, страшных женщин. Бабник что-то завопил об усвоением уроке и взмолился о прекращении его испытания."
                                      " Сатана забрал и его душу.Открыв комнату торчка, Сатана несказанно удивился, увидев ни один грамм штырева не тронутым и сразу же поймал на себе укоризненный взгляд наркомана:Ты бы хоть зажигалку оставил")

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "как дела?":
        bot.send_message(message.chat.id, 'Все нормально, попробуй другие функции')
    if message.text.lower() == "легко быть ботом?":
        bot.send_message(message.chat.id, 'лучше промолчу')
    if message.text.lower() == "считать умеешь?":
        bot.send_message(message.chat.id, 'нет,но скоро научусь)')
bot.polling()
