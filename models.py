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
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            wrong1 TEXT NOT NULL,
            wrong2 TEXT NOT NULL,
            wrong3 TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz_content(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quiz_id INTEGER,
            question_id INTEGER,
            FOREIGN KEY (quiz_id) REFERENCES quiz(id),
            FOREIGN KEY (question_id) REFERENCES question(id)
        )
    ''')

    conn.commit()
    conn.close()

# def fill_questions(path_to_db):
#     conn = sqlite3.connect('db.sqlite')
#     cur = conn.cursor()
#     n = input('Введіть кількість запитань: ')
    
#     for i in range(int(n)):
#         question = input(f"Введіть питання під номером {i}: ")
#         answer = input("Введіть правильну відповідь: ")
#         wrong_1 = input("Введіть першу не правильну відповідь: ")
#         wrong_2 = input("Введіть другу не правильну відповідь: ")
#         wrong_3 = input("Введіть третю не правильну відповідь: ")

#         cur.execute('''INSERT INTO question 
#                         (question, answer, wrong1, wrong2, wrong3) 
#                         VALUES (?, ?, ?, ?, ?)''', 
#                     (question, answer, wrong_1, wrong_2, wrong_3))

#     conn.commit()
#     conn.close()
5


# def fill_quiz(path_to_db):
#     conn = sqlite3.connect("db.sqlite")
#     cur = conn.cursor()
#     f = input('Кількість вікторин:')

#     for i in range(int(f)):
#         name = input('Теми вікторини')

#         cur.execute('''INSERT INTO quiz(name)
#                     VALUES(?)''',
#                     [name])
#     conn.commit()
#     conn.close()

# fill_quiz('quiz.db')

def quiz_content(path_to_db):
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()

    while True:

        k = input("Чи хочете встановити зв'язок між питанням та вікториною").strip().lower()


        if k == 'ні':
            break

        try:
            question_id = int(input("Введіть id питання: ").strip())
            quiz_id = int(input("Введіть id вікторини: ").strip())

            cur.execute('''INSERT INTO quiz_content(quiz_id, question_id)
                            VALUES(?,?)''',
                            [quiz_id, question_id])
            conn.commit()
        except Exception as e:
            print(e)
    
    conn.close()

quiz_content('quiz_content.db')



#fill_questions('question.db')

#def get_question_after(question_id=0, quiz_id=1):
