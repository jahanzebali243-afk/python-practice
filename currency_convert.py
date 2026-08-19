# Currency Exchange - PKR to USD/INR/EURO using dictionary
rates = {
    "usd" : 280 ,
    "inr" : 3.4 ,
    "euro" : 311
 }
def curency_exhange():
 ask = input ("Please enter which currency you want to convert pkr with usd/inr/euro : ")
 amount = int (input("How much amount in PKR you want to convert \n PKR : "))
 if ask in rates :
  return amount / rates[ask]
 else :
  return ("Enter valid currency only") 

print (curency_exhange())
 