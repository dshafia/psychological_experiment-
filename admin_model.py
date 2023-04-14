from Extension import db


class Admin(db.Model):
    user_name = db.Column(db.String(40), unique=False, nullable=False, primary_key=True)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.password}')"
