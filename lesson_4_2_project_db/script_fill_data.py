from db_connetor import get_connection

with get_connection() as conn:
    with conn.cursor() as cursor:
        
        # ==========================================
        # STUDENTS
        # ==========================================

        students = [
            ("Oleksandr", "Panchenko", "oleksandr.panchenko@example.com"),
            ("Ivan", "Petrenko", "ivan.petrenko@example.com"),
            ("Anna", "Kovalenko", "anna.kovalenko@example.com"),
            ("Dmytro", "Shevchenko", "dmytro.shevchenko@example.com"),
            ("Olena", "Bondarenko", "olena.bondarenko@example.com"),
            ("Maksym", "Melnyk", "maksym.melnyk@example.com"),
            ("Kateryna", "Tkachenko", "kateryna.tkachenko@example.com"),
            ("Andrii", "Boyko", "andrii.boyko@example.com"),
            ("Maria", "Kravchenko", "maria.kravchenko@example.com"),
            ("Serhii", "Marchenko", "serhii.marchenko@example.com"),
        ]

        cursor.executemany("""
            INSERT INTO students (first_name, last_name, email)
            VALUES (%s, %s, %s)
        """, students)


        # ==========================================
        # TEACHERS
        # ==========================================

        teachers = [
            ("James", "Smith", "james.smith@example.com"),
            ("Emily", "Johnson", "emily.johnson@example.com"),
            ("Robert", "Williams", "robert.williams@example.com"),
            ("Sophie", "Brown", "sophie.brown@example.com"),
        ]

        cursor.executemany("""
            INSERT INTO teachers (first_name, last_name, email)
            VALUES (%s, %s, %s)
        """, teachers)


        # ==========================================
        # COURSES
        # ==========================================

        courses = [
            ("Python Programming", 1),
            ("Advanced Python", 1),
            ("SQL and Databases", 2),
            ("PostgreSQL for Developers", 2),
            ("Django Web Development", 3),
            ("REST API Development", 3),
            ("Software Testing", 4),
            ("Test Automation with Python", 4),
        ]

        cursor.executemany("""
            INSERT INTO courses (title, teacher_id)
            VALUES (%s, %s)
        """, courses)


        # ==========================================
        # ENROLLMENTS
        # ==========================================

        enrollments = [
            # Student 1
            (1, 1),
            (1, 3),
            (1, 7),

            # Student 2
            (2, 1),
            (2, 2),
            (2, 6),

            # Student 3
            (3, 1),
            (3, 3),
            (3, 4),
            (3, 7),

            # Student 4
            (4, 2),
            (4, 5),
            (4, 6),

            # Student 5
            (5, 1),
            (5, 3),
            (5, 7),
            (5, 8),

            # Student 6
            (6, 2),
            (6, 4),
            (6, 5),

            # Student 7
            (7, 1),
            (7, 6),
            (7, 8),

            # Student 8
            (8, 3),
            (8, 4),
            (8, 7),

            # Student 9
            (9, 5),
            (9, 6),
            (9, 8),

            # Student 10
            (10, 2),
            (10, 3),
            (10, 5),
            (10, 7),
        ]

        cursor.executemany("""
            INSERT INTO enrollments (student_id, course_id)
            VALUES (%s, %s)
        """, enrollments)


    conn.commit()

print("Data inserted successfully!")