# chia-plots-optimizer

Подсчитывает оптимально колличество плотов (k32, k33, k34) для максимального заполнения жесткого диска.

Консольный аналог этой страницы.
[plot-plan.chia](https://plot-plan.chia.foxypool.io/)

## Как пользоваться

Программа считает плоты в Гигабайтах (GB) (Пожалуйста не путайте с Гибибайтами GiB).
Чтоб увидеть размер диска в Гигабайтах:

```bash
#  для текущей папки
df -BGB .

# покажет что то типа

user@chiaserver:~/plt/12tb/addplots$ df -BGB .
Filesystem     1GB-blocks    Used Available Use% Mounted on
/dev/sdb1         12001GB 11573GB     428GB  97% /home/user/plt/12tb
```

Работа со скриптом:

```bash
# клонировать репу
git clone git@github.com:stavis-dev/chia-plots-optimizer.git

# зайти в папку с файлом
cd chia-plots-optimizer

# 1. Можно запустить скрипт, сразу передав в него параметры (например для размера 12001GB)
python3.9 ./calc_chia_plots.py 12001

# вывод:

#k32     #k33    #k34    Space Used 
110      0       0       11972.07 GB (≈99.76%) 
67       21      0       12000.846 GB (≈100.0%) 
67       21      0       12000.846 GB (≈100.0%)

# 2. Можно запустить скрипт интерактивно, указав размер диска внутри
python3.9 ./calc_chia_plots.py
Enter the Free space on the hard disk in GB: 12001
#k32     #k33    #k34    Space Used 
110      0       0       11972.07 GB (≈99.76%) 
67       21      0       12000.846 GB (≈100.0%) 
67       21      0       12000.846 GB (≈100.0%) 
```