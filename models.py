from google.appengine.ext import ndb

class Log(ndb.Model):
    access_time = ndb.DateTimeProperty(auto_now_add=True)
    ip_address = ndb.StringProperty()
    alarm_id = ndb.StringProperty()
    alarm_status = ndb.StringProperty()
    #alarm_count = ndb.IntegerProperty()
    alarm_count = ndb.StringProperty()

