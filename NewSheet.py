from openpyxl import Workbook

name = 	'Polystichum glaciale_2018-08-30_5'

####before run wb = load_workbook('D:\\ZGFSft\\Environment\\NSII\\GetResults\\' + name + '.xlsx')
wb = Workbook()
sheet = wb['Sheet']
row = ['science_name','chinese_name','collector','collector_num','collector_date','collector_loc','GUID','herbarium','provider','url','image_path']
sheet.append(row)
wb.save('D:\\ZGFSft\\Environment\\NSII\\GetResults\\' + name + '.xlsx')