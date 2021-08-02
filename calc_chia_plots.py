#!/usr/bin/env python
""" This calculation is based on
k32 plots being 108.837 GB,
k33 plots being 224.227 GB,
k34 plots being 461.535 GB """


def calc_chia_plots(disc_size: int) -> dict:
    size_k32 = 108.837
    size_k33 = 224.227
    size_k34 = 461.535

    k32_count_k32_plots: int = 0
    k32_space_used = 0

    k33_count_k32_plots: int = 0
    k33_count_k33_plots: int = 0
    k33_space_used = 0

    k34_count_k32_plots: int = 0
    k34_count_k33_plots: int = 0
    k34_count_k34_plots: int = 0
    k34_space_used = 0

    k32_count_k32_plots = int(disc_size / size_k32)
    k32_space_used = (k32_count_k32_plots * size_k32)

    k33_space_used = k32_space_used
    k33_count_k32_plots = k32_count_k32_plots

    k34_space_used = k32_space_used
    k34_count_k32_plots = k32_count_k32_plots

    for k32Count in range(k32_count_k32_plots):
        k32UsedSpace = size_k32 * k32Count
        k33Count = int((disc_size - k32UsedSpace) / size_k33)
        usedSpaceInGb = k33Count * size_k33 + k32UsedSpace

        if usedSpaceInGb > k33_space_used:
            k33_count_k32_plots = k32Count
            k33_count_k33_plots = k33Count
            k33_space_used = usedSpaceInGb

    for k32Count in range(0, k32_count_k32_plots):
        k32UsedSpace = size_k32 * k32Count
        k33Count = 0
        while k32UsedSpace + (size_k33 * k33Count) <= disc_size:
            k33UsedSpace = size_k33 * k33Count
            remainingSpaceInGb = disc_size - k33UsedSpace - k32UsedSpace
            k34Count = int(remainingSpaceInGb / size_k34)
            usedSpaceInGb = k34Count * size_k34 + k33UsedSpace + k32UsedSpace
            if usedSpaceInGb > k34_space_used:
                k34_count_k32_plots = k32Count
                k34_count_k33_plots = k33Count
                k34_count_k34_plots = k34Count
                k34_space_used = round(usedSpaceInGb, 3)
            k33Count += 1

    plot_plan = {
        'k32': {
            'number_k32': k32_count_k32_plots,
            'space_used': k32_space_used,
                },
        'k33': {
            'number_k32': k33_count_k32_plots,
            'number_k33': k33_count_k33_plots,
            'space_used': k33_space_used,
                        },
        'k34': {
            'number_k32': k34_count_k32_plots,
            'number_k33': k34_count_k33_plots,
            'number_k34': k34_count_k34_plots,
            'space_used': k34_space_used,
                        },
            }
    return plot_plan


def out_space_used(space_used: float) -> str:
    """ добавил вывод в процентах для понимания """
    return (f"{space_used['space_used']} GB "
            f"(≈{round((space_used['space_used'] / disc_size * 100), 2)}%)")


if __name__ == "__main__":
    import sys
    if sys.argv[1:2]:
        disc_size = int(sys.argv[1])
    else:
        disc_size = int(input("Enter the Free space on the hard disk in GB: "))
    
    plots = calc_chia_plots(disc_size)
    print('#k32 \t #k33 \t #k34 \t Space Used \n'
          f"{plots['k32']['number_k32']} \t 0 \t 0 \t {out_space_used(plots['k32'])} \n"
          f"{plots['k33']['number_k32']} \t {plots['k33']['number_k33']} \t 0 \t {out_space_used(plots['k33'])} \n"
          f"{plots['k34']['number_k32']} \t {plots['k34']['number_k33']} \t {plots['k34']['number_k34']} \t {out_space_used(plots['k34'])} \n"
          )
