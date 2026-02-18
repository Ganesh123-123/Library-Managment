# create user class

class User:
    def__init__(self,userid:int,password:str,username:str):
    self.userid =userid
    self.password =password
    self.email = email
    self.name = name
    self.role ='user'
    self.is_active =True


    #display user details
    def display_details(self):
        user ={}
        user["userid"]=self.userid
        user["email"]=self.email
        user['name'] =self.name
        user['role'] = self.role
      #  user['is_active'] = self.is_active
        return user

        #can manage books
        def manage_books(self):
            return  False

        # login check password
        def login_auth(self,password):
            return self.password == password


