import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

# Aluno
cur.execute('INSERT INTO Users (name, CPF, email, password, phone, phone_alt, cep, street_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            ('Brendon Vicente Rocha Silva', '476.582.928-69', 'bredstone13@gmail.com', 'senha123', '(13) 99135-3538', '(13) 98808-5713', '11349-190', 527))
cur.execute('INSERT INTO Students (id, birth_date, blood_type, weight, height, gender, objective, body_fat) VALUES ((SELECT id from Users WHERE email = ?), ?, ?, ?, ?, ?, ?, ?)',
            ('bredstone13@gmail.com', '13/09/1999', 'B+', 61.5, 1.65, 'Masculino', 'Ganho de massa magra', 9.2))

# Treinador
cur.execute('INSERT INTO Users (name, CPF, email, password, phone, phone_alt, cep, street_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            ('Júlio Vicente Rocha Silva', '251.123.453-78', 'julio.vicente2008@gmail.com', 'senha123', '(13) 99120-7124', '(13) 98808-5713', '11349-190', 527))
cur.execute('INSERT INTO Trainers (id, hour_start, hour_end, service_days) VALUES ((SELECT id from Users WHERE email = ?), ?, ?, ?)',
            ('julio.vicente2008@gmail.com', '07:00:00', '13:00:00', 'dom, seg, ter, qua, qui, sex, sab'))

# Recepcionista
cur.execute('INSERT INTO Users (name, CPF, email, password, phone, phone_alt, cep, street_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            ('Breno de Brida', '123.456.789-78', 'brenodebrida@gmail.com', 'senha123', '(48) 99179-2464', '(13) 99135-3538', '88063-301', 1157))
cur.execute('INSERT INTO Receptionists (id, hour_start, hour_end, service_days) VALUES ((SELECT id from Users WHERE email = ?), ?, ?, ?)',
            ('brenodebrida@gmail.com', '07:00:00', '13:00:00', 'dom, seg, ter, qua, qui, sex, sab'))

# Plano
cur.execute('INSERT INTO Plans (title, duration, price) VALUES (?, ?, ?)',
            ('Standard', 1, 119.90))
cur.execute('INSERT INTO Plans (title, duration, price) VALUES (?, ?, ?)',
            ('Silver', 3, 99.90))
cur.execute('INSERT INTO Plans (title, duration, price) VALUES (?, ?, ?)',
            ('Gold', 6, 79.90))
cur.execute('INSERT INTO Plans (title, duration, price) VALUES (?, ?, ?)',
            ('Titan', 12, 59.90))

connection.commit()
connection.close()