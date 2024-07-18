import sys
import logging

def error_message_detail(error,error_details:sys):
    __,__,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occoured in python script name[{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineo,str(error))


    return error_message
    

class customexception(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details=error_details)


    def __str__(self) :
        return self.error_message
    
# if __name__=="__main__":
#     try:
#         a=1/10
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise customexception(e,sys)
