# sys provides various function and vars that are used to manipulate
# different parts of the Python runtime env
import sys
from src.logger import logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # execution info bout lines exceptions occur
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
    
        return self.error_message

if __name__=="__main__":
    try:
        result = 1 / 0  # Deliberate error: Division by zero
    except Exception as e:
        logging.error("An exception occurred!")
        raise CustomException("An error occurred while performing division", sys)


        
