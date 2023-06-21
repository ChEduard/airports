import mysql.connector
import config
import ui

class Table:

    def __init__(self, root, data):
        self.data = data
        if len(data)>0:
            self.total_rows = len(data)
            self.total_columns = len(data[0])
            for i in range(self.total_rows):
                for j in range(self.total_columns):
                    #self.e = Entry(root, width=20, fg='blue', font=('Arial', 16, 'bold'))
                    #self.e = Entry(root, width=20)
                    self.e = ui.Entry(root)
                    self.e.grid(row=i, column=j)
                    self.e.insert(ui.END, self.data[i][j])
                #self.btn = Button(root, text='Show all flights', command=clicked1)
                #self.btn.grid(column=5, row=i, rowspan=3, ipadx=5, ipady=5, padx=5, pady=5)
        else:
            Label(root, text="NO DATA").grid(row=0, column=0, sticky=EW, pady=10, padx=10)

    def destroy(self, root):
        for widget in root.winfo_children():
            widget.destroy()


def clicked1():
    """
    For searching airports by latitude and longitude
    :return:
    """

    cursor = db_conn.cursor()

    query = ("SELECT iata, city, country, latitude, longitude FROM airports "
             "WHERE latitude BETWEEN %s AND %s AND longitude BETWEEN %s AND %s")

    cursor.execute(query, (float(ui.min_lat.get()), float(ui.max_lat.get()), float(ui.min_lon.get()), float(ui.max_lon.get())))

    lst = []
    for (iata, city, country, latitude, longitude) in cursor:
        lst.append((iata, city, country, latitude, longitude))
    cursor.close()
    global t
    if t is not None:
        t.destroy(ui.bottom_frame)
    t = Table(ui.bottom_frame, lst)


def clicked2():
    """
    For searching airports by IATA, airport name, city or country
    :return:
    """
    cursor = db_conn.cursor()

    depart = ui.departure.get()
    arrive = ui.arrival.get()

    query = find_route_query(depart, arrive)
    cursor.execute(query)

    lst = []
    for (dep_country, dep_city, dep_airport, dep_iata, ar_iata, ar_airport, ar_city, ar_country) in cursor:
        lst.append((dep_country, dep_city, dep_airport, dep_iata, ar_iata, ar_airport, ar_city, ar_country))
    cursor.close()
    global t
    if t is not None:
        t.destroy(ui.bottom_frame)
    t = Table(ui.bottom_frame, lst)


def find_route_query(depart, arrive):
    """
    Forming request string to MySQL by departure/arrival IATA/airport/city/country
    :param depart: str
    :param arrive:  str
    :return: str
    """
    #Формируем строку запроса в зависимости от разных конбинаций значений в полях "DEPARTURE" и "ARRIVAL"

    if depart != None and arrive != None:

        if len(depart) < 3:
            #depart_query = ''
            depart_query = f'ap.airport LIKE "%{depart}%" OR ap.city LIKE "%{depart}%" OR ap.country LIKE "%{depart}%"'
        elif len(depart) == 3:
            depart_query = f'r.src_airport="{depart}"'
        elif len(depart) > 3:
            depart_query = f'ap.airport LIKE "%{depart}%" OR ap.city LIKE "%{depart}%" OR ap.country LIKE "%{depart}%"'

        if len(arrive) < 3:
            #arrive_query = ''
            arrive_query = f'ap2.airport LIKE "%{arrive}%" OR ap2.city LIKE "%{arrive}%" OR ap2.country LIKE "%{arrive}%"'
        elif len(arrive) == 3:
            arrive_query = f'r.dst_airport="{arrive}"'
        elif len(arrive) > 3:
            arrive_query = f'ap2.airport LIKE "%{arrive}%" OR ap2.city LIKE "%{arrive}%" OR ap2.country LIKE "%{arrive}%"'

        main_query = 'SELECT ap.country, ap.city, ap.airport, r.src_airport, r.dst_airport, ap2.airport, ap2.city, ap2.country \
                        FROM airports AS ap INNER JOIN routes AS r ON ap.iata = r.src_airport INNER JOIN airports AS ap2 ON ap2.iata = r.dst_airport \
                        WHERE ('

        if len(depart_query) > 0:
            if len(arrive_query) > 0:
                query = (main_query + depart_query + ') AND (' + arrive_query + ')')
            else:
                query = (main_query + depart_query + ')')
        else:
            if len(arrive_query) > 0:
                query = (main_query + arrive_query + ')')

    else:
        query = (f'''SELECT ap.country, ap.city, ap.airport, r.src_airport, r.dst_airport, ap2.airport, ap2.city, ap2.country 
            FROM airports AS ap INNER JOIN routes AS r ON ap.iata = r.src_airport INNER JOIN airports AS ap2 ON ap2.iata = r.dst_airport 
            WHERE ap.city LIKE "%Petersburg%"''')
    return query

t = None

#Connection to DataBase
db_conn = mysql.connector.connect(user = config.user,
                                  password = config.password,
                                  host = config.host,
                                  database = config.database)
