import math 


class Spike():
    
    def __init__(self, start_x, start_y, spike_init_time, spike_height):
        self.start_x = start_x
        self.x = start_x
        self.y = start_y
        self.speed = 1
        self.init_time = spike_init_time
        self.spike_height = spike_height
        self.spike_stroke = 0
        self.spike_strokeweight = 1
        self.end_time_axis = 200
        
    def move_in_time(self):
        self.x = self.x + self.speed
        
    def spike_finished(self):
        return self.x > (self.start_x + self.end_time_axis)
        
    def display(self):
       stroke(self.spike_stroke)
       strokeWeight(self.spike_strokeweight)
       line(self.x, self.y, self.x, self.y + self.spike_height)
       fill(0, 0)
       
       #rect(self.x, self.y, 20, self.spike_height)  

# in Particle, you make a spike object for each element. 
# In the ElectrodeLocation class, parse according to P and Q? 

# try to make this flexible so that you could eventually have the 
# assemblies be generated on the fly. start with something very simple like a bernoulli draw.  

class Particle:
    def __init__(self, id):
        self.length_of_simulation = 2000
        self.neurons_per_assembly = 2
        self.kq = 5
        self.kp = 10
        self.num_states = 2 
        # can make this amenable to larger assembly sizes and more latents. 
        # hand code for now. 
        self.assembly_indices = ["q0", "q1", "p0", "p1"]   
        self.assemblies = {i : [] for i in assembly_indices}
        self.mux = {"q": [], 
                    "p": []}
        self.tik = {"q": [], 
                    "p": []}
        self.accum = {"q": []}
        self.wta = {"0": [],
                    "1": []}      
        self.normalizer = []
        self.resampler = []
        self.all_spikes = []
        
    
    def populate_assemblies(self):        
        sim_params = [random(0, .2) for i in self.assembly_indices]
       # assembly_params = [s for s in sim_params for _ in (0, self.neurons_per_assembly)]
        print(assembly_params)
        for ai, sp in zip(self.assembly_indices, sim_params):
            self.assemblies[ai] = [[bernoulli(sp) for i in range(self.length_of_simulation)] 
                                   for n in range(self.neurons_per_assembly)] 
                    
    def run_snmc(self):
        state = float("Nan")
        for t in range(self.length_of_simulation):
            if math.isnan(state):
                state = self.detect_winner(t)            
                            
            if not math.isnan(state):
                self.mux["q"].append(find_spikes_in_assemblies(t, "q" + str(state)))
                self.mux["p"].append(find_spikes_in_assemblies(t, "q" + str(state)))
                self.wta[state].append(1)
                self.wta[!state].append(0)
                
            else:
                self.mux["q"].append(0)
                self.mux["p"].append(0)
                self.wta[0].append(0)
                self.wta[1].append(0)
            
          
    def detect_winner(self, time):
        spike_in_0 = self.find_spikes_in_assemblies(time, "q0")
        spike_in_1 = self.find_spikes_in_assemblies(time, "q1")
        if spike_in_0 and not spike_in_1:
            return 0 
        elif spike_in_1 and not spike_in_0:
            return 1
        elif spike_in_1 and spike_in_2:
            return bernoulli(.5) 
        else:
            return float("NaN")
        
    def find_spikes_in_assemblies(self, time, assembly):
        spikes = sum([self.assemblies[assembly][i][time] for i in self.neurons_per_assembly])
        return spikes
        
    def populate_spikes(self):
    
        spike_height = 4
        spacing = 1
        cortex_x = 300
        cortex_y = 300
        # elements have to be arranged in y-order        
        elements = [self.wta[0], self.wta[1]] + [self.assemblies[pq + pq_ind][n_id] for pq in ["p", "q"] for n_ind in range(
                                                 self.neurons_per_assembly) for pq_ind in range(self.num_states)] + [self.mux["p"], self.mux["q"]]
    
        sp_train_ylocs = range(cortex_y, cortex_y + ((spike_height + spacing) * len(elements)))
        
        for i, elem in enumerate(elements):
            assign_spikes(elem, cortex_x, sp_train_ylocs(i), spike_height)
        
                    
    def assign_spikes(self, spikelist, x, y, spike_height):
        self.all_spikes += [Spike(x, y, t, spike_height) if spikelist[t] != 0 for t in range(len(self.length_of_simulation))]
          
                
        
def bernoulli(p):
    d = random(0, 1)
    if d < p:
        return 1
    else: 
        return 0
    
    
    
