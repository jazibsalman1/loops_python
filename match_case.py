# def match_case(value):
#     match value:
#         case 1:
#             return "One"
#         case 2:
#             return "Two"
#         case _:
#             return "Something else"
# print(match_case(1))  # Output: One        
value = int(input("Enter a number (1 or 2): "))
match value:
    case 1:
        print("You entered One")
    case 2:
        print("You entered Two")
    case _:
        print("You entered something else")
# --- IGNORE ---