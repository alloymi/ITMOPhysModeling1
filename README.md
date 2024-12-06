# "Прецессия гироскопа"

## Описание задачи
Задача заключается в расчетах максимального гироскопического давления на подшипники турбины при килевой качке. Турбина установлена вдоль продольной оси корабля, и её ротор вращается с определенной скоростью. Необходимо определить максимальные давления на подшипники при различных амплитудах качки и периодах вращения.

## Формулы
Для расчёта максимального давления используется следующая формула для гироскопического момента:

    I = 1/2 * M * R^2

где:

    I — момент инерции ротора турбины,
    M — масса ротора,
    R — радиус ротора.

Далее, гироскопический момент вычисляется с использованием угловой скорости качки (ω) и угловой скорости вращения ротора:

Gyroscopic Moment = I * ω_pitch * ω_rotor

где:
    
    ω_pitch = (2 * π) / T * sin(a),
    ω_rotor = (2 * π * N) / 60 — угловая скорость ротора в радианах в секунду (где N — частота вращения ротора в об/мин),
    T — период качки,
    a — амплитуда качки.

Максимальное давление на подшипники вычисляется как:

    Max Pressure = Gyroscopic Moment / Distance between bearings

где расстояние между подшипниками задано как 5 метров.

## Входные данные
    
    Масса ротора: 2000 кг
    Радиус ротора: 0.4 м
    Амплитуда качки: от 4° до 9°
    Период качки: от 9 с до 14 с
    Расстояние между подшипниками: 5 м
    Скорость вращения ротора: 3000 об/мин

## Реализация

Программы для расчета максимальных гироскопических давлений и построения графика:

[Код вычисления максимального давления](main.py)

[Код для построения графика зависимости давления от периода и амплитуды](Graph.py)

## Итоговые данные

Максимальное гироскопическое давления на подшипники турбины: ~1097.92 Н

График зависимости давления от периода и амплитуды:


![график](Graph.png)

