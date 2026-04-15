def plan(question:str):
    question_lower=question.lower()

    #detecting problem type

    if "time" in question_lower or ":" in question_lower:
        return [
            "extract start and end time",
            "convert both times into minutes",
            "computer difference between end and start time",
            "convert result back into hours and minutes"
        ]
    
    elif "apple" in question_lower or "twice" in question_lower:
        return [ "extract given quantities",
                "identify relationships",
                "computer unknown values",
                "Calculate total"

        ]
    
    else:
        return[
            "Extract key values from the question",
            "Determine required operations",
            "Perform step-by-step calculations",
            "Return final result"
        ]
    

    

        