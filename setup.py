from setuptools import setup, find_packages

setup(
    name='student_grade_calculator',
    version='1.0.0',
    author='Satya Repala',
    author_email='satyarepala3@gmail.com',
    description='Student Grade Calculator',
    long_description='A simple student grade calculator project using Python.',
    url='https://github.com/satyarepala/student_grade_calculator',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'student_grade_calculator=student_grade_calculator.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
