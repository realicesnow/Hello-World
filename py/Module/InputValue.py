def input_value(input_msg, error_msg=None, is_int=True, ran=(1, 0)):
    while True:
        try:
            value = int(input(input_msg)) if is_int else float(input(input_msg))
            if ran[0] > ran[1]:
                return value
            if value < ran[0] or value > ran[1]:
                raise Exception()
            return value
        except Exception:
            if error_msg != None:
                print(error_msg)
