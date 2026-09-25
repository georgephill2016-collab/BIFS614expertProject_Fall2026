# BIFS 614 Expert System

**2026 Fall Project for BIOT 670I by Sara Drennan, George Hill, Michael Jersey, and Edward Matovu**

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
