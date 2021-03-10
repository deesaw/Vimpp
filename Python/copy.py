from openpyxl import Workbook
wb = Workbook()
ws = wb.active
f=open('marks.csv','r')
f1=open('marks.xlsx','w')
for line in f:
     ws.append(line.split(","))
wb.save('marks.xlsx')
f1.close
f.close()