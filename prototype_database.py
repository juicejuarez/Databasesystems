import sqlite3


connector = sqlite3.connect('database32.db')
cursor = connector.cursor()



cursor.execute("""BEGIN TRANSACTION;""")


cursor.execute("""CREATE TABLE IF NOT EXISTS "child" (
	"child_id"	INTEGER,
	"parent_id"	INTEGER,
	"program_id"	INTEGER,
	"child_first"	TEXT,
	"child_last"	TEXT,
	PRIMARY KEY("child_id" AUTOINCREMENT),
	FOREIGN KEY("parent_id") REFERENCES "parent"("parent_id"),
	FOREIGN KEY("program_id") REFERENCES "program"("program_id")
);""")


cursor.execute("""CREATE TABLE IF NOT EXISTS "parent" (
	"parent_id"	INTEGER,
	"parent_first"	TEXT,
	"parent_last"	TEXT,
	"parent_streetnumber"	INTEGER,
	"parent_street"	TEXT,
	"parent_zip"	INTEGER,
	"parent_phoneareacode"	INTEGER,
	"parent_phoneprefix"	INTEGER,
	"parent_phonesuffix"	INTEGER,
	"parent_email"	TEXT,
	PRIMARY KEY("parent_id" AUTOINCREMENT)
);""")


cursor.execute("""CREATE TABLE IF NOT EXISTS "program" (
	"program_id"	INTEGER,
	"program_name"	TEXT,
	"program_streetnumber"	TEXT,
	"program_street"	TEXT,
	"program_zip"	INTEGER,
	"program_areacode"	INTEGER,
	"program_phoneprefix"	INTEGER,
	"program_phonesuffix"	INTEGER,
	"program_email"	TEXT,
	"program_hasfinancialassistance"	TEXT,
	"program_waitlistdays"	INTEGER,
	"program_cost"	INTEGER,
	"program_rating"	INTEGER,
	PRIMARY KEY("program_id" AUTOINCREMENT)
);""")


cursor.execute("""CREATE TABLE IF NOT EXISTS "zip" (
	"zip_code"	INTEGER,
	"zip_medianincome"	INTEGER,
	PRIMARY KEY("zip_code")
);""")


cursor.execute("""INSERT INTO "child" VALUES (1,1,1,'Billy','Smith'),
 (2,1,1,'Melissa','Smith'),
 (3,2,3,'Roger','Cain'),
 (4,3,5,'George','Morales'),
 (5,4,7,'Elena','Jenson'),
 (6,5,8,'Charles','Roberts'),
 (7,6,2,'Lisa','Jimenez'),
 (8,7,3,'Samuel','Costanza'),
 (9,8,5,'Suzy','Fences'),
 (10,9,4,'Katherine','Quiroz');""")


cursor.execute("""INSERT INTO "parent" VALUES (1,'John','Smith',4739,'N Flores',78207,210,555,7325,'jsmith@email.com'),
 (2,'Maria','Cain',735,'Soledad',78243,210,555,6422,'cain@mailc.om'),
 (3,'Jesus','Morales',3788,'St Marys',78234,210,555,9864,'morales@email.com'),
 (4,'Marcos','Jenson',12456,'N Alamo',78288,210,555,3567,'jenson@mail.com'),
 (5,'Bob','Roberts',6538,'S Loop 410',78234,210,555,4467,'roberts@email.com'),
 (6,'Regina','Jimenez',3776,'W Commerce',78224,210,555,2363,'rj@email.com'),
 (7,'Arthur','Costanza',643,'E Houston',78202,210,555,9804,'acostanza@email.com'),
 (8,'Bill','Fences',9776,'Santa Rosa',78288,210,555,5589,'bill@fences.com'),
 (9,'Angela','Quiroz',35522,'Durango',78212,210,555,1430,'aquiroz@mail.com');""")


cursor.execute("""INSERT INTO "program" VALUES (1,'YMCA','1213','lowa St',78203,210,555,1234,'ymcawest@ymca.com','NO',0,0,5),
 (2,'Recess','234','N. Main',78204,210,555,2345,'email@recess.com','NO',0,200,4),
 (3,'Code_ninjas','20322','Huebner',78258,210,555,6254,'codeninjas@email.com','YES',7,300,3),
 (4,'AOC''s Best Afterschool','26108','Overlook',78260,210,555,7765,'aocsbest@email.com','NO',14,1200,2),
 (5,'EdQuisitive Montessori','22215','Wilde',78258,210,555,5789,'edquisitive@email.com','NO',0,300,5),
 (6,'IVY Kids ELC','24278','Wilde',78258,210,555,6543,'elc@email.com','NO',0,150,4),
 (7,'Kin','234','Vaughn',78258,210,555,7877,'kin@email.com','YES',14,250,3),
 (8,'Kumon','19239','Stone',78258,210,555,5443,'kumon@email.com','NO',0,350,2),
 (9,'Youth Movement Art','510','S. Braun',78203,210,555,4345,'youth@move.com','YES',7,450,5),
 (10,'New Kids On The Block','623','S WW White',78220,210,555,6785,'new@block.com','YES',0,600,3),
 (11,'Boys & Girls Club','123','Ralph Ave',78204,210,555,4355,'bc@club.com','YES',0,125,5),
 (12,'Catholic Charities Afterschool','1801','W. Cesar Chavez',78207,210,555,5677,'aft@cc.com','YES',7,0,5),
 (13,'After School Chandler','111','Chandler',78226,210,555,2567,'after@chandler.com','NO',0,200,4);""")


cursor.execute("""INSERT INTO "zip" VALUES (78203,29000),
 (78204,34000),
 (78207,22000),
 (78220,30000),
 (78226,32000),
 (78258,102000),
 (78260,112000);""")


cursor.execute("""COMMIT;""")


connector.commit()
connector.close()

