import csv
from os import listdir
from os.path import isfile, join, splitext

# main configuration items
prefix = 'name-segments'
check = u'\u2713'
cross = u'\u2715'

def get_report_rows(search_folders):
    report_items = []

    for item in [join(prefix, item) for item in search_folders]:
        report_items += [f for f in listdir(item) if isfile(join(item, f)) and f.endswith('.txt')]
    report_items = list(set(report_items))
    return report_items

def find_availability(search_folder, rows):
    report_dictionary = {}
    for items in rows:
        report_dictionary[items] = {}
        print(f"Checking for {items} files")
        for item in list_of_folders:
            report_dictionary[items][item] = isfile(join(join(prefix, item), items))
    return report_dictionary

def generate_reports(entries, title="Region", name="availability_report"):
    report_name = f"{name}.html"
    csv_name = f"{name}.csv"

    report_headers = ['Noun', "Adj", "Postfix"]
    html_output = f"""<html><table border="1"><tr><th>{title}</th>"""
    csv_output = [[f'{title}'] +  report_headers]
    for items in report_headers:
        html_output += f"<th>{items}</th>"
    html_output += """</tr>"""
    for report_item in entries:
        region = splitext(report_item)[0].capitalize()
        csv_row = [region]
        html_output += f"<tr><td>{region}</td>"
        for location in entries[report_item]: 
            if entries[report_item][location]:
                html_output += f"<td>{check}</td>"
                csv_row += [check]
            else:
                html_output += f"<td>{cross}</td>"
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

if __name__ == "__main__":
    list_of_folders = ['nouns', 'adjectives', 'postfixes']
    rows = get_report_rows(list_of_folders)
    d = find_availability(list_of_folders, rows)
    generate_reports(d)
