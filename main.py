def get_stack_key():
    try:
        import os

        return os.environ["STACK_KEY"]
    except KeyError:
        return None


if __name__ == "__main__":
    key = get_stack_key()

    from api.stackoverflow import SAILClient

    client = SAILClient(key=key)

    print([question["title"] for question in client.get_ten_newest_questions()])
