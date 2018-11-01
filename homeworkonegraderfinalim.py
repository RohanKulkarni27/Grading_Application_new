a = " "

def homeworkone(a):
    ## inports the file to store it in the 2nd var
    #a = input('Type the file name to input: ')
    #gradefileimported = importlib.__import__(gradefilename)
    gradefile = open(a)
    with open(a) as f:
        gradefiler = list(f)
        ##print(gradefiler)
    gradefilers = ''.join(gradefiler)

    answer = open('homeworkanswerone.py')
        ##cheatfiler = cheatfile.read
    with open('homeworkanswerone.py') as f:
        answerr = list(f)
    answerrs = ''.join(answerr)

    ## create the holder for the grader
    __assignmentgrade = 0


    ## check if it complies, this works and grades a 0
    try:
        py_compile.compile(a)
        doesreturn = py_compile.compile(a,doraise=True)
        #print(doesreturn)
    except:
        print("Your homework has errors. Please try again.")
        __grade = 0;
        print("You have a grade of " + str(__grade))

    __count = 0
    __answercount = 0
    __assignmentgrade = 0
    __variablecount = 0

    __variablecount = answerrs.count(" = ")
    __count = a.count(" = ")

    #5 var
    if __count >= __answercount :
        __assignmentgrade = 60
    elif __count < __answercount:
        __assignmentgrade = __count*12
        print("You don't have enough variables")
    #elif __count > __answercount:
        #__assignmentgrade = 80 - (__count*12)
        #print("You have too many variables")

    # one comment
    __commentcount = answerrs.count(" # ")
    __ccount = a.count(" # ")

    #istherec = False

    if __ccount >= __commentcount :
        __assignmentgrade = __assignmentgrade + 20
        #istherec = True
    elif __ccount < __commentcount:
        __assignmentgrade = __count*4
        print("You don't have any comments.")

    #if istherec:
        #__assignmentgrade = __assignmentgrade + 20

    #elif __ccount > __commentcount:
        #__assignmentgrade = __assignmentgrade - (__count*4)
        #print("You have too many comments.")

    #find the places before the =, and store it in a list
    # if it has 2 matching values = it is true.
    for grade in gradefiler:
        if any("=" in s for s in gradefiler):
            #startpos = gradefiler.index("=")
            variables = gradefiler[0:len(gradefiler) - 1] #gradefiler[:startpos]

    seen = []

    isthere = False

    for variable in variables:
        if variable in seen:
            #__assignmentgrade = __assignmentgrade + 20
            isthere = True
            #print(variable)
        else:
            seen.append(variable)
            #print(variable)

    if isthere:
        __assignmentgrade = __assignmentgrade + 20

    print("Your grade is right now equal to " + "%" + str(__assignmentgrade) + " You can accept this grade or send it to blackboard.")
    return __assignmentgrade
#homeworkone(a)

def checkcheat(a,b):
    __count = 0
    __answercount = 0
    __similar = 0


    cheatfile = open(a)
    with open(a) as f:
        cheatfiler = list(f)
    cheatfilers = ''.join(cheatfiler)

    a = open(b)
    with open(b) as f:
        a = list(f)
    a = ''.join(cheatfiler)

    if a != b:
        for word in range(len(a)):
            #print(a)
            for wordt in range(len(b)):
                #print(b)
                __similar = a[word].count(b[wordt])
                if __similar >= 45:
                    __didcheat = True
                else:
                    __didcheat = False

        #__answercount = len(cheatfilers)
        #__count = len(a)
        #__similar = (__count/__answercount) * 100
        #__didcheat = False
    #print(str(__answercount))
    #print(str(__count))
    #print(__similar)
        #if __similar >= 75:
        #print("Your file is very similar to someone else's. You have been reported for cheating. ")
            #__didcheat = True
    #else:
        #__didcheat = False

    return __didcheat
