"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    x=temperature*neutrons_emitted
    if temperature<800 and neutrons_emitted>500 and (x)<500000:
        return True
    else:
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power=voltage*current
    generated_power=generated_power/theoretical_max_power*100
    if generated_power>=80:
        return "green"
    elif generated_power>=60:
        return "orange"
    elif generated_power>=30:
        return "red"
    else:
        return "black"
   

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    x=temperature*neutrons_produced_per_second
    if x<(90*threshold)/100:
        return "LOW"
    elif (90*threshold)/100<=x<=(110*threshold)/100:
        return "NORMAL"
    else:
        return "DANGER"
        
    