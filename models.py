import sqlite3

def init_db():
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    conn.commit()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS question(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Question TEXT NOT NULL,
            answer TEXT NOT NULL,
            wrong1 TEXT NOT NULL,
            wrong2 TEXT NOT NULL,
            wrong3 TEXT NOT NULL

        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS  quiz_content(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quiz_id INTEGER,
            question 5_id INTEGER,
            FOREIGN KEY (quiz_id) REFERENCES quiz(id),
            FOREIGN KEY (question_id) REFERENCES question(id)

        )
    ''')

    conn.commit()
    conn.close()

def fill_questions(path_to_db):
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    n = input('Введіть кількість запитань')
    
    for i in range(int(n)):
        question = input(f"Введіть питання під номером {i}: ")
        answer = input("Введіть правильну відповідь: ")
        wrong_1 = input("Введіть першу не правильну відповідь: ")
        wrong_2 = input("Введіть другу не правильну відповідь: ")
        wrong_3 = input("Введіть третю не правильну відповідь: ")

        cur.execute('''INSERT INTO questions 
                        (question, answer, wrong_answer_1, wrong_answer_2, wrong_answer_3) 
                        VALUES (?, ?, ?, ?, ?)''', 
                    (question, answer, wrong_1, wrong_2, wrong_3))

    conn.commit()  # Зберігаємо зміни після кожного запису

    conn.close()  # Закриваємо з'єднання після завершення циклу
init_db()
fill_questions('questions.db')

            





   
