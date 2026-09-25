# BIFS 614 Expert System

**2026 Fall Project for BIOT 670I- Biotechnology Capstone: Bioinformatics by Sara Drennan, George Hill, Michael Jersey, and Edward Matovu**

## Project Overview

The BIFS 614 Expert System is a capstone project focused on the development of a Large Language Model (LLM)-based expert system for the course BIFS 614-Data Structures and Algorithms.

The goal of the project is to develop an LLM expert for the BIFS 614 course capable of operating in two distinct modes:

- **TUTOR Mode** – An online interactive tutor for students to use as a learning resource to ask questions and receive answers based on relevant course content.
- **PROCTOR Mode** – A restricted mode designed for online examination scenarios, with appropriate behavioral guardrails and restrictions to prevent the system from providing unauthorized assistance.

The system must be able to distinguish between these contexts and apply the appropriate behaviors and restrictions for each mode.

This repository contains the course-content resources, preprocessing scripts, validation tools, and other development components used to build and test the BIFS 614 Expert System.

---

## Project Status

This project is currently under active development. Current progress includes:

- Course materials have been collected, converted to plain-text format, cleaned, organized, combined, and validated for use as the system's knowledge base.
- Multiple versions of the CourseAgent Python script have been developed and tested, progressing from basic prompting and user interaction to incorporating course content and Retrieval-Augmented Generation (RAG).
- RAG development is underway using text chunking, embeddings, and FAISS vector search to retrieve relevant BIFS 614 course content for user questions.
- CourseAgent versions are being tested with different LLM models and computing environments to evaluate performance and determine an appropriate model for the final system.
- Tutor and Proctor behaviors, guardrails, and additional system functionality remain under development.

Additional functionality and testing will continue as the project progresses.

---

## Setup and Running the Current Project 

To run the latest version of our project, first make sure Python is installed on your computer. Clone or download the BIFS614expertProject_Fall2026 repository and open the project in an IDE such as PyCharm.

1. Open a terminal in the root project directory and install the required Python packages:

       pip install -r requirements.txt

2. Run the build_index.py script to process knowledge.txt and create the knowledge.index and chunks.pkl files:

       python scripts/build_index.py

3. Once the index and chunk files have been created, run CourseAgentV6.py:

       python LLMscript/CourseAgentV6.py

After the models have loaded, you can enter questions related to the BIFS 614 course content. Enter "quit", "exit", or "q" to stop the program.

---
