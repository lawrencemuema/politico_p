from datetime import datetime
from ....db_config import DbSetup
#
# parties = []
# offices = []
# users = []
# vote = []
# candidates = []
# petition = []

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

            """INSERT INTO parties( partyname, hqAddress,
             logoUrl, datecreated) VALUES(%s,%s, %s, %s)""",

            ( self.name, self.hqAddress, self.logoUrl, self.date_created)
        )
        self.database.conn.commit()



    def get_name(self, name):
        self.cursor.execute(
            "SELECT * FROM parties WHERE partyname=%s", (name,)
        )
        p_name = self.cursor.fetchone()
        self.database.conn.commit()
        return p_name


    def get_id(self, party_id):
        self.cursor.execute(
            "SELECT * FROM parties WHERE party_id=%s", (party_id,)
        )

        p_id = self.cursor.fetchall()
        self.database.conn.commit()

        res = []

        for i, items in enumerate(p_id):
            party_id, partyname, hqAddress, logoUrl, datecreated = items
            parties = dict(
                party_id=int(party_id),
                partyname=partyname,
                hqAddress=hqAddress,
                logoUrl=logoUrl,
                datecreated=str(datecreated)
            )
            res.append(parties)

        return res



    def all_parties(self):
        self.cursor.execute("SELECT party_id, partyname, hqAddress, logoUrl, datecreated FROM parties")
        all_p = self.cursor.fetchall()
        self.database.conn.commit()

        res = []

        for i, items in enumerate(all_p):
            party_id, partyname, hqAddress, logoUrl, datecreated = items
            parties = dict(
                party_id=int(party_id),
                partyname=partyname,
                hqAddress=hqAddress,
                logoUrl=logoUrl,
                datecreated=str(datecreated)
            )
            res.append(parties)

        return res


    def delete_party(self, party_id):
        self.cursor.execute(
            "DELETE FROM parties WHERE party_id=%s", (party_id,)
        )
        self.database.conn.commit()

    def update_party(self, party_id,name,hqAddress,logoUrl):
        self.cursor.execute(
            """
            UPDATE parties SET partyname =%s,hqaddress=%s, logourl=%s WHERE party_id=%s""",
            (name, hqAddress, logoUrl, party_id)
        )
        self.database.conn.commit()

    # def simplify(self):
    #     #returning in json
    #     return dict(
    #         party_id=self.party_id,
    #         name=self.name,
    #         hqAddress=self.hqAddress,
    #         logoUrl=self.logoUrl,
    #         date_created=str(self.date_created)
    #     )


class CreateOffice():
    def __init__(self, name=None, Type=None):

        self.database = DbSetup()
        self.cursor = self.database.cursor

        self.name = name
        self.Type = Type
        self.date_created = datetime.now().replace(microsecond=0, second=0)
        self.office_id = None


    def create_office(self):
        self.cursor.execute(

            """INSERT INTO offices(Type,officename,datecreated) VALUES(%s, %s, %s)""",
            (self.Type, self.name, self.date_created)
        )
        self.database.conn.commit()

    # def simplify(self):
    #     return dict(
    #         office_id=self.office_id,
    #         name=self.name,
    #         Type=self.Type,
    #         date_created=str(self.date_created)
    #     )

    def all_offices(self):
        self.cursor.execute("SELECT * FROM offices")
        all_off = self.cursor.fetchall()
        self.database.conn.commit()

        res = []

        for i, items in enumerate(all_off):
            office_id, officename, type, datecreated = items
            offices = dict(
                office_id=int(office_id),
                officename=officename,
                Type=type,
                date_created=str(datecreated)
            )
            res.append(offices)

        return res


    def get_name(self, name):
        self.cursor.execute(
            "SELECT officename FROM offices WHERE officename=%s", (name,)
        )

        off_name = self.cursor.fetchone()
        self.database.conn.commit()
        return off_name

    def get_id(self, office_id):
        self.cursor.execute(
            "SELECT * FROM offices WHERE office_id=%s", (office_id,)
        )
        off_id = self.cursor.fetchall()
        self.database.conn.commit()

        res = []

        for i, items in enumerate(off_id):
            office_id, officename, type, datecreated = items
            offices = dict(
                office_id=int(office_id),
                officename=officename,
                Type=type,
                date_created=str(datecreated)
            )
            res.append(offices)

        return res

    def delete_office(self, office_id):
        self.cursor.execute(
            "DELETE FROM offices WHERE office_id =%s", (office_id,)
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
        self.user_id = None


    def register_user(self):
        self.cursor.execute(
            """
            INSERT INTO users (firstname,lastname,othername,email,phone,passporturl,national_id
            ) VALUES(%s,%s,%s,%s,%s,%s,%s)
            """,(self.firstname, self.lastname, self.othername, self.email,
             self.phoneNumber, self.passportUrl, self.national_id)
        )
        self.database.conn.commit()



    def all_users(self):
        self.cursor.execute("SELECT * FROM users")
        all = self.cursor.fetchall()
        self.database.conn.commit()

        res = []

        for i, items in enumerate(all):
            user_id, firstname,lastname,othername,email,phone, national_id,passporturl = items
            users = dict(
                user_id=int(user_id),
                full_name=firstname +" "+ lastname +" "+ othername ,
                email=email,
                phone=phone,
                national_id=national_id,
                passportUrl=passporturl
            )
            res.append(users)

        return res


    def get_id(self, id):
        self.cursor.execute(
            "SELECT user_id FROM users WHERE user_id=%s", (id,)
        )

        u_id = self.cursor.fetchall()
        self.database.conn.commit()
        return u_id

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







class Candidates():
    def __init__(self, name = None, party=None,o_id=None ):
        self.database = DbSetup()
        self.cursor = self.database.cursor

        self.candidate_name = name
        self.o_id = o_id
        self.party = party
        self.datecreated = str(datetime.now().replace(second=0, microsecond=0))
        self.candidate_id = None


    def register_candidates(self):

        self.cursor.execute(
            """
            INSERT INTO candidates (candidate_name, party, office_id, datecreated)
             VALUES(%s,%s,%s,%s)
            """,
            (self.candidate_name,self.party, self.o_id,  self.datecreated)
        )
        self.database.conn.commit()

    # def simplify(self):
    #     return dict(
    #         office_id=self.office_id,
    #         party_id=self.party_id,
    #         candidate_id=self.candidate_id,
    #         date_created=self.date_created,
    #
    #     )

    def get_name(self, c_name):
        self.cursor.execute("SELECT * FROM candidates WHERE candidate_name=%s", (c_name,) )
        candi = self.cursor.fetchone()
        self.database.conn.commit()
        return candi


    def get_id(self, c_id):
        self.cursor.execute(
            "SELECT * FROM candidates WHERE candidate_id=%s", (c_id,)
        )
        candidate = self.cursor.fetchall()
        self.database.conn.commit()

        res = []

        for i, items in enumerate(candidate):
            candidate_id,candidate_name,party,office_id,datecreated = items
            cands = dict(
                candidate_id=int(candidate_id),
                candidate_name = candidate_name,
                party_name=party,
                office_id=office_id,

                date_created=str(datecreated)
            )
            res.append(cands)

        return res

    def all_cands(self):
        self.cursor.execute("SELECT * FROM candidates")
        all = self.cursor.fetchall()
        self.database.conn.commit()

        res = []

        for i, items in enumerate(all):
            candidate_id, candidate_name, party, office_id, datecreated = items
            cands = dict(
                candidate_id=int(candidate_id),
                candidate_name=candidate_name,
                party_name=party,
                office_id=office_id,

                date_created=str(datecreated)
            )
            res.append(cands)

        return res


class Vote():
    def __init__(self, voter_id = None, candidate_name=None, office=None ):
        self.database = DbSetup()
        self.cursor = self.database.cursor


        self.voter_id = voter_id
        self.candidate_name = candidate_name
        self.office = office
        self.datevoted = str(datetime.now().replace(second=0, microsecond=0))
        self.vote_id = None


    def register_vote(self):

        self.cursor.execute(
            """
            INSERT INTO votes (voter_id, candidate_name, office, datevoted)
             VALUES(%s,%s,%s,%s)
            """,
            (self.voter_id,self.candidate_name, self.office,  self.datevoted)
        )
        self.database.conn.commit()


    def get_candidate_voted(self, c_name):
        self.cursor.execute("SELECT * FROM votes WHERE candidate_name=%s", (c_name,) )
        candy = self.cursor.fetchall()
        self.database.conn.commit()
        res = []

        for i, items in enumerate(candy):
            vote_id, voter_id, candidate_name, office, datevoted = items
            vot = dict(
                vote_id=int(vote_id),
                voter_id=voter_id,
                candidate_name=candidate_name,
                office=office,
                date_voted=str(datevoted)
            )
            res.append(vot)

        return res

    def get_office_and_voterid(self,office,vid):
        self.cursor.execute("SELECT * FROM votes WHERE office=%s AND voter_id=%s", (office,str(vid),))
        office = self.cursor.fetchall()
        self.database.conn.commit()
        return office

    def get_id(self, v_id):
        self.cursor.execute(
            "SELECT * FROM votes WHERE vote_id=%s", (v_id,)
        )
        voter = self.cursor.fetchall()
        self.database.conn.commit()

        res = []

        for i, items in enumerate(voter):
            vote_id,voter_id,candidate_name,office,datevoted = items
            vot = dict(
                vote_id=int(vote_id),
                voter_id=int(voter_id),
                candidate_name = candidate_name,
                office=office,
                date_voted=str(datevoted)
            )
            res.append(vot)

        return res


    def all_votes(self):
        self.cursor.execute("SELECT * FROM votes")
        all_votes = self.cursor.fetchall()
        self.database.conn.commit()

        res = []

        for i, items in enumerate(all_votes):
            vote_id,voter_id,candidate_name,office,datevoted = items
            vot = dict(
                vote_id=int(vote_id),
                voter_id=int(voter_id),
                candidate_name = candidate_name,
                office=office,
                date_voted=str(datevoted)
            )
            res.append(vot)

        return res