import sys
import logging

def error_message_detail(error: Exception) -> str:
    '''returns the line of code where error has occured.'''

    _, _, exc_tb = sys.exc_info()

#Shows file name where error occured
    filename = exc_tb.tb_frame.f_code.co_filename

    line_number = exc_tb.tb_lineno

    error_message = f"The error occured in python script [{filename}] at line number [{line_number}]: {str(error)}"

    logging.error(error_message)

    return error_message

class MyException(Exception):
    def __init__(self,error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
