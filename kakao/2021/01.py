import string

def is_available(s: str):
    available_char = string.ascii_lowercase + string.digits + '-' + '_' + '.'
    for c in s:
        if c not in available_char:
            return False
    return True


def check(new_id: str):
    # Check the length of new id
    if len(new_id) <3 or len(new_id) > 15:
        print('Too short or too long')
        return False
    
    # Check the character avilability of new id
    no_overlap = ''.join(set(new_id))
    # for c in no_overlap:
    #     if c not in available_char:
    #         print('Not available character')
    #         return False
    if not is_available(no_overlap):
        print('Not available character')
        return False

    # Check where '.' exists and if consecutive '.' exists
    if new_id[0] == '.' or new_id[len(new_id) - 1] == '.':
        print('First or last hot point')
        return False
    for i in range(len(new_id)):
        if new_id[i] == '.':
            if new_id[i + 1] == '.':
                print('Consecutive hot point')
                return False
    
def to_lowercase(new_id: str):
    return new_id.lower()
        
def remove_unavailable(new_id: str):
    filtered = ''.join(filter(is_available, new_id))
    return filtered

def remove_consecutive_hot_point(new_id: str):
    while new_id.find('..') != -1:
        new_id = new_id.replace('..', '.')
    return new_id

def remove_first_last_hot_point(new_id: str):
    new_id = new_id.lstrip('.').rstrip('.')
    return new_id

def add_a(new_id: str):
    if len(new_id) == 0:
        return "a"
    return new_id

def cut_over_length(new_id: str):
    if len(new_id) >= 16:
        new_id = new_id[:15]
        return remove_first_last_hot_point(new_id)
    return new_id

def make_longer(new_id: str):
    while len(new_id) <= 2:
        new_id += new_id[len(new_id) - 1]
    return new_id


def solution(new_id):
    ok = check(new_id)
    answer = ''
    if not ok:
        answer = make_longer(cut_over_length(add_a(remove_first_last_hot_point(remove_consecutive_hot_point(remove_unavailable(to_lowercase(new_id)))))))
    return answer

print(solution('...!@BaT#*..y.abcdefghijklm'))