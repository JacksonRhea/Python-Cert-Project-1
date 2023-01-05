def arithmetic_arranger(problems, solution=False):

    if len(problems) > 5:
      return "Error: Too many problems."
  
    arranged_problems = ''
    topLine = ''
    midLine = ''
    bottomLine = ''
    solLine = ''
    midCount = 0
    midSpace = ''
    longestProblem = 0
    problemList = []
    spaceCount = 0
    between = '    '
    solBet = ''
    solAdd = ''
    count = 0
    betCount = 0
    
    for elements in problems:
      arranged_problems = arranged_problems + " " + problems[count]
      count += 1

    problemList = problemList + arranged_problems.split(' ')
    
    for element in problemList:
      if (element == ''):
        problemList.remove(element)

    for element in problemList:
      if len(element) > 4:
        return "Error: Numbers cannot be more than four digits."

    errorCount = 0
    test = 0
    question = [3, '+', 7]
    while errorCount < len(problemList) / 3:
      question[0] = problemList[test]
      test += 1
      question[1] = problemList[test]
      test += 1
      question[2] = problemList[test]
      test += 1
      
      try:
        int(question[0])
        int(question[2])
      except:
        return "Error: Numbers must only contain digits."

      if question[1] == '+':
        answer = int(question[0]) + int(question[2])
      else:
        if question[1] != '-':
          return "Error: Operator must be \'+\' or \'-\'."
        else:
          answer = int(question[0]) - int(question[2])
        
      if len(question[0]) >= len(question[2]):

        spaceCount = len(question[0])
        longestProblem = len(question[0])
        while spaceCount < longestProblem + 2:
          topLine = topLine + ' '
          spaceCount += 1
        topLine = topLine + question[0]

        if betCount < len(problems) - 1:
          topLine = topLine + between

        spaceCount = 0
        if (len(question[2]) >= len(question[0])):
          midSpace = ' '
        else:
          midSpace = ' '
          midCount = len(question[0]) - len(question[2])
          while spaceCount < midCount:
            midSpace = midSpace + ' '
            spaceCount += 1
          
        midLine = midLine + question[1] + midSpace + question[2]

        if betCount < len(problems) - 1:
          midLine = midLine + between
        
        spaceCount = 0
        while spaceCount < longestProblem + 2:
          bottomLine = bottomLine + '-'
          spaceCount += 1
        if betCount < len(problems) - 1:
          bottomLine = bottomLine + between

        solBet = (longestProblem + 2) - len(str(answer))
        solAdd = ''
        spaceCount = 0
        while spaceCount < solBet:
          solAdd = solAdd + ' '
          spaceCount += 1
        
        solLine = solLine + solAdd + str(answer)
        if betCount < len(problems) - 1:
          solLine = solLine + between
        errorCount += 1
        betCount += 1
        
      else:

        longestProblem = len(question[2])
        spaceCount = len(question[0])
        
        while spaceCount < longestProblem + 2:
          topLine = topLine + ' '
          spaceCount += 1
        topLine = topLine + question[0]
        if betCount < len(problems) - 1:
          topLine = topLine + between

        spaceCount = 0
        if (len(question[2]) >= len(question[0])):
          midSpace = ' '
        else:
          
          midSpace = ' '
          midCount = len(question[0]) - len(question[2])
          while spaceCount < midCount:
            midSpace = midSpace + ' '
            spaceCount += 1
            
        midLine = midLine + question[1] + midSpace + question[2]
        if betCount < len(problems) - 1:
          midLine = midLine + between
        
        spaceCount = 0
        while spaceCount < longestProblem + 2:
          bottomLine = bottomLine + '-'
          spaceCount += 1
        if betCount < len(problems) - 1:
          bottomLine = bottomLine + between
        
        solBet = (longestProblem + 2) - len(str(answer))
        solAdd = ''
        spaceCount = 0
        while spaceCount < solBet:
          solAdd = solAdd + ' '
          spaceCount += 1
        
        solLine = solLine + solAdd + str(answer)
        if betCount < len(problems) - 1:
          solLine = solLine + between
        errorCount += 1
        betCount += 1
        
    #if solution != False:
      #print(topLine + '\n' + midLine + '\n' + bottomLine + '\n' + solLine)
    #else:
      #print(topLine + '\n' + midLine + '\n' + bottomLine)
        
    arranged_problems = ''
    
    if solution != False:
      arranged_problems = topLine + '\n' + midLine + '\n' + bottomLine + '\n' + solLine
    else:
      arranged_problems = topLine + '\n' + midLine + '\n' + bottomLine
    
    return arranged_problems
