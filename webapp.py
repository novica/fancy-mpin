from flask import Flask, render_template
import click

import dbmodel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/novica/src/fancy-mpin/test.db'
dbmodel.db.init_app(app)

@app.cli.command()
def initdb():
    """Initialize the database."""
    click.echo('Init the db')

@app.route("/")
def index():
    companies = dbmodel.CompanyRecord.query.all()
    return render_template('hello.html', companies=companies)

@app.route("/company/<int:id>")
def company(id):
    company=dbmodel.CompanyRecord.query.get(id)
    return render_template('company.html', company=company)

if __name__ == '__main__':
    app.run()
