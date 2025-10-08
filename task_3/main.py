import sys
from collections import defaultdict


def parse_log_line(line: str) -> dict[str, str]:
    parts_log_entry = line.split(" ", 3)
    if len(parts_log_entry) < 4:
        print(f"Помилка розбору рядка логу: '{line}'.")
        sys.exit(1)
    return {
        "date": parts_log_entry[0],
        "time": parts_log_entry[1],
        "level": parts_log_entry[2],
        "message": parts_log_entry[3]
    }


def load_logs(file_path: str) -> list[dict[str, str]]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [parse_log_line(line.strip()) for line in file]
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу '{file_path}': {e}")
        sys.exit(1)


def filter_logs_by_level(logs: list[dict[str, str]], level: str) -> list[dict[str, str]]:
    normalized_level = level.lower()
    return [log_entry for log_entry in logs if log_entry['level'].lower() == normalized_level]


def count_logs_by_level(logs: list[dict[str, str]]) -> dict[str, int]:
    result = defaultdict(int)
    for log_entry in logs:
        result[log_entry['level']] += 1
    return dict(result)


def display_log_counts(counts: dict[str, int]):
    print("Рівень логування | Кількість")
    print("-----------------+----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def display_log_details(logs: list[dict[str, str]], level_filter: str):
    filtered_logs = filter_logs_by_level(logs, level_filter)
    print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
    for log in filtered_logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def check_args():
    if len(sys.argv) < 2:
        print("Не вказан шлях до файлу з логами.")
        print("Приклад: python main.py /шлях/до/файлу/логів [рівень_логування]")
        sys.exit(1)

    if len(sys.argv) > 3:
        print(f"Не очікувані аргументи: {sys.argv[3:]}.")
        sys.exit(1)


def main():
    check_args()

    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    level_filter = sys.argv[2] if len(sys.argv) > 2 else None
    if level_filter:
        display_log_details(logs, level_filter)


if __name__ == "__main__":
    main()
