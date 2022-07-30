from openpyxl import load_workbook
from flask import Flask
import pandas as pd
from flask_restful import Resource, Api

wb = load_workbook("jobs.xlsx")

app = Flask(__name__)
api = Api(app)

class Results(Resource):
    def get(self):
        data = pd.read_excel("jobs.xlsx")
        data = data.to_dict()
        return {"Results": data}, 200 

api.add_resource(Results, "/Results")

app.run()