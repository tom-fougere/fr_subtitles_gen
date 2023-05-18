import re
import pandas as pd

COLUMNS_NAME = {
    'id': 'id',
    'start_time': 'start_time',
    'end_time': 'end_time',
    'sentence': 'sentence',
}


def read_srt(srt_file_path):

    # Read file
    with open(srt_file_path, 'r') as f:
        srt_data = f.read()

    # Parse data
    srt_regex = r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.+?(?=\n\d|$))'
    srt_matches = re.findall(srt_regex, srt_data, re.DOTALL)

    # Extract each data
    srt_data_list = [(int(m[0]), m[1], m[2], m[3].replace('\n', ' ').strip()) for m in srt_matches]

    return pd.DataFrame(srt_data_list, columns=list(COLUMNS_NAME.values()))


def write_srt_file(df, column_name_sentence, output_file_path):
    with open(output_file_path, 'w') as f:
        for index, row in df.iterrows():

            # Build each line
            f.write(str(row[COLUMNS_NAME['id']]) + '\n')
            f.write(row[COLUMNS_NAME['start_time']] + ' --> ' + row[COLUMNS_NAME['end_time']] + '\n')
            f.write(row[column_name_sentence].strip() + '\n\n')
