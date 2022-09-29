import pandas as pd
import weasyprint as wp
from airium import Airium
from engine import config as conf
from datetime import datetime as dt


class Report:

    def create_report(self):
        df = pd.read_csv(conf.Config.PATH_CSV, sep=';')
        df.fillna('', inplace=True)
        self.__improve_report(df)
        try:
            wp.HTML(conf.Config.PATH_HTML).write_pdf(conf.Config.PATH_PDF)
        except():
            print('An exception occurred while writting %s', conf.Config.PATH_PDF)
        conf.Config().clean()

    def __improve_report(self, df):
        a = Airium()
        a('<!DOCTYPE html>')
        with a.html(lang='es-ES'):
            with a.head():
                a.meta(charset='utf-8')
                a.title(_t=conf.Config.APP_NAME)
            with a.style():
                a('h1, h2 {text-align:center;}')
                a('h3 {text-align:right;}')
                a('h4 {padding: 0.3em; color: #fff; background: #000;}')
                a('table {width: 100%;border: 1px solid #000;}')
                a('th, td {width: 25%; text-align: left; vertical-align: top;border: 1px solid #000; border-collapse: collapse;padding: 0.3em; caption-side: bottom;}')
                a('caption {padding: 0.3em; color: #fff; background: #000;}')
                a('th {background: #eee;}')
                a('footer {margin-top: 15px; text-align: center; font-size: 13px; color: #aaa; margin-bottom:0;}')
            with a.body():
                with a.h1():
                    a(conf.Config.APP_NAME + ' report scan')
                a.br()
                with a.h2():
                    row = next(df.iterrows())[1]
                    a('Host: ' + str(row['host']) + ' (' + str(row['hostname']) + ')')
                a.br()
                with a.h3():
                    a('Scan date: ' + dt.now().strftime('%Y') + '/' + dt.now().strftime('%m') + '/' + dt.now().strftime('%d'))
                a.br()
                for index, rows in df.iterrows():
                    with a.h4():
                        a('Port: ' + str(rows['port']) + ' Protocol: ' + str(rows['protocol']))
                    with a.table():
                        with a.tr():
                            a.th(_t='Name')
                            a.th(_t='State')
                            a.th(_t='Reason')
                        with a.tr():
                            a.td(_t=str(rows['name']))
                            a.td(_t=str(rows['state']))
                            a.td(_t=str(rows['reason']))
                        with a.tr():
                            a.th(_t='Product')
                            a.th(_t='Conf')
                            a.th(_t='Version')
                        with a.tr():
                            a.td(_t=str(rows['product']))
                            a.td(_t=str(rows['conf']))
                            a.td(_t=str(rows['version']))
                        with a.tr():
                            a.th(_t='CPE')
                            a.th(_t='Extrainfo')
                        with a.tr():
                            a.td(_t=str(rows['cpe']))
                            a.td(_t=str(rows['extrainfo']))
                    a.br()
                with a.footer():
                    a.br()
                    a('<p>' + conf.Config.APP_NAME + ' © ' + dt.now().strftime('%Y') + '</p>')
                    a('<p>This application is for educational use only. Use it at your own risk.</p>')
        html = str(a)
        try:
            with open(conf.Config.PATH_HTML, 'wb') as f:
                f.write(bytes(html, encoding='utf8'))
        except():
            print('An exception occurred while writting %s', conf.Config.PATH_HTML)
