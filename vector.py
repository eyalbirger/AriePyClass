import numpy
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

print(vector(9, init_values=(1, 2, 3, 6, 2, 8)))
print(vector(9, is_col=False, fill = 0, init_values=(1, 2, 3, 6, 2, 8)))


    