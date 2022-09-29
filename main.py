import sys
import webbrowser as wb
from engine import portscanner
from engine import config as conf

try:
    if __name__ == '__main__':
        if len(sys.argv) == 1:
            exit(0)

        myip = ''
        try:
            myip = sys.argv[1]
        except:
            exit(0)

        myrange = ''
        try:
            myrange = sys.argv[2]
        except:
            myrange = ''

        myargument = ''
        try:
            myargument = sys.argv[3]
        except:
            myargument = ''

        myps = portscanner.Portscanner(myip, myrange, myargument)
        myps.start()
        try:
            wb.open_new(conf.Config.PATH_PDF)
        except:
            print('An exception occurred while opening %s', conf.Config.PATH_PDF)
except:
    print('An exception occurred while using ' + conf.Config.APP_NAME)
