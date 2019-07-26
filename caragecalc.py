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

def GetProcedure(description, data):
    for procedure in data:
        if procedure["desc"] == description:
            return procedure["desc"], procedure["repair"]["repair_hours"], procedure["repair"]["total_cost"], procedure["repair"]["repair_difficulty"]

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
                response = '{"message":{"code":0,"message":"ok","credentials":"valid","version":"v3.0.0","endpoint":"maint","counter":3},"data":[{"desc":"Lube Front Driveshaft U-Joint","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Air Filter","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Change Engine Oil and Filter","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Steering & Suspension Components","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Wheels For End Play & Noise","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect All Fluids and Correct Level","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":2,"repair_hours":0.00,"labor_rate_per_hour":101.44,"part_cost":18.47,"labor_cost":0.00,"misc_cost":0.00,"total_cost":18.47},"parts":[{"desc":"Windshield / Headlight Washer Fluid","manufacturer":"","price":18.47,"qty":1}]},{"desc":"Inspect Cabin Air Filter","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Brake System, Friction Material & Hydraulic System","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect CV Joints & Boots","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Exhaust System","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Horn, Lights, A/C & Heater For Proper Operation","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Rotate Tires, Inspect Tire Wear, & Adjust Tire Pressure","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":2,"repair_hours":0.40,"labor_rate_per_hour":101.44,"part_cost":0.00,"labor_cost":40.57,"misc_cost":25.00,"total_cost":65.57},"parts":"null"},{"desc":"Inspect Battery Performance","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect For Fluid Leaks","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Lubricate Ball Joints, Steering Linkage & U-Joints","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Clutch Pedal Freeplay","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Wiper & Washer System","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":1,"repair_hours":0.00,"labor_rate_per_hour":101.44,"part_cost":18.47,"labor_cost":0.00,"misc_cost":0.00,"total_cost":18.47},"parts":[{"desc":"Windshield / Headlight Washer Fluid","manufacturer":"","price":18.47,"qty":1}]},{"desc":"Inspect Cooling System","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Replace Engine Air Filter","due_mileage":90000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Lube Front Driveshaft U-Joint","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Air Filter","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Change Engine Oil and Filter","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Steering & Suspension Components","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Wheels For End Play & Noise","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect All Fluids and Correct Level","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":2,"repair_hours":0.00,"labor_rate_per_hour":101.44,"part_cost":18.47,"labor_cost":0.00,"misc_cost":0.00,"total_cost":18.47},"parts":[{"desc":"Windshield / Headlight Washer Fluid","manufacturer":"","price":18.47,"qty":1}]},{"desc":"Inspect Cabin Air Filter","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Brake System, Friction Material & Hydraulic System","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect CV Joints & Boots","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Exhaust System","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Horn, Lights, A/C & Heater For Proper Operation","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Rotate Tires, Inspect Tire Wear, & Adjust Tire Pressure","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":2,"repair_hours":0.40,"labor_rate_per_hour":101.44,"part_cost":0.00,"labor_cost":40.57,"misc_cost":25.00,"total_cost":65.57},"parts":"null"},{"desc":"Inspect Battery Performance","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect For Fluid Leaks","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Lubricate Ball Joints, Steering Linkage & U-Joints","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Clutch Pedal Freeplay","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Wiper & Washer System","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":1,"repair_hours":0.00,"labor_rate_per_hour":101.44,"part_cost":18.47,"labor_cost":0.00,"misc_cost":0.00,"total_cost":18.47},"parts":[{"desc":"Windshield / Headlight Washer Fluid","manufacturer":"","price":18.47,"qty":1}]},{"desc":"Inspect Cooling System","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Replace Cabin Filter","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Replace Spark Plugs","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Change Engine Coolant","due_mileage":100000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Lube Front Driveshaft U-Joint","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Air Filter","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Change Engine Oil and Filter","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Steering & Suspension Components","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Wheels For End Play & Noise","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect All Fluids and Correct Level","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":2,"repair_hours":0.00,"labor_rate_per_hour":101.44,"part_cost":18.47,"labor_cost":0.00,"misc_cost":0.00,"total_cost":18.47},"parts":[{"desc":"Windshield / Headlight Washer Fluid","manufacturer":"","price":18.47,"qty":1}]},{"desc":"Inspect Cabin Air Filter","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Brake System, Friction Material & Hydraulic System","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect CV Joints & Boots","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Exhaust System","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Horn, Lights, A/C & Heater For Proper Operation","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Rotate Tires, Inspect Tire Wear, & Adjust Tire Pressure","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":2,"repair_hours":0.40,"labor_rate_per_hour":101.44,"part_cost":0.00,"labor_cost":40.57,"misc_cost":25.00,"total_cost":65.57},"parts":"null"},{"desc":"Inspect Battery Performance","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect For Fluid Leaks","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Lubricate Ball Joints, Steering Linkage & U-Joints","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Clutch Pedal Freeplay","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"},{"desc":"Inspect Wiper & Washer System","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":1,"repair_hours":0.00,"labor_rate_per_hour":101.44,"part_cost":18.47,"labor_cost":0.00,"misc_cost":0.00,"total_cost":18.47},"parts":[{"desc":"Windshield / Headlight Washer Fluid","manufacturer":"","price":18.47,"qty":1}]},{"desc":"Inspect Cooling System","due_mileage":110000,"is_oem":"true","repair":{"repair_difficulty":0,"repair_hours":0.00,"labor_rate_per_hour":0.00,"part_cost":0.00,"labor_cost":0.00,"misc_cost":0.00,"total_cost":0.00},"parts":"null"}]}'
                dict= json.loads(response)

                desc1, brake_time, brake_cost, brake_difficulty = GetProcedure("Inspect Brake System, Friction Material & Hydraulic System", dict["data"])
                desc2, rotate_time, rotate_cost, rotate_difficulty = GetProcedure("Rotate Tires, Inspect Tire Wear, & Adjust Tire Pressure", dict["data"])
                desc3, fluid_time, fluid_cost, fluid_difficulty = GetProcedure("Inspect All Fluids and Correct Level", dict["data"])
                # print("mileage: " + str(oilchange_mileage) + " cost: " + str(oilchange_cost) + " is_oem: " + str(oilchange_difficulty))
                the_variable_dict = {"carAge": Age,

                                    "desc1": desc1,
                                    "time1": brake_time,
                                    # "mileage1": oilchange_mileage,
                                    "cost1": brake_cost,
                                    "difficulty1": brake_difficulty,

                                    "desc2": desc2,
                                    "time2": rotate_time,
                                    # "mileage2": rotate_mileage,
                                    "cost2": rotate_cost,
                                    "difficulty2": rotate_difficulty,

                                    "desc3": desc3,
                                    "time3": fluid_time,
                                    # "mileage2": rotate_mileage,
                                    "cost3": fluid_cost,
                                    "difficulty3": fluid_difficulty,
                                    #NOTE THAT ALWAYS PULLING SMALLEST DUE MILEAGE!!!! Also work out elif for String and Blank, then API Key error page
                                    }
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
