class emp:
    def __init__(self,u_id=None,name=None,password=None,user_type=None,user_status=None,contact=None,dob=None,email=None):
        
        self.u_id=u_id
        self.name=name
        self.password=password
        self.user_type=user_type
        self.user_status=user_status
        self.contact=contact
        self.dob=dob
        self.email=email
        
    def setId(self,u_id):
        self.u_id=u_id
    def setName(self,name):
        self.name=name
    def setPassword(self,password):
        self.password=password
    def setuser_type(self,user_type):
        self.user_type=user_type
    def setuser_status(self,user_status):
        self.user_status=user_status
    def setcontact(self,contact):
        self.contact=contact
    def setdob(self,dob):
        self.dob=dob
    def setemail(self,email):
        self.email=email
        
            
        
    def getId(self):
        return self.u_id
    def getName(self):
        return self.name
    def getPassword(self):
        return self.password
    def getuser_type(self):
        return self.user_type
    def getuser_status(self):
        return self.user_status
    def getcontact(self):
        return self.contact
    def getdob(self):
        return self.dob
    def getemail(self):
        return self.email