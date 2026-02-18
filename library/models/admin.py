# import user class
from library.models.user import User
from .user import User

#create admin class
class Admin(User):
    def __init__(self, userid, passwod ,email,name):
        super().__init__(userid,password,email,name)
        self.role ="Admin"

        #manage books
        def manage_books(self):
            return True

