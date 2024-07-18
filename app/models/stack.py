class Stack:

    def __init__(self):
        self._stack = []

    def push(self, value):
        self._stack.append(value)

    def _pop(self):
        if not self._stack:
            raise IndexError("pop from an empty stack")
        return self._stack.pop()

    """
    Apply the operation op on the two recent elements of the stack.
    
    Args:
        op (function): arithmetic operation to apply.
    """
    def _opp(self, op):
        # supposed that the operations op is a binary operation (minimum two elements must exist in the stack)
        if len(self._stack) < 2:
            raise IndexError("not enough elements")
        b = self._pop()
        a = self._pop()
        result = op(a, b)
        self.push(result)
        return result

    def add(self):
        op = lambda x, y: x + y
        return self._opp(op)

    def subtract(self):
        """
        Performs subtraction on the top two elements of the stack.
        """
        op = lambda x, y: x - y
        self._opp(op)

    def multiply(self):
        """
        Performs multiplication on the top two elements of the stack.
        """
        op = lambda x, y: x * y
        self._opp(op)

    def divide(self):
        """
        Performs division on the top two elements of the stack.
        """
        if len(self._stack) < 2:
            raise IndexError("not enough elements")
        b = self._pop()
        a = self._pop()
        if b == 0:
            raise ZeroDivisionError("division by zero")
        result = a / b
        self.push(result)
        return result

    def items(self):
        """
        Returns the current items in the stack.

        Returns
        -------
        list
            A list of the current items in the stack.
        """
        return self._stack

    def clear(self):
        """
        Clears the stack.
        """
        self._stack = []


