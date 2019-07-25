import webapp2
import jinja2
import os
from timeline_model import timeline_data

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class inputTimeline(webapp2.RequestHandler):
  def get(self):
      timeline_template = jinja_env.get_template("templates/inputTimeline.html")
      self.response.write(timeline_template.render())




class displayTimeline(webapp2.RequestHandler):
    def get(self):
        the_carage = self.request.get("carage")
        the_year = self.request.get("year")
        the_make = self.request.get("Make")
        the_model = self.request.get("Model")

        timeline_input = timeline_data(carAge= the_carage,email="google@google.com", year = the_year, make = the_make, model = the_model).put()
        timeline_input.put()

    def post(self):
        the_carage = self.request.get("carage")
        the_year = self.request.get("Year")
        the_make = self.request.get("Make")
        the_model = self.request.get("Model")
        timeline_input = timeline_data(carAge= the_carage, email="google@google.com", year = the_year, make = the_make, model = the_model).put()
        timeline_entity_list = timeline_data.query().order(timeline_data.carAge).fetch()
        timeline_template = jinja_env.get_template("templates/timeline.html")
        self.response.write(timeline_template.render({'timeline_info' : timeline_entity_list}))
