import covid_data as cd
import time

if __name__ == "__main__":
    covid = cd.CovidData()
    while True:
        covid.retreive()
        time.sleep(10)