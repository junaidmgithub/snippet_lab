import string, random

def generate_invite_code(length=15):
    model = get_user_model()
    code = ''.join([random.choice(string.ascii_letters +
                                  string.digits + '_') 
                    for _ in range(length)])
    try:
        model.objects.get(invite_code=code)
        return generate_invite_code()
    except:
        pass
    return code
