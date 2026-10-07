venv — virtual environment
What: A private, isolated Python setup for one project.
Why: So on the same machine, different projects can use different versions of the same library without clashing.
Example: Project A uses numpy 1.20, Project B uses numpy 2.0 → each has its own venv, no conflict.
Command to make one: python -m venv venv
Activate:
Windows: venv\Scripts\activate