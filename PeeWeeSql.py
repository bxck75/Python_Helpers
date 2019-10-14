from functools import partial
from peewee import *
DATABASE='Youstupid.sqlbitch'


# db = peewee.PostgresqlDatabase(DATABASE)

# class BaseModel(Model):
#     class Meta:
#         database = db

# class Member(BaseModel):
#     memid = AutoField()  # Auto-incrementing primary key.
#     surname = CharField()
#     firstname = CharField()
#     address = CharField(max_length=300)
#     zipcode = IntegerField()
#     telephone = CharField()
#     recommendedby = ForeignKeyField('self', backref='recommended',
#                                     column_name='recommendedby', null=True)
#     joindate = DateTimeField()
#     class Meta:
#         table_name = 'members'

# class Facility(BaseModel):
#     facid = AutoField()
#     name = CharField()
#     membercost = MoneyField()
#     guestcost = MoneyField()
#     initialoutlay = MoneyField()
#     monthlymaintenance = MoneyField()
#     class Meta:
#         table_name = 'facilities'

# class Booking(BaseModel):
#     bookid = AutoField()
#     facility = ForeignKeyField(Facility, column_name='facid')
#     member = ForeignKeyField(Member, column_name='memid')
#     starttime = DateTimeField()
#     slots = IntegerField()
#     class Meta:
#         table_name = 'bookings'



# create a peewee database instance -- our models will use this database to
# persist information
database = SqliteDatabase(DATABASE)

# model definitions -- the standard "pattern" is to define a base model class
# that specifies which database to use.  then, any subclasses will automatically
# use the correct storage.
class BaseModel(Model):
    class Meta:
        database = database

# the user model specifies its fields (or columns) declaratively, like django
class Config(BaseModel):
    uid = AutoField()
    name = CharField(unique=True)
    value = CharField()
    info = CharField()
    date = DateTimeField()
    class Meta:  
        table_name = 'core_settings'

# # this model contains two foreign keys to user -- it essentially allows us to
# # model a "many-to-many" relationship between users.  by querying and joining
# # on different columns we can expose who a user is "related to" and who is
# # "related to" a given user
# class Relationship(BaseModel):
#     rid = AutoField()
#     from_user = ForeignKeyField(User, backref='relationships')
#     to_user = ForeignKeyField(User, backref='related_to')
#     class Meta:
#         # `indexes` is a tuple of 2-tuples, where the 2-tuples are
#         # a tuple of column names to index and a boolean indicating
#         # whether the index is unique or not.
#         indexes = (
#             # Specify a unique multi-column index on from/to-user.
#             (('from_user', 'to_user'), True),
#         )

# # a dead simple one-to-many relationship: one user has 0..n messages, exposed by
# # the foreign key.  because we didn't specify, a users messages will be accessible
# # as a special attribute, User.messages
# class Message(BaseModel):
#     user = ForeignKeyField(User, backref='messages')
#     content = TextField()
#     pub_date = DateTimeField()