from success import (
    setParseSuccessPos,
    setParseSuccessTree,
    setParseSuccessRemainder,
    parseSuccessPos,
    parseSuccessTree,
    parseSuccessRemainder,
    initialParseState,
    updateParseSuccess
)


from error import (
    ParseError,
    setParseErrorPos,
    setParseErrorMsg,
    parseErrorPos,
    parseErrorMsg,
    mergeErrors,
    mergeErrorsMany
)




def isParseSuccess(state):
    return hasattr(state, 'tree')


def isParseError(state):
    return not isParseSuccess(state)


def mplusStates(state1, state2):
    '''If at least one of the states is ParseSuccess, return the first one.
    Otherwise, merge errors'''
    if isParseSuccess(state1):
        return state1
    elif isParseSuccess(state2):
        return state2
    else:
        return mergeErrors(state1, state2)



def mplusStatesMany(*states):
    return reduce(mplusStates, states)



def parseErrorFromSuccessState(state, errorMsg):
    '''Creates a ParseError from a previos state (of type ParseSuccess)'''
    return ParseError(parseSuccessPos(state), errorMsg)