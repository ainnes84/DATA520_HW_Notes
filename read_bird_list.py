# read_bird_list.py
observations_file = open('birdlist.txt')
birds_observed = set()
for line in observations_file:
    bird = line.strip()
    birds_observed.add(bird)
