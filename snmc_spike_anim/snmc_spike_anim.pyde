# first load a text file with the spike times of the assemblies. 
# next write types that transform those spikes into spikes of other elements. 
# setup will establish a location for the spikes to be shown. 
# create mux, wta, gate, and tik states. resampler states with num particles 
# as an input. KQ and KP will be a tracked variable. 
# A nice sampler can be made here out of simply random() 
# by 

from spike import Spike

spike_queue = []

num_particles = 3
y_spacing = 5


# will have a frame count. if a spike with that init time is present in a particle, 
# add it to the spike_queue. 




def setup():
    size(1000, 1000)
    background(255)
    noStroke()
    frameRate(60)
    particles = [Particle(i) for i in range(num_particles)]
    map(lambda x: x.populate_spikes, particles)

    
    
    
    
    
  #  spikes.append(Spike(width / 2, height / 2))
    
def draw():
    background(255)
    print("yo")
    for sp in spikes:
        print(sp.x)
        sp.move_in_time()
        sp.display()
        print(spikes)
        if sp.spike_finished():
            spikes.remove(sp)
    

    
