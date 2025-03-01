import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# Set your OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY" # Replace with your actual API key

# Initialize the language model with a single API key
llm = ChatOpenAI(model="gpt-4-turbo-preview") # Or another suitable model

# Define agents
medical_record_analysis_agent = Agent(
    role="Medical Record Analyst",
    goal="Analyze medical records to identify diagnoses and procedures.",
    backstory="You have extensive experience in medical record analysis.",
    llm=llm,
    allow_delegation=False,
)

coding_agent = Agent(
    role="Medical Coder",
    goal="Assign accurate medical codes (ICD-10, CPT) based on the analysis.",
    backstory="You are an expert in medical coding.",
    llm=llm,
    allow_delegation=False,
)

billing_agent = Agent(
    role="Billing Specialist",
    goal="Generate billing statements and submit claims to insurance companies.",
    backstory="You are skilled in medical billing and claims processing.",
    llm=llm,
    allow_delegation=False,
)

error_detection_agent = Agent(
    role="Error Detection Specialist",
    goal="Check for coding and billing errors and flag potential issues.",
    backstory="You have a keen eye for detail and are an expert at error detection.",
    llm=llm,
    allow_delegation=False,
)

# Define tasks
analyze_record_task = Task(
    description="Analyze the provided medical record and extract relevant diagnoses and procedures.",
    agent=medical_record_analysis_agent,
)

assign_codes_task = Task(
    description="Based on the analysis, assign appropriate ICD-10 and CPT codes.",
    agent=coding_agent,
    input_from_tasks=[analyze_record_task],
)

generate_bill_task = Task(
    description="Generate a billing statement and prepare the insurance claim.",
    agent=billing_agent,
    input_from_tasks=[assign_codes_task],
)

detect_errors_task = Task(
    description="Review the coding and billing information for any potential errors or inconsistencies.",
    agent=error_detection_agent,
    input_from_tasks=[assign_codes_task, generate_bill_task],
)

# Create the crew
crew = Crew(
    agents=[
        medical_record_analysis_agent,
        coding_agent,
        billing_agent,
        error_detection_agent,
    ],
    tasks=[
        analyze_record_task,
        assign_codes_task,
        generate_bill_task,
        detect_errors_task,
    ],
    process=Process.sequential,  # Tasks are executed in order
)

# Provide a sample medical record (replace with your actual data)
sample_record = """
Patient: John Doe
Date: 2023-10-26
Diagnosis: Acute bronchitis
Procedure: Chest X-ray
"""

# Run the crew with the sample record
result = crew.kickoff(inputs={"analyze_record_task": {"input": sample_record}})

print("Results:")
print(result)
