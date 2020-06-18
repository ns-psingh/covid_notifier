import requests
import main
import traceback

class CovidData:
    def __init__(self):
        """ Initalising state code - state name dict """
        url = "https://api.covid19india.org/state_district_wise.json"
        response = requests.get(url)
        state_data = response.json()
        self.states = {}
        state_names = state_data.keys()
        for state in state_names:
            self.states[state_data[state]["statecode"]] = state
        self.states_confirmed = {}
        self.states_recovered = {}
        self.states_active = {}
        return
    
    def retreive(self):
        url = "https://api.covid19india.org/v3/data.json"
        response = requests.get(url)
        states = []
        data = response.json()
        states = data.keys()
        for state in states:
            if 'delta' in data[state].keys():
                if not state in self.states_active.keys():
                    if 'confirmed' in data[state]['delta'].keys():
                        self.states_confirmed[state] = data[state]['delta']['confirmed']
                    if 'recovered' in data[state]['delta'].keys():
                        self.states_recovered[state] = data[state]['delta']['recovered']
                    if 'confirmed' in data[state]['total'].keys():
                        self.states_active[state] = data[state]['total']['confirmed']
                    if 'recovered' in data[state]['total'].keys():
                        self.states_active[state] = self.states_active[state] - data[state]['total']['recovered']
                    if 'deceased' in data[state]['total'].keys():
                        self.states_active[state] = self.states_active[state] - data[state]['total']['deceased']
                    try:
                        main_state_name = self.states[state]
                        main_state = self.states_active[state]
                        main_state_new = self.states_confirmed[state]
                        main_state_recovered = self.states_recovered[state]
                        print('{} {} {} {}'.format(main_state_name, main_state, main_state_new, main_state_recovered))
                    except Exception:
                        print('Error for State {} {}'.format(main_state_name, traceback.format_exc()))
                    #main.enqueue(main_state_name, main_state, main_state_new, main_state_recovered)
            else:
                print('{}'.format(state))
        

        
