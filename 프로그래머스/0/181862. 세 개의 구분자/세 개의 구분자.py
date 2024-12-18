import re
def solution(myStr):
    result = [part for part in re.split(r'[abc]', myStr) if part]
    return result if result else ["EMPTY"]
    