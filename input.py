import webapp2
import logging
import urllib
# [START urllib2-imports]
import urllib2
from google.appengine.api import urlfetch
import json
import jinja2
import os


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# result_template_dictionary = {
#     'line1': 'Test',
#     'line2': 'Testing',


class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        input_template = the_jinja_env.get_template('templates_copy/input.html')
        self.response.write(input_template.render())  # the response
    def post(self):
        self.response.write("Ooof")

class ShowInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates_copy/input.html')
        self.response.write(welcome_template.render())
    def post(self):
        results_template = the_jinja_env.get_template('templates_copy/output.html')
        Age = (float(self.request.get("Mileage"))/200000)*80.3
        # FIND A WAY TO DISPLAY AS YEARS/MONTHS/DAYS/HOURS/MINUTES/SECONDS

        Year = self.request.get("Year")
        # pic_url = get_meme_url(meme_img_choice)

        the_variable_dict = {"carAge": Age,
                                "year": Year,}
                             # "img_url": pic_url
        self.response.write(results_template.render(the_variable_dict))




# buried code:
    # if Age <= 1:
    #     info_dict = {"info": "Katie"}
    #     self.response.write(results_template.render(info_dict))
    #
    #     # Infancy
    # elif Age <= 8:
    #     self.response.write(results_template.render(info_dict))
    #
    #     # Childhood
    # elif Age <= 13:
    #     self.response.write(results_template.render(info_dict))
    #
    #     # Puberty
    # elif Age <= 18:
    #     self.response.write(results_template.render(info_dict))
    #
    #     # Adolescence
    # elif Age <= 31:
    #     the_variable_dict.update(info = 'Katie')
    #
    #
    #     # Adulthood
    # elif Age <= 50:
    #     self.response.write(results_template.render(info_dict))
    #
    #     # Middle Age
    # else:
    #     self.response.write(results_template.render(info_dict))
    #     #
    #     # Old Age
    #
    #     def Merge(the_variable_dict, info_dict):
    #         return(info_dict.update(the_variable_dict))
