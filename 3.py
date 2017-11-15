#coding : utf-8
import xlwt

data = {
    "1":[u"张三", 150, 120, 100],
    "2":[u"李四", 90, 99, 95],
    "3":[u"王五", 60, 66, 68]
}
wb = xlwt.Workbook()
sheet = wb.add_sheet('A New Sheet', cell_overwrite_ok=True)

row_id = 0;
for key in sorted(data.keys()):
    sheet.write(row_id, 0, key)
    for n in range(4):
        sheet.write(row_id, n+1, data[key][n])
    row_id += 1
wb.save('3.xls')

