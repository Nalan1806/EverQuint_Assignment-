import re #for extracting numbers/patterns from text

def execute(question:str, plan:list):
    question_lower=question.lower() #for easier keyword matching

    #CASE 1: Time difference problems
    if ":" in question: 
        times= re.findall(r'(\d{1,2}):(\d{2})',question) #extract time patterns like HH:MM using regex

        if len(times)>=2: 
            h1,m1=map(int,times[0]) #unpack start time
            h2,m2=map(int,times[1]) #unpack end time

            #convert both into total minutes
            start=h1*60 + m1
            end = h2*60 + m2 

            #compute difference
            diff=end-start

            #handle overnight case
            if diff < 0: 
                 diff+=24*60 
            
            #convert back into hours and mins
            hours = diff//60
            minutes= diff%60

            return{
                "result" : f"{hours} hours {minutes} minutes",

                #store internal reasoning steps (NOT for user directly)
                "steps": [ f"converted start time to minutes: {start}",
                          f"converted end time to minutes: {end}",
                          f"Difference: {diff} minutes"]

            }
        
    #CASE 2 : APPLE Problems

    if "apple" in question_lower:

        # extract all numbers from question
        numbers = list(map(int, re.findall(r'\d+', question)))

        if len(numbers) >= 1:
            red = numbers[0]  # first number = red apples

            # check if relationship keyword exists
        if "twice" in question_lower:
                green = 2 * red
        else:
                green = 0  # default fallback

        total = red + green

        return {
                "result": total,
                "steps": [
                    f"Red apples: {red}",
                    f"Green apples: {green}",
                    f"Total apples: {total}"
                ]
            }
        

    #CASE 3: SIMPLE MATH 
    # fallback: try evaluating arithmetic expressions
    try:
    # extract expression after "What is"
       if "what is" in question_lower:
          expression = question_lower.replace("what is", "").strip(" ?")

          result = eval(expression)

          return {
            "result": result,
            "steps": [
                f"Evaluated expression: {expression}"
            ]
          }
    except:
     pass


    #FALLBACK for fail case
    return{
        "result": None,
        "steps": ["Could not solve the problem"]
    }



