import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("tkagg")
import math

# Constants
thrust = 15 # N
air_density = 1.2041 # kg/m^3
prop_area = 0.0049 # m^2
vane_area = 0.001 # m^2
chord_length = 0.05 # m
moment_arm = 0.1 # m

# NACA 0015 Reynold 100000
# http://airfoiltools.com/airfoil/details?airfoil=naca0015-il
# http://airfoiltools.com/calculator/reynoldsnumber
# Format: [vane angle (deg), C_l]
lift_coeffs = np.array([[0, 0],
                        [2.5, 0.5],
                        [10, 1.1],
                        [13, 1.1],
                        [14, 1.0]])

# Calculate exhaust velocity
exhaust_velocity = math.sqrt(thrust / (2 * air_density * prop_area)) # m/s
print("Exhaust Velocity: " + str(exhaust_velocity))

# Reynolds number
kinematic_viscosity = 1.4207e-5 # m^2/s at 1atm and 10 degrees celsius
reynold = exhaust_velocity * chord_length / kinematic_viscosity
print("Reynold's Number: " + str(reynold))

# Calculate torque for each vane angle
torque_data = list()
for x in lift_coeffs:
    lift_coefficient = x[1]
    lift = lift_coefficient * air_density * math.pow(exhaust_velocity, 2) * vane_area / 2
    torque = lift * moment_arm
    torque_data.append(torque)

# Polynomial Regression
degree = 3
x = np.linspace(0, lift_coeffs[-1, 0], 100)
p = np.polyfit(lift_coeffs[:, 0], torque_data, degree)
f = np.poly1d(p)

# Get polynomial equation
label = str()
for i, v in enumerate(p[::-1]):
    label = '{:0.3e}'.format(v) + "x^" + str(i) + " + " + label
label = label[0:len(label) - 3] # Remove last addition sign
print(label)

# Plot points and curve
plt.scatter(lift_coeffs[:, 0], torque_data)
plt.plot(x, f(x), label=label)

plt.xlabel("Vane Angle (deg)")
plt.ylabel("Torque (Nm)")

plt.legend()
plt.grid()
plt.show()
