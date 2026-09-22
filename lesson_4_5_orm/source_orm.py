from sqlalchemy.orm import Session
from sqlalchemy import select
from db_connetor import sqlalchemy_engine
from model import Base, Student

engine = sqlalchemy_engine()

Base.metadata.create_all(engine)

def out_results(results):
    for s in results:
        print(s)



with Session(engine) as session:
    result = session.execute(
        select(Student)
    )

    students = result.scalars().all()
    out_results(students)
    ##

    results = session.scalars(
        select(Student).where(Student.email.contains("@gmail.com"))
    ).all()
    out_results(results)
    ##

    results = session.scalars(
        select(Student).where(Student.id == 8)
    ).all()
    out_results(results)

    ##       
    results = session.scalars(
            select(Student).where(Student.first_name == "Andrii")
        ).all()
    out_results(results)
