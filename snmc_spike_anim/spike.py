class Spike():
    
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.x = start_x
        self.y = start_y
        self.speed = 1
        self.spike_height = 50
        self.spike_stroke = 0
        self.spike_strokeweight = 3
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
        
    
        

class Particle:
    def __init__(self, id):
        self.assemblies = {"q1_1": [], 
                           "q2_2": [], 
                           "p1_1": [],
                           "p2_2": []}
        self.mux = {"q1": [], 
                    "p1": []}
        self.wta = {"wta1": [],
                    "wta2": []}        
        self.normalizer = []
        self.resampler = []
        

def particle_assembly_activity(particle):
    # here populate the assembly dict with a binary vector 
    return particle 
    
