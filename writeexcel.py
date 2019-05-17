import xlsxwriter

# # # # Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('sample3.xlsx')

worksheet = workbook.add_worksheet()

# # with xlsxwriter.Workbook('/home/sanjeeva/Pictures/demo.xlsx') as file:
# # 	# pass

# # # # Write some simple text.
# worksheet.write('B2', 'Hello')

# # # # # Text with formatting.
# worksheet.write('A2', 'World')

# worksheet.write(3,4,'python')

# # Write some numbers, with row/column notation.
a=[1]
b=["sanje","ttettyeer","eyyrgr"]
for i in a:
	for j in range(len(b)):
		worksheet.append(i, j, b[j])
	


# #if its not create file we will use other method

# workbook.save("filename")

# # print("success")

# workbook.close()

# help(xlsxwriter.worksheet)


# xampp server
# 





















# encoding="utf-8"