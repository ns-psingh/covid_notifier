import requests
import notifiy_mgr
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
        print("Retry")
        url = "https://api.covid19india.org/v3/data.json"
        response = requests.get(url)
        states = []
        data = response.json()
        states = data.keys()
        for state in states:
            if 'delta' in data[state].keys():
                if not state in self.states_active.keys():
                    if state == "TT":
                        continue
                    main_state = 0
                    main_state_new = 0
                    main_state_recovered = 0
                    if 'confirmed' in data[state]['delta'].keys():
                        self.states_confirmed[state] = data[state]['delta']['confirmed']
                        main_state_new = self.states_confirmed[state]
                    if 'recovered' in data[state]['delta'].keys():
                        self.states_recovered[state] = data[state]['delta']['recovered']
                        main_state_recovered = self.states_recovered[state]
                    if 'confirmed' in data[state]['total'].keys():
                        self.states_active[state] = data[state]['total']['confirmed']
                        main_state = self.states_active[state]
                    if 'recovered' in data[state]['total'].keys():
                        self.states_active[state] = self.states_active[state] - data[state]['total']['recovered']
                        main_state = self.states_active[state]
                    if 'deceased' in data[state]['total'].keys():
                        self.states_active[state] = self.states_active[state] - data[state]['total']['deceased']
                        main_state = self.states_active[state]
                    try:
                        main_state_name = self.states[state]
                        print('{} {} {} {}'.format(main_state_name, main_state, main_state_new, main_state_recovered))
                        notifiy_mgr.enqueue(main_state_name, main_state, main_state_new, main_state_recovered)
                    except Exception:
                        print('Error for State {} {}'.format(main_state_name, traceback.format_exc()))
        

        
