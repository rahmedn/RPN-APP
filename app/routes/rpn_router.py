from fastapi import APIRouter, HTTPException
from app.models.stack import Stack
from enum import Enum


router = APIRouter()
stacks = {}


class Operation(str, Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"


@router.get("/rpn/op")
async def list_operations():
    """
    List all available operations.

    Returns
    -------
    dict
        A dictionary containing a list of available operations.
    """
    return {"operations": [Operation.add, Operation.subtract, Operation.multiply, Operation.divide]}


@router.post("/rpn/op/{op}/stack/{stack_id}")
async def apply_operation_to_stack(op: Operation, stack_id: str):

    """
    Apply an operation to the specified stack.

    Parameters
    ----------
    op : Operation
        The operation to apply (add, subtract, multiply, divide).
    stack_id : str
        The ID of the stack to which the operation should be applied.

    Returns
    -------
    dict
        A dictionary containing a message indicating the operation was applied and the stack ID.
    """

    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack not found")

    stack = stacks[stack_id]

    try:
        if op == Operation.add:
            stack.add()

        elif op == Operation.subtract:
            stack.subtract()

        elif op == Operation.multiply:
            stack.multiply()

        elif op == Operation.divide:
            stack.divide()

        else:
            raise HTTPException(status_code=400, detail="Invalid operation")
    except IndexError:
        raise HTTPException(status_code=400, detail="Not enough elements in the stack, minimum two elements must exist in the stack")
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by 0 is not allowed")

    return {"message": "Operation applied", "stack": stack_id}


@router.post("/rpn/stack")
async def create_stack():
    """
    Create a new stack.

    Returns
    -------
    dict
        A dictionary containing a message indicating the stack was created and the stack ID.
    """

    stack_id = str(len(stacks) + 1)
    stacks[stack_id] = Stack()
    return {"message": "Stack created", "stack_id": stack_id}


@router.get("/rpn/stack")
async def list_stacks():
    return {"stacks": list(stacks.keys())}


@router.delete("/rpn/stack/{stack_id}")
async def clear_stack(stack_id: str):

    """
    Clear the specified stack.

    Parameters
    ----------
    stack_id : str
        The ID of the stack to clear.

    Returns
    -------
    dict
        A dictionary containing a message indicating the stack was cleared.
    """

    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack not found")

    stack = stacks[stack_id]
    stack.clear()
    return {"message": "Stack cleared"}


@router.post("/rpn/stack/{stack_id}")
async def push_value_to_stack(stack_id: str, value: float):
    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack not found")

    stack = stacks[stack_id]
    stack.push(value)

    return {"message": "Value added to stack", "stack": stack.items()}


@router.get("/rpn/stack/{stack_id}")
async def get_stack(stack_id: str):
    """
    Retrieve the items in the specified stack.

    Parameters
    ----------
    stack_id : str
        The ID of the stack to retrieve.

    Returns
    -------
    dict
        A dictionary containing the items in the stack.
    """
    if stack_id not in stacks:
        raise HTTPException(status_code=404, detail="Stack not found")

    stack = stacks[stack_id]
    return {"stack": stack.items()}









