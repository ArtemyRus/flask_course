def human_size(size):
    units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ', 'ПБ']
    for unit in units:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024

def get_summary_rss(ps_output_file_path: str) -> str:
    summary_rss = 0
    with open(ps_output_file_path, "r") as file:
        lines = file.readlines()[1:]
        for line in lines:
            columns = line.split()
            try:
                rss = int(columns[5])
                summary_rss += rss
            except Exception as ex:
                continue
    return human_size(summary_rss)

file_path = './output_file.txt'

if __name__ == '__main__':
    path: str = file_path
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)