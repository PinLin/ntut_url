from datetime import datetime

from extensions.db import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(99), unique=True)
    target = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    @staticmethod
    def create(name: str, target: str):
        """建立縮網址"""
        url = Url(name=name, target=target)

        return url

    @staticmethod
    def find(name: str):
        """取得縮網址"""
        return Url.query.filter_by(name=name).first()
