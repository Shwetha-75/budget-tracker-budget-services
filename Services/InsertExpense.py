from flask import jsonify
import requests
class CreateExpenseTag:

      def insertExpense(self,data):
          expenses=data['expense'] 
          new_expense_amt=float(expenses['value']) 
          expense_amt= float(data['expense_amt']) if data['expense_amt'] else 0 +new_expense_amt
          savings=float(data['savings']) if data['savings'] else 0 -new_expense_amt   
          userData={
            'savings':savings,
            'expense':expenses,
            'expense_amt':expense_amt,
            'mail':data['mail']
          }
          requests.post("http://localhost:7006/insert-expense",json=userData)
          return jsonify({"user_model":userData})
          