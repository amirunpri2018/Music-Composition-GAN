#!/usr/bin/env python
# coding: utf-8

# In[3]:


def note_reg(note):
    C = [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
    C_sharp = [1, 13, 25, 37, 49, 61, 73, 85, 97, 109, 121]
    D = [2, 14, 26, 38, 50, 62, 74, 86, 98, 110, 122]
    D_sharp = [3, 15, 27, 39, 51, 63, 75, 87, 99, 111, 123]
    E = [4, 16, 28, 40, 52, 64, 76, 88, 100, 112, 124]
    F = [5, 17, 29, 41, 53, 65, 77, 89, 101, 113, 125]
    F_sharp = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126]
    G = [7, 19, 31, 43, 55, 67, 79, 91, 103, 115, 127]
    G_sharp = [8, 20, 32, 44, 56, 68, 80, 92, 104, 116]
    A = [9, 21, 33, 45, 57, 69, 81, 93, 105, 117]
    A_sharp = [10, 22, 34, 46, 58, 70, 82, 94, 106, 118]
    B = [11, 23, 35, 47, 59, 71, 83, 95, 107, 119]
    if (note in C):
        return 0
    elif(note in C_sharp):
        return 1
    elif(note in D):
        return 2
    elif(note in D_sharp):
        return 3
    elif(note in E):
        return 4
    elif(note in F):
        return 5
    elif(note in F_sharp):
        return 6
    elif(note in G):
        return 7
    elif(note in G_sharp):
        return 8
    elif(note in A):
        return 9
    elif(note in A_sharp):
        return 10
    elif(note in B):
        return 11
    else:
        return 'fail'


# In[ ]:




