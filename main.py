from flask import Flask, render_template
from sql import engine, Groups
from sqlalchemy.orm import Session
from sqlalchemy import desc

app = Flask(__name__)

@app.route('/')
def index():
    with Session(engine) as s:
        groups = s.query(Groups).order_by(desc(Groups.group_name)).all()
    return render_template('index.html', groups=groups)

if __name__ == '__main__':
    app.run()