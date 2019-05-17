import xlrd
# # # #open
book=xlrd.open_workbook("sample1.xlsx")
# # # #open sheet with name
sheet=book.sheet_by_name('Sheet1')
# # # # # open with index
# sheet=book.sheet_by_index(0)
# # # #get value of particular cell
# print(sheet.cell_value(6,6))
# print("get value of  row and  colums as {}".format(sheet.cell_value(3,1)))
# # # # #no.of sheets
# num_sheets=book.nsheets
# print(num_sheets)
# # # # #name of sheet
name_sheets=book.sheet_names()
# print(name_sheets)
# # # # #row and colummn count
sheet_row=sheet.nrows
sheet_col=sheet.ncols
# print(sheet_col)
# print(sheet_row)

# for j in range(sheet_row):
# 	for k in range(sheet_col):
# 		print(sheet.cell_value(j,k))
# 	print("-------------"+str(j)+" row data--------------------")

# # for priniting row values and column values at a time
# print(sheet.row_values(4))
print(sheet.col_values(6))



