class BankInfo:
    def __init__(self, fn ,ln):
        self.fn = fn
        self.ln = ln


class BankAccount():

    def __init__(self, bi, acc_no, amt):
         self.acc_no = acc_no
         self.amt = amt

         # bankInfo object
         self.bi = bi

    def calc_interest(self,n):
        pass

    def valid_amt(self,min_amt):
        return self.amt >= min_amt

    def viewprofile(self):

        print("profile: ")
        print("")
        print("Your Profile Complete Account Profile is:-")
        print("First Name: ", self.bi.fn)
        print("Last Name: ", self.bi.ln)
        print("Account Number: ", self.acc_no)
        print("Total Amount: ", self.amt)



class Saving(BankAccount):
    min_amt = 10000
    rate = 6
    interest = 0.0

    def calc_interest(self,n):

        self.interest = float((self.amt*self.rate*n)/100)
        print('intrest: ',self.interest)


class Current(BankAccount):
    min_amt = 5000
    rate = 0
    interest = 0.0

    def calc_interest(self, n):

        print('sorry instest is not available in current')



class main:

    def __init__(self):

        self.fn="kavan"
        self.ln="ardeshana"

        bi = BankInfo(self.fn, self.ln)

        self.acc_no = 987654321025
        self.amt = 8000

        svng = Current(bi, self.acc_no, self.amt)

        svng.calc_interest(5)
        svng.viewprofile()
mn = main()




