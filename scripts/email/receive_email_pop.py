
import poplib
pop = poplib.POP3("server") 
pop.user("user") 
pop.pass_("password")

for i in xrange(1, pop.stat()[0]+1): 
    for zeile in pop.retr(i)[1]: 
        print zeile 
    print "***"

pop.quit()
