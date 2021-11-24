# Creer une liste de contact

import sqlite3
from sqlite3.dbapi2 import connect


con = sqlite3.connect(":memory:")

con = sqlite3.connect("liste_contacte.db")

cur = con.cursor() 

print("Connexion a la basse de donnes reuissit")



# Ajouter un contact
cur.execute('''create table liste_contact(
            id integer primary key autoincrement, Nom text null, Prenom text null, Email text, Numero int null, Adress text)''')

cur.execute("insert into liste_contact values(1,'Mor','Sene','niamebaye@gmail.com','761255792','Pout')")



# Ajouter plusieurs contacts
contactlist = [
    (2,'Omar','Diop','diopomar23@gmail.com','781200987','Thies'),
    (3,'Bocar','Diagne','diagneboacr@gmail.com','708322189','Dakar'),
    (4,'Saly','Gueye','diagnesaly90@gmail,com','778901243','fatick'),
    (5,'Daba','Diop','seckameth98@gmail.com','771172440','Pout')
]
cur.executemany("insert into liste_contact values(?, ?, ?, ?, ?, ?)", contactlist)

print("ajoue de contact avec succer")



# Modifier un contacts
cur.execute("update liste_contact set Adress (louga) where id=1")



# Supprimer un contacts
cur.execute("delete from liste_contact where id=2")



# 5) Afficher la liste de tout les contacts
cur.execute("select * from liste_contact")

print(cur.fetchall())



# Rechercher un contact par son numero
cur.execute("select Numero from liste_contact where=? like value")




con.commit()

con.close()