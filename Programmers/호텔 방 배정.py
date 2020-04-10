import sys
import math
sys.setrecursionlimit(123456789) #재귀함수 호출횟수 제한

def find_empty_room(num, room):
    #방이 비어있다면
    if num not in room:
        room[num] = num + 1
        return num

    empty_room = find_empty_room(room[num], room)
    room[num] = empty_room + 1
    return empty_room

def solution(k, room_number):
    ans = []
    room = dict()
    #room의 key는 가장가까운 비어있는 방의 번호(value)를 가리킴

    for num in room_number:
        empty_room = find_empty_room(num, room)
        ans.append(empty_room)
    return ans
