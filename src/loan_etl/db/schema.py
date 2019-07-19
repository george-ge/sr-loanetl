# -- FILE: src/loan_etl/db/schema.py
import sqlalchemy as db
from   sqlalchemy import (Column, Integer, BigInteger, String, 
                            Date, Float, Numeric)
from   sqlalchemy.ext.declarative import declarative_base
from   sqlalchemy.orm import relationship

Base = declarative_base()

def get_schema():
    return Base.metadata

class Loans(Base):
    __tablename__   = "loans"
    LoanId          = Column("loan_id", BigInteger(), primary_key=True)
    PlatformName    = Column("platform_name", String(255), primary_key=True)
    IssueDate       = Column("issue_date", Date(), nullable=False)
    OriginalBalance = Column("original_balance", Numeric(precision=15, scale=2), nullable=False)
    InterestRate    = Column("interest_rate", Float(), nullable=False)
    PlatformRating  = Column("platform_rating", String(255), nullable=False)
    LoanStatus      = Column("loan_status", String(255), nullable=False)

class Status(Base):
    __tablename__ = "status"
    LoanId        = Column("loan_id", BigInteger(), db.schema.ForeignKey("loans.loan_id"), primary_key=True)
    PlatformName  = Column("platform_name", String(255), db.schema.ForeignKey("loans.platform_name"), primary_key=True)
    RecordDate    = Column("record_date", Date(), primary_key=True)
    PrincipalPaid = Column("principal_paid", Numeric(precision=15, scale=2), nullable=False)
    InterestPaid  = Column("interest_paid", Numeric(precision=15, scale=2), nullable=False)
    LoanStatus    = Column("loan_status", String(255), nullable=False)
    Loans         = relationship('loans', backref='status')