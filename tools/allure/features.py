from enum import Enum


class AllureFeatures(str, Enum):
    USERS = "Users"
    FILES = "Files"
    COURSES = "Courses"
    EXERCISES = "Exercises"
    AUTHENTICATION = "Authentication"
