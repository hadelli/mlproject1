import sys 
import logging

def error_message_detail(error, error_detail:sys):

    #sys has exc_info() which returns three values out of which we only want the third one which we are storing in exc_info  
    # exc_info will have info like whic file the exception occured in and which line number etc

    
    _,_,exc_tb = error_detail.exc_info()

    #through exc_tb and its many properties, we can even get the file name
    #you can find this in the custom exception handling documentation for python 
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
       file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message
     

#create a class and call error_message_detail() when exception is encountered 
#inheriting from Exception, so we need to write super.__init__() to override the __init__() function

class CustomException(Exception):
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    #inheriting one more function from Exception to print the error message evrytime 
    def __str__(self):
        return self.error_message
    

    