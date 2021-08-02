# chia-plots-optimizer

git@github.com:stavis-dev/chia-plots-optimizer.git

Подсчитывает оптимально колличество плотов (k32, k33, k34) для максимального заполнения жесткого диска.

Консольный аналог этой страницы.
[plot-plan.chia](https://plot-plan.chia.foxypool.io/)

## Как пользоваться

Программа считает плоты в Гигабайтах (GB) (Пожалуйста не путайте с Гибибайтами GiB).
Чтоб увидеть размер диска:

```bash
#  для текущей папки
df -BGB .

# покажет что то типа

user@chiaserver:~/plt/12tb/addplots$ df -BGB .
Filesystem     1GB-blocks    Used Available Use% Mounted on
/dev/sdb1         12001GB 11573GB     428GB  97% /home/user/plt/12tb
```