import unittest
import os
import numpy as np
from welib.FEM.frame3d import *


MyDir=os.path.dirname(__file__)

class Test(unittest.TestCase):
    def test_MeKe(self):

        L    = 100                       # Beam Length [m]
        G    = 79.3e9                    # Shear modulus. Steel: 79.3  [Pa] [N/m^2]
        E    = 210e9                     # Young modulus [Pa] [N/m^2]
        D    = 8
        t    = 0.045
        A   = np.pi*( (D/2)**2 - (D/2-t)**2)
        rho  = 7850
        m0   = rho*A
        EIx = E*np.pi/32*(D**4-(D-2*t)**4)# Polar second moment of area [m^4]
        EIy = E*np.pi/64*(D**4-(D-2*t)**4)# Planar second moment of area [m^4]
        EIz = EIy
        EA  = E*A
        Kt   = np.pi/64*(D**4 - (D-2*t)**4)   # Torsion constant [m^4]


        np.set_printoptions(linewidth=300, precision=3)

        ke, me, _ = frame3d_KeMe(E,G,Kt,EA,EIx,EIy,EIz,L,A,rho*A*L) 
        me_ref=np.array(
              [[   294273.37656084 , 0.                , 0.                , 0.                 , 0.                 , 0.                 , 147136.68828042 , 0.                , 0.                , 0.              , 0.                 , 0.        ]          , 
              [        0.          , 327904.61959636   , 0.                , 0.                 , 0.                 , 4624295.91738459   , 0.              , 113505.44524489   , 0.                , 0.              , 0.                 , -2732538.49663635]   , 
              [        0.          , 0.                , 327904.61959636   , 0.                 , -4624295.91738459  , 0.                 , 0.              , 0.                , 113505.44524489   , 0.              , 2732538.49663635   , 0.        ]          , 
              [        0.          , 0.                , 0.                , 4655702.76898621   , 0.                 , 0.                 , 0.              , 0.                , 0.                , 2327851.3844931074 , 0.                 , 0.        ]          , 
              [        0.          , 0.                , -4624295.91738459 , 0.                 , 84078107.5888107   , 0.                 , 0.              , 0.                , -2732538.49663635 , 0.              , -63058580.69160801 , 0.        ]          , 
              [        0.          , 4624295.91738459  , 0.                , 0.                 , 0.                 , 84078107.5888107   , 0.              , 2732538.49663635  , 0.                , 0.              , 0.                 , -63058580.69160801]  , 
              [   147136.68828042  , 0.                , 0.                , 0.                 , 0.                 , 0.                 , 294273.37656084 , 0.                , 0.                , 0.              , 0.                 , 0.        ]          , 
              [        0.          , 113505.44524489   , 0.                , 0.                 , 0.                 , 2732538.49663635   , 0.              , 327904.61959636   , 0.                , 0.              , 0.                 , -4624295.91738459]   , 
              [        0.          , 0.                , 113505.44524489   , 0.                 , -2732538.49663635  , 0.                 , 0.              , 0.                , 327904.61959636   , 0.              , 4624295.91738459   , 0.        ]          , 
              [        0.          , 0.                , 0.                , 2327851.3844931074 , 0.                 , 0.                 , 0.              , 0.                , 0.                , 4655702.76898621, 0.                 , 0.        ]          , 
              [        0.          , 0.                , 2732538.49663635  , 0.                 , -63058580.69160801 , 0.                 , 0.              , 0.                , 4624295.91738459  , 0.              , 84078107.5888107   , 0.        ]          , 
              [        0.          , -2732538.49663635 , 0.                , 0.                 , 0.                 , -63058580.69160801 , 0.              , -4624295.91738459 , 0.                , 0.              , 0.                 , 84078107.5888107 ]])
        np.testing.assert_almost_equal(me, me_ref,7)




if __name__=='__main__':
    unittest.main()
