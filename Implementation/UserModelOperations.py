class UserModelOperations:
        def __init__(self,cursor):
            self.cursor=cursor
        def getTheData(self,email:str):
            return self.cursor.collection('user_model_table').document(email).get().to_dict()
            
            