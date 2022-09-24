import numpy as np

class CouponBond:

    def __init__(self, faceValue, couponRate, maturityTime):
        self.par = faceValue
        self.r = couponRate
        self.T = maturityTime

    def ZCB_Annual(self):
        '''
        :param par: face value of the bond
        :param r: annual rate of the bond
        :param T: time to maturity
        :return: Price of a zero coupon bond
        '''
        return self.par/(1+self.r)**self.T

    def ZCB_SemiAnnual(self):
        return self.par/(1+0.5*self.r)**(2*self.T)

    def ZCB_ContinousCompound(self):
        return self.par/np.exp(self.r*self.T)
