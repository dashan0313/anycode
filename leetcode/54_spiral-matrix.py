def spiralOrder(matrix):
        answer = []
        m,n = len(matrix),len(matrix[0])
        m0,n0 = m,n
        length,full_length = 0,m*n
        i,j = 0,0
        quan = 0
        flag = 1
        while length < full_length:
            if flag == 1:
                if j == n-1:
                    flag = 2
                else:
                    answer.append(matrix[i][j])
                    length += 1
                    j += 1
            elif flag == 2:
                if i == m-1:
                    flag = 3
                else:
                    answer.append(matrix[i][j])
                    length += 1
                    i += 1
            elif flag == 3:
                if j == n0-n:
                    flag = 4
                else:
                    answer.append(matrix[i][j])
                    length += 1
                    j -= 1
            else:
                if i == m0 - m + 1:
                    answer.append(matrix[i][j])
                    m, n,quan = m-1,n-1,quan+1
                    i,j = quan,quan
                    flag = 1
                else:
                    answer.append(matrix[i][j])
                    length += 1
                    i -= 1
            print(flag,i,j,answer)
        return answer

spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
