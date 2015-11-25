
def _isPalindrome_(str):

    if str:
        str = str.replace(' ','').lower()
        rev =''
        for char in str:
            rev = char+rev
        if rev == str:
            return True
        else:
            return False

    else:
       print('Empty String')
bool = _isPalindrome_('rad ar')
print(bool)