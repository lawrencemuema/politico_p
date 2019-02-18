import psycopg2

url = "dbname='Politico' user='postgres' host='localhost' port=5432 password='Remax'"


class DbSetup(object):

    def __init__(self):
        self.conn = psycopg2.connect(url)
        self.cursor = self.conn.cursor()

    def destroy_tables(self):
        self.cursor.execute("""DROP TABLE IF EXISTS Users CASCADE;""")
        self.cursor.execute("""DROP TABLE IF EXISTS Posts CASCADE;""")

        self.conn.commit()

    def create_tables(self):

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id serial PRIMARY KEY NOT NULL,
        firstname varchar(50),
        lastname varchar(50),
        othername varchar(50),
        email varchar(50),
        phone varchar(50),
        passporturl varchar(50),
        national_id varchar(25)
        );""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS parties(
        party_id serial PRIMARY KEY NOT NULL,
        partyname varchar(50),
        hqAddress varchar(50),
        logoUrl varchar(50),
        datecreated timestamp
        );""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS offices(
                office_id serial PRIMARY KEY NOT NULL,
                officename varchar(50),
                type varchar(50),
                datecreated timestamp
                );""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS candidates(
                        candidate_id serial PRIMARY KEY NOT NULL,
                        candidate_name varchar(50),
                        party varchar(50),
                        office_id varchar(50),
                        datecreated timestamp
                        );""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS votes(
                                vote_id serial PRIMARY KEY NOT NULL,
                                voter_id varchar(50),
                                candidate_name varchar(50),
                                office varchar(50),
                                datevoted timestamp
                                );""")

        self.conn.commit()



                    # # set DATABASE_URL to this variable and commented
                    # # con_url = "dbname='politico' host='127.0.0.1' port='5432' user='lawrence' password='Remax'"
                    #
                    # # db connection
                    # uri = os.getenv(['DATABASE_URL'])
                    #
                    # # url for test databse connection
                    # test_uri = os.getenv(['DATABASE_TEST_URL'])
                    #
                    # # return connection
                    # def connection(url):
                    #     con = pyscopg2.connect(url)
                    #     return con
                    #
                    # # return conn and create tables
                    # def init_db():
                    #     con = connection(uri)
                    #     cur = con.cursor()
                    #     queries = tables()
                    #
                    #     for query in queries:
                    #         cur.execute(query)
                    #     con.commit()
                    #     return con
                    #
                    # # return conn and create tables(test)
                    # def init_test_db(test_url):
                    #     con = connection(test_uri)
                    #     cur = con.cursor()
                    #     queries = tables()
                    #
                    #     for query in queries:
                    #         cur.execute(query)
                    #     con.commit()
                    #     return con
                    #
                    # # deletes all tables after test run
                    # def destroy_db():
                    #     con = connection(test_uri)
                    #     cur = con.cursor()
                    #
                    #     users = """" DROP TABLE IF EXISTS users CASCADE; """
                    #     parties = """" DROP TABLE IF EXISTS parties CASCADE; """
                    #
                    #     queries = [users, parties]
                    #
                    #     for query in queries:
                    #         cur.execute(query)
                    #     con.commit()
                    #
                    # # contains all table creaiion queries
                    # def tables():
                    #     users = """CREATE TABLE IF NOT EXISTS users(
                    #     user_id serial PRIMARY KEY NOT NULL,
                    #     firstname character varying(50),
                    #     lastname character varying(50),
                    #     othername character varying(50),
                    #     email character varying(50),
                    #     phone character varying(50),
                    #     passporturl character varying(50),
                    #     datecreated timestamp with time zone DEFAULT ('now'::text)::date,
                    #     national_id character varying(50)
                    #     );"""
                    #     parties = """CREATE TABLE IF NOT EXISTS parties(
                    #     party_id serial PRIMARY KEY NOT NULL,
                    #     partyname character varying(50),
                    #     hqAddress character varying(50),
                    #     logoUrl character varying(50),
                    #     datecreated timestamp with time zone DEFAULT ('now'::text)::date
                    #     );"""
                    #
                    #     queries = [users, parties]
                    #     return queries
