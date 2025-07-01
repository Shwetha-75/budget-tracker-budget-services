from flask import Flask,request,jsonify
import os
from flask_cors import CORS
from dotenv import load_dotenv
from flask_socketio import SocketIO, emit
from Services.InsertExpense import CreateExpenseTag
from Services.UpdateSalary import UpdateSalary


load_dotenv()
app=Flask(__name__)
# enabling the CORS 
CORS(app,supports_credentials=True, origins={r"/*":{"origins":[]}})
socketio = SocketIO(app, cors_allowed_origins=os.getenv('FRONT_END'))

# CRUD operations 
# creating an expense 
@app.route("/create",methods=['POST','GET'])
def create():
    # implementation 
    if request.method == 'POST':
       data=request.json
       print(data)
       return CreateExpenseTag().insertExpense(data)
    return "creating.."

@app.route("/delete",methods=['POST','GET'])
def delete():
    return "Deleting..."

@app.route("/update",methods=['POST','GET'])
def update():
    
    
    return "Updating....."

@app.route("/")
def index():
    
    return "ok"

# Update Salary 
@app.route("/update-salary",methods=['POST','GET'])
def salaryUpdate():
    if request.method=='POST':
       result=UpdateSalary().updateSalary(request.json)
       return jsonify({"data_model":result})
   
@app.route("/delete-expense",methods=['POST','GET'])
def deleteExpense():
    if request.method=='POST':
        data=request.get_json()
        pass
              
if __name__=="__main__":
  app.run(host='0.0.0.0',   port=os.getenv('PORT'),debug=True)
  