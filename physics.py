import math

def aFromDT(d, t):
    return d/t

def dFromAT(a, t):
    return a * t

def tFromAD(a, d):
    return d/a

def vfFromViAT(vi, a, t):
    return vi + a * t

def viFromVfAT(vf, a, t):
    return a*t-vf

def aFromVfViT(vf, vi, t):
    return (vf-vi)/t

def tFromVfViA(vf, vi, a):
    return (vf-vi)/a

def dFromViTA(vi, t, a):
    return vi*t+(1/2)*a*(t*t)

def viFromDTA(d, t, a):
    return (d/t) - ((a*t)/2)

def tFromViD(vi, d):
    return -vi * d

def aFromdViT(d, vi, t):
    return (2 * (d - vi * t) / (t * t))

def vfFromViAD(vi, a, d):
    return math.sqrt((vi * vi) + 2 * a * d)

def viFromVfAD(vf, a, d):
    return math.sqrt((vf * vf) + 2 * a * d)

def aFromVfD(vf, d):
    return ((vf * vf) + 1) / (2 * d)

def dFromVfA(vf, a):
    return ((vf * vf) + 1) / (2 * a)