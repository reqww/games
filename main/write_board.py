def write_table(x):
	line = "<html>\n\t<head>\n"
	line += "\t\t<style type='text/css'>\n"
	line += "\t\t\ttable {\n\t\t\t\twidth: 100px;\n\t\t\t\tborder-collapse: collapse;\n\t\t\t\tborder: 2px solid white;\n\t\t\t}\n"
	line += "\t\t\ttd, th {\n\t\t\t\tpadding: 3px;\n\t\t\t\tborder: 1px solid black;\n\t\t\t\ttext-align: center;\n\t\t\t}\n"
	line += "\t\t</style>\n"
	line += "\t</head>\n\t<body>\n\t\t<table>\n\t\t\t<tbody>\n"
	for arr in x:
		line += "\t\t\t\t<tr>\n"
		for el in arr:
			line += "\t\t\t\t\t<td>"
			if el == 1:
				line += "X"
			elif el == 2:
				line += "O"
			line += "</td>\n"
		line += "\t\t\t\t</tr>\n"
	line += "\t\t\t</tbody>\n\t\t</table>\n\t</body>\n</html>"
	with open("doc.html", "w") as f:
		f.write(line)

	return line
	
x = [
	[2, 2, 2],
	[1, 2, 0],
	[1, 1, 0],
]

write_table(x)