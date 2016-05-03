# MyGPIO
python raspberry GPIO features with I/O schield

  LED COMMAND
  - LEDn(True)
  - LEDn(False)
  - ALL(True, timeout)
  - ALL(False, timeout)
  - EFFECT(True,SIDE,timeout)
  - EFFECT(False,SIDE,timeout)
  
    import LED      # import LED module in python
  
    #LED.LEDn(STATE)  # n = LED1 | LED2 | LED3 | LED4 | LED5
    LED.LED1(True)    # STATE =  True for turn ON | False for turn OFF
    
    #LED.ALL(STATE, timeout)  # STATE =  True for turn ON | False for turn OFF
    LED.ALL(True,2)           # timeout = time in seconds
    
    #LED.EFFECT(STATE,SIDE,timeout) # STATE =  True for turn ON | False for turn OFF
    LED.EFFECT(True,'LEFT',2)       # SIDE = 'LEFT' | 'RIGHT'
                                    # timeout = time in seconds
                                    
  
