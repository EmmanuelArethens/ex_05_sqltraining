
CREATE TABLE Students (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,   
	nom VARCHAR(30),
	prenom VARCHAR(30),
	dateNaissance DATE,
	latitude FLOAT,
	longitude FLOAT,
	PRIMARY KEY(id)
);

INSERT INTO Students
VALUES (NULL, "Fulleringer", "Adrien", "1993-12-22", 52.530644, 13.383068),
(NULL, "Dentand", "Athur", "1994-04-01", 24.555186, -81.802336),
(NULL, "Kettab", "Bachir", "1987-07-08", -16.5044211, -151.773669),
(NULL, "Merel", "Caroline", "1997-12-29", 45.599461, -19.374353),
(NULL, "Coste", "Christine", "1981-09-02", -73.968898, 40.778848),
(NULL, "Oroudjian", "Haikouhi", "1989-09-11", 48.866667, 2.333333),
(NULL, "Ros", "Hugo", "1988-11-18", 45.7580538, 4.7649088),
(NULL, "TOBLOME", "KOJO", "1983-05-30", 6.1374800, 1.2122700),
(NULL, "Mai", "Dao", "1989-12-15", 45.691999, 4.792768),
(NULL, "ARETHENS", "Emmanuel", "1995-04-10", 35.0116, 135.7681),
(NULL, "Champredon", "Marina", "1990-06-20", 34.683353, 135.839869),
(NULL, "vavrille", "nory", "1988-01-06", 45.530855, 4.862137),
(NULL, "Guseynov", "Rustam", "1991-03-17", 73.555186, -12.802336),
(NULL, "Flaus", "Théo", "1996-09-16", -22.275800, 166.458000),
(NULL, "Scheurer", "Timothée", "1993-09-03", 126.9779692, 37.566535),
(NULL, "﻿Tin", "William", "1980-05-08", -22.9201, -43.3307);



CREATE TABLE Pygame (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,   
	nomProjet VARCHAR(60),
	id1 VARCHAR(60),
	id2 VARCHAR(60),
	id3 VARCHAR(60),
	id4 VARCHAR(60),
	classes INT,
	codeline INT,
	github VARCHAR(100),
	PRIMARY KEY (id)
);



INSERT INTO Pygame
VALUES (NULL,"Lapyrinth","Théo","Timothée","Maidao","Christine",2,249,"https://github.com/timotheescheurer/LAPYRINTHE"),
(NULL,"Morpion","Kodjo","William","Emmanuel","Nory",0,49,"https://github.com/tinwilliam/Pygame_morpion"),
(NULL,"PETTRON","Hugo","Adrien","Caroline","Haikouhi",1,102,"https://github.com/cmerel/pygame"),
(NULL,"Snake","Rustam","Marina","Arthur","Bachir",1,236,"https://github.com/Azumana/PygameSnake");


SELECT prenom
FROM Students
WHERE (MONTH(dateNaissance) = 08 AND DAY(dateNaissance) >= 23)
OR (MONTH(dateNaissance) = 09 AND DAY(dateNaissance) <= 22);

ou 

SELECT COUNT(dateNaissance)
FROM Students
WHERE (MONTH(dateNaissance) = 08 AND DAY(dateNaissance) >= 23)
OR (MONTH(dateNaissance) = 09 AND DAY(dateNaissance) <= 22); 
