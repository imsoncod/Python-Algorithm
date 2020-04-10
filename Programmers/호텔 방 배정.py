import sys
import math
sys.setrecursionlimit(123456789)

def find_empty_room(num, room):
    if num not in room:
        room[num] = num + 1
        return num

    empty_room = find_empty_room(room[num], room)
    room[num] = empty_room + 1
    return empty_room

def solution(k, room_number):
    ans = []
    room = dict()

    for num in room_number:
        empty_room = find_empty_room(num, room)
        ans.append(empty_room)
    return ans
