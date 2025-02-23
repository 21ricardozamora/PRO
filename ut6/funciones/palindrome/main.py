def is_palindrome(text: str) -> bool:
    palindrome = True
    clean_text = text.replace(' ', '').lower()
    if clean_text[::-1] != clean_text:
        palindrome = False
    return palindrome


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_palindrome)
