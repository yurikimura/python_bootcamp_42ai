class Vector:
    def __init__(self, obj):
        """
        You should be able to initialize the object with either:
        • a list of floats: Vector([0.0, 1.0, 2.0, 3.0]) -> then the size of the vector will be 4
        • a size: Vector(3) -> the vector will be created with default values starting from 0.0: [0.0, 1.0, 2.0]
        • a range (min, max): Vector((10,16)) -> the vector will be created with values in the given range: [10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
        """
        try:
            if isinstance(obj, list):
                if all(isinstance(x, float) for x in obj):
                    self.values = obj
                    self.size = len(self.values)
                else:
                    print('The list must only contain float values.')

            elif isinstance(obj, int):
                self.values = [float(i) for i in range(obj)]
                self.size = obj

            elif isinstance(obj, tuple):
                if len(obj) == 2 and all(isinstance(x, int) for x in obj):
                    self.values = [float(i) for i in range(obj[1])][obj[0]:]
                    self.size = obj[1] - obj[0]
                else:
                    print('range must be a tuple of 2 integer.')
            else:
                print("ERROR")
        except:
            print("ERROR")

    def __add__(self, vector_or_scalar):

        if isinstance(vector_or_scalar, Vector) and self.size == vector_or_scalar.size:
            obj = [self.values[i] + vector_or_scalar.values[i] for i in range(self.size)]
            return Vector(obj)

        elif isinstance(vector_or_scalar, float) or isinstance(vector_or_scalar, int):
            obj = [self.values[i] + vector_or_scalar for i in range(self.size)]
            return Vector(obj)
        else:
            print("Try again")

    def __radd__(self, vector_or_scalar):

        if isinstance(vector_or_scalar, Vector) and self.size == vector_or_scalar.size:
            obj = [self.values[i] + vector_or_scalar.values[i] for i in range(self.size)]
            return Vector(obj)

        elif isinstance(vector_or_scalar, float) or isinstance(vector_or_scalar, int):
            obj = [self.values[i] + vector_or_scalar for i in range(self.size)]
            return Vector(obj)
        else:
            print("Try again")

    def __sub__(self, vector_or_scalar):

        if isinstance(vector_or_scalar, Vector) and self.size == vector_or_scalar.size:
            obj = [self.values[i] - vector_or_scalar.values[i] for i in range(self.size)]
            return Vector(obj)

        elif isinstance(vector_or_scalar, float) or isinstance(vector_or_scalar, int):
            obj = [self.values[i] - vector_or_scalar for i in range(self.size)]
            return Vector(obj)
        else:
            print("Try again")

    def __rsub__(self, vector_or_scalar):

        if isinstance(vector_or_scalar, Vector) and self.size == vector_or_scalar.size:
            obj = [self.values[i] - vector_or_scalar.values[i] for i in range(self.size)]
            return Vector(obj)

        elif isinstance(vector_or_scalar, float) or isinstance(vector_or_scalar, int):
            obj = [self.values[i] - vector_or_scalar for i in range(self.size)]
            return Vector(obj)
        else:
            print("Try again")

    def __truediv__(self, scalar):

        if isinstance(scalar, float) or isinstance(scalar, int):
            obj = [self.values[i] / scalar for i in range(self.size)]
            return Vector(obj)
        else:
            print("Try again")

    def __rtruediv__(self, vector_or_scalar):

        if isinstance(vector_or_scalar, float) or isinstance(vector_or_scalar, int):
            obj = [self.values[i] / vector_or_scalar for i in range(self.size)]
            return Vector(obj)
        else:
            print("Try again")

    def __mul__(self, vector_or_scalar):
        if isinstance(vector_or_scalar, Vector) and self.size == vector_or_scalar.size:
            obj = + self.values[i] * vector_or_scalar.values[i]
            return obj

        elif isinstance(vector_or_scalar, float) or isinstance(vector_or_scalar, int):
            obj = [self.values[i] * vector_or_scalar for i in range(self.size)]
            return Vector(obj)
        else:
            print("Try again")

    def __rmul__(self, vector_or_scalar):
        if isinstance(vector_or_scalar, Vector) and self.size == vector_or_scalar.size:
            obj = + self.values[i] * vector_or_scalar.values[i]
            return obj

        elif isinstance(vector_or_scalar, float) or isinstance(vector_or_scalar, int):
            obj = [self.values[i] * vector_or_scalar for i in range(self.size)]
            return Vector(obj)
        else:
            print("Try again")

    def __str__(self):
        return f"values: {self.values}\nsize: {self.size}"

    def __repr__(self):
        return f"values: {self.values}\nsize: {self.size}"
