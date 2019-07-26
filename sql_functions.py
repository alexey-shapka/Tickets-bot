import pymysql

def create_connection_cursor():
    cnx = pymysql.connect(user='', password='', host='',
                        database='')
    cursor = cnx.cursor()
    return cnx, cursor

def close_connection_cursor(cnx, cursor):
    cnx.close()
    cursor.close()

def add_event(table, Name, Place, Date, Price):
    cnx, cursor = create_connection_cursor()
    cursor.execute("INSERT INTO {} (Name, Place, Date, Price) VALUES \
                  ('{}', '{}', '{}', '{}')".format(table, Name, Place, Date, Price))
    cnx.commit()
    close_connection_cursor(cnx, cursor)

def get_events(table):
    cnx, cursor = create_connection_cursor()
    cursor.execute("SELECT * FROM {}".format(table))
    response = cursor.fetchall()
    close_connection_cursor(cnx, cursor)
    return response

def get_event_info(table, id_event):
    cnx, cursor = create_connection_cursor()
    cursor.execute("SELECT Name, Place, Date, Price FROM {} WHERE ID = '{}'".format(table, id_event))
    response = cursor.fetchone()
    close_connection_cursor(cnx, cursor)
    return response

def get_event_name(table, id_event):
    cnx, cursor = create_connection_cursor()
    cursor.execute("SELECT Name FROM {} WHERE ID = '{}'".format(table, id_event))
    response = cursor.fetchone()[0]
    close_connection_cursor(cnx, cursor)
    return response

def get_seats(table, id_event):
    cnx, cursor = create_connection_cursor()
    seats = ', '.join(['Seat_{}'.format(str(i)) for i in range(1, 17)])
    cursor.execute("SELECT {} FROM {} WHERE ID = {}".format(seats, table, id_event))
    response = cursor.fetchone()
    close_connection_cursor(cnx, cursor)
    return response

def seat_info(table, id_event, seat):
    cnx, cursor = create_connection_cursor()
    cursor.execute("SELECT Seat_{} FROM {} WHERE ID = {}".format(seat, table, id_event))
    response = cursor.fetchone()[0]
    close_connection_cursor(cnx, cursor)
    return response

def clear_seat(table, event_id, seat):
    cnx, cursor = create_connection_cursor()
    cursor.execute("UPDATE {} SET Seat_{} = '' WHERE ID = {}".format(table, seat, event_id))
    cnx.commit()
    close_connection_cursor(cnx, cursor)

def remove_ticket_from_user(ticket, user_id):
    cnx, cursor = create_connection_cursor()
    cursor.execute("SELECT Tickets FROM Users WHERE ID = {}".format(user_id))
    old_tickets = cursor.fetchone()[0].split(',')
    #remove ticket from ticket list
    update_tickets = [i for i in old_tickets if ticket not in i]
    if len(old_tickets) != len(update_tickets):
        cursor.execute("UPDATE Users SET Tickets = '{}' WHERE ID = {}".format(','.join(update_tickets), user_id))
        cnx.commit()
        close_connection_cursor(cnx, cursor)
        return 'ok'
    else:
        close_connection_cursor(cnx, cursor)
        return ''

def add_user_id(id_user, status_input):
    cnx, cursor = create_connection_cursor()
    cursor.execute("INSERT IGNORE INTO Users (ID) VALUES ('{}')".format(id_user))
    cursor.execute("UPDATE Users SET Status_bot = '{}' WHERE ID = {}".format(status_input, id_user))
    cnx.commit()
    close_connection_cursor(cnx, cursor)

def get_user_info(id_user):
    cnx, cursor = create_connection_cursor()
    cursor.execute("SELECT * FROM Users WHERE ID = {}".format(id_user))
    response = cursor.fetchone()
    close_connection_cursor(cnx, cursor)
    return response

def add_user_name(id_user, name):
    cnx, cursor = create_connection_cursor()
    cursor.execute("UPDATE Users SET Name = '{}' WHERE ID = {}".format(name, id_user))
    cnx.commit()
    close_connection_cursor(cnx, cursor)

def add_user_surname(id_user, surname):
    cnx, cursor = create_connection_cursor()
    cursor.execute("UPDATE Users SET Surname = '{}' WHERE ID = {}".format(surname, id_user))
    cnx.commit()
    close_connection_cursor(cnx, cursor)

def change_user_status(id_user, status):
    cnx, cursor = create_connection_cursor()
    cursor.execute("UPDATE Users SET Status_bot = '{}' WHERE ID = {}".format(status, id_user))
    cnx.commit()
    close_connection_cursor(cnx, cursor)

def confirm_ticket(table, id_event, seat, user_id, name, surname):
    cnx, cursor = create_connection_cursor()
    cursor.execute("UPDATE {} SET Seat_{} = '{} {} {}' WHERE ID = {} AND Seat_{} = ''".format(table,
                   seat, user_id, name, surname, id_event, seat))
    cnx.commit()
    close_connection_cursor(cnx, cursor)

def add_ticket_to_user(user_id, ticket):
    cnx, cursor = create_connection_cursor()
    cursor.execute("SELECT Name, Surname, Tickets FROM Users WHERE ID = {}".format(user_id))
    user_info = list(cursor.fetchone())
    if user_info[2]:
        current_tickets = user_info[2].split(', ')
        new_ticket = ' '.join(user_info[:2] + ticket)
        if new_ticket not in current_tickets:
            current_tickets.append(new_ticket)
        cursor.execute("UPDATE Users SET Tickets = '{}' WHERE ID = {}".format(','.join(current_tickets), user_id))
        cnx.commit()
        close_connection_cursor(cnx, cursor)
    else:
        cursor.execute("UPDATE Users SET Tickets = '{}' WHERE ID = {}".format(' '.join(user_info[:2] + ticket), user_id))
        cnx.commit()
        close_connection_cursor(cnx, cursor)

def get_user_tickets(user_id):
    cnx, cursor = create_connection_cursor()
    cursor.execute("SELECT Tickets FROM Users WHERE ID = {}".format(user_id))
    response = cursor.fetchone()
    close_connection_cursor(cnx, cursor)
    if response:
        return response[0]
    else:
        #for none result
        return response 
