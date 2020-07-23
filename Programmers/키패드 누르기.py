def solution(numbers, hand):
    keypad = {
        1 : (0,0), 2 : (0,1), 3 : (0,2),
        4 : (1,0), 5 : (1,1), 6 : (1,2),
        7 : (2,0), 8 : (2,1), 9 : (2,2),
        '*' : (3,0), 0 : (3,1), '#' : (3,2)
    }
    
    ans = ''
    hand = 'L' if hand == 'left' else 'R'
    left = '*'
    right = '#'
    
    for num in numbers:
        n = num%3
        if n == 1:
            left = num
            ans += 'L'
        elif n == 0 and num != 0:
            right = num
            ans += 'R'
        else:
            ld = abs((keypad[num])[0] - (keypad[left])[0]) + abs((keypad[num])[1] - (keypad[left])[1])
            rd = abs((keypad[num])[0] - (keypad[right])[0]) + abs((keypad[num])[1] - (keypad[right])[1])
            if ld < rd:
                left = num
                ans += 'L'
            elif ld == rd:
                if hand == 'L':
                    left = num
                else:
                    right = num
                ans += hand
            else:
                right = num
                ans += 'R'            
    
    return ans
