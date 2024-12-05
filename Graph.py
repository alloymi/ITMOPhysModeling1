import math
import matplotlib.pyplot as plt

# Код для построения графика
def calculate_gyroscopic_pressure_with_details(data):
    all_pressures = []  # Для хранения всех давлений (для графика)
    max_pressure_result = None  # Для хранения результата с максимальным давлением
    distance_between_bearings = 5  # Расстояние между подшипниками, метры
    rotor_speed_rpm = 3000  # Скорость вращения ротора, об/мин
    rotor_speed_rad_s = 2 * math.pi * rotor_speed_rpm / 60  # Преобразование скорости в радианы/секунду

    for row in data:
        M, R, a_min, a_max, T_min, T_max = row
        moment_of_inertia = 0.5 * M * R**2  # Момент инерции

        for a in range(a_min, a_max + 1):  # Амплитуды (градусы)
            for T in range(T_min, T_max + 1):  # Периоды (секунды)
                a_rad = math.radians(a)  # Преобразуем амплитуду в радианы
                omega_pitch = 2 * math.pi / T * math.sin(a_rad)  # Угловая скорость килевой качки
                gyroscopic_moment = moment_of_inertia * rotor_speed_rad_s * omega_pitch  # Гироскопический момент
                max_pressure = gyroscopic_moment / distance_between_bearings  # Давление на подшипники

                # Сохраняем результаты для графика
                all_pressures.append({
                    "Amplitude (deg)": a, "Period (s)": T, "Pressure (N)": max_pressure
                })

                # Определяем максимальное давление
                if max_pressure_result is None or max_pressure > max_pressure_result['Max Pressure (N)']:
                    max_pressure_result = {
                        "Mass (kg)": M, "Radius (m)": R,
                        "Amplitude (deg)": a, "Period (s)": T,
                        "Max Pressure (N)": max_pressure
                    }

    return all_pressures, max_pressure_result

# Входные данные: масса, радиус, диапазон амплитуд, диапазон периодов
input_data = [(2000, 0.4, 4, 9, 9, 14)]

# Вычисляем давления и максимум
all_pressures, max_pressure_result = calculate_gyroscopic_pressure_with_details(input_data)

# Построение графиков
plt.figure(figsize=(12, 6))

# График 1: Полная зависимость давления от периода и амплитуды
for amplitude in range(4, 10):  # Для каждой амплитуды (градусы)
    periods = [point["Period (s)"] for point in all_pressures if point["Amplitude (deg)"] == amplitude]
    pressures = [point["Pressure (N)"] for point in all_pressures if point["Amplitude (deg)"] == amplitude]
    plt.plot(periods, pressures, label=f"Амплитуда {amplitude}°")

# Выделение точки максимального давления
plt.scatter(
    max_pressure_result["Period (s)"],
    max_pressure_result["Max Pressure (N)"],
    color="red", label="Максимальное давление", zorder=5
)

# Настройки графика
plt.title("Зависимость гироскопического давления от периода при разных амплитудах")
plt.xlabel("Период (секунды)")
plt.ylabel("Давление (Ньютон)")
plt.legend()
plt.grid()

# Отображение графика
plt.show()

# Печатаем максимум
max_pressure_result
