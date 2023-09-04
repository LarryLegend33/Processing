# first load a text file with the spike times of the assemblies. 
# next write types that transform those spikes into spikes of other elements. 
# setup will establish a location for the spikes to be shown. 
# create mux, wta, gate, and tik states. resampler states with num particles 
# as an input. KQ and KP will be a tracked variable. 
# A nice sampler can be made here out of simply random() 
# by 

from spike import Spike, Particle 

spike_queue = []
num_particles = 1
# will have a frame count. if a spike with that init time is present in a particle, 
# add it to the spike_queue. 

def setup():
 #   global spike_queue
    size(1000, 1000)
    background(255)
    noStroke()
    frameRate(60)
   # print(spike_queue)
    particles = [Particle(i) for i in range(num_particles)]
    for p in particles:
        p.populate_assemblies()
        p.run_snmc()
        p.populate_wta_and_scoring()
        spike_queue.append(p.all_spikes[0])
       

  #  spikes.append(Spike(width / 2, height / 2))
    
def draw():
    print("drawing")
    background(255)
   # print("yo")
    for sp in spike_queue:
        print(sp.x)
        sp.move_in_time(frameCount)
        sp.display(frameCount)
        if sp.spike_finished(frameCount):
            spike_queue.remove(sp)
    

    
