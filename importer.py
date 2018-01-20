# -*- encoding: utf-8 -*-

from webapp import app
from dbmodel import *

import csv
import sys

def get_csv_info(csvfile):
    csvreader = csv.reader(csvfile, delimiter=';')
    #first three lines contain some genereal info that we need only parts of it
    info={}

    row = next(csvreader)
    info["taxdeduction"] = row[1]
    info["hours"] = row[3]

    row = next(csvreader)
    info["month"] = row[0]
    info["year"] = row[1]

    row = next(csvreader)
    info["edb"] = row[0]
    info["embs"] = row[1]
    info["company"] = row[2]
    return info

def get_all_pay_rows(csvfile):
    csvreader = csv.reader(csvfile, delimiter=';')
    while True:
        row = next(csvreader)
        if not len(row) == 1: # len(['***********************************']) == 1
            yield row
        else:
            break

def payrecord(row, year, month, hours, companyid):
    p = PayRecord(
        EMBG = row[1],
        LastName = row[2],
        FirstName = row[3],
        CompanyUnit = row[4],
        HealthId = row[5],
        MunicipalityId = row[6],
        WorkDays = row[7],
        WorkHours = row[8],
        OvertimeHours = row[9],
        UnpaidHours = row[10],
        EffectiveWork = row[11],
        FeeHours = row[12],
        FeeType = row[13],
        FeeAmount = row[14],
        UnemploymentYear = row[15],
        GrossPay = row[16],
        DeductionPiom = row[17],
        AdditionalPiom = row[18],
        DeductionFzom = row[19],
        AdditionalFzom = row[20],
        DeductionWorkInjury = row[21],
        AdditionalWorkInjury = row[22],
        DeductionUnemploment = row[23],
        AdditioanlUnemployment = row[24],
        PDD = row[25],
        InsuranceCode = row[26],
        WaivaerCode = row[27],
        InsuranceRate  = row[28],
        FromDay = row[29],
        ToDay = row[30],
        TotalDays = row[31],
        BenefitsPay = row[32],
        DeductionBenefits = row[33],
        AdditionallBenefits = row[34],
        StateAuthorityID = row[35],
        StateAuthorityHours = row[36],
        StateAuthorityPay = row[37],
        EDB = row[38],
        BeginDate = row[39],
        EndDate  = row[40],
        EmployementCode  = row[41],
        RecordNumber  = row[42],
        NetPay = row[43],
        PayDue = row[44],
        BankAccount = row[45],
        Year = year,
        Month = month,
        Hours = hours,
        CompanyId = companyid
    )

    return p

def companyrecord(info):
     return CompanyRecord(CompanyName=info["company"], EDB=info['edb'], EMBS=info['embs'])


def deductions(info):
    return Deductions(Year=info['year'], TaxDeduction=info['taxdeduction'])

def process_file(filename):
    csvfile = open(filename)#, encoding='cp1251')
    info = get_csv_info(csvfile)

    company = companyrecord(info)
    if not CompanyRecord.query.filter(CompanyRecord.EMBS==info['embs']).one_or_none():
        db.session.add(company)
        db.session.commit()

    taxdeduction = deductions(info):
        if not Deductions.query.filename(Deductions.TaxDeductions==info['taxdeduction'].one_or_none():
        db.session.add(taxdeduction)
        db.session.commit()

    for row in get_all_pay_rows(csvfile):
        p = payrecord(row, info['year'], info['month'], info['hours'], company.id)
        db.session.add(p)
    db.session.commit()

with app.app_context():
    if len(sys.argv) < 2:
        print('Usage: importer.py <filename>')
        exit(1)
    filename = sys.argv[1]
    process_file(filename)
