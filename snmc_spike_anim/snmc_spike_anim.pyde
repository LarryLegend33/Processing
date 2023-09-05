# first load a text file with the spike times of the assemblies. 
# next write types that transform those spikes into spikes of other elements. 
# setup will establish a location for the spikes to be shown. 
# create mux, wta, gate, and tik states. resampler states with num particles 
# as an input. KQ and KP will be a tracked variable. 
# A nice sampler can be made here out of simply random() 
# by 

from spike import Spike, Particle, electrode 

spike_queue = []
num_particles = 1
v1_electrode = (490, 300, 100, 100)
cp_electrode = (300, 200, 100, 100)
gpi_electrode = (200, 200, 100, 100)
lp_electrode = (200, 200, 100, 100)
brain_location = (200, 300, 400, 400)

# will have a frame count. if a spike with that init time is present in a particle, 
# add it to the spike_queue. 

def setup():
    global brain, electrode_l, electrode_r 
    size(1200, 800)
    background(0)
    noStroke()
    frameRate(60)
    brain = loadImage("MouseBrain.png")
    electrode_r = loadImage("Electrode.png")
    electrode_l = loadImage("Electrode_Reflected.png")
    image(brain, *brain_location)
    image(electrode_l, *v1_electrode)
    particles = [Particle(i) for i in range(num_particles)]
    for p in particles:
        p.populate_assemblies()
        p.run_snmc()
        p.populate_wta_and_scoring()
        spike_queue.extend(p.all_spikes)
            
def draw():
    background(0)
    noSmooth()
    image(brain, *brain_location)
    image(electrode_l, *v1_electrode)
    for sp in spike_queue:
        print(sp.x)
        sp.move_in_time(frameCount)
        sp.display(frameCount)
        if sp.spike_finished(frameCount):
            print("removing spike")
            spike_queue.remove(sp)
    

    
