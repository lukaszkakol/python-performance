#!/bin/bash

for NUMBER in 0a_cprofile 0b_timeit 0c_cli 0d_memory 0e_both 0f_dis 0g_rep 1 2 3 4 5 6 7 8 9 10 11
do
    echo "example $NUMBER"
    time python3 profiling/profile_example_$NUMBER.py > results/results_example_$NUMBER.txt
    echo
done
