# Medical Coding Automation Script

This repository contains a Python script for medical coding automation using CrewAI.

## Overview

This script utilizes CrewAI agents to automate the process of medical coding and billing. It analyzes medical records, assigns appropriate medical codes (ICD-10, CPT), generates billing statements, and performs basic error detection.

## Files

* `medical_coder.py`: The main Python script containing the CrewAI agent definitions and task execution.
* `.gitignore`: Specifies files and directories that should be ignored by Git.
* `.env`: Stores the OpenAI API key (replace the placeholder).

## Important Notes

* **API Key Security:** This script requires an OpenAI API key. **Replace `"YOUR_OPENAI_API_KEY_HERE"` in the `.env` file with your actual API key.** Never commit your actual API key directly to the repository.
* **Placeholder API Key:** The `.env` file in this repository uses a placeholder value. You must replace it with your own API key for the script to function.
* **No Local Execution Required:** This repository is intended for storing the code. Local execution is not necessary to preserve the code on GitHub.
* **Dependencies:** If you intend to run this code locally, you will need to install the dependencies in a python virtual environment.
    * `pip install crewai langchain-openai python-dotenv`
* **Disclaimer:** This is a basic example. For real-world medical coding and billing, you need to ensure compliance with all applicable regulations and standards.
