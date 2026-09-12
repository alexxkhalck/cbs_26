from db_connetor import get_connection

with get_connection() as conn:
    with conn.cursor() as cursor:
        # Students
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL
            )
        """)

        # Teachers
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL
            )
        """)

        # Courses
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                teacher_id INTEGER NOT NULL,

                CONSTRAINT fk_course_teacher
                    FOREIGN KEY (teacher_id)
                    REFERENCES teachers(id)
            )
        """)

        # Enrollments
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                id SERIAL PRIMARY KEY,
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

                CONSTRAINT fk_enrollment_student
                    FOREIGN KEY (student_id)
                    REFERENCES students(id),

                CONSTRAINT fk_enrollment_course
                    FOREIGN KEY (course_id)
                    REFERENCES courses(id),

                CONSTRAINT unique_student_course
                    UNIQUE (student_id, course_id)
            )
        """)


        print(f"Database created successfully!")