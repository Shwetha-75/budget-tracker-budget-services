
class UserModelDisplay:
      def __init__(self,currentUser):
        self.currentUser=currentUser 
      def methodUserObject(self):
            
            model={
                  'first_name':self.currentUser['first_name'],
                  'last_name':self.currentUser['last_name'],
                  'phone':self.currentUser['phone'],
                  'gender':self.currentUser['gender'],
                  'mail':self.currentUser['mail'],
                  'expenditure':self.currentUser['expenditure'],
                  'salary':self.currentUser['salary'],
                  'savings':self.currentUser['savings'],
                  'expense_amt':self.currentUser['expense_amt']
            }
         
            return model 