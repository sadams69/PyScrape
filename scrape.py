from bs4 import BeautifulSoup
import urllib2

sheets = {'balance': 'balance_sheet', 'income': 'income_statement', 'cash' : 'cash_flow'}

for akey in sheets.keys():
    url = 'http://www.motleyfool.idmanagedsolutions.com/stocks/%s.idms?SYMBOL_US=IBM&TIME=ANNUAL)' % sheets[akey]

    soup = BeautifulSoup(urllib2.urlopen(url).read())

    a = soup('tr')

    sheet = {}
    for index in range(0,len(soup('tr'))):
        if (a[index]('td')): # As long as there is something inside, get it
            if (index==0):
                field = a[index]['class'][0]
                values = [a[index]('td')[ii].get_text() for ii in range(1,5)]
            
            else:
                field = a[index]('td')[0].get_text()
                values = []
                for ii in range(1,5):
                    aa = a[index]('td')[ii].get_text()
                    aa = aa.replace(',','')  # Get rid of commas
                    aa = aa.replace('(','-') # Get rid of parentheses that indicate negative
                    aa = aa.replace(')','')
                    values.append(float(aa))

                    field = field.encode("utf-8")
                    print index, field, values
                    sheet[field] = values
    
                
    sheets[akey] = sheet




