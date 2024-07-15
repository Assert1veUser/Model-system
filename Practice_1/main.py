import random


def task2():
    x0 = 1
    A = 0
    B = 10
    N = 10 ** 2
    rParamsArr_e1 = []
    rParamsArr_e2 = []
    rParamsArr_e3 = []
    rParamsArr_e4 = []

    for i in range(0, 10 ** 2):
        rParamsArr_e1.append(random.uniform(0, 10))
    for i in range(0, 10**3):
        rParamsArr_e2.append(random.uniform(0, 10))
    for i in range(0, 10**4):
        rParamsArr_e3.append(random.uniform(0, 10))
    for i in range(0, 10**5):
        rParamsArr_e4.append(random.uniform(0, 10))

    return (rParamsArr_e1,rParamsArr_e2,rParamsArr_e3,rParamsArr_e4)

def task3(A, B, rParamsArr_e1, rParamsArr_e2, rParamsArr_e3, rParamsArr_e4):
    M = (A + B)/2
    D = ((B - A)**2)/12
    N1 = 10**2
    N2 = 10**3
    N3 = 10**4
    N4 = 10**5
    count_rParamsArr_e1_M = 0
    count_rParamsArr_e1_D = 0

    for i in range(0, N1 - 1):
        count_rParamsArr_e1_M = count_rParamsArr_e1_M + rParamsArr_e1[i]
    M_e1 = count_rParamsArr_e1_M / N1
    EpsM1 = abs((M - M_e1)/M) * 100

    for i in range(0, N1 - 1):
        count_rParamsArr_e1_D = count_rParamsArr_e1_D + rParamsArr_e1**2
    D_e1 = (count_rParamsArr_e1_D/N1 - M_e1**2) * N1/(N1 - 1)
    EpsD1 = abs((D - D_e1)/D)* 100

    for i in range(0, N2 - 1):
        count_rParamsArr_e2_M = count_rParamsArr_e2_M + rParamsArr_e2[i]
    M_e2 = count_rParamsArr_e2_M / N2
    EpsM2 = abs((M - M_e2) / M) * 100

    for i in range(0, N2 - 1):
        count_rParamsArr_e2_D = count_rParamsArr_e2_D + rParamsArr_e2**2
    D_e2 = (count_rParamsArr_e2_D / N2 - M_e2 ** 2) * N2 / (N2 - 1)
    EpsD2 = abs((D - D_e2) / D) * 100

    for i in range(0, N3 - 1):
        count_rParamsArr_e3_M = count_rParamsArr_e3_M + rParamsArr_e3[i]
    M_e3 = count_rParamsArr_e3_M / N3
    EpsM3 = abs((M - M_e3) / M) * 100

    for i in range(0, N3 - 1):
        count_rParamsArr_e3_D = count_rParamsArr_e3_D + rParamsArr_e3 ** 2
    D_e3 = (count_rParamsArr_e3_D / N3 - M_e3 ** 2) * N3 / (N3 - 1)
    EpsD3 = abs((D - D_e3) / D) * 100

    for i in range(0, N4 - 1):
        count_rParamsArr_e4_M = count_rParamsArr_e4_M + rParamsArr_e4[i]
    M_e4 = count_rParamsArr_e4_M / N4
    EpsM4 = abs((M - M_e4) / M) * 100

    for i in range(0, N4 - 1):
        count_rParamsArr_e4_D = count_rParamsArr_e4_D + rParamsArr_e4 ** 2
    D_e4 = (count_rParamsArr_e4_D / N4 - M_e4 ** 2) * N4 / (N4 - 1)
    EpsD4 = abs((D - D_e4) / D) * 100

    epsM = []
    epsM.append(EpsM1)
    epsM.append(EpsM2)
    epsM.append(EpsM3)
    epsM.append(EpsM4)

    epsD = []
    epsD.append(EpsD1)
    epsD.append(EpsD2)
    epsD.append(EpsD3)
    epsD.append(EpsD4)

    return (epsM, epsD)

def randPeriod(X):
    result = []
    n = len(X)
    for i in range(0, n - 1):
        ele = X[i]
        for j in range(i, n - 1):
            if ((ele == X[j]) & (i != j)):
                result[0] = j - 1
                result[1] = i
                result[2] = j
                return result
    result[0] = -1
    result[1] = -1
    result[2] = -1
    return result

def task4(rParamsArr_e1, rParamsArr_e2, rParamsArr_e3, rParamsArr_e4):
    test_1 = randPeriod(rParamsArr_e1)
    test_2 = randPeriod(rParamsArr_e2)
    test_3 = randPeriod(rParamsArr_e3)
    test_4 = randPeriod(rParamsArr_e4)
    return (test_1, test_2, test_3, test_4)



if __name__ == '__main__':




