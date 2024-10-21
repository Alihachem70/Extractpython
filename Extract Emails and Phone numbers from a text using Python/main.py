import pyperclip
import re

# Regular expression for Lebanese phone numbers
lebaneseNumber = re.compile(r'''(
    (\+961)?                    # Country code (optional)
    (\s|-)?                     # Separator (optional)
    (\d{3})                     # First three digits
    (\s|-)?                     # Separator (optional)
    (\d{3})                     # Next three digits
    (\s|-)?                     # Separator (optional)
    (\d{3})                     # Last three digits
)''', re.VERBOSE)

# Regular expression for Lebanese email addresses
lebaneseEmailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # Username
    @                           # @ symbol
    [a-zA-Z0-9.-]+              # Domain name
    \.                          # Dot
    (com|org|net|gov|edu)       # Top-level domain
)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
phone_matches = lebaneseNumber.findall(text)
email_matches = lebaneseEmailRegex.findall(text)

matched_info = []

# Append phone numbers to matched_info
for match in phone_matches:
    matched_info.append(''.join(match))

# Append email addresses to matched_info
for match in email_matches:
    matched_info.append(match[0])

if len(matched_info) > 0:
    # Copy matched items to clipboard again
    pyperclip.copy('\n'.join(matched_info))
    print('Copied to clipboard!\n')
    # Print matched items
    print('\n'.join(matched_info))
else:
    print('No phone numbers or emails found for Lebanon.')
