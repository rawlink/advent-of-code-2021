#!/usr/bin/env python3
from collections import deque

def load(file):
    with open(file) as f:
        depths = [int(line.strip()) for line in f.readlines()]

    return depths

def part1(depths):
    '''
    >>> part1(load('input.txt'))
    1624
    '''
    count = 0
    last = depths[0]
    for depth in depths:
        if depth > last:
            count += 1
        last = depth
    return count

def part2(depths):
    '''
    >>> part2(load('input.txt'))
    1653
    '''
    windowWidth = 3
    count = 0
    window = deque(depths[:windowWidth])
    lastSum = sum(window)
    for depth in depths[windowWidth:]:
        window.append(depth)
        window.popleft()
        currentSum = sum(window)
        if currentSum > lastSum:
            count += 1
        lastSum = currentSum
    return count

def main():
    depths = load('input.txt')
    value = part1(depths)
    print(f'Part 1: {value}')
    assert value == 1624

    value = part2(depths)
    print(f'Part 2: {value}')
    assert value == 1653

if __name__ == '__main__':
    main()
