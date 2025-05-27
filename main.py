from sqlalchemy import create_engine , Column, Integer, String ,ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

con = create_engine("sqlite:///company.db", echo=True)
Session = sessionmaker(bind=con)
session = Session()

Base = declarative_base()
class Company(Base):
    __tablename__ = "company"
    id = Column(Integer , primary_key= True)
    name = Column(String(50) , nullable = False)
    email = Column(String(50) , nullable = False)
    devs = relationship("Dev", back_populates="company")
    freebies = relationship("Freebie", back_populates="company")

class Dev(Base):
    __tablename__ = "dev"
    id = Column(Integer , primary_key= True)
    name = Column(String(50) , nullable = False)
    email = Column(String(50) , nullable = False)
    company_id = Column(Integer , ForeignKey("company.id") , nullable = False)
    company = relationship("Company", back_populates="devs")
    
class Freebie(Base):
    __tablename__ = "freebie"
    id = Column(Integer , primary_key= True)
    name = Column(String(50) , nullable = False)
    company_id = Column(Integer , ForeignKey("company.id") , nullable = False)
    company = relationship("Company", back_populates="freebies")

Base.metadata.create_all(con)




    