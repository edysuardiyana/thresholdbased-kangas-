def integrate(arrdat, freq):

    Tperiod = 1/float(freq) #calculate period

    velocity = 0; #initial value of velocity

    for n in range(0,len(arrdat)):

        velocity = velocity + arrdat[n] * Tperiod

    return velocity
