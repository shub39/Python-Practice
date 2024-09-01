import os

def generate_markdown_table(base_folder, output_file):
    days = sorted([d for d in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, d))])
    
    files_by_day = {}
    for day in days:
        files = sorted(os.listdir(os.path.join(base_folder, day)))
        files_by_day[day] = files
    
    max_files = max(len(files) for files in files_by_day.values())
    
    header = "| " + " | ".join(days) + " |"
    divider = "| " + " | ".join(["---------" for _ in days]) + " |"
    rows = []
    
    for i in range(max_files):
        row = []
        for day in days:
            files = files_by_day[day]
            if i < len(files):
                file_link = f"[{files[i]}]({base_folder}/{day}/{files[i]})"
            else:
                file_link = ""
            row.append(file_link)
        
        rows.append("| " + " | ".join(row) + " |")
    
    with open(output_file, 'w') as f:
        f.write(header + "\n")
        f.write(divider + "\n")
        for row in rows:
            f.write(row + "\n")

generate_markdown_table('PCC-DS-391', 'output_table.txt')