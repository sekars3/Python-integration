from asyncio import tasks


def create_parallel_json(tasks):
    if not tasks:
        return None

    child_parts = []

    for task in tasks:
        # create the current child part
        # print(task)
        if task['label']:
            child_part = {
                "partType": "PARALLEL",
                "planPartTaskId": task['label']
            }
            child_parts.append(child_part)

    return child_parts


def create_nested_json(tasks):
    if not tasks:
        return None

    nested_json = {}
    # print(tasks)

    first_task = tasks.pop(0)
    try:
        nested_json = {
            "partType": first_task["condition"].upper(),
            "planPartTaskId": first_task["label"],
            "useParalle": False
        }
    except KeyError as e:
        print('Can not find:', e.args[0])

    if tasks:
        nested_json["childParts"] = [create_nested_json(tasks)]

    return nested_json


def create_plan_parts(tasks):
    planParts = []

    if not tasks:
        return None

    try:
        print("Processing root node")
        root = tasks["root"]
        if root[0]["parallel"]:
            plan = root[0]["parallel"]
            childParts = create_parallel_json(plan)
            planParts = {"childParts": childParts}
    except KeyError as e:
        print('Can not find:', e.args[0])

    print("Processing on_ok node")
    try:
        on_ok = tasks["on_ok"]
        if on_ok[0]["sequential"]:
            sequential = on_ok[0]["sequential"]
            on_ok_json = {
                "childParts": [create_nested_json(sequential)]
            }
            planParts["childParts"].append(on_ok_json)

    except KeyError as e:
        print('Can not find:', e.args[0])

    try:
        on_ok = tasks["on_ok"]
        if on_ok[0]["parallel"]:
            parallel = on_ok[0]["parallel"]
            on_ok_json = {
                "childParts": create_parallel_json(parallel),
                "useParalle": True,
                "partType": "NONE"
            }
            planParts["childParts"].append(on_ok_json)

    except KeyError as e:
        print('Can not find:', e.args[0])

    print("Processing on_error node")

    try:
        on_error = tasks["on_error"]
        if on_error[0]["sequential"]:
            sequential = on_error[0]["sequential"]
            on_error_json = {
                "childParts": [create_nested_json(sequential)]
            }
            planParts["childParts"].append(on_error_json)

    except KeyError as e:
        print('Can not find:', e.args[0])

    try:
        on_error = tasks["on_error"]
        if on_error[0]["parallel"]:
            parallel = on_error[0]["parallel"]
            on_error_json = {
                "childParts": create_parallel_json(parallel),
                "useParalle": True,
                "partType": "NONE"

            }
            planParts["childParts"].append(on_error_json)

    except KeyError as e:
        print('Can not find:', e.args[0])

    return planParts
