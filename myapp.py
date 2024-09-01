from peewee import *
import datetime,hashlib,secrets
db=SqliteDatabase('mydata.db')
SALT="12ewdfer4t43refer4egtr55-3453498098134!2509680mysalt@"
def secure_pass(password:str):
    return hashlib.pbkdf2_hmac('sha256',password.encode(),SALT.encode(),12000).hex()
class Baseclass(Model):
    class Meta:
        database=db
class User(Baseclass):
    username=CharField(primary_key=True,max_length=100)
    password=CharField()
    email=CharField(unique=True,null=True)
    created_at=DateTimeField(default=datetime.datetime.now())
    @classmethod
    def new_user(self,username,password):
        User.create(username=username,password=secure_pass(password))
    @classmethod
    def resetpassword(self,username):
        newpass=secrets.token_hex(16)
        User.update(password=secure_pass(newpass)).where(User.username==username).execute()
        return newpass
class payment(Baseclass):
    id=AutoField()
    method=CharField()
    created_at=DateTimeField(default=datetime.datetime.now())
    amount=IntegerField()
    

db.create_tables([User,payment],safe=True)
