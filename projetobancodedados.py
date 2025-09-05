import sqlite3



banco= sqlite3.connect('hospital.db')

cursor= banco.cursor()


cursor.execute("SELECT nome FROM pacientes WHERE cidade = 'São Paulo'")
print(cursor.fetchall())

cursor.execute("SELECT nome, diagnostico FROM pacientes WHERE idade > 40")
print(cursor.fetchall())

cursor.execute("SELECT nome, plano_saude FROM pacientes WHERE plano_saude = 'Unimad' ")
print(cursor.fetchall())

cursor.execute("SELECT nome, data_internacao FROM pacientes ORDER BY data_internacao ASC")
print(cursor.fetchall())

cursor.execute("SELECT nome, diagnostico FROM pacientes WHERE diagnostico = 'Fratura'")
print(cursor.fetchall())

cursor.execute("SELECT nome, medico_responsavel FROM pacientes WHERE medico_responsavel = 'Dr. João'")
print(cursor.fetchall())








