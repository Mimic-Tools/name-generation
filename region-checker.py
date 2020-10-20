import csv
from os import listdir
from os.path import isfile, join, splitext

# main configuration items
prefix = 'name-segments'
list_of_folders = ['nouns', 'adjectives', 'postfixes']
report_headers = ['Noun', "Adj", "Postfix"]
report_name = "availability_report.html"
csv_name = "availability_report.csv"
check = u'\u2713'
cross = u'\u2715'

print(f"\nBuilding initial list of regions to check for")
report_items = []
report_dictionary = {}

for item in [join(prefix, item) for item in list_of_folders]:
    report_items += [f for f in listdir(item) if isfile(join(item, f)) and f.endswith('.txt')]
report_items = list(set(report_items))

print(f"\nRegion List built. Checking regions for availability:")
for items in report_items:
    report_dictionary[items] = {}
    print(f"Checking for {items} files")
    for item in list_of_folders:
        report_dictionary[items][item] = isfile(join(join(prefix, item), items))

print(f"\nAvailability list created. Outputting report")

html_output = """<html><table border="1"><tr><th>Region</th>"""
csv_output = [['Region'] +  report_headers]
for items in report_headers:
    html_output += "<th>{}</th>".format(items)
html_output += """</tr>"""
for report_item in report_dictionary:
    region = splitext(report_item)[0].capitalize()
    csv_row = [region]
    html_output += "<tr><td>{}</td>".format(region)
    for location in report_dictionary[report_item]: 
        if report_dictionary[report_item][location]:
            html_output += "<td>{}</td>".format(check)
            csv_row += [check]
        else:
            html_output += "<td>{}</td>".format(cross)
            csv_row += [cross]    
    csv_output.append(csv_row)        
    html_output += "</tr>"
html_output += "</table></html>"

csv_file = open(csv_name, 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerows(csv_output)
csv_file.close()

html_file = open(report_name, "w", encoding="utf-8")
html_file.write(html_output)
html_file.close()
print(f"\n.Reports Generated.")