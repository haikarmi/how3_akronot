from Course import Course  # Assuming Course class is imported from another module

class Student:
    """
    Represents a student with their name, ID, and courses taken.

    Attributes:
        name (str): The name of the student.
        _id (str): The ID of the student.
        courses (list): A list of courses taken by the student.
    """

    def __init__(self, name, id):
        """
        Initializes a new student with a name, ID, and an empty list of courses.

        Args:
            name (str): The name of the student.
            id (str): The ID of the student.
        """
        self.name = name
        self._id = id
        self.courses = []

    def GetID(self):
        """Returns the ID of the student."""
        return self._id

    def addCourse(self, course_name, grade):
        """
        Adds a new course to the student's list of courses or updates an existing course's grade.

        Args:
            course_name (str): The name of the course to add/update.
            grade (int): The grade obtained in the course.
        """
        for course in self.courses:
            if course.name_Course == course_name:
                course.setGrade(grade)
                return
        # If the course is not found, create a new Course instance and add it to the list
        t_course = Course(course_name)
        t_course.setGrade(grade)
        self.courses.append(t_course)

    def avgGrade(self):
        """Calculates the average grade of all courses taken by the student."""
        sum_grade = sum(map(lambda x: x.grade_Course, self.courses))
        count_grade = len(self.courses)
        return sum_grade / count_grade if count_grade != 0 else 0  # Avoid division by zero

    def get_course(self, course_name):
        """
        Retrieves a course object by its name.

        Args:
            course_name (str): The name of the course to retrieve.

        Returns:
            Course or None: The course object if found, otherwise None.
        """
        course_list = list(filter(lambda x: x.name_Course == course_name, self.courses))
        return course_list[0] if course_list else None
