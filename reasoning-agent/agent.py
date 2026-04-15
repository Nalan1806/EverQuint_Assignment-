from planner import plan
from executor import execute
from verifier import verify

import json

def solve(question: str):

    #planner
    plan_steps=plan(question)

    #executor
    execution_result = execute(question, plan_steps)

    #verifier
    verification = verify(question, execution_result)

    status=verification["status"]
    checks=verification["checks"]
    retries=verification["retries"]

    result = execution_result["result"]
    #explanation for verification failure/success
    if status == "success": 
        explanation=f"The final answer is {result} based on structured reasoning." 
    else: 
        explanation = "The solution failed verification checks. Plese review the input or logic."

    #final output

    output = {
        "answer": str(result),
        "status": status,
        "reasoning_visible_to_user": explanation, 

        #metadata contains internal reasoning hidden from the user

        "metadata":{
            "plan": "->".join(plan_steps),
            "checks": checks,
            "retries": retries
        }
    }

    return output

#CLI INTERFACE
if __name__ == "__main__":
    print("Reasoning Agent(type 'exit' to quit)\n")

    while True: 
        question = input("Enter question: ")
        if question.lower() == "exit": 
            break 

        result = solve(question)

        print("\nOutput:")
        print(json.dumps(result, indent=2))
        print("\n")

     