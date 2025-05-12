
def check_status_code(status_code: int) -> str:
    data_status_code = {
        '1': "Informational responses(100 – 199)",
        '2': "Successful responses(200 – 299)",
        '3': "Redirection messages(300 – 399)",
        '4': "Client error responses(400 – 499)",
        '5': "Server error responses(500 – 599)"
    }
    return data_status_code.get(str(status_code)[0], "Unknown error")


def check_status_code_use_match(status_code):
    match status_code:
        case 100:
            return "Informational responses(100 – 199)"
        case 200:
            return "Successful responses(200 – 299)"
        case 300:
            return "Redirection messages(300 – 399)"
        case 400:
            return "Client error responses(400 – 499)"
        case 500:
            return "Server error responses(500 – 599)"
        case _:
            return "Unknown error"


if __name__ == '__main__':
    print(check_status_code(200))