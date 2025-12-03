# Example Program: Web Status Codes with match-case (better version using OR |)

status = int(input("Enter http status code: "))

match status:
    case 200 | 201 | 202 | 203 | 204:
        print("Success")
    case 300 | 301 | 302 | 303:
        print("Additional Action Required")
    case 400 | 401 | 402 | 403 | 404 | 405:
        print("Client Error")
    case 500 | 501 | 502 | 503 | 504 | 505:
        print("Server Error")
    case _:
        print("Undefined")