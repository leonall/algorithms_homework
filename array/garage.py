#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
There is a parking lot with only one empty spot. Given the initial state
of the parking lot and the final state. Each step we are only allowed to
move a car
out of its place and move it into the empty spot.
The goal is to find out the least movement needed to rearrange
the parking lot from the initial state to the final state.
Say the initial state is an array:
[1, 2, 3, 0, 4],
where 1, 2, 3, 4 are different cars, and 0 is the empty spot.
And the final state is
[0, 3, 2, 1, 4].
We can swap 1 with 0 in the initial array to get [0, 2, 3, 1, 4] and so on.
Each step swap with 0 only.
Edit:
Now also prints the sequence of changes in states.
Output of this example :-
initial: [1, 2, 3, 0, 4]
final:   [0, 3, 2, 1, 4]
Steps =  4
Sequence :
0 2 3 1 4
2 0 3 1 4
2 3 0 1 4
0 3 2 1 4

https://github.com/keon/algorithms/blob/master/array/garage.py
"""

def garage(initial, final):
    """
    :param initial: List
    :param final: List
    :return steps: int
    :return seq: List
    """
    initial = initial[:]
    steps = 0
    seq = []
    while initial != final:
        zero = initial.index(0)
        if zero != final.index(0):
            car_to_move = final[zero]
            pos = initial.index(car_to_move)
            initial[zero], initial[pos] = initial[pos], initial[zero]
        else:
            for i in range(len(final)):
                if initial[i] != final[i]:
                    initial[zero], initial[i] = initial[i], initial[zero]
                    break
        seq.append(initial[:])
        steps += 1
    return steps, seq

steps, seq = garage([1, 2, 3, 0, 4], [0, 3, 2, 1, 4])
print(steps)
print(seq)

initial = list(range(5))
final = initial[::-1]
steps, seq = garage(initial, final)
print(steps)
print(seq)