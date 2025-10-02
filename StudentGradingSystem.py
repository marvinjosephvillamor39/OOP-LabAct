class GradeProcessor:
    def __init__(self):
        self.grades = []

    def input_grades(self):
        print("Enter grades (0-100). Enter -1 to finish:")
        while True:
            try:
                g = int(input("Grade: "))
                if g == -1:
                    break
                if 0 <= g <= 100:
                    self.grades.append(g)
                else:
                    print(f"{g} is ignored (Invalid).")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def calculate_point(self, avg):
        return ((100 - avg) + 10) / 10

    def determine_remarks(self, avg):
        if avg < 50:
            return "Dropped"
        elif avg < 75:
            return "Failed"
        elif avg <= 79:
            return "Passed - Satisfactory"
        elif avg <= 84:
            return "Passed - Good"
        elif avg <= 89:
            return "Passed - Average"
        elif avg <= 99:
            return "Passed - Very Good"
        else:
            return "Passed - Excellent"

    def display_results(self):
        if not self.grades:
            print("No valid grades entered.")
            return

        avg = self.calculate_average()
        point = self.calculate_point(avg)
        remarks = self.determine_remarks(avg)

        print("\nGrades:", self.grades)
        print("Average Grade:", round(avg, 2))
        print("Point Grade:", round(point, 2))
        print("Remarks:", remarks)


if __name__ == "__main__":
    grade_processor = GradeProcessor()
    grade_processor.input_grades()
    grade_processor.display_results()
