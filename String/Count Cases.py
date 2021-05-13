#Example  input : This WorlD Is Full Of OpportunTiES  output : lower,upper , othercase
print("")


def counting_char():
    data = "This WorlD Is Full Of OpportunTiES"
    count_lower = count_upper = count_other = 0
    for ch in data:
        if ch >= 'a' and ch <= 'z':
            count_lower += 1
        elif ch >= 'A' and ch <= 'Z':
            count_upper += 1
        else:
            count_other += 1
    print(f'No of lowercase: {count_lower}')
    print(f'No of uppercase: {count_upper}')
    print(f'No of othercase: {count_other}')


if __name__ == "__main__":
    counting_char()
