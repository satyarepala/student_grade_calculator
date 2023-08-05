# Student Grade Calculator

Welcome to the Student Grade Calculator! This is a simple Python project that allows you to manage and calculate grades for students.

## Features

- Add new students and their grades.
- Update grades for existing students.
- Delete students from the database.
- Display all students and their average grades.
- View class statistics, such as the average grade for the entire class and the highest and lowest average grades.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/student_grade_calculator.git
cd student_grade_calculator
```

2. Install the package using setup.py:
```commandline
python setup.py install
```

## Usage
To run the Student Grade Calculator, simply execute the following command in your terminal:
```
student_grade_calculator
```

The program will start, and you can follow the on-screen instructions to interact with the calculator and manage student grades.

## Requirements
The following external packages are required to run the project. The installation using setup.py will take care of these dependencies:
```doctest
# setup.py
install_requires=[
    # 'numpy>=1.18.0',
    # 'pandas>=1.0.0',
    # 'matplotlib>=3.1.0',
    # 'seaborn>=0.10.0',
]
```

Please ensure that you have Python 3.6 or higher installed before proceeding with the installation.

## Full Project Directory Structure
The complete directory structure for the project is as follows:
```markdown
student_grade_calculator/
│   setup.py
│   README.md
│   requirements.txt
│
└───student_grade_calculator/
    │   main.py
    │   student.py
    │   __init__.py
    │
    └───utils/
            __init__.py
            student.py

```