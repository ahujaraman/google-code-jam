def solve_maze():
    global ans 
    ans = ''
    n = int(input())
    maze_path = str(input())
    for i in range(len(maze_path)):
        if maze_path[i]=='S':
            ans+='E'
        else:
            ans+='S'
    return ans

T = int(input())
for i in range(1,T+1):
    result = solve_maze()
    print("Case #{0}: {1}".format(i,result))
