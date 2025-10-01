grades = []
print("Enter grades (0-100). Enter -1 to finish:")

while True:
    g = int(input("Grade: "))
    if g == -1:
        break
    if 0 <= g <= 100:
        grades.append(g)
    else:
        print(g, "is ignored (Invalid).")

if grades:
    avg = sum(grades) / len(grades)
    point = ((100 - avg) + 10) / 10

    if avg < 50: remarks = "Dropped"
    elif avg < 75: remarks = "Failed"
    elif avg <= 79: remarks = "Passed - Satisfactory"
    elif avg <= 84: remarks = "Passed - Good"
    elif avg <=89: remarks = "Passed - Average"
    elif avg <=99: remarks = "Passed - Verry Good"
    else: reamark = "Passed - Excellent"

    print("\nGrades:", grades)
    print("Average Grade:", round(avg, 2))
    print("Point Grade:", round(point, 2))
    print("Remarks:", remarks)
else:
    print("No valid grades entered.")

