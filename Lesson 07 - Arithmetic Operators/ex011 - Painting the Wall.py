width = float(input('Wall width: '))
height = float(input('Wall height: '))
area = width * height
paint = area / 2
print(f'This wall is {width}x{height} and it\'s area is {area:.3f}m².')
print(f'To paint this wall, you\'ll need {paint:.4f}l of paint.')