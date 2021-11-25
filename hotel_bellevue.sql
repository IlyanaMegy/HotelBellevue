CREATE TABLE clients (
    id INT PRIMARY KEY NOT NULL,
    id_client INT NOT NULL,
    date_debut DATE NOT NULL,
    date_fin DATE NOT NULL,
    id_chambre INT NOT NULL,
    FOREIGN KEY (id_client) REFERENCES client(id_client),
    FOREIGN KEY (id_chambre) REFERENCES chambre(id_chambre)
);
CREATE TABLE client (
    id_client INT PRIMARY KEY NOT NULL,
    nom varchar(20) not null,
    prenom varchar(20) not null,
    age int not null,
    nb_adultes int not null,
    nb_enfants int,
    animaux binary not null,
    mail varchar(50) not null,
    tel varchar(20) not null,
    sexe binary not null,
    services_id INT not NULL,
    adresse_id INT not null,
    FOREIGN KEY (services_id) REFERENCES services(services_id),
    FOREIGN KEY (adresse_id) REFERENCES adresse(adresse_id)
);
CREATE TABLE services (
    services_id INT PRIMARY KEY NOT NULL,
    menage binary,
    parking binary,
    pension int not null,
    spa_pass binary
);
CREATE TABLE adresse(
    adresse_id INT PRIMARY KEY not null,
    adresse varchar(100) not null,
    pays varchar(40) not null,
    ville varchar(20) not null,
    code_postal varchar(20) not null
);
CREATE TABLE chambres (
    chambre_id INT not null,
    libre binary,
    FOREIGN KEY (chambre_id) REFERENCES chambre(chambre_id)
);
CREATE TABLE chambre (
    chambre_id INT PRIMARY KEY not NULL,
    nb_place int not null,
    nb_lits int not null,
    nb_pieces int not null,
    prix_nuit int not null,
    handicap_service binary,
    code_acces varchar(20) not null,
    etage int not null
);
CREATE TABLE menu (
    id_menu INT PRIMARY KEY not null,
    nom varchar (50) not null,
    prix int not null,
    disponibilite binary,
    halal binary,
    casher binary,
    vegan binary,
    vegetarien binary,
    gluten_free binary
);