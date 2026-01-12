# Ход работы

## Подготовка сырых данных

- добавил our world in data в качестве подмодуля
- добавил BP / Energy Institute — Статистический обзор мировой энергетики
- добавил EIA (Управление энергетической информации США):
  - потребление и производство угля и кокса
  - потребление и производство сухого природного газа
  - потребление, мощность и производство электроэнергии
  - выбросы по видам топлива
  - общее потребление и производство энергии

## Унифицирование данных

Структура таблицы:
- country        – страна
- iso_code       – ISO-3 код 
- region         – регион 
- year           – год
- resource       – Oil | Gas | Coal | Electricity | Energy | CO2 | Water
- metric         – Consumption | Production | Reserves | Capacity | Emissions
- value          – числовое значение
- unit           – единица измерения
- source         – OWID | BP | EIA


## Общий пайплайн

```pipeline
RAW DATA
│
├── OWID  ──┐
├── BP    ──┼── normalize → long format
├── EIA   ──┘
│
▼
HARMONIZATION
- страны
- годы
- единицы
│
▼
energy_long.csv
```
