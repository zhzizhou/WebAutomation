import time

from bupa.bupa import Bupa
# now i am completing the other half of the project on macintosh


def main():
    with Bupa() as bot:
        print("starting the selenium driver...")
        time.sleep(1)
        print("initialising the automation...")
        time.sleep(1)
        bot.land_first_page()
        bot.startFresh()
        bot.newIndividual()
        bot.select_centre()
        print("Exiting....")
        time.sleep(100)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


