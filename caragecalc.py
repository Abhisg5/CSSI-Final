import webapp2
import logging
from google.appengine.api import urlfetch
import json
import jinja2
import os
# from api import CarmdApi
# api = CarmdApi()

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape="true")


class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        input_template = the_jinja_env.get_template('templates/input.html')
        self.response.write(input_template.render())  # the response
    # def post(self):
        self.response.write("Ooof")
    def post(self):  # for a get request
        input_template = the_jinja_env.get_template('templates/input.html')
        self.response.write(input_template.render())  # the response
    # def post(self):

class ShowInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/input.html')
        self.response.write(welcome_template.render())
    def post(self):
        results_template = the_jinja_env.get_template('templates/output.html')
        try:
            if float(self.request.get("Mileage")).is_integer() is True:
                Age = (float(self.request.get("Mileage"))/200000)*80.3
                # FIND A WAY TO DISPLAY AS YEARS/MONTHS/DAYS/HOURS/MINUTES/SECONDS
                Year = self.request.get("Year")
                # pic_url = get_meme_url(meme_img_choice)

                the_variable_dict = {"carAge": Age,
                                        "year": Year,}
                # "img_url": pic_url
                self.response.write(results_template.render(the_variable_dict))
        except:
            self.response.write('''
                Please input an integer value!
                <p> Click below to Calculate the Age of your Car! </p>
                  <form method="post" action="/enter-info">
                    <input type="submit" value="Go!">
                    </input>
                  </form>''')


            the_variable_dict = {"carAge": Age,
                                        "year": Year,}
                # "img_url": pic_url
            self.response.write(results_template.render(the_variable_dict))

# TestFunction()
#
# app = webapp2.WSGIApplication([
#     ('/EnterInfo', EnterInfoHandler),
#     ('/carResult', ShowInfoHandler),
# ], debug="true")

#
# # buried code:
#     # if Age <= 1:
#     #     info_dict = {"info": "Katie"}
#     #     self.response.write(results_template.render(info_dict))
#     #
#     #     # Infancy
#     # elif Age <= 8:
#     #     self.response.write(results_template.render(info_dict))
#     #
#     #     # Childhood
#     # elif Age <= 13:
#     #     self.response.write(results_template.render(info_dict))
#     #
#     #     # Puberty
#     # elif Age <= 18:
#     #     self.response.write(results_template.render(info_dict))
#     #
#     #     # Adolescence
#     # elif Age <= 31:
#     #     the_variable_dict.update(info = 'Katie')
#     #
#     #
#     #     # Adulthood
#     # elif Age <= 50:
#     #     self.response.write(results_template.render(info_dict))
#     #
#     #     # Middle Age
#     # else:
#     #     self.response.write(results_template.render(info_dict))
#     #     #
#     #     # Old Age
#     #
#     #     def Merge(the_variable_dict, info_dict):
#     #         return(info_dict.update(the_variable_dict))
