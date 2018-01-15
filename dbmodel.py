from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class PayRecord(db.Model):
    __tablename__='PayRecord'
    id = db.Column(db.Integer, primary_key=True)
    EMBG = db.Column(db.String(13),  nullable=False)
    LastName = db.Column(db.String(30),  nullable=False)
    FirstName = db.Column(db.String(30),  nullable=False)
    CompanyUnit = db.Column(db.String(3),  nullable=False)
    HealthId = db.Column(db.Integer,  nullable=False)
    MunicipalityId = db.Column(db.Integer,  nullable=False)
    WorkDays = db.Column(db.Integer,  nullable=False)
    WorkHours = db.Column(db.Integer,  nullable=False)
    OvertimeHours = db.Column(db.Integer)
    UnpaidHours = db.Column(db.Integer)
    EffectiveWork = db.Column(db.Float,  nullable=False)
    FeeHours = db.Column(db.Integer)
    FeeType = db.Column(db.String(3))
    FeeAmount = db.Column(db.Float,  nullable=False)
    UnemploymentYear = db.Column(db.String(4))
    GrossPay = db.Column(db.Float,  nullable=False)
    DeductionPiom = db.Column(db.Float,  nullable=False)
    AdditionalPiom = db.Column(db.Float,  nullable=False)
    DeductionFzom = db.Column(db.Float,  nullable=False)
    AdditionalFzom = db.Column(db.Float,  nullable=False)
    DeductionWorkInjury = db.Column(db.Float,  nullable=False)
    AdditionalWorkInjury = db.Column(db.Float,  nullable=False)
    DeductionUnemploment = db.Column(db.Float,  nullable=False)
    AdditioanlUnemployment = db.Column(db.Float,  nullable=False)
    PDD = db.Column(db.Float,  nullable=False)
    InsuranceCode = db.Column(db.String(4),  nullable=False)
    WaivaerCode = db.Column(db.String(3))
    InsuranceRate  = db.Column(db.String(1))
    FromDay = db.Column(db.String(2))
    ToDay = db.Column(db.String(2)) 
    TotalDays = db.Column(db.Integer)
    BenefitsPay = db.Column(db.Float,  nullable=False)
    DeductionBenefits = db.Column(db.Float,  nullable=False)
    AdditionallBenefits = db.Column(db.Float,  nullable=False)
    StateAuthorityID = db.Column(db.String(3))
    StateAuthorityHours = db.Column(db.Integer)
    StateAuthorityPay =  db.Column(db.Float,  nullable=False)
    EDB =  db.Column(db.String(13))
    BeginDate  = db.Column(db.String(2))
    EndDate  = db.Column(db.String(2))
    EmployementCode  = db.Column(db.String(2))
    RecordNumber  = db.Column(db.Integer,  nullable=False)
    NetPay = db.Column(db.Float,  nullable=False)
    PayDue = db.Column(db.Float,  nullable=False)
    BankAccount = db.Column(db.Integer,  nullable=False)
    Year = db.Column(db.Integer, nullable=False)
    Month = db.Column(db.Integer, nullable=False)
    Hours = db.Column(db.Integer, nullable=False)
    CompanyId = db.Column(db.Integer, db.ForeignKey('CompanyRecord.id'))
    CompanyRecord = db.relationship("CompanyRecord")

class CompanyRecord(db.Model):
    __tablename__='CompanyRecord'
    id = db.Column(db.Integer, primary_key=True)
    ComapnyName = db.Column(db.String(30), nullable=False)
    EDB = db.Column(db.String(13), nullable=False)
    EMBS = db.Column(db.String(7), nullable=False)

class Deductions(db.Model):
    __tablename__='Deductions'
    id = db.Column(db.Integer, primary_key=True)
    Year = db.Column(db.Integer, nullable=False)
    TaxDeductions = db.Column(db.Float,  nullable=False)

def __repr__(self):
    return '<PayRecord %r>' % self.username

def __repr__(self):
    return '<CompanyRecord %r>' % self.username

def __repr__(self):
    return '<Deductions %r>' % self.username
