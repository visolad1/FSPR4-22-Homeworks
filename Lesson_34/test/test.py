import requests
import hashlib
import sys


def request_api_data(query_param):
    url = "https://api.pwnedpasswords.com/range/" + str(query_param)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fatching: {res.status_code}, check an API and try again"
        )
    return res

def get_psw_leaks_count(hashes, hash_to_check):
    hashes = (hash.split(':') for hash in hashes.splitlines())

    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1_password[:5], sha1_password[5:]

    response = request_api_data(first5_char)

    return get_psw_leaks_count(response.text, tail)

def main(passwords):
    for psw in passwords:
        count = pwned_api_check(psw)
        if count:
            print((f"{psw} was found {count} times"))
        else:
            print(f"{psw} was not found")

    return "Success"

def get_passwords(file):
    with open(file, 'r') as file:
        passwords = file.readlines()
        passwords = (psw.replace('\n', '') for psw in passwords)
    
    return list(passwords)

if len(sys.argv) < 2:
    print("Необходимо передать список паролей в командной строке.")
    sys.exit()

passwords = sys.argv[1:]

main(get_passwords('test.txt'))
main(passwords)