from cli_main import *
try:
	os.environ['HELPERS_STATE'] = '0'
	if sys.argv[1] == 'new':
		os.environ['HELPERS_STATE'] = '1'
		someVariable = int(os.environ['state'])
		print(os.environ)	
except:
	pass
this_env = str(os.environ).replace('[','').replace(']','').split(',')
# this_env.sort()
pprint(this_env)
pprint(dir(main.high_core))
# init the core
# import os
# os.environ['DEBUSSY'] = '1'
# os.environ['FSDB'] = '1'
# # Open child processes via os.system(), popen() or fork() and execv()
# someVariable = int(os.environ['DEBUSSY'])
>>> from peewee import SqliteDatabase
>>> from playhouse.reflection import generate_models, print_model, print_table_sql
>>>


from peewee import *

#!/usr/bin/env python3

import peewee
import datetime

db = peewee.SqliteDatabase('test.db')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:

        database = db
        db_table = 'notes'


Note.create_table()
note1 = Note.create(text='Went to the cinema')
note1.save()
note2 = Note.create(text='Exercised in the morning',
        created=datetime.date(2018, 10, 20))
note2.save()
note3 = Note.create(text='Worked in the garden',
        created=datetime.date(2018, 10, 22))
note3.save()
note4 = Note.create(text='Listened to music')
note4.save()
note1 = Note.create(text='Went to the cinema')
note1.save()


from functools import partial
from peewee import *


db = PostgresqlDatabase('peewee_test')

class BaseModel(Model):
    class Meta:
        database = db

class Member(BaseModel):
    memid = AutoField()  # Auto-incrementing primary key.
    surname = CharField()
    firstname = CharField()
    address = CharField(max_length=300)
    zipcode = IntegerField()
    telephone = CharField()
    recommendedby = ForeignKeyField('self', backref='recommended',
                                    column_name='recommendedby', null=True)
    joindate = DateTimeField()

    class Meta:
        table_name = 'members'


# Conveniently declare decimal fields suitable for storing currency.
MoneyField = partial(DecimalField, decimal_places=2)


class Facility(BaseModel):
    facid = AutoField()
    name = CharField()
    membercost = MoneyField()
    guestcost = MoneyField()
    initialoutlay = MoneyField()
    monthlymaintenance = MoneyField()

    class Meta:
        table_name = 'facilities'


class Booking(BaseModel):
    bookid = AutoField()
    facility = ForeignKeyField(Facility, column_name='facid')
    member = ForeignKeyField(Member, column_name='memid')
    starttime = DateTimeField()
    slots = IntegerField()

    class Meta:
        table_name = 'bookings'











# core.get_detector_stuff(core) 

# print(detect_model_locs)
''' ############################################################################################ '''
# core.pix2pix(self, dataset_path, images_set_name, epochs=2, loops=2, mode='train', first_run=True)
''' ############################################################################################ '''





# print(dir(main))
# print(main.main_root)
# print(main.get_project_root())