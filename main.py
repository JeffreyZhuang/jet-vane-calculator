import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("tkagg")
import math

# Constants
thrust = 21.5 # N
air_density = 1.2041 # kg/m^3
prop_area = 0.0049 # m^2
vane_area = 0.000846 # m^2
moment_arm = 0.1 # m

# NACA 0012 Reynold # 200000
# http://airfoiltools.com/airfoil/details?airfoil=naca0012h-sa
# http://airfoiltools.com/calculator/reynoldsnumber
# Format: [vane angle (deg), C_l]
lift_coeffs = np.array([[0, 0],
                        [3, 0.4],
                        [5, 0.6],
                        [10, 1.1],
                        [13.5, 1.2],
                        [15, 1]])

# Calculate exhaust velocity
exhaust_velocity = math.sqrt(thrust / (2 * air_density * prop_area)) # m/s

# Calculate torque for each vane angle
torque_data = list()
for x in lift_coeffs:
    lift_coefficient = x[1]
    lift = lift_coefficient * air_density * math.pow(exhaust_velocity, 2) * vane_area / 2
    torque = lift * moment_arm
    torque_data.append(torque)

# Plot curve
plt.plot(lift_coeffs[:, 0], torque_data)

plt.xlabel("Vane Angle (deg)")
plt.ylabel("Torque (Nm)")

plt.grid()
plt.show()
