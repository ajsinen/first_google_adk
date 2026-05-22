from repositories.todo_repo import insert_todo


async def create_todo(title: str):

    # business rule example
    if len(title.strip()) < 3:
        return {
            "success": False,
            "message": "Todo title too short"
        }

    todo = await insert_todo(title)

    return {
        "success": True,
        "todo": dict(todo)
    }