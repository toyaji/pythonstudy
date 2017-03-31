# csv 구분자가 많아서 자신한테 맞도록 방언 설정해서 활용할 수 있음
import csv
from os.path import expanduser


class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL

if __name__ == '__main__':
    f = expanduser()
    reader = csv.reader(f, dialect=my_dialect)