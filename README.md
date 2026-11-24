# Numeric-Pattern
# Case Study 27: Advanced Numeric Pattern Generator

## Python Activity-Based Learning

### Student Details
- **Name:**DURGA SURYA PRAVALLIKA
- **Roll Number:** N26V01A0383
- **Branch:** CSE
- **Section:** 5
- **Programming Language:** Python

---

## 1. Problem Statement

The Advanced Numeric Pattern Generator is a Python-based program that generates different patterns based on user input.

The program generates a Hollow Diamond Pattern and a Symmetric Numerical Diamond Pattern. It uses nested loops and conditional statements to produce properly aligned patterns. It also validates user input and displays error messages for invalid dimensions or choices.

## 2. Objectives

- To generate a hollow diamond pattern.
- To generate a symmetric numerical pattern.
- To understand nested loops in Python.
- To use conditional statements for pattern selection.
- To validate user input.
- To improve logical thinking and programming skills.

## 3. Assumptions

1. The user can select either of the two available patterns.
2. The pattern size must be a positive integer.
3. The hollow diamond requires a minimum size of 2.
4. The symmetric numerical pattern accepts a minimum size of 1.
5. Invalid choices and dimensions are rejected.
6. The patterns are generated using nested loops.

## 4. Algorithm

1. Start the program.
2. Display the pattern menu.
3. Ask the user to select a pattern.
4. Read the user's choice.
5. Check whether the choice is valid.
6. Ask the user to enter the pattern size.
7. Validate the entered size.
8. If the choice is 1:
   - Generate the upper half of the hollow diamond.
   - Generate the lower half of the hollow diamond.
9. If the choice is 2:
   - Generate the upper half of the numerical diamond.
   - Generate the lower half of the numerical diamond.
10. Display the generated pattern.
11. Stop the program.

## 5. Pseudocode

```text
START

DISPLAY pattern menu
1. Hollow Diamond
2. Symmetric Number Pattern

INPUT choice

IF choice is invalid
    DISPLAY Invalid choice

ELSE
    INPUT size

    IF size is invalid
        DISPLAY Invalid size

    ELSE IF choice = 1 AND size < 2
        DISPLAY Minimum size is 2

    ELSE

        IF choice = 1

            FOR i = 1 TO size
                PRINT leading spaces

                IF i = 1
                    PRINT single star
                ELSE
                    PRINT hollow diamond row
                END IF
            END FOR

            FOR i = size-1 DOWN TO 1
                PRINT leading spaces
                PRINT hollow diamond row
            END FOR

        ELSE IF choice = 2

            FOR i = 1 TO size
                PRINT leading spaces
                PRINT increasing numbers
                PRINT decreasing numbers
            END FOR

            FOR i = size-1 DOWN TO 1
                PRINT leading spaces
                PRINT increasing numbers
                PRINT decreasing numbers
            END FOR

        END IF
    END IF
END IF

STOP
```

## 6. Python Source Code

**File name:** `numeric_pattern.py`

The complete Python implementation is available in this file.

## 7. Test Cases

| Test Case | Choice | Size | Expected Result |
|---|---|---:|---|
| 1 | 1 | 5 | Hollow diamond generated |
| 2 | 1 | 3 | Small hollow diamond generated |
| 3 | 2 | 4 | Symmetric number pattern generated |
| 4 | 2 | 1 | Single number displayed |
| 5 | 1 | 1 | Invalid size |
| 6 | 2 | 0 | Invalid size |
| 7 | 3 | 5 | Invalid choice |
| 8 | 2 | abc | Invalid input |

## 8. Expected Output

### Hollow Diamond Pattern

```text
Enter your choice: 1
Enter the size: 5

    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
```

### Symmetric Numerical Pattern

```text
Enter your choice: 2
Enter the size: 4

    1
   1 2 1
  1 2 3 2 1
 1 2 3 4 3 2 1
  1 2 3 2 1
   1 2 1
    1
```

## 9. Conclusion

The Advanced Numeric Pattern Generator successfully generates hollow diamond and symmetric numerical patterns based on user input.

This project helps us understand Python variables, strings, conditional statements, for loops and nested loops. It also improves logical thinking and problem-solving skills through pattern generation.

---

**Project:** Python Activity-Based Learning  
**Case Study Number:** 27  
**Topic:** Advanced Numeric Pattern Generator
