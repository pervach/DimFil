
from data_loader import load_csv
from data_processing import check_nulls, missing_report, fill_missing
from visualization import Visualizer

# Загрузка данных
df = load_csv('data.csv')

# Анализ пропусков
print("Пропущенные значения:")
print(check_nulls(df))

print("\nОтчёт:")
print(missing_report(df))

# Заполнение пропусков
df = fill_missing(df, strategy='mean')

# Визуализация
viz = Visualizer()

viz.add_histogram(df, 'age')
viz.add_line_plot(df, 'date', 'sales')
viz.add_scatter_plot(df, 'age', 'income')

viz.show_all()
