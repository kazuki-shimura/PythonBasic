import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# engine = sqlalchemy.create_engine('sqlite:///:memory:')
# engine = sqlalchemy.create_engine('sqlite:///test_mysql_database2', echo=True)
#Mysqlに接続（パスワードを指定する場合）
engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:Root/root8@localhost/test_mysql_database2?charset=utf8'
)



Base = sqlalchemy.ext.declarative.declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

p1 = Person(name='Luffy')
session.add(p1)
p2 = Person(name='Nami')
session.add(p2)
p3 = Person(name='Sanzi')
session.add(p3)
session.commit()

p4 = session.query(Person).filter_by(name='Sanzi').first()
p4.name = 'Zoro'
session.add(p4)
session.commit()

p5 = session.query(Person).filter_by(id=1).first()
session.delete(p5)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
