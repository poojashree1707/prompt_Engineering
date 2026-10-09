def build_prompt(technique, task):

    if technique == "Zero-shot":
        return f"""
You are a helpful AI assistant.
Answer the given task using your own knowledge.

Task:
{task}

Provide a clear and relevant answer.
""".strip()

    if technique == "One-shot":
        return f"""
Follow the pattern shown in the example and apply the same style
to the new task.

Example:
Question: What is Cloud Computing?
Answer: Cloud computing provides on-demand access to computing
resources such as servers, storage, and applications over the internet.

Now answer:
{task}
""".strip()

    if technique == "Few-shot":
        return f"""
Use the following examples as guidance for answering the task.

Example 1:
Question: What is Python?
Answer: Python is a programming language known for its simplicity
and wide range of applications.

Example 2:
Question: What is Database?
Answer: A database is an organized collection of data that can be
stored, managed, and retrieved efficiently.

Example 3:
Question: What is API?
Answer: An API allows different software applications to communicate
and exchange data.

Now answer the following task in a similar style:

{task}
""".strip()

    if technique == "CoT":
        return f"""
Analyze the task carefully before answering.
Identify the important information, determine the appropriate
method, and provide the final result with a brief explanation.

Task:
{task}

Give only the necessary reasoning and final answer.
""".strip()

    if technique == "Manual CoT":
        return f"""
Follow this structured problem-solving process.

Step 1:
Understand what the task is asking.

Step 2:
Identify the important information and requirements.

Step 3:
Choose the appropriate method or concept.

Step 4:
Apply the method and obtain the result.

Step 5:
Check the result for correctness.

Final:
Present the answer clearly.

Task:
{task}
""".strip()

    if technique == "ToT":
        return f"""
Explore different possible approaches before selecting the best one.

Option 1:
Develop one possible approach and evaluate its suitability.

Option 2:
Develop another possible approach and evaluate its suitability.

Option 3:
Consider another approach if required.

Comparison:
Compare the possible approaches based on accuracy,
simplicity, and relevance.

Final:
Select the most suitable approach and provide the answer.

Task:
{task}
""".strip()

    raise ValueError("Unknown prompting technique")