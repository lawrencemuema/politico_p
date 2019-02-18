from datetime import datetime
from ...db_config import DbSetup

parties = []
offices = []
users = []
vote = []
candidates = []
petition = []

#classes hold related data
#each class has initialization method for variable setup
#each class contains a simplify method to output in json format as a dictionary

class Parties():

    def __init__(self, name=None, hqAddress=None, logoUrl=None):

        self.database = DbSetup()
        self.cursor = self.database.cursor

        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl
        self.date_created = datetime.now().replace(microsecond=0, second=0)
        self.party_id = None


    def create_party(self):
        self.cursor.execute(

            '''INSERT INTO parties(party_id, name, hqAddress,
             logoUrl, date_created) VALUES(%s,%s, %s, %s, %s)''',

            (self.party_id, self.name, self.hqAddress, self.logoUrl, self.date_created)
        )
        self.database.conn.commit()

    def simplify(self):
        #returning in json
        return dict(
            id=self.id,
            name=self.name,
            hqAddress=self.hqAddress,
            logoUrl=self.logoUrl,
            date_created=str(self.date_created)
        )

    def get_party_by_name(self, name):
        self.cursor.execute(
            "SELECT * FROM parties WHERE name=%s", (name,)
        )
        p_name = self.cursor.fetchone()
        self.database.conn.commit()
        return p_name


    def get_specific_party_by_id(self, party_id):
        self.cursor.execute(
            "SELECT * FROM parties WHERE party_id=%s", (party_id,)
        )

        p_id = self.cursor.fetchone()
        self.database.conn.commit()
        return p_id



    def all_parties(self):
        self.cursor.execute("SELECT * FROM parties")
        all_p = self.cursor.fetchall()
        self.database.conn.commit()
        return all_p


    def delete_party(self, party_id):
        self.cursor.execute(
            "DELETE FROM parties WHERE party_id=%s", (party_id,)
        )
        self.database.conn.commit()

    def update_party(self, party_id):
        self.cursor.execute(
            """
            UPDATE parties SET name =%s,hqaddress=%s, logourl=%s WHERE party_id=%s""",
            (self.name, self.hqAddress, self.logoUrl, party_id)
        )
        self.database.conn.commit()




class CreatePoliticalOffice():
    def __init__(self, name=None, Type=None):

        self.database = DbSetup()
        self.cursor = self.database.cursor

        self.name = name
        self.Type = Type
        self.date_created = datetime.now().replace(microsecond=0, second=0)



    def create_office(self):
        self.cursor.execute(

            """INSERT INTO offices(Type,name,date_created) VALUES(%s, %s, %s)""",
            (self.Type, self.name, self.date_created)
        )
        self.database.conn.commit()

    def simplify(self):
        return dict(
            office_id=self.office_id,
            name=self.name,
            Type=self.Type,
            date_created=str(self.date_created)
        )

    def fetch_all_offices(self):
        self.cursor.execute("SELECT * FROM offices")
        all_off = self.cursor.fetchall()
        self.database.conn.commit()
        return all_off


    def get_office_by_name(self, name):
        self.cursor.execute(
            "SELECT * FROM offices WHERE name=%s", (name,)
        )

        off_name = self.cursor.fetchone()
        self.database.conn.commit()
        return off_name

    def get_office_by_id(self, office_id):
        self.cursor.execute(
            "SELECT * FROM offices WHERE office_id=%s", (office_id,)
        )
        off_id = self.cursor.fetchone()
        self.database.conn.commit()
        return off_id

    def delete_office(self, office_id):
        self.cursor.execute(
            "DELETE FROM offices WHERE office_id =%s", (office_id,)
        )
        self.database.conn.commit()

    def update_office(self, office_id):
        self.cursor.execute(
            """UPDATE offices SET name=%s, Type=%s WHERE office_id=%s""",
            (self.name, self.Type, office_id)

        )
        self.database.conn.commit()




class User():

    def __init__(

        self, firstname=None, lastname=None, othername=None, email=None, phoneNumber=None, passportUrl=None,
                 national_id=None):

        self.database = DbSetup()
        self.cursor = self.database.cursor

        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phoneNumber
        self.passportUrl = passportUrl
        self.national_id = national_id
        self.creation = str(datetime.now().replace(second=0, microsecond=0))
        self.user_id = None


    def register_user(self):
        self.cursor.execute(
            """
            INSERT INTO users (firstname,lastname,othername,email,phoneNumber,passportUrl,national_id,isAdmin,createdDate
            ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,(self.firstname, self.lastname, self.othername, self.email,
             self.phoneNumber, self.passportUrl, self.national_id,
             self.creation)
        )
        self.database.conn.commit()

    def simplify(self):
        return dict(
            firstname=self.firstname,
            lastname=self.lastname,
            othername=self.othername,
            email=self.email,
            password = self.password,
            phoneNumber=self.phoneNumber,
            passportUrl=self.passportUrl,
            creation=str(self.creation),
            user_id=self.user_id,

        )

    def all_users(self):
        self.cursor.execute("SELECT * FROM users")
        all = self.cursor.fetchall()
        self.database.conn.commit()

        return all


    def get_email(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email=%s", (email,) )
        user_mail = self.cursor.fetchone()
        self.database.conn.commit()
        return user_mail


    def get_natID(self, national_id):
        self.cursor.execute("SELECT * FROM users WHERE national_id=%s", (national_id,))
        nat_id = self.cursor.fetchone()
        self.database.conn.commit()

        return nat_id


class Candidates(DB_conn):
    def __init__(self, office_id=None, party_id=None):
        self.database = DbSetup()
        self.cursor = self.database.cursor

        self.office_id = office_id
        self.party_id = party_id
        self.date_created = str(datetime.now().replace(second=0, microsecond=0))
        self.candidate_id = None


    def register_candidates(self):

        self.cursor.execute(
            """
            INSERT INTO candidates (office_id,party_id, candidate_id, date_created)
             VALUES(%s,%s,%s,%s)
            """,
            (self.office_id, self.party_id, self.candidate_id, self.date_created)
        )
        self.database.conn.commit()

    def simplify(self):
        return dict(
            office_id=self.office_id,
            party_id=self.party_id,
            candidate_id=self.candidate_id,
            date_created=self.date_created,

        )

    def get_candidate_by_id(self, c_id):
        self.cursor.execute(
            "SELECT * FROM candidates WHERE candidate_id=%s", (c_id,)
        )
        candidate = self.cursor.fetchone()
        self.database.conn.commit()

        return candidate