# print(f"""{"-=" * 20}
# {"Triangle Analyzer":^40}
# {"-=" * 20}""")

print("-=" * 20)
print(f"{"Triangle Analyzer":^40}")
print("-=" * 20)

segment1 = float(input("First segment: "))
segment2 = float(input("Second segment: "))
segment3 = float(input("Third segment: "))

print("The above segments", end=" ")

if (segment1 + segment2 > segment3 and
    segment2 + segment3 > segment1 and
        segment1 + segment3 > segment2):
    print("can form a triangle!")
else:
    print("cannot form a triangle!")