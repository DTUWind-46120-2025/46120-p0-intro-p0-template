def clean_pitch(measurements, status):
    """_summary_
    
    """
    for i, (measurement,signal) in enumerate(zip(measurements,status)):
        if (measurement> 90 or measurement<0) and signal ==1:
            measurements[i] = -999
    
    print(measurements)




x = [-1, 2, 6, 95]  # "raw" pitch angle at four time steps
status = [1, 0, 0, 0]  # status signal
clean_pitch(x, status)