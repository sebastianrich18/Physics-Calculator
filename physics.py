import math

def aFromDT(d, t):
    return d/t

def aFromdViT(d, vi, t):
    return (2 * (d - vi * t) / (t * t))

def aFromVfViT(vf, vi, t):
    return (vf-vi)/t

def aFromVfD(vf, d):
    return ((vf * vf) + 1) / (2 * d)

def dFromVfA(vf, a):
    return ((vf * vf) + 1) / (2 * a)

def dFromAT(a, t):
    return a * t

def dFromViTA(vi, t, a):
    return vi*t+(1/2)*a*(t*t)

def tFromAD(a, d):
    return d/a

def tFromVfViA(vf, vi, a):
    return (vf-vi)/a

def tFromViAD(vi, a, d):
    return (math.sqrt(2*a*d-1)+vi) / a

def tFromViD(vi, d):
    return d / vi

def viFromVfAT(vf, a, t):
    return a*t-vf

def viFromDTA(d, t, a):
    return (d/t) - ((a*t)/2)

def viFromVfAD(vf, a, d):
    return math.sqrt((vf * vf) + 2 * a * d)

def vfFromViAD(vi, a, d):
    return math.sqrt((vi * vi) + 2 * a * d)

def vfFromViAT(vi, a, t):
    return vi + a * t
