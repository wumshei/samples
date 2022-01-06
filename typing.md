"""A document for describing the actual labels that should go into this model."""
#SEARCHING/ TRAINING LABELS
KICK
SNARE
TOM
    FLOOR TOM = {low, deep, floor}
    RACK TOM = {hi, mid, rack}
TAMBOURINE
CYMBAL{#technically cymbals but it isnt useful to consider them as such i reckon
HAT
    OPEN
    CLOSED
RIDE
CRASH}

"""After model can successfully discern drums as typed above, it could be useful to hand label them and seperate them a bit more"""



#IDEAL OUTPUTS
HAT
    OPEN
        
    CLOSED
        Tiny hat