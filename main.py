from flask import Flask, render_template
from sql import engine, Groups
from sqlalchemy.orm import Session
from sqlalchemy import and_

app = Flask(__name__)

@app.route('/')
def index():
    with Session(engine) as s:
        groups = s.query(Groups).filter(and_(Groups.group_active, Groups.group_invite_link != "")).order_by(Groups.group_name).all()
    return render_template('index.html', groups=groups)

if __name__ == '__main__':
    app.run()