import math

# Код для нахождения максимального гироскопического давления на подшипники турбины
def calculate_gyroscopic_pressure(data):
    max_pressure_result = None  # Для хранения результата с максимальным давлением
    distance_between_bearings = 5  # Расстояние между подшипниками, метры
    rotor_speed_rpm = 3000  # Скорость вращения ротора, об/мин
    rotor_speed_rad_s = 2 * math.pi * rotor_speed_rpm / 60  # Преобразование скорости в радианы/секунду

    for row in data:
        # Распаковываем параметры: масса, радиус, амплитуда (минимум и максимум), период (минимум и максимум)
        M, R, a_min, a_max, T_min, T_max = row
        moment_of_inertia = 0.5 * M * R**2  # Вычисляем момент инерции (формула для сплошного цилиндра: I = 1/2 * M * R^2)

        # Проходим по диапазону амплитуд (градусы)
        for a in range(a_min, a_max + 1):
            # Проходим по диапазону периодов (секунды)
            for T in range(T_min, T_max + 1):
                # Преобразуем амплитуду в радианы
                a_rad = math.radians(a)

                # Вычисляем угловую скорость килевой качки
                omega_pitch = 2 * math.pi / T * math.sin(a_rad)

                # Вычисляем гироскопический момент
                gyroscopic_moment = moment_of_inertia * rotor_speed_rad_s * omega_pitch

                # Вычисляем давление на подшипники
                max_pressure = gyroscopic_moment / distance_between_bearings

                # Если текущее давление больше найденного ранее, обновляем результат
                if max_pressure_result is None or max_pressure > max_pressure_result['Max Pressure (N)']:
                    max_pressure_result = {
                        "Mass (kg)": M,           # Масса (кг)
                        "Radius (m)": R,          # Радиус (м)
                        "Amplitude (deg)": a,     # Амплитуда (градусы)
                        "Period (s)": T,          # Период (секунды)
                        "Max Pressure (N)": max_pressure  # Максимальное давление (Н)
                    }

    return max_pressure_result

# Входные данные: масса, радиус, диапазон амплитуд, диапазон периодов
input_data = [
    (2000, 0.4, 4, 9, 9, 14)
]

# Вычисление максимального давления
max_pressure_result = calculate_gyroscopic_pressure(input_data)

# Вывод результата
print("Максимальное гироскопическое давление и соответствующие параметры:")
print(max_pressure_result)
