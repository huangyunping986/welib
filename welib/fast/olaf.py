"""
Tools to work with OLAF the vortex code implemented in openfast
"""
import numpy as np


def OLAFParams(omega_rpm, deltaPsiDeg=6, nNWrot=2, nFWrot=10, nFWrotFree=3, nPerRot=None, totalRot=None, show=True):
    """ 
    Computes recommended time step and wake length based on the rotational speed in RPM

    INPUTS:
     - omega_rpm: rotational speed in RPM
     - deltaPsiDeg : azimuthal discretization in deg
     - nNWrot : number of near wake rotations
     - nFWrot : total number of far wake rotations
     - nFWrotFree : number of far wake rotations that are free

        deltaPsiDeg  -  nPerRot
             5            72    
             6            60    
             7            51.5  
             8            45    
    """
    omega_rpm = np.asarray(omega_rpm)
    omega = omega_rpm*2*np.pi/60
    T = 2*np.pi/omega
    if nPerRot is not None:
        dt_wanted    = np.around(T/nPerRot,4)
    else:
        dt_wanted    = np.around(deltaPsiDeg/(6*omega_rpm),4)
        nPerRot = int(2*np.pi /(deltaPsiDeg*np.pi/180))

    nNWPanel     = nNWrot*nPerRot
    nFWPanel     = nFWrot*nPerRot
    nFWPanelFree = nFWrotFree*nPerRot

    if totalRot is None:
        totalRot = (nNWrot + nFWrot)*3 # going three-times through the entire wake

    tMax = dt_wanted*nPerRot*totalRot

    if show:
        print(dt_wanted              , '  dt')
        print(int      (nNWPanel    ), '  nNWPanel          ({} rotations)'.format(nNWrot))
        print(int      (nFWPanel    ), '  FarWakeLength     ({} rotations)'.format(nFWrot))
        print(int      (nFWPanelFree), '  FreeFarWakeLength ({} rotations)'.format(nFWrotFree))
        print(tMax              , '  Tmax ({} rotations)'.format(totalRot))

    return dt_wanted, tMax, nNWPanel, nFWPanel, nFWPanelFree
