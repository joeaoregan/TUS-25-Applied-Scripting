 # Example Program: Web Status Codes with match-case (simple version)

status = int(input("Enter http status code: "))

match status:
    case 200:
        print("OK - Request succeeded")
    case 400:
        print("Bad Request - The server could not understand the request")
    case 401:
        print("Unauthorized - Authentication required")
    case 403:
        print("Forbidden - You do not have permission")
    case 404:
        print("Not Found - The requested resource does not exist")
    case 500:
        print("Internal Server Error - Something went wrong on the server")
    case 503:
        print("Service Unavailable - Server temporarily unavailable")
    case _:
        print("Other status code - unhandled case")
    