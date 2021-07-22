import time
import keyboard
from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession

target = input("User ID: ")


# Sample : 748482011446116403

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def rob_someone(id):
    keyboard.write('*rob ' + id)
    keyboard.press_and_release('enter')


with FuturesSession() as session:
    print()
    print('Press "down" to start the script...')

    keyboard.wait('down')
    print('Starting the Script...')
    print()

    url = "https://unbelievaboat.com/api/v1/guilds/769974708312473610/users/{0}".format(target)
    headers = {
        "Authorization": "<insert auth id here>"}

    while not keyboard.is_pressed("esc"):

        futures = [session.get(url, headers=headers, stream=False)]
        for future in as_completed(futures):
            response = future.result()
            response = str(response.content)
            with_out_the_b = response[1:]
            cash = find_between(with_out_the_b, '"cash":', ',')
            print('Current Balance: {0}'.format(cash))

            if cash.isdigit():
                if int(cash) >= 2000000000:
                    rob_someone(target)
                    exit()
            else:
                print()
                print("Something went wrong.")
                print("LOGS: " + with_out_the_b)
                retry_time = find_between(with_out_the_b, '"retry_after":', '}')
                print('Pausing the script for 0.{0} ms'.format(retry_time))
                time.sleep(0. + int(retry_time))
                print('You can now rob again, press down to continue...')
                keyboard.wait('down')
