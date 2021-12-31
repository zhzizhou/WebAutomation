from bupa.bupa import Bupa



def main():
    with Bupa() as bot:
        bot.land_first_page()
        bot.startFresh()
        print("Exiting....")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


