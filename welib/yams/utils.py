""" 
Set of utils useful for Structural and Multi-Body dynamics

"""

import numpy as np

# --- Definitions to ease comparison with sympy versions
from numpy import cos ,sin

def Matrix(m):
    return np.asarray(m)

# --------------------------------------------------------------------------------}
# --- Rotation matrices
# --------------------------------------------------------------------------------{
def R_x(t):
    return Matrix( [[1,0,0], [0,cos(t),-sin(t)], [0,sin(t),cos(t)]])

def R_y(t):
    return Matrix( [[cos(t),0,sin(t)], [0,1,0], [-sin(t),0,cos(t)] ])

def R_z(t): 
    return Matrix( [[cos(t),-sin(t),0], [sin(t),cos(t),0], [0,0,1]])

def skew(x):
    x=np.asarray(x).ravel()
    """ Returns the skew symmetric matrix M, such that: cross(x,v) = M v """
    return np.array([[0, -x[2], x[1]],[x[2],0,-x[0]],[-x[1],x[0],0]])

def rigidBodyMassMatrix(Mass,J,rho): # TODO change interface
    """ Mass matrix for a rigid body (i.e. mass matrix) Eq.(15) of [1] """
    S=Mass*skew(rho)
    MM=np.zeros((6,6))
    MM[0:3,0:3] = Mass*np.eye(3);
    MM[0:3,3:6] = -S;
    MM[3:6,0:3] = S ; # transpose(S)=-S;
    MM[3:6,3:6] = J ;
    return MM
# --------------------------------------------------------------------------------}
# --- Inertia functions 
# --------------------------------------------------------------------------------{
def translateInertiaMatrix(I_A, Mass, r_BG, r_AG = np.array([0,0,0])):
    """
    Transform inertia matrix with respect to point A to the inertia matrix with respect to point B
    NOTE: the vectors and the inertia matrix needs to be expressed in the same coordinate system. 
    NOTE: one of the vector r_BG or r_AG may be empty or 0 instead of [0,0,0];
    NOTE: if r_AG is not provided it is assumed to be 0, i.e. A=G
    To avoid this confusion you can use translateInertiaMatrixFromCOG  and translateInertiaMatrixToCOG
    
    INPUTS:
       I_A  : Inertia matrix 3x3 in the coordinate system A
       Mass : Mass of the body
       r_BG: vector from point B to COG of the body
    
    OPTIONAL INPUTS:
       r_AG: vector from point A to point G
    """
    if len(r_AG) < 3:
        r_AG = np.array([0,0,0])
    if len(r_BG) < 3:
        r_BG = np.array([0,0,0])   
    return I_A - Mass*(np.dot(skew(r_BG), skew(r_BG))-np.dot(skew(r_AG),skew(r_AG)))

def translateInertiaMatrixToCOG(I_P, Mass, r_PG): 
    """ Transform inertia matrix with respect to point P to the inertia matrix with respect to the COG
    NOTE: the vectors and the inertia matrix needs to be expressed in the same coordinate system.
    
    INPUTS:
      I_G  : Inertia matrix 3x3 with respect to COG
      Mass : Mass of the body
      r_PG: vector from P to COG 
    """
    I_G = I_P + Mass * np.dot(skew(r_PG), skew(r_PG))
    return I_G

def translateInertiaMatrixFromCOG(I_G, Mass, r_GP): 
    """
    Transform inertia matrix with respect to COG to the inertia matrix with respect to point P
    NOTE: the vectors and the inertia matrix needs to be expressed in the same coordinate system.
    INPUTS:
       I_G  : Inertia matrix 3x3 with respect to COG
       Mass : Mass of the body
       r_GP: vector from COG of the body to point P
    """
    I_P = I_G - Mass * np.dot(skew(r_GP),skew(r_GP))
    return I_P
    

