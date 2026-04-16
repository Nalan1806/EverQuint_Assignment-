# Reasoning Agent

## 1. Overview

I built a modular reasoning agent that solves structured problems using a pipeline of:

* Planner - breaks down the problem
* Executor - computes the solution
* Verifier - validates the result

This design separates reasoning, execution, and validation for clarity and extensibility.

---

## 2. How to Run

```bash
python agent.py
```

Or run test cases:

```bash
python test_cases.py
```

---

## 3. Where Prompts Live

All prompts are defined in:

```bash
prompts.py
```

Includes:

* Planner prompt
* Executor prompt
* Verifier prompt

These are designed for modular LLM integration.

---

## 4. Assumptions

* Input questions are simple and structured (math, time, basic logic)
* Limited problem types are supported (time, arithmetic, apple problems)
* No external LLM API is used — rule-based fallback is implemented

---

## 5. Prompt Design

The prompts were designed to clearly separate responsibilities:

* Planner → generate structured steps
* Executor → perform calculations step-by-step
* Verifier → validate correctness

This ensures modular reasoning and easier debugging.

---

## 6. What Didn’t Work Well

* Fully LLM-based execution was not implemented due to constraints
* Rule-based execution limits generalization to unseen problem types
* Verifier does not deeply re-evaluate logic (only basic checks)

---

## 7. Improvements (If Given More Time)

* Integrate LLM for planner and executor for better generalization
* Add retry mechanism when verification fails
* Improve verifier with independent recomputation
* Expand support for more complex problem types

---

## 8. Example Runs

Question: What is 2 + 3?
{'answer': '5', 'status': 'success', 'reasoning_visible_to_user': 'The final answer is 5 based on structured reasoning.', 'metadata': {'plan': 'Extract key values from the question->Determine required operations->Perform step-by-step calculations->Return final result', 'checks': [{'check_name': 'Result exists', 'passed': True, 'details': 'Result computed successfully'}, {'check_name': 'consistency check', 'passed': True, 'details': 'Result not explicitly in steps, but acceptable'}], 'retries': 0}}

Question: What is 10 * 5?
{'answer': '50', 'status': 'success', 'reasoning_visible_to_user': 'The final answer is 50 based on structured reasoning.', 'metadata': {'plan': 'Extract key values from the question->Determine required operations->Perform step-by-step calculations->Return final result', 'checks': [{'check_name': 'Result exists', 'passed': True, 'details': 'Result computed successfully'}, {'check_name': 'consistency check', 'passed': True, 'details': 'Result not explicitly in steps, but acceptable'}], 'retries': 0}}

Question: Alice has 3 apples and twice as many green apples. How many apples?
{'answer': '9', 'status': 'success', 'reasoning_visible_to_user': 'The final answer is 9 based on structured reasoning.', 'metadata': {'plan': 'extract given quantities->identify relationships->computer unknown values->Calculate total', 'checks': [{'check_name': 'Result exists', 'passed': True, 'details': 'Result computed successfully'}, {'check_name': 'Consistency check', 'passed': True, 'details': 'Result aligns with steps'}], 'retries': 0}}

Question: Train leaves at 14:30 and arrives at 18:05. Duration?       
{'answer': '3 hours 35 minutes', 'status': 'success', 'reasoning_visible_to_user': 'The final answer is 3 hours 35 minutes based on structured reasoning.', 'metadata': {'plan': 'extract start and end time->convert both times into minutes->computer difference between end and start time->convert result back into hours and minutes', 'checks': [{'check_name': 'Result exists', 'passed': True, 'details': 'Result computed successfully'}, {'check_name': 'Non-negative result', 'passed': True, 'details': 'valid numeric result'}, {'check_name': 'consistency check', 'passed': True, 'details': 'Result not explicitly in steps, but acceptable'}], 'retries': 0}}

Question: What is 100 / 4?
{'answer': '25.0', 'status': 'success', 'reasoning_visible_to_user': 'The final answer is 25.0 based on structured reasoning.', 'metadata': {'plan': 'Extract key values from the question->Determine required operations->Perform step-by-step calculations->Return final result', 'checks': [{'check_name': 'Result exists', 'passed': True, 'details': 'Result computed successfully'}, {'check_name': 'consistency check', 'passed': True, 'details': 'Result not explicitly in steps, but acceptable'}], 'retries': 0}}

Question: Alice has 5 apples, gives away 2, then doubles remaining. Total?
{'answer': '5', 'status': 'success', 'reasoning_visible_to_user': 'The final answer is 5 based on structured reasoning.', 'metadata': {'plan': 'extract given quantities->identify relationships->computer unknown values->Calculate total', 'checks': [{'check_name': 'Result exists', 'passed': True, 'details': 'Result computed successfully'}, {'check_name': 'Consistency check', 'passed': True, 'details': 'Result aligns with steps'}], 'retries': 0}}

Question: Meeting is 60 min, slots 09:00–09:30, 09:45–10:30, 11:00–12:00. Which works?
{'answer': '0 hours 30 minutes', 'status': 'success', 'reasoning_visible_to_user': 'The final answer is 0 hours 30 minutes based on structured reasoning.', 'metadata': {'plan': 'extract start and end time->convert both times into minutes->computer difference between end and start time->convert result back into hours and minutes', 'checks': [{'check_name': 'Result exists', 'passed': True, 'details': 'Result computed successfully'}, {'check_name': 'Non-negative result', 'passed': True, 'details': 'valid numeric result'}, {'check_name': 'consistency check', 'passed': True, 'details': 'Result not explicitly in steps, but acceptable'}], 'retries': 0}}

Question: What is (2 + 3) * 4?
{'answer': '20', 'status': 'success', 'reasoning_visible_to_user': 'The final answer is 20 based on structured reasoning.', 'metadata': {'plan': 'Extract key values from the question->Determine required operations->Perform step-by-step calculations->Return final result', 'checks': [{'check_name': 'Result exists', 'passed': True, 'details': 'Result computed successfully'}, {'check_name': 'consistency check', 'passed': True, 'details': 'Result not explicitly in steps, but acceptable'}], 'retries': 0}}

Question: Train leaves at 23:30 and arrives at 01:00. Duration?       
{'answer': '1 hours 30 minutes', 'status': 'success', 'reasoning_visible_to_user': 'The final answer is 1 hours 30 minutes based on structured reasoning.', 'metadata': {'plan': 'extract start and end time->convert both times into minutes->computer difference between end and start time->convert result back into hours and minutes', 'checks': [{'check_name': 'Result exists', 'passed': True, 'details': 'Result computed successfully'}, {'check_name': 'Non-negative result', 'passed': True, 'details': 'valid numeric result'}, {'check_name': 'consistency check', 'passed': True, 'details': 'Result not explicitly in steps, but acceptable'}], 'retries': 0}}

---
