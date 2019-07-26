import re
import telebot
from emoji import emojize
import sql_functions as sqlf

token_bot = ''
bot = telebot.TeleBot(token_bot)

print('tickets bot was started..')

def categories_markup():
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(telebot.types.InlineKeyboardButton(text='Concerts', callback_data='Concerts'),
               telebot.types.InlineKeyboardButton(text='Theater', callback_data='Theater'),
               telebot.types.InlineKeyboardButton(text='Festivals', callback_data='Festivals'))
    return markup

def events_list_markup(table):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    for i in sqlf.get_events(table):
        markup.add(telebot.types.InlineKeyboardButton(text=i[1], 
                   callback_data='evnt-inf-call={}={}'.format(table, i[0])))
    return markup

def event_seats_markup(table, id_event):
    markup = telebot.types.InlineKeyboardMarkup(row_width=4)
    seats = sqlf.get_seats(table, id_event)
    #create seats for event
    for i in range(4):
        row = []
        for j in range(4):
            if seats[i*4 + j]:
                seat_marker = '{} {}'.format(str(i*4 + j + 1), emojize(":x:", use_aliases=True))
            else:
                seat_marker = '{} {}'.format(str(i*4 + j + 1), emojize(':white_check_mark:', use_aliases=True))
            row.append(telebot.types.InlineKeyboardButton(text=seat_marker,
                       callback_data='seat-call={}={}={}'.format(table, id_event, str(i*4 + j + 1))))
        markup.add(*row)
    return markup

def ticket_buying_markup(table, id_event, seat):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(telebot.types.InlineKeyboardButton(text='Issue ticket', 
               callback_data='seat-issue={}={}={}'.format(table, id_event, seat)))
    return markup

def pay_markup():
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(telebot.types.InlineKeyboardButton(text='Pay', 
               callback_data='press-to-pay'))
    return markup

def tickets_markup(events, user_id):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    for i in events:
        markup.add(telebot.types.InlineKeyboardButton(text=sqlf.get_event_name(*i.split("-")), 
                   callback_data='{}-{}'.format(str(user_id), i)))
    return markup

def ticket_holders_markup(tickets):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    for i in tickets:
        markup.add(telebot.types.InlineKeyboardButton(text=' '.join(i[:2]), 
                   callback_data='tickets-hold-{}'.format('-'.join(i[2:]))))
    return markup  

def ticket_return_markup(ticket):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(telebot.types.InlineKeyboardButton(text='Return ticket', 
                   callback_data='ticket-return-{}'.format('-'.join(ticket))))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! I`m tickets bot.\n'
                     'You can buy tickets on your favorite performance with my help.\n'
                     'Choose the event category:', reply_markup=categories_markup())

@bot.message_handler(commands=['events'])
def events(message):
    bot.send_message(message.chat.id, 'Choose the event category:', reply_markup=categories_markup())

@bot.message_handler(commands=['mytickets'])
def mytickets(message):
    tickets = sqlf.get_user_tickets(message.chat.id)
    if tickets:
        #get unique events for which bought tickets
        events = list(dict.fromkeys(['-'.join(i.split(' ')[2:4]) for i in tickets.split(',')]))
        bot.send_message(message.chat.id, 'You have tickets on these events:', 
                         reply_markup=tickets_markup(events, message.chat.id))
    else:
        bot.send_message(message.chat.id, 'You haven\'t any tickets.\nYou can buy it with use command /events.')

@bot.callback_query_handler(func=lambda call:True)
def inlin(call):
    #print categories
    if 'evnt-inf-call=' in call.data:
        flags = call.data.split('=')[1:]
        bot.send_message(call.message.chat.id, text='***{}***\n' \
                                                    '***Place:*** {}\n' \
                                                    '***Time:*** {}\n'  \
                                                    '***Price:*** {} грн'.format(*sqlf.get_event_info(*flags)),
                         reply_markup=event_seats_markup(*flags), parse_mode='markdown')
    
    #handle press on seat buttons
    elif 'seat-call=' in call.data:
        flags = call.data.split('=')[1:]
        seat_information = sqlf.seat_info(*flags).split(' ')
        #if return info - seat isn't free
        if len(seat_information) == 3:
            bot.send_message(call.message.chat.id, text='You can\'t buy this place '
                            'because {} {} bought before you.'.format(*seat_information[1:3]),
                             parse_mode='markdown')
        else:
            bot.send_message(call.message.chat.id, text='Place №{} is free. You can buy a ticket.'.format(str(flags[-1])),
                             reply_markup=ticket_buying_markup(*flags), parse_mode='markdown')

    #issue button, user status -> inp-name
    elif 'seat-issue=' in call.data:
        flags = call.data.split('=')[1:]
        sqlf.add_user_id(call.message.chat.id, 'inp-name '+' '.join(flags))
        bot.send_message(call.message.chat.id, text='Input your name',
                         parse_mode='markdown')

    #print bought tickets on chosen event and delete event duplicates in print
    elif str(call.message.chat.id) in call.data:
        tickets = sqlf.get_user_tickets(call.message.chat.id).split(',')
        sort_tickets = [i.split(' ') for i in tickets if ' '.join(call.data.split('-')[1:]) in i]
        bot.send_message(call.message.chat.id, text='Select ticket, to show more information.',
                         reply_markup=ticket_holders_markup(sort_tickets), parse_mode='markdown')

    #print ticket information
    elif 'tickets-hold-' in call.data:
        ticket_info = call.data.split('-')
        seat_owner = sqlf.seat_info(*ticket_info[2:]).split(' ')[1:]
        event_info = sqlf.get_event_info(*ticket_info[2:-1])
        ticket = '***Ticket***\n' \
                 '***Title:*** {}\n' \
                 '***Place:*** {}\n' \
                 '***Time:*** {}\n'  \
                 '***Person:*** {} {}\n' \
                 '***Seat №:*** {}'.format(*event_info[:3], *seat_owner, ticket_info[-1])
        bot.send_message(call.message.chat.id, ticket, 
                         reply_markup=ticket_return_markup(ticket_info[2:]), parse_mode='markdown')

    #check return button and delete ticket from user and set seat free
    elif 'ticket-return-' in call.data:
        data = call.data.split('-')
        sqlf.clear_seat(*data[2:])
        result = sqlf.remove_ticket_from_user(' '.join(data[2:]), call.message.chat.id)
        if result:
            bot.send_message(call.message.chat.id, "Ticket was successfully returned.")
        else:
            bot.send_message(call.message.chat.id, "You have already returned this ticket.")

    #print list events from Concerts table
    elif call.data == 'Concerts':
        bot.send_message(call.message.chat.id, '***Concerts***\nNearest events:',
                         reply_markup=events_list_markup('Concerts'), parse_mode='markdown')

    #print list events from Theater table
    elif call.data == 'Theater':
        bot.send_message(call.message.chat.id, '***Theater***\nNearest events:',
                         reply_markup=events_list_markup('Theater'), parse_mode='markdown')

    #print list events from Festivals table
    elif call.data == 'Festivals':
        bot.send_message(call.message.chat.id, '***Festivals***\nNearest events:',
                         reply_markup=events_list_markup('Festivals'), parse_mode='markdown')

    #button to buy chosen ticket
    elif call.data == 'press-to-pay':
        info = sqlf.get_user_info(call.message.chat.id)
        if info[4]:
            check = sqlf.seat_info(*info[4].split(' ')).split(' ')
            #check if seat is free
            if len(check) == 3:
                sqlf.change_user_status(call.message.chat.id, '')
                bot.send_message(call.message.chat.id, text='{} {} has just bought this '
                                 'ticket.'.format(*check[1:3]))
            else:
                #set personal data to the seat, clear bot status, add ticket to user
                sqlf.confirm_ticket(*info[4].split(' '), call.message.chat.id, info[1], info[2])
                sqlf.change_user_status(call.message.chat.id, '')
                sqlf.add_ticket_to_user(call.message.chat.id, info[4].split(' '))
                bot.send_message(call.message.chat.id, text='Ticket was successfully bought.\n' \
                                'Your seat - ***№{}***.'.format(info[4].split(' ')[-1]),
                                 parse_mode='markdown')
        else:
            #if status doesn't exist
            bot.send_message(call.message.chat.id, 'Nothing to buy.')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def input(message):
    #check if user exist in database
    if sqlf.get_user_info(message.chat.id):
        status = sqlf.get_user_info(message.chat.id)[4].split(' ')
        if status[0] == 'inp-name':
            #clear symbols and nums from user input and set status inp-sname, add name if good input
            name = re.sub('[^a-zA-Zа-яА-Я]+', '', message.text)
            if name:
                if len(name) < 20:
                    sqlf.add_user_name(str(message.chat.id), name)
                    sqlf.change_user_status(str(message.chat.id), 'inp-sname ' + ' '.join(status[1:]))
                    bot.send_message(message.chat.id, 'Your name was successfully saved.\nInput your surname')
                else:
                    bot.send_message(message.chat.id, 'Too long, limit 20 letters.\nPlease try again.')
            else:
                bot.send_message(message.chat.id, 'You must input letters.\nPlease try again.')

        elif status[0] == 'inp-sname':
            #clear symbols and nums from user input and clear status, add surname if good input
            surname = re.sub('[^a-zA-Zа-яА-Я]+', '', message.text)
            if surname:
                if len(surname) < 20:
                    sqlf.add_user_surname(str(message.chat.id), surname)
                    sqlf.change_user_status(str(message.chat.id), ' '.join(status[1:]))
                    bot.send_message(message.chat.id, 'Your surname was successfully saved.\nPress button to paid.',
                                    reply_markup=pay_markup())
                else:
                    bot.send_message(message.chat.id, 'Too long, limit 20 letters.\nPlease try again.')
            else:
                bot.send_message(message.chat.id, 'You must input letters.\nPlease try again.')

        else:
            bot.send_message(message.chat.id, 'At first select event.\nThis command can help you \\events.')

bot.polling(none_stop=True)