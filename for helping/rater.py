class Rater:
    def __init__(self, nomra, rate):
        self.nomra = nomra
        self.rate = rate
 
   
    def check(self):
     avg = sum(self.nomra)
     avg2 = avg / len(self.nomra)
     if avg >= 600 :
      print(f"You are successed 💯 and here is your result {avg2, avg}")
     elif avg >= 305:
      print(f"You are successed good and here is your result {avg2, avg}")
     elif avg >= 205:
            print(f"You are not 💥💢 successed  and here is your result {avg2, avg}")
     else:
      print(f"Not accepted 👎 and here is your result {avg2, avg} your result should be more than 600")
s1 = Rater([40, 40, 40,40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40], "Your are successed")
# s2 = Rater([12, 23, 13,12,20, 10] "not suceed")
s1.check()
