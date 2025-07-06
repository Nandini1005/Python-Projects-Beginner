print("✅ Script started...")
def analyze_marks(filename):
    try:
        with open(filename, 'r') as file:
            marks = [int(line.strip()) for line in file if line.strip().isdigit()]
        
        if not marks:
            print("No valid marks found.")
            return

        total_students = len(marks)
        average = sum(marks) / total_students
        highest = max(marks)
        lowest = min(marks)

        print(f"📊 Total Students: {total_students}")
        print(f"📈 Average Marks: {average:.2f}")
        print(f"🏆 Highest Marks: {highest}")
        print(f"😢 Lowest Marks: {lowest}")

    except FileNotFoundError:
        print("marks.txt not found!")

# Run the function
analyze_marks("marks.txt")
