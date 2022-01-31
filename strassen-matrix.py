import numpy as np

def Two_Matrix_Plus(Matix_One, Matix_Two, size):
    Total = [[[0] for i in range(0, size)] for j in range(0, size)]
    for i in range(0,size):
        for j in range(0,size):
            Total[i][j] = Matix_One[i][j] + Matix_Two[i][j]
    return Total

def Two_Matrix_Minus(Matix_One, Matix_Two, size):
    Total = [[[0] for i in range(0, size)] for j in range(0, size)]
    for i in range(0, size):
        for j in range(0, size):
            Total[i][j] = Matix_One[i][j] - Matix_Two[i][j]
    return Total

def Merge(div11, div12, div21, div22, size):
    Size = int(2 * size)
    Matix_One = [[[0] for i in range(0, Size)] for j in range(0, Size)]
    for i in range(0, size):
        for j in range(0, size):
            Matix_One[i][j] = div11[i][j]
            Matix_One[i][j+size] = div12[i][j]
            Matix_One[i+size][j] = div21[i][j]
            Matix_One[i+size][j+size] = div22[i][j]
    return Matix_One

def Div11(Matix_One, size):
    Size = int(size / 2)   
    div11 = [ [[0] for i in range(0,Size)] for j in range(0,Size)]
    for i in range(0, Size):   
        for j in range(0, Size):   
            div11[i][j] = Matix_One[i][j]  
    return div11

def Div12(Matix_One, size):
    Size = int(size / 2)
    div12 = [ [ [0] for i in range(0,Size)] for j in range(0,Size)]
    for i in range(0, Size):
        for j in range(0, Size):
            div12[i][j] = Matix_One[i][j+Size]
    return div12

def Div21(Matix_One, size):
    Size = int(size / 2)
    div21 = [ [ [0] for i in range(0,Size)] for j in range(0,Size)]
    for i in range(0, Size):
        for j in range(0, Size):
            div21[i][j] = Matix_One[i + Size][j]
    return div21

def Div22(Matix_One, size):
    Size = int(size / 2)
    div22 = [ [ [0] for i in range(0,Size)] for j in range(0,Size)]
    for i in range(0, Size):
        for j in range(0, Size):
            div22[i][j] = Matix_One[i + Size][j + Size]
    return div22

def strassen_multi(Matix_One, Matix_Two, size):
    Size = size
    if Size == 2:
        First_Total = [[[0] for i in range(2)] for i in range(2)]
        First_Total[0][0] = Matix_One[0][0] * Matix_Two[0][0] + Matix_One[0][1] * Matix_Two[1][0]
        First_Total[0][1] = Matix_One[0][0] * Matix_Two[0][1] + Matix_One[0][1] * Matix_Two[1][1]
        First_Total[1][0] = Matix_One[1][0] * Matix_Two[0][0] + Matix_One[1][1] * Matix_Two[1][0]
        First_Total[1][1] = Matix_One[1][0] * Matix_Two[0][1] + Matix_One[1][1] * Matix_Two[1][1]
        return First_Total
    else:
        div11 = Div11(Matix_One, size)
        div12 = Div12(Matix_One, size)
        div21 = Div21(Matix_One, size)
        div22 = Div22(Matix_One, size)
        Sdiv11 = Div11(Matix_Two, size)
        Sdiv12 = Div12(Matix_Two, size)
        Sdiv21 = Div21(Matix_Two, size)
        Sdiv22 = Div22(Matix_Two, size)
        Size = int(size / 2)
        multi1 = strassen_multi(div11, Two_Matrix_Minus(Sdiv12, Sdiv22, Size), Size)
        multi2 = strassen_multi(Two_Matrix_Plus(div11, div12, Size), Sdiv22, Size)
        multi3 = strassen_multi(Two_Matrix_Plus(div21, div22, Size), Sdiv11, Size)
        multi4 = strassen_multi(div22, Two_Matrix_Minus(Sdiv21, Sdiv11, Size), Size)
        multi5 = strassen_multi(Two_Matrix_Plus(div11, div22, Size), Two_Matrix_Plus(Sdiv11, Sdiv22, Size), Size)
        multi6 = strassen_multi(Two_Matrix_Minus(div12, div22, Size), Two_Matrix_Plus(Sdiv21, Sdiv22, Size), Size)
        multi7 = strassen_multi(Two_Matrix_Minus(div11, div21, Size), Two_Matrix_Plus(Sdiv11, Sdiv12, Size), Size)
        Total11 = Two_Matrix_Plus(Two_Matrix_Minus(Two_Matrix_Plus(multi5, multi4, Size), multi2, Size), multi6, Size)
        Total12 = Two_Matrix_Plus(multi1, multi2, Size)
        Total21 = Two_Matrix_Plus(multi3, multi4, Size)
        Total22 = Two_Matrix_Minus(Two_Matrix_Minus(Two_Matrix_Plus(multi5, multi1, Size), multi3, Size), multi7, Size)
        Total = Merge(Total11, Total12, Total21, Total22, Size)
        return Total
        
Matix_One=np.array([[4, 5, 7, 4], [5, 2, 4, 5], [5, 5, 5, 7], [8, 9, 5, 4]], dtype=int)
Matix_Two=np.array([[5, 45, 7, 4], [1, 2, 5, 4], [7, 85, 5, 2], [4, 5, 78 , 9]], dtype=int)
print strassen_multi(Matix_One, Matix_Two, 4)
print np.dot(Matix_One,Matix_Two)