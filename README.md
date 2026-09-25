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
## Setup and Running the Project

To run the project, first install Python and an IDE such as PyCharm. Clone or download the `BIFS614expertProject_Fall2026` repository and open the project folder in PyCharm. Open a terminal in the root project directory and install the required Python packages using the included `requirements.txt` file:

    pip install -r requirements.txt

From the root project directory, run `python scripts/build_index.py` to process `knowledge.txt` and generate the `knowledge.index` and `chunks.pkl` files required by the RAG system. Once the index and chunk files have been successfully created, run `python LLMscript/CourseAgentV6.py` to start the course assistant. After the language and embedding models have loaded, the user can enter questions related to the BIFS 614 course content. Enter `quit`, `exit`, or `q` to stop the program.

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

