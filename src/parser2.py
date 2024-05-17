import string

class Parser2:
    def _tokenizer(self, data: str):
        """
        Tokenizes the data.
        """

        tokens = []

        i = 0

        while i < len(data):
            char = data[i]

            if char in ' \t':
                i += 1
            elif char in '{}[]:,':
                tokens.append(char)
                i += 1
            # strings
            elif char == '"':
                start = i
                i += 1

                while i < len(data):
                    if data[i] == '"':
                        # Count the number of consecutive backslashes before this quote
                        backslashes = 0
                        j = i - 1
                        while j >= 0 and data[j] == '\\':
                            d = data[j]
                            backslashes += 1
                            j -= 1
                        if backslashes % 2 == 0:
                            # Even number of backslashes means the quote is not escaped
                            break
                    i += 1

                i += 1

                tokens.append(data[start:i])
            # digits
            elif char.isdigit() or char in '-':
                start = i
                i += 1

                while i < len(data) and data[i].isdigit() or data[i] in '+-.eE':
                    i += 1

                d = data[start:i]

                tokens.append(data[start:i])
            # true/false/null
            elif char in 'tfn':
                start = i
                i += 1

                if data[start] in 'tn':
                    if i+3 < len(data) and data[i:i+3] in ('rue', 'ull'):
                        tokens.append(data[start:i+3])
                        i += 3
                elif data[start] == 'f':
                    if i+4 < len(data) and data[i:i+4] == 'alse':
                        tokens.append(data[start:i+4])
                        i += 4
            else:
                i += 1

        for token in tokens:
            print(token)

# write code to read in test.json and parse into an object
with open('test.json', 'r') as f:
    data = f.read()

p = Parser2()

p._tokenizer(data)