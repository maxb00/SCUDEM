# SCUDEM VI: Modeling Bird Populations

### USAGE: 
    python3 main.py

# Equations:
    dB/dt = G(re, ri) * B * (1 - B/B0)
    G(re, ri) = {Pi + re - Pd - ri(1-Pd), re >= ri(1-Pd)
                {Pi - Pd,                 re < ri(1-Pd)
    ri(a, I) = (a + I)/(a0 + I0)
    re(O, p, n) = (p + n + T(O))/(r0 + p0 + Be)
    T(O) = |Be*cos(O)|
