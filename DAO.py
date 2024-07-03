from database.DB_connect import DBConnect
from model.location import Location


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getProvider():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = ("""select distinct Provider p
                    from nyc_wifi_hotspot_locations
                    order by p""")
        cursor.execute(query, )

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi1(provider):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ("""select Location as l, avg(n.latitude) as lat, avg(n.longitude) as log
                    from nyc_wifi_hotspot_locations n
                    where n.provider = %s
                    group by l""")
        cursor.execute(query, (provider,))

        for row in cursor:
            result.append(Location(row["l"], row["lat"], row["log"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi2(provider):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ("""select n1.location as l1, n2.location as l2, avg(n1.latitude) as lat1, avg(n1.longitude) as log1,
                    avg(n2.latitude) as lat2, avg(n2.longitude) as log2
                    from nyc_wifi_hotspot_locations n1, nyc_wifi_hotspot_locations n2
                    where n1.provider = %s and n1.provider = n2.provider
                    and n1.location < n2.location
                    group by n1.location, n2.location
                    """)

        cursor.execute(query, (provider,))

        for row in cursor:
            l1 = Location(row["l1"], row["lat1"], row["log1"])
            l2 = Location(row["l2"], row["lat2"], row["log2"])
            result.append((l1,l2))

        cursor.close()
        conn.close()
        return result



