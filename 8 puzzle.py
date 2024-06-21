l = [[8, 2, 5], [6, 9, 1], [4, 3, " "]]
for i in range(3):
    for j in range(3):
        print(l[i][j], end=" ")
    print()

r = 2
c = 2
n = 3
while n > 0:
    print("enter w/a/s/d or q to quit :")
    d = input()
    if d == 'q':
        break
    if d == 'w' and r > 0:  # Move up if not at the top boundary
        l[r][c], l[r-1][c] = l[r-1][c], l[r][c]
        r -= 1
    elif d == 's' and r < 2:  # Move down if not at the bottom boundary
        l[r][c], l[r+1][c] = l[r+1][c], l[r][c]
        r += 1
    elif d == 'a' and c > 0:  # Move left if not at the left boundary
        l[r][c], l[r][c-1] = l[r][c-1], l[r][c]
        c -= 1
    elif d == 'd' and c < 2:  # Move right if not at the right boundary
        l[r][c], l[r][c+1] = l[r][c+1], l[r][c]
        c += 1
    else:
        print("Invalid move!")
        continue

    for i in range(3):
        for j in range(3):
            print(l[i][j], end=" ")
        print()

    
