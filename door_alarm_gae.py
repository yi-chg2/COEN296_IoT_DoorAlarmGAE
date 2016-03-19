import webapp2, jinja2, os, json, urllib, urllib2
from models import Log



JINJA_ENVIRONMENT = jinja2.Environment(
                    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
                    extensions = ['jinja2.ext.autoescape'],
                    autoescape = True)

class DataHandler(webapp2.RequestHandler):
   def post(self):
        # init models object
        custom_index_log = Log()
        custom_index_log.ip_address = self.request.remote_addr
        custom_index_log.alarm_id = self.request.get("SENSOR_ID")
        custom_index_log.alarm_status = self.request.get("SENSOR_STATUS")
        custom_index_log.alarm_count = self.request.get("SENSOR_COUNT")
        custom_index_log.put()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('return successful')
        # store data door alarm
        #if self.request.remote_addr:






# request handler
class MainPage(webapp2.RequestHandler):
    def get(self):

        
        # set template
        template = JINJA_ENVIRONMENT.get_template('index.html')
        
        # get ip addresses of visitors
        ip_logs = Log.query().order(-Log.access_time)
        
        # values to pass to front-end
        template_values = { 'title' : 'COEN296 IoT',
                            'greeting' : 'Door Alarm Demo',
                            'ip_logs' : ip_logs}
                            
        # dispatch template and values to front-end
        self.response.write(template.render(template_values))

# WSGI setting
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/upload_data', DataHandler),
], debug=True)
