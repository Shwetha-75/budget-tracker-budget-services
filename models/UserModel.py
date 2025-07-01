class User:
    def __init__(self,first_name,last_name,phone,gender,password,confirm_password,mail):
        
        self.first_name=first_name 
        self.last_name=last_name
        self.mail=mail
        self.phone=phone 
        self.gender=gender
        self.password=password
        self.confirm_password=confirm_password 
        self.salary=None 
        self.expenditure=None 
        self.savings=None 
        self.expenses=None 
        self.expense_amt=None
        
    def set_first_name(self,first_name):
        self.first_name=first_name 
    def set_last_name(self,last_name):
        self.last_name=last_name
    def set_mail(self,mail):
        self.mail=mail 
    def set_phone(self,phone):
        self.phone=phone
    def set_gender(self,gender):
        self.gender=gender 
    def set_password(self,password):
        self.password=password
    def set_confirm_password(self,confirm_password):
        self.confirm_password=confirm_password 
    def set_salary(self,salary):
        self.salary=salary
    def set_expenditure(self,expenditure):
        self.expenditure=expenditure
    def set_savings(self,savings):
        self.savings=savings
    def set_expenses(self,expenses):
        self.expenses=expenses
    def set_expense_amt(self,expense_amt):
        self.expense_amt=expense_amt
    # --------------------------------------
    def get_first_name(self):
        return self.first_name 
    def get_last_name(self):
        return self.last_name
    def get_mail(self):
        return self.mail
    def get_phone(self):
        return self.phone
    def get_gender(self):
        return self.gender
    def get_password(self):
        return self.password
    def get_confirm_password(self):
        return self.confirm_password
    def get_salary(self):
        return self.salary 
    def get_expenditure(self):
        return self.expenditure 
    def get_savings(self):
        return self.savings 
    def get_expenses(self):
        return self.expenses
    def get_expense_amt(self):
        return self.expense_amt
    
    def __str__(self):
        return {'first_name':self.get_first_name(),
                'last_name':self.get_last_name(),
                'phone':self.get_phone(),
                'gender':self.get_gender(),
                'password':self.get_password(),
                'confirm_password':self.get_confirm_password(),
                'mail':self.get_mail(),
                'expenditure':self.get_expenditure(),
                'salary':self.get_salary(),
                'savings':self.get_savings(),
                'expenses':self.get_expenses(),
                'expense_amt':self.get_expense_amt()
                }
    