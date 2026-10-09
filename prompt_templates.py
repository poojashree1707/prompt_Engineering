
def build_prompt(technique, task):
    task = task.strip()

    if technique == "zero-shot":
        prompt = f"""
Task:
{task}

Answer the task directly without using any examples.
"""

    elif technique == "one-shot":
        prompt = f"""
Example:
Task: What is Python?
Answer: Python is a high-level programming language.

Now complete this task:
{task}
"""

    elif technique == "two-shot":
        prompt = f"""
Example 1:
Task: What is Java?
Answer: Java is an object-oriented programming language.

Example 2:
Task: What is SQL?
Answer: SQL is used to manage and query databases.

Now complete this task:
{task}
"""

    elif technique == "three-shot":
        prompt = f"""
Example 1:
Task: What is Python?
Answer: Python is a high-level programming language.

Example 2:
Task: What is Java?
Answer: Java is an object-oriented programming language.

Example 3:
Task: What is SQL?
Answer: SQL is used to manage and query databases.

Now complete this task:
{task}
"""

    else:
        raise ValueError("Invalid prompting technique.")

    return prompt.strip()