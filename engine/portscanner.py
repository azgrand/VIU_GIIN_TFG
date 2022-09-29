import nmap
from engine import report
from engine import config as conf


class Portscanner:

    def __init__(self, myip, myrange, myargument):
        self.MY_IP = myip
        self.MY_RANGE = myrange
        self.MY_ARGUMENT = myargument

    def start(self):
        conf.Config().clean()
        self.__scan()

    def __print(self):
        rp = report.Report()
        rp.create_report()

    def __scan(self):
        myscan = nmap.PortScanner()
        if len(self.MY_IP) != 0 and len(self.MY_RANGE) != 0 and len(self.MY_ARGUMENT) != 0:
            myscan.scan(self.MY_IP, self.MY_RANGE, self.MY_ARGUMENT)
        elif len(self.MY_IP) != 0 and len(self.MY_RANGE) != 0:
            myscan.scan(self.MY_IP, self.MY_RANGE)
        else:
            myscan.scan(self.MY_IP)
        try:
            print(myscan.csv(), file=open(conf.Config.PATH_CSV, 'w'))
        except():
            print('An exception occurred while writting %s', conf.Config.PATH_CSV)
        self.__print()
