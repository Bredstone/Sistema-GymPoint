DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Trainers;
DROP TABLE IF EXISTS Receptionists;

CREATE TABLE Users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(100) NOT NULL,
  CPF VARCHAR(14) NOT NULL UNIQUE,
  email VARCHAR(60) NOT NULL UNIQUE,
  phone VARCHAR(19) NOT NULL,
  phone_alt VARCHAR(19),
  cep VARCHAR(9) NOT NULL,
  street_number INTEGER NOT NULL,
  user_type VARCHAR(15) DEFAULT 'Student'
);

CREATE TABLE Students (
  id INTEGER NOT NULL,
  password VARCHAR(20) NOT NULL,
  birth_date DATETIME NOT NULL,
  blood_type VARCHAR(3) NOT NULL,
  weight DECIMAL(4, 1) NOT NULL,
  height DECIMAL(3, 2) NOT NULL,
  objective VARCHAR(60) NOT NULL,
  body_fat DECIMAL(3, 1),
  observations VARCHAR(255),
  FOREIGN KEY (id) REFERENCES Users(id)
);

CREATE TABLE Trainers (
  id INTEGER NOT NULL,
  hour_start TIME NOT NULL,
  hour_end TIME NOT NULL,
  service_days VARCHAR(255) NOT NULL,
  FOREIGN KEY (id) REFERENCES Users(id)
);

CREATE TABLE Receptionists (
  id INTEGER NOT NULL,
  hour_start TIME NOT NULL,
  hour_end TIME NOT NULL,
  service_days VARCHAR(255) NOT NULL,
  FOREIGN KEY (id) REFERENCES Users(id)
);

