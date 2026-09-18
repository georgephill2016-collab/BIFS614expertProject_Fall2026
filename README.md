# BIFS 614 Expert System

**2026 Fall Project for BIOT 670I**

## Project Overview

The BIFS 614 Expert System is a capstone project focused on the development of a Large Language Model (LLM)-based expert system for the BIFS 614 course.

The goal of the project is to develop an AI system capable of operating in two distinct modes:

- **TUTOR Mode** – An interactive learning resource designed to assist students with BIFS 614 course concepts and course-related questions.
- **PROCTOR Mode** – A restricted mode designed for online examination scenarios, with appropriate behavioral guardrails to prevent the system from providing unauthorized assistance.

The system must be able to distinguish between these contexts and apply the appropriate behaviors and restrictions for each mode.

This repository contains the course-content resources, preprocessing scripts, validation tools, and other development components used to build and test the BIFS 614 Expert System.

---

## Project Status

This project is currently under active development.

Work completed or currently in progress includes:

- Collection and organization of BIFS 614 course materials
- Conversion of course documents from DOCX to plain-text format
- Manual review and cleaning of extracted course content
- Organization of lecture, assignment, and examination material
- Creation of a combined Weeks 1–11 lecture corpus
- Programmatic validation of the combined lecture corpus
- Development of Tutor and Proctor behaviors and guardrails
- Testing of course-content retrieval and expert-system functionality

Additional functionality and documentation will be added as the project progresses.

---

## Course Content Curation

Accurate course content is necessary for developing and evaluating the BIFS 614 Expert System. Course materials were therefore prepared using a multi-step content curation and quality-control process.

### Content Processing Workflow

```text
Original BIFS 614 DOCX Files
            |
            v
    DOCX-to-TXT Extraction
            |
            v
      Extracted Text
            |
            v
 Manual Review and Cleaning
            |
            v
      Cleaned Text
            |
            v
   Corpus Combination
            |
            v
 Combined Lecture Corpus
            |
            v
    Corpus Validation
            |
            v
Validated Course Content
```

## Repository Structure

```text
BIFS614expertProject_Fall2026/
|
├── course_content/
│   |
│   ├── assignments/
│   │   ├── BIFS614_Assignment_01_Questions.txt
│   │   ├── BIFS614_Assignment_02_Questions.txt
│   │   ├── BIFS614_Assignment_03_Questions.txt
│   │   ├── BIFS614_Assignment_04_Questions.txt
│   │   ├── BIFS614_Assignment_05_Questions.txt
│   │   └── BIFS614_Assignment_06_Questions.txt
│   |
│   ├── combined/
│   │   └── BIFS614_combined_lectures.txt
│   |
│   ├── exam_questions/
│   │   └── BIFS614_Exam_Questions.txt
│   |
│   └── lectures/
│       ├── week_01_lecture.txt
│       ├── week_02_lecture.txt
│       ├── week_03_lecture.txt
│       ├── week_04_lecture.txt
│       ├── week_05_lecture.txt
│       ├── week_06_lecture.txt
│       ├── week_07_lecture.txt
│       ├── week_08_lecture.txt
│       ├── week_09_lecture.txt
│       ├── week_10_lecture.txt
│       └── week_11_lecture.txt
|
├── scripts/
│   ├── extract_text.py
│   ├── combine_lectures.py
│   └── validate_combined_lectures.py
|
└── README.md
```

---

## Course Content

### Lectures

Individual curated lecture files for Weeks 1–11 are located in:

```text
course_content/lectures/
```

These files preserve the lecture material as separate weekly sources.

### Assignments

Curated assignment question files are located in:

```text
course_content/assignments/
```

### Exam Questions

Curated examination material is located in:

```text
course_content/exam_questions/
```

### Combined Lecture Corpus

The consolidated Weeks 1–11 lecture corpus is located at:

```text
course_content/combined/BIFS614_combined_lectures.txt
```

The combined corpus provides a single source containing the lecture material for use in expert-system development and testing.

---

## Scripts

### `extract_text.py`

Extracts text from BIFS 614 DOCX course documents and converts the content to plain-text format for review and further processing.

### `combine_lectures.py`

Combines the eleven curated BIFS 614 lecture files into a single lecture corpus while preserving chronological order and identifying individual lecture boundaries.

### `validate_combined_lectures.py`

Validates the generated combined lecture corpus against the eleven individual curated lecture files.

Successful validation confirms that the lecture content contained within the combined corpus matches the curated source files.

---

## Tutor and Proctor Modes

The BIFS 614 Expert System is intended to support two operational modes with different behaviors and guardrails.

### TUTOR Mode

TUTOR Mode is intended to provide students with an interactive learning resource grounded in BIFS 614 course content.

Planned capabilities include:

- Answering course-related questions
- Explaining BIFS 614 concepts
- Retrieving relevant information from course materials
- Supporting student learning without an examination context

### PROCTOR Mode

PROCTOR Mode is intended for online examination contexts and requires more restrictive behavior than TUTOR Mode.

The system must identify the examination context and apply appropriate guardrails so that it can support the proctoring environment without providing assistance that would compromise the assessment.

The implementation and testing of these behaviors are currently under development.

---

## Project Team

This repository is maintained as part of the **Fall 2026 BIOT 670I capstone project**.

Project responsibilities include course-content curation, expert-system development, Tutor and Proctor behavior design, guardrail development, testing, validation, and project documentation.

---

## Disclaimer

This project is being developed for educational and academic purposes as part of a capstone course.

Course materials included in this repository are intended for authorized project and educational use.
