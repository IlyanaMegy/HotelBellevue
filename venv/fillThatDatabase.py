from sqlalchemy import create_engine, MetaData
from faker import Faker
import sys

engine = create_engine(
    "postgresql://ily:root@localhost:5432/fakedata"
)

metadata = MetaData()
faker = Faker()
with engine.connect() as conn:
    metadata.reflect(conn)

clients = metadata.tables.keys["clients"]
client = metadata.tables.keys["client"]
chambres = metadata.tables.keys["chambres"]
chambre = metadata.tables.keys["chambre"]
services = metadata.tables.keys["services"]
adresse = metadata.tables.keys["adresse"]
menu = metadata.tables.keys["menu"]


class GenerateData:
    def __init__(self):
        self.table = sys.argv[1]
        self.num_records = int(sys.argv[2])

    def create_data(self):
        if self.table not in metadata.tables.keys():
            return print(f"{self.table} does not exist")

        # Clients
        if self.table == "clients":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = client.insert().values(
                        date_debut=faker.date_time_between(
                            start_date="-1y", end_date="now")(),
                        date_fin=faker.date_time_between(
                            start_date="now", end_date="+1y")()
                    )
                conn.execute(insert_stmt)

        # Client
        if self.table == "client":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = client.insert().values(
                        prenom=faker.first_name(),
                        nom=faker.last_name(),
                        nb_adultes=faker.random_digit(min=1, max=6),
                        nb_enfants=faker.number(min=0, max=5),
                        animaux=faker.random.array_element([True, False]),
                        sexe=faker.random.array_element([True, False]),
                        mail=faker.email(),
                        age=faker.number(minimum_age=18, maximum_age=99),
                        tel=faker.phone_number(),
                    )
                conn.execute(insert_stmt)

        # Services
        if self.table == "services":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = client.insert().values(
                        menage=faker.random.array_element([True, False]),
                        spa_pass=faker.random.array_element([True, False]),
                        parking=faker.random.array_element([True, False]),
                        pension=faker.random_digit(min=0, max=3),
                    )
                conn.execute(insert_stmt)

        # Adresse
        if self.table == "adresse":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = client.insert().values(
                        adresse=faker.street_address(),
                        code_postal=faker.postcode(),
                        pays=faker.country(),
                        ville=faker.city()
                    )
                conn.execute(insert_stmt)

        # Chambres
        if self.table == "chambres":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = client.insert().values(
                        libre=faker.random.array_element([True, False])
                    )
                conn.execute(insert_stmt)

        # Chambre
        if self.table == "chambre":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = client.insert().values(
                        nb_places=faker.random_digit(min=1, max=6),
                        nb_lits=faker.random_digit(min=1, max=6),
                        nb_pieces=faker.random_digit(min=1, max=3),
                        prix_nuit=faker.random_digit(min=80, max=350),
                        handicap_service=faker.random.array_element(
                            [True, False]),
                        etage=faker.random_digit(min=1, max=6),
                        code_acces=faker.random_digit(min=10000, max=99999)
                    )
                conn.execute(insert_stmt)

        # Menu
        if self.table == "menu":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = client.insert().values(
                        nom=faker.Food.En.dish(),
                        prix=faker.random_digit(min=5, max=45),
                        disponible=faker.random.array_element([True, False]),
                        halal=faker.random.array_element([True, False]),
                        vegan=faker.random.array_element([True, False]),
                        vegetarien=faker.random.array_element([True, False]),
                        casher=faker.random.array_element([True, False]),
                        gluten_free=faker.random.array_element([True, False])
                    )
                conn.execute(insert_stmt)


if __name__ == "__main__":
    generate_data = GenerateData()
    generate_data.create_data()
