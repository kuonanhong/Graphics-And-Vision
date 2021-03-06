#<!--------------------------------------------------------------------------->
#<!--                   ITU - IT University of Copenhagen                   -->
#<!--                   SSS - Software and Systems Section                  -->
#<!-- File       : CalibrationEnum.py                                       -->
#<!-- Description: Class used for enumarating the calibration process       -->
#<!-- Author     : Fabricio Batista Narcizo                                 -->
#<!--            : Rued Langgaards Vej 7 - 4D06 - DK-2300 - Copenhagen S    -->
#<!--            : fabn[at]itu[dot]dk                                       -->
#<!-- Responsable: Dan Witzner Hansen (witzner[at]itu[dot]dk)               -->
#<!--              Fabricio Batista Narcizo (fabn[at]itu[dot]dk)            -->
#<!-- Information: No additional information                                -->
#<!-- Date       : 09/04/2015                                               -->
#<!-- Change     : 09/04/2015 - Creation of these classes                   -->
#<!-- Review     : 09/04/2015 - Finalized                                   -->
#<!--------------------------------------------------------------------------->

__version__ = '$Revision: 2015040901 $'

########################################################################
class CalibrationEnum(object):
    """Parameters used for selecting the stereo cameras calibration method."""
    CHESSBOARD = 0
    CIRCLES    = 1
