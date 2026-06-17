import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    
    for i in range(1, t + 1):
        n = int(input_data[i])
        
        ans = []
        for j in range(n):
            odd_number = 2 * j + 1
            ans.append(str(odd_number))
            
        print(" ".join(ans))

if __name__ == '__main__':
    solve()
