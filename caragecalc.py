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

# result_template_dictionary = {
#     'line1': 'Test',
#     'line2': 'Testing',
def TestFunction():
     # API = "http://api.carmd.com/v3.0/maint?year=2014&make=FORD&model=FUSION&mileage=100000"
     # # header = {"content-type":"application/json",
     # #            "authorization":"Basic N2Y2NmRiZWMtNDljOS00ODM1LWI0NzQtNDZiZWZkZTY2NDdk",
     # #            "partner-token":"055a7b7f2d774a95acccc35d27c04e69"}
     # Whatever = urlfetch.fetch(url=API, headers=header).content
     # json_response = json.loads(Whatever)
    response = {"message":{"code":0,"message":"ok","credentials":"valid","version":"v3.0.0","endpoint":"maint","counter":3},"data":[{"desc":"Lube Front Driveshaft U-Joint","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Air Filter","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Change Engine Oil and Filter","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Steering & Suspension Components","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Wheels For End Play & Noise","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect All Fluids and Correct Level","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":2,"repair_hours":0.00,"labor_rate_per_hour":101.44,"part_cost":18.47,"labor_cost":0.00,"misc_cost":0.00,"total_cost":18.47},"parts":[{"desc":"Windshield / Headlight Washer Fluid","manufacturer":"","price":18.47,"qty":1}]},{"desc":"Inspect Cabin Air Filter","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Brake System, Friction Material & Hydraulic System","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect CV Joints & Boots","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Exhaust System","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Horn, Lights, A/C & Heater For Proper Operation","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Rotate Tires, Inspect Tire Wear, & Adjust Tire Pressure","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":2,"repair_hours":0.40,"labor_rate_per_hour":101.44,"part_cost":0.00,"labor_cost":40.57,"misc_cost":25.00,"total_cost":65.57},"parts":"null"},{"desc":"Inspect Battery Performance","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect For Fluid Leaks","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Lubricate Ball Joints, Steering Linkage & U-Joints","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Clutch Pedal Freeplay","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Wiper & Washer System","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":1,"repair_hours":0.00,"labor_rate_per_hour":101.44,"part_cost":18.47,"labor_cost":0.00,"misc_cost":0.00,"total_cost":18.47},"parts":[{"desc":"Windshield / Headlight Washer Fluid","manufacturer":"","price":18.47,"qty":1}]},{"desc":"Inspect Cooling System","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Replace Engine Air Filter","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Lube Front Driveshaft U-Joint","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Air Filter","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Change Engine Oil and Filter","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Steering & Suspension Components","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Wheels For End Play & Noise","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect All Fluids and Correct Level","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":2,"repair_hours":0.00,"labor_rate_per_hour":101.44,"part_cost":18.47,"labor_cost":0.00,"misc_cost":0.00,"total_cost":18.47},"parts":[{"desc":"Windshield / Headlight Washer Fluid","manufacturer":"","price":18.47,"qty":1}]},{"desc":"Inspect Cabin Air Filter","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Brake System, Friction Material & Hydraulic System","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect CV Joints & Boots","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Exhaust System","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Horn, Lights, A/C & Heater For Proper Operation","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Rotate Tires, Inspect Tire Wear, & Adjust Tire Pressure","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":2,"repair_hours":0.40,"labor_rate_per_hour":101.44,"part_cost":0.00,"labor_cost":40.57,"misc_cost":25.00,"total_cost":65.57},"parts":"null"},{"desc":"Inspect Battery Performance","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect For Fluid Leaks","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Lubricate Ball Joints, Steering Linkage & U-Joints","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Clutch Pedal Freeplay","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Wiper & Washer System","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":1,"repair_hours":0.00,"labor_rate_per_hour":101.44,"part_cost":18.47,"labor_cost":0.00,"misc_cost":0.00,"total_cost":18.47},"parts":[{"desc":"Windshield / Headlight Washer Fluid","manufacturer":"","price":18.47,"qty":1}]},{"desc":"Inspect Cooling System","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Replace Cabin Filter","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Replace Spark Plugs","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Change Engine Coolant","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Lube Front Driveshaft U-Joint","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Air Filter","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Change Engine Oil and Filter","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Steering & Suspension Components","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Wheels For End Play & Noise","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect All Fluids and Correct Level","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":2,"repair_hours":0.00,"labor_rate_per_hour":101.44,"part_cost":18.47,"labor_cost":0.00,"misc_cost":0.00,"total_cost":18.47},"parts":[{"desc":"Windshield / Headlight Washer Fluid","manufacturer":"","price":18.47,"qty":1}]},{"desc":"Inspect Cabin Air Filter","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Brake System, Friction Material & Hydraulic System","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect CV Joints & Boots","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Exhaust System","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Horn, Lights, A/C & Heater For Proper Operation","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Rotate Tires, Inspect Tire Wear, & Adjust Tire Pressure","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":2,"repair_hours":0.40,"labor_rate_per_hour":101.44,"part_cost":0.00,"labor_cost":40.57,"misc_cost":25.00,"total_cost":65.57},"parts":"null"},{"desc":"Inspect Battery Performance","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect For Fluid Leaks","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Lubricate Ball Joints, Steering Linkage & U-Joints","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Clutch Pedal Freeplay","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Wiper & Washer System","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":1,"repair_hours":0.00,"labor_rate_per_hour":101.44,"part_cost":18.47,"labor_cost":0.00,"misc_cost":0.00,"total_cost":18.47},"parts":[{"desc":"Windshield / Headlight Washer Fluid","manufacturer":"","price":18.47,"qty":1}]},{"desc":"Inspect Cooling System","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"}]}
     # return json_response.data
    dict= json.loads(response)
    print dict.get('data').get('desc')
    # print '"desc":', result['data']['desc']
    #
    # print "-" * 10
    # print "Car Maintenance advice for your vehicle (+- 10,000 mi): "
    # print "-" * 10
    # print dict
    # for info in dict.data:
    #     print info

     # return response.data


class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request

        self.response.write(TestFunction())

        input_template = the_jinja_env.get_template('templates_copy/input.html')
        self.response.write(input_template.render())  # the response
    # def post(self):
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


# #
# TestFunction()
#
# app = webapp2.WSGIApplication([
#     ('/', EnterInfoHandler),
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
