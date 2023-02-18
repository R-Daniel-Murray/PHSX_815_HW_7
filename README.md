# PHSX815 Spring 2021 Week 5

## Rejection Sampling

This program calculates the integral of sin(pi*X) function from  X = 0 to X = 1,  and plots the calculated value of the integral versus the number of samples. 

Running CalculateSin.py will generate a uniform random sampling of region (0,1). Points that are under y=sin(pi*x) are accepted and points above it are rejected. I then take Naccepted/Ntotal to simulate the integral of sin(pi*x) betwee 0 and 1. 

### Requirements



The python scripts require the following libraries: `numpy` and `matplotlib`

### Usage

All of the executables can be called from the
command line with the `-h` or `--help` flag, which will print the options

The python scripts can be run with the following options
- `python python/CalculatePi.py -Nsample [# samples]`
- `python python/GaussRandom.py -Nsample [# samples] -range [Xmax] --log --expo`
