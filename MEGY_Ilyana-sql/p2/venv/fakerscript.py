from sqlalchemy import create_engine, MetaData
from faker import Faker
import sys
import random

engine = create_engine(
    "postgresql://ily:root@localhost:5432/fakedata"
)

metadata = MetaData()
faker = Faker()
with engine.connect() as conn:
    metadata.reflect(conn)
    # print(engine.table_names())

# table = sys.argv[1]
# if table not in metadata.tables.keys():
#     print("clients does not exist")
# else:
#     print("clients exist")

# for t in metadata.sorted_tables:
#     print(t.name)


clients = metadata.sorted_tables[6]
client = metadata.sorted_tables[5]
chambres = metadata.sorted_tables[4]
chambre = metadata.sorted_tables[1]
services = metadata.sorted_tables[3]
adresse = metadata.sorted_tables[0]
menu = metadata.sorted_tables[2]

menu_list = ["Le pot-au-feu", "La poule au pot", "Quiche Lorraine", "Le clafoutis aux cerises", "La daube de boeuf", "Foie gras", "Huîtres",
             "Cassoulet", "Poulet basquaise", "Escargots au beurre", "Sandwich Jambon Beurre", "Croque-Monsieur", "Fondue savoyarde", "Baba au rhum"]


class GenerateData:
    def __init__(self):
        self.table = sys.argv[1]
        self.num_records = int(sys.argv[2])

    def create_data(self):
        if self.table not in metadata.tables.keys():
            return print(f"{self.table} does not exist")

        # Menu
        if self.table == "menu":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = menu.insert().values(
                        nom=random.choice(menu_list),
                        prix=faker.random_int(min=5, max=45),
                        disponible=faker.boolean(chance_of_getting_true=50),
                        halal=faker.boolean(chance_of_getting_true=50),
                        vegan=faker.boolean(chance_of_getting_true=50),
                        vegetarien=faker.boolean(chance_of_getting_true=50),
                        casher=faker.boolean(chance_of_getting_true=50),
                        gluten_free=faker.boolean(chance_of_getting_true=50)
                    )
                    conn.execute(insert_stmt)

        # Services
        if self.table == "services":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = services.insert().values(
                        menage=faker.boolean(chance_of_getting_true=50),
                        spa_pass=faker.boolean(chance_of_getting_true=50),
                        parking=faker.boolean(chance_of_getting_true=50),
                        pension=faker.random_int(min=0, max=3)
                    )
                    conn.execute(insert_stmt)

        # Adresse
        if self.table == "adresse":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = adresse.insert().values(
                        adresse=faker.street_address(),
                        code_postal=faker.postcode(),
                        pays=faker.country(),
                        ville=faker.city()
                    )
                    conn.execute(insert_stmt)

        # Chambre
        if self.table == "chambre":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = chambre.insert().values(
                        nb_places=faker.random_int(min=1, max=6),
                        nb_lits=faker.random_int(min=1, max=6),
                        nb_pieces=faker.random_int(min=1, max=3),
                        prix_nuit=faker.random_int(min=80, max=350),
                        handicap_service=faker.boolean(
                            chance_of_getting_true=50),
                        etage=faker.random_int(min=1, max=6),
                        code_acces=faker.random_int(min=10000, max=99999)
                    )
                    conn.execute(insert_stmt)

        # Chambres
        if self.table == "chambres":
            with engine.begin() as conn:
                for i in range(self.num_records):
                    insert_stmt = chambres.insert().values(
                        chambre_id=i,
                        libre=faker.boolean(chance_of_getting_true=50)
                    )
                    conn.execute(insert_stmt)

        # Client
        if self.table == "client":
            with engine.begin() as conn:
                for i in range(self.num_records):
                    insert_stmt = client.insert().values(
                        prenom=faker.first_name(),
                        nom=faker.last_name(),
                        nb_adultes=faker.random_int(min=1, max=5),
                        nb_enfants=faker.random_int(min=0, max=4),
                        animaux=faker.boolean(chance_of_getting_true=10),
                        sexe=faker.boolean(chance_of_getting_true=50),
                        mail=faker.email(),
                        services_id=i,
                        adresse_id=i,
                        age=faker.random_int(min=18, max=99),
                        tel=faker.phone_number(),
                    )
                    conn.execute(insert_stmt)

        # Clients
        if self.table == "clients":
            with engine.begin() as conn:
                for _ in range(self.num_records):
                    insert_stmt = clients.insert().values(
                        client_id=i,
                        chambre_id=i,
                        date_debut=faker.date_time_between(
                            start_date="-1y", end_date="now")(),
                        date_fin=faker.date_time_between(
                            start_date="now", end_date="+1y")()
                    )
                    conn.execute(insert_stmt)


if __name__ == "__main__":
    generate_data = GenerateData()
    generate_data.create_data()
