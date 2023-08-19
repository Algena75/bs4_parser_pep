# outputs.py
import csv
import datetime as dt
import logging

from prettytable import PrettyTable

from constants import BASE_DIR, DATETIME_FORMAT


def control_output(results, cli_args):
    output_options = {
        'pretty': pretty_output,
        'file': file_output
    }
    output = cli_args.output
    if output in output_options.keys():
        output_options[output](results, cli_args)
    else:
        default_output(results)


def default_output(results):
    message = 'Таблица результатов'
    for row in results:
        message = message + '\n' + ' '.join(map(str, row))
        print(*row)
    logging.info(message)


def pretty_output(results, cli_args=None):
    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'l'
    table.add_rows(results[1:])
    logging.info(f'Таблица результатов:\n{table}')
    print(f'Таблица результатов:\n{table}')


def file_output(results, cli_args):
    results_dir = BASE_DIR / 'results'
    results_dir.mkdir(exist_ok=True)
    parser_mode = cli_args.mode
    now = dt.datetime.now()
    now_formatted = now.strftime(DATETIME_FORMAT)
    file_name = f'{parser_mode}_{now_formatted}.csv'
    file_path = results_dir / file_name
    with open(file_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='unix')
        writer.writerows(results)
    logging.info(f'Файл с результатами был сохранен: {file_path}')
