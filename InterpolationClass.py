import math as m 


class InterpolationClass:
    def __init__(self):
        self.h = 1
        self.M = -1.0 / (58 * 58)
        self.Vx0 = float()
        self.Vy0 = float()
        self.Vz0 = float()
        self.X0 = float()
        self.Y0 = float()
        self.Z0 = float()
        self.t0 = float()
        self.t = float()
        self.Vx = []
        self.Vy = []
        self.Vz = []
        self.X = []
        self.Y = []
        self.Z = []
        self.Ax = []
        self.Ay = []
        self.Az = []
        self.T = []

    def Input(self, vx0, vy0, vz0, x0, y0, z0, t0, t):
        self.Vx0 = vx0
        self.Vy0 = vy0
        self.Vz0 = vz0
        self.X0 = x0
        self.Y0 = y0
        self.Z0 = z0
        self.t0 = t0
        self.t = t
    
    def R(self, x, y, z):
        return (x * x + y * y + z * z) ** 0.5

    def Aix(self, x, y, z):
        return (self.M * x) / (self.R(x, y, z) * self.R(x, y, z) * self.R(x, y, z))

    def Aiy(self, x, y, z):
        return (self.M * y) / (self.R(x, y, z) * self.R(x, y, z) * self.R(x, y, z))

    def Aiz(self, x, y, z):
        return (self.M * z) / (self.R(x, y, z) * self.R(x, y, z) * self.R(x, y, z))

    def Calc(self):
        T = []
        Vx = []
        Vy = []
        Vz = []
        X = []
        Y = []
        Z = []
        Ax = []
        Ay = []
        Az = []

        Ax.append(self.Aix(self.X0, self.Y0, self.Z0))
        Ay.append(self.Aiy(self.X0, self.Y0, self.Z0))
        Az.append(self.Aiz(self.X0, self.Y0, self.Z0))

        Vx.append(self.Vx0)
        Vy.append(self.Vy0)
        Vz.append(self.Vz0)

        X.append(self.X0)
        Y.append(self.Y0)
        Z.append(self.Z0)

        T.append(self.t0)

        i = 1

        while (T[len(T)-1] < self.t):
            T.append(T[len(T)-1] + self.h)

            Vx.append(Vx[i-1] + Ax[i-1] * self.h)
            Vy.append(Vy[i-1] + Ay[i-1] * self.h)
            Vz.append(Vz[i-1] + Az[i-1] * self.h)

            X.append(X[i-1] + Vx[i] * self.h)
            Y.append(Y[i-1] + Vy[i] * self.h)
            Z.append(Z[i-1] + Vz[i] * self.h)

            Ax.append(self.Aix(X[i], Y[i], Z[i]))
            Ay.append(self.Aiy(X[i], Y[i], Z[i]))
            Az.append(self.Aiz(X[i], Y[i], Z[i]))
            
            i += 1

        output = {}

        for i in range(len(T)):
            output[T[i]] = {
                'ax': Ax[i],
                'ay': Ay[i],
                'az': Az[i],
                'vx': Vx[i],
                'vy': Vy[i],
                'vz': Vz[i],
                'x': X[i],
                'y': Y[i],
                'z': Z[i]
            }
            print(T[i])
        return output, T