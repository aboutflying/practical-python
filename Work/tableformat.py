class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        th = ''
        for h in headers:
            th += f'<th>{h}</th>'
        print(f'<tr>{th}</tr>')

    def row(self, rowdata):
        td = ''
        for d in rowdata:
            td += f'<td>{d}</td>'
        print(f'<tr>{td}</tr>')  

class FormatError(Exception):
    pass

def create_formatter(name):
    if name == 'txt':
        formatter = TextTableFormatter()
    elif name == 'csv':
        formatter = CSVTableFormatter()
    elif name == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format: {name}')

    return formatter

def print_table(obj, cols, formatter):
    formatter.headings(cols)
    for o in obj:
        rowdata = [ str(getattr(o, colname)) for colname in cols ]
        formatter.row(rowdata)