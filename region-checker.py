from os import listdir
from os.path import isfile, join, splitext

# main configuration items
prefix = 'name-segments'
list_of_folders = ['nouns', 'adjectives', 'postfixes']
report_headers = ['Noun', "Adj", "Postfix"]
report_name = "availability_report.html"

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
for items in report_headers:
    html_output += "<th>{}</th>".format(items)
html_output += """</tr>"""
for report_item in report_dictionary:
    html_output += "<tr><td>{}</td>".format(splitext(report_item)[0].capitalize())
    for location in report_dictionary[report_item]:
        if report_dictionary[report_item][location]:
            html_output += "<td>{}</td>".format(u'\u2713')
        else:
            html_output += "<td>X</td>"
    html_output += "</tr>"
html_output += "</table></html>"

html_file = open(report_name, "w", encoding="utf-8")
html_file.write(html_output)
html_file.close()
print(f"\n.Report Generated.")
