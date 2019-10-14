from functools import partial
from peewee import *
DATABASE='HelpersDB.sqlite'
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
class ConfigTable(BaseModel):
    uid = AutoField()
    var = CharField(unique=True)
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






# from peewee import SqliteDatabase
# from playhouse.reflection import generate_models, print_model, print_table_sql



# from peewee import *

# #!/usr/bin/env python3

# import peewee
# import datetime

# db = peewee.SqliteDatabase('test.db')

# class Note(peewee.Model):

#     text = peewee.CharField()
#     created = peewee.DateField(default=datetime.date.today)

#     class Meta:

#         database = db
#         db_table = 'notes'


# Note.create_table()
# note1 = Note.create(text='Went to the cinema')
# note1.save()
# note2 = Note.create(text='Exercised in the morning',
#         created=datetime.date(2018, 10, 20))
# note2.save()
# note3 = Note.create(text='Worked in the garden',
#         created=datetime.date(2018, 10, 22))
# note3.save()
# note4 = Note.create(text='Listened to music')
# note4.save()
# note1 = Note.create(text='Went to the cinema')
# note1.save()


# from functools import partial
# from peewee import *


# db = PostgresqlDatabase('peewee_test')

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


# # Conveniently declare decimal fields suitable for storing currency.
# MoneyField = partial(DecimalField, decimal_places=2)


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






