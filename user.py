from datetime import datetime
import uuid


# User class
class User():
    def __init__(self, title,blood, first_name, last_name, email,address,contacts, id="", verified=False):
        # Main initialiser
        self.title = title if title != "none" else ""
        self.blood = blood
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.contacts = contacts
        self.id = uuid.uuid4().hex if not id else id
        self.verified = verified

    @classmethod
    def make_from_dict(cls, d):
        # Initialise User object from a dictionary
        return cls(d['title'],d['blood'], d['first_name'], d['last_name'], d['email'],d['address'],d['contacts'], d['id'], d['verified'])

    def dict(self):
        # Return dictionary representation of the object
        return {
            "id": self.id,
            "title": self.title,
            "blood": self.blood,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "address":self.address,
            "contacts":self.contacts,
            "verified": self.verified
        }

    def display_name(self):
        # Return concatenation of name components
        if self.title:
            return self.title + " " + self.first_name + " " + self.last_name
        else:
            return self.first_name + " " + self.last_name

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


# Anonymous user class
class Anonymous():

    @property
    def is_authenticated(self):
        return False

    @property
    def is_active(self):
        return False

    @property
    def is_anonymous(self):
        return True

    def get_id(self):
        return None
