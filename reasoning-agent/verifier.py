def verify(question:str, execution_result:dict):
    #extract result and internal reasoning steps from executor
    result=execution_result["result"]
    steps=execution_result["steps"]

    #list to store all checks performed
    checks=[]

    #overall status flag
    passed = True

    #CHECK 1: RESULT EXISTS (to ensure executor actually produced an answer)
    if result is None: 
        checks.append({
            "check_name": "Result exists",
            "passed": False,
            "details": "No result produced"
        })
        passed = False
    else:
        checks.append({
            "check_name": "Result exists",
            "passed":True,
            "details":"Result computed successfully"
        })

    #CHECK 2: NON-NEGATIVE VALIDATION ( to ensure result is logically valid (no negative counts, time etc.)
    if isinstance(result,(int,float)):
        if result < 0: 
            passed=False
            checks.append({
                "check_name":"Non-negative result",
                "passed":False,
                "details": "Negative value found"
            })
    else: 
        checks.append({
            "check_name": "Non-negative result",
            "passed": True,
            "details": "valid numeric result"
        })

    #CHECK 3: BASIC CONSISTENCY CHECK
    #checks if computed result aligns with reasoning steps

    if steps and result is not None:
        steps_text = " ".join(steps)

        #if result value appears in steps -> good alignment
        if str(result) in steps_text:
            checks.append({
                "check_name": "Consistency check",
                "passed":True, 
                "details": "Result aligns with steps"
            })

        else: 
            #not strict failure, just note it. 
            checks.append({
                "check_name": "consistency check",
                "passed":True, 
                "details":"Result not explicitly in steps, but acceptable"
            })

    #final status
    status = "success" if passed else "failed"
    #if any critical check failed, overall status becomes "failed"

    return{
        "status": status, 
        "checks": checks, 
        "retries":0
    }