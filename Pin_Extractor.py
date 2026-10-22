#Pin Extractor 
def pin_extractor(poems):
    # Create an empty list to store all extracted PINs
    secret_codes = []

    # Loop through each poem in the poems list
    for poem in poems:
        # Start with an empty PIN for the current poem
        secret_code = ''

        # Split the poem into separate lines
        lines = poem.split('\n')

        # Loop through each line and its index number
        for line_index, line in enumerate(lines):
            # Split the line into individual words
            words = line.split()

            # Check if there is a word at the current line index
            if len(words) > line_index:
                # Add the length of that word to the secret code
                secret_code += str(len(words[line_index]))
            else:
                # If no word exists at that position, add 0
                secret_code += '0'

        # Add the completed secret code to the list
        secret_codes.append(secret_code)

    # Return all secret codes
    return secret_codes


# Example poems
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = """The grass is green
here and there
hoping for rain
before it turns yellow"""

poem3 = """There
once
was
a
dragon"""

# Store all poems in a list
poems = [poem, poem2, poem3]

# Extract and print the secret codes for all poems
print(pin_extractor(poems))