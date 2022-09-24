'''
#Exercise 1: Make a function each for calculating the price of a zero coupon bond
1. using annual rate
2. semi-annual rate
3. continuous compounding
4. make a class called CouponBond, and place these 3 functions in the class
5. make main function, and call the three functions by initiating a class object for Bonds

Price of zero coupon bond (annual return) = par /(1+r)^T
Price of zero coupon bond (semi annual return)= par/(1+0.5r)^2T
Price of zero coupon bond using continuous compounded returns = par/exp(r*T)
'''
#I have moved the class implementation to another file called Bond.py
import Bond

if __name__ == '__main__':
    my_zeroCouponBond = Bond.CouponBond(1000, 0.06, 20)
    print("Discounted price/Zero (annual, semi-annual, continuously compounded: \n",
          my_zeroCouponBond.ZCB_Annual(), my_zeroCouponBond.ZCB_SemiAnnual(), my_zeroCouponBond.ZCB_ContinousCompound())


