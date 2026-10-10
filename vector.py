import numpy as np
class vector:
    def __init__(self, size, is_col = True, fill = 0, init_values = None):
        self.vec = list()
        self.size = size
        self.is_col = is_col
        self.vec = [fill for i in range(size)]

        if (init_values != None):
            n = len(init_values) 
            count = 0
            for i in range (self.size):
                if count >= n: count = 0
                self.vec[i] = init_values[count]
                count += 1



    def __str__(self):
        n = self.size
        string = "[ "
        if (self.is_col):
            for i in range (n-1):
                string += str(self.vec[i]) + ",\n" 
            return string + str(self.vec[n-1]) + " ]"
        else:
            for i in range (len(self.vec)-1):
                string += str(self.vec[i]) + ", "
            return string + str(self.vec[n-1]) + " ]"

    def is_it_col(self):
        return bool(self.is_col)
    
    def T(self):
        if self.is_col:
            self.is_col = False
            return 
        self.is_col = True
        return

    def __add__(self, other):
        new_vec = list()
        if isinstance(other, vector):
            if other.size == self.size and other.is_col == self.is_col:
                for i in range(self.size):
                    new_vec.append(self.vec[i] + other.vec[i]) 
            else:
                return TypeError("broski")
        elif isinstance(other, (int, float)):
            for i in range(self.size):
                new_vec.append(self.vec[i] + other) 
        else:
            return TypeError("unsupported type")
        return vector(self.size, is_col=self.is_col, init_values=new_vec)

    
    def __sub__(self, other):
        new_vec = list()
        if isinstance(other, vector):
            if other.size == self.size and other.is_col == self.is_col:
                for i in range(self.size):
                    new_vec.append(self.vec[i] - other.vec[i]) 
            else:
                return TypeError("broski")
        elif isinstance(other, (int, float)):
            for i in range(self.size):
                new_vec.append(self.vec[i] - other) 
        else:
            return TypeError("unsupported type")
        return vector(self.size, is_col=self.is_col, init_values=new_vec)
    

    def __mul__(self, other):
        new_vec = list()
        if isinstance(other, vector):
            if other.size == self.size and other.is_col == self.is_col:
                for i in range(self.size):
                    new_vec.append(self.vec[i] * other.vec[i]) 
            else:
                return TypeError("broski")
        elif isinstance(other, (int, float)):
            for i in range(self.size):
                new_vec.append(self.vec[i] * other) 
        else:
            return TypeError("unsupported type")
        return vector(self.size, is_col=self.is_col, init_values=new_vec)


    def __truediv__(self, other):
        new_vec = list()
        if isinstance(other, vector):
            if other.size == self.size and other.is_col == self.is_col:
                for i in range(self.size):
                    new_vec.append(self.vec[i] / other.vec[i]) 
            else:
                return TypeError("broski")
        elif isinstance(other, (int, float)):
            for i in range(self.size):
                new_vec.append(self.vec[i] / other) 
        else:
            return TypeError("unsupported type")
        return vector(self.size, is_col=self.is_col, init_values=new_vec)
        

    
def multiply(v1: vector, v2: vector):
    n1, n2 = len(v1), len(v2)

    if len(n1) != len(n2):
        return False
    if v1.is_it_col() != v2.is_it_col():
        return False

    initial = list()
    for i in range(n1):
        initial(v1[i]*v2[i])
    vec = vector(n1, )
    return vec 

print(vector(9, init_values=(1, 2, 3, 6, 2, 8)))
print(vector(9, is_col=False, fill = 0, init_values=(1, 2, 3, 6, 2, 8)))
print("--------")

v1 = vector(3, is_col=False, fill=0, init_values=(1, 2, 3))
v2 = vector(3, is_col=False, fill=0, init_values=(2, 4, 6))
mul = v1 * v2
add = v1 + v2
sub = v1 - v2
div = v1 / v2

print("mul", mul)
print("add", add)
print("sub", sub)
print("div", div)

    