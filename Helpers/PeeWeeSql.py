
import peewee
import datetime

helpers_db = peewee.SqliteDatabase('helpers.db') # saved in git .sqlite is ignored

class ConfigTable(peewee.Model):
    cfg_id = peewee.AutoField()
    var = peewee.CharField()
    val = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = helpers_db
        db_table = 'config_values'

print(help(ConfigTable.create_table))
print(dir(ConfigTable.create_table))
ConfigTable.create_table()
q = ConfigTable.create(var='system_creator', val='K00B404')
q.save()
