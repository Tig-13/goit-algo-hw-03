from datetime import datetime

def get_days_from_today(date_str):
    try:
        input_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        current_date = datetime.today().date()
        delta = current_date - input_date
        print('Кількість днів між заданою датою і поточною датою:  ',delta.days)
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."

date_str = input('Введіть дату: ')
get_days_from_today(date_str)