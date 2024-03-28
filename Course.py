class Course:
    """Represents a course and its grade."""

    def __init__(self, name_Course):
        """Initializes a new course with a name and a placeholder grade."""
        self.name_Course = name_Course
        self.grade_Course = 101  # Placeholder value for grade

    def setGrade(self, new_grade):
        """Sets the grade for the course if it's within the valid range (0-100)."""
        if 0 <= new_grade <= 100:
            self.grade_Course = new_grade

    def print_course(self):
        """Prints the name and grade of the course."""
        print(self.name_Course)
        print(self.grade_Course)

    def get_name_course(self):
        """Returns the name of the course."""
        return self.name_Course
