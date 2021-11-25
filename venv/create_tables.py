from sqlalchemy import create_engine, MetaData, \
    Column, Integer, Numeric, String, Date, Table, ForeignKey, BOOLEAN

engine = create_engine(
    "postgresql://ily:root@localhost:5432/fakedata"
)
metadata = MetaData()

clients = Table(
    "clients",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("client_id", Integer, ForeignKey(
        "client.client_id"), nullable=False),
    Column("chambre_id", Integer, ForeignKey(
        "chambre.chambre_id"), nullable=False),
    Column("date_debut", Date, nullable=False),
    Column("date_fin", Date, nullable=False),
)

client = Table(
    "client",
    metadata,
    Column("client_id", Integer, primary_key=True),
    Column("nom", String(100), nullable=False),
    Column("prenom", String(100), nullable=False),
    Column("mail", String(100), nullable=False),
    Column("tel", String(100), nullable=False),
    Column("age", Integer, nullable=False),
    Column("nb_adultes", Integer, nullable=False),
    Column("nb_enfants", Integer, nullable=False),
    Column("services_id", Integer, ForeignKey(
        "services.services_id"), nullable=False),
    Column("adresse_id", Integer, ForeignKey(
        "adresse.adresse_id"), nullable=False),
    Column("animaux", BOOLEAN, nullable=False),
    Column("sexe", BOOLEAN, nullable=False)
)

services = Table(
    "services",
    metadata,
    Column("services_id", Integer, primary_key=True, nullable=False),
    Column("menage", BOOLEAN, nullable=False),
    Column("spa_pass", BOOLEAN, nullable=False),
    Column("parking", BOOLEAN, nullable=False),
    Column("pension", Integer, nullable=False),
)

adresse = Table(
    "adresse",
    metadata,
    Column("adresse_id", Integer, primary_key=True, nullable=False),
    Column("adresse", String(100), nullable=False),
    Column("pays", String(100), nullable=False),
    Column("ville", String(100), nullable=False),
    Column("code_postal", String(100), nullable=False)
)

chambres = Table(
    "chambres",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("chambre_id", Integer, ForeignKey(
        "chambre.chambre_id"), nullable=False),
    Column("libre", BOOLEAN, nullable=False)
)

chambre = Table(
    "chambre",
    metadata,
    Column("chambre_id", Integer, primary_key=True, nullable=False),
    Column("nb_places", Integer, nullable=False),
    Column("nb_lits", Integer, nullable=False),
    Column("nb_pieces", Integer, nullable=False),
    Column("etage", Integer, nullable=False),
    Column("prix_nuit", Integer, nullable=False),
    Column("handicap_service", BOOLEAN, nullable=False),
    Column("code_acces", String(100), nullable=False)
)

menu = Table(
    "menu",
    metadata,
    Column("menu_id", Integer, primary_key=True, nullable=False),
    Column("nom", String(100), nullable=False),
    Column("prix", Integer, nullable=False),
    Column("disponible", BOOLEAN, nullable=False),
    Column("halal", BOOLEAN, nullable=False),
    Column("casher", BOOLEAN, nullable=False),
    Column("vegan", BOOLEAN, nullable=False),
    Column("vegetarien", BOOLEAN, nullable=False),
    Column("gluten_free", BOOLEAN, nullable=False)
)

with engine.begin() as conn:
    metadata.create_all(conn)
    for table in metadata.tables.keys():
        print(f"{table} successfully created")
