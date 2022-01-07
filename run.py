import time

from bupa.bupa import Bupa
# now i am completing the other half of the project on macintosh
def automation():
    print("starting the selenium driver...")
    time.sleep(2)
    print("initialising the automation...")
    time.sleep(3)

    print("Accessing the Bupa Website ")
    time.sleep(3)

def exiting():
    print("Reacting the end of automation")
    print("Exiting the program")


def main():
    with Bupa() as bot:
        automation()
        bot.land_first_page()
        bot.startFresh()
        bot.newIndividual()
        bot.select_centre()
        bot.select_assessments()
        bot.earliest_time()
        exiting()
        # this line of code needs simplification
        # try to work out an alternative making the command line automation

        time.sleep(50)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


