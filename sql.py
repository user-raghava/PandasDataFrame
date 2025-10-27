
with Session(engine) as session:
    student1 = Student(name='std1', mobile='9999999', email='std1@gmail.com')
    session.add(student1)
    student2 = Student(name='std2', mobile='9999999', email='std2@gmail.com')
    session.add(student2)

    session.commit()