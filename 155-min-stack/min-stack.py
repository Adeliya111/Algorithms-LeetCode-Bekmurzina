class MinStack:
    def __init__(sf):
        sf.stack = []  #стек
        sf.min_stack = []  #стек для минимумов

    def push(sf, val: int) -> None:
        sf.stack.append(val)
        #если стек минимумов пуст или новое значение меньше текущего минимума
        if not sf.min_stack or val <= sf.min_stack[-1]:
            sf.min_stack.append(val)

    def pop(sf) -> None:
        if sf.stack:
            val = sf.stack.pop()
            #если удаляется текущий минимум, то и в min_stack
            if sf.min_stack and val == sf.min_stack[-1]:
                sf.min_stack.pop()

    def top(sf) -> int:
        return sf.stack[-1] if sf.stack else None

    def getMin(sf) -> int:
        return sf.min_stack[-1] if sf.min_stack else None