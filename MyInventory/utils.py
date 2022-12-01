from django.core.mail import EmailMessage
import xlsxwriter
import jwt
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import os
import datetime

def sendEmail(to,sub,body):
    email = EmailMessage(sub,body,to = ['usamak552@gmail.com','ravikantiwar.21910235@viit.ac.in','rohit.21910004@viit.ac.in'])
    email.send()
    print("email send")

class QuerysetToXLSX:
    def __init__(self,columns,rows,title,token) -> None:
        self.columns = columns
        self.rows = rows
        self.title = title
        self.token = token
        self.sk = "dfv"
    
    def __decode(self):
        try:
            decoded=jwt.decode(self.token,'export','HS256')
            return False
        except jwt.ExpiredSignatureError:
            return True

    @property
    def convert(self):
        if self.__decode():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        self.rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in self.rows]
        wb = xlsxwriter.Workbook(self.title+'.xlsx')
        ws = wb.add_worksheet(self.title)
        row_num = 0
        font_style = wb.add_format({'bold': True})
        for col_num in range(len(self.columns)):
            ws.write(row_num, col_num, self.columns[col_num], font_style)
        for row in self.rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        wb.close()
        response = HttpResponse(open(self.title+'.xlsx', "rb"),content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}.xlsx"'.format(self.title)
        if os.path.exists(self.title+'.xlsx'):
            os.remove(self.title+'.xlsx')
        return response

