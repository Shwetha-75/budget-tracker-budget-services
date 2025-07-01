import requests
from flask import json 
class UpdateSalary:
    
      def updateSalary(self,data):
          total=0
          if data['expense']:
            data['expense']=json.loads(data['expense'])
            
            for value in data['expense']:
                total+=float(value['value'])
          new_salary=float(data['salary'])
          savings=new_salary-total 
          updated_data={
              "savings":str(savings),
              "salary":data['salary'],
              'email':data['email']
          }
          requests.post("http://localhost:7006/update",json=updated_data)
          return updated_data
      
      