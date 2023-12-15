from math import sin, cos, tan, radians
angle = int(input("Enter an angle: "))
angle_in_radians = radians(angle)
sine = sin(angle_in_radians)
cosine = cos(angle_in_radians)
tangent = tan(angle_in_radians)
print(f"Sine of {angle}°: {sine:.2f}")
print(f"Cosine of {angle}°: {cosine:.2f}")
print(f"Tangent of {angle}°: {tangent:.2f}")