'''
This is a simple bruteforce algorithm for
printing out all combination of a character collection.
'''

class BruteForce():
    def __init__(self):
        self.start=int(input('Start character length: '))
        self.end=int(input('End character length: '))
        self.collection=[chr(i) for i in range(ord('a'),ord('z')+1)]
        if self.end<self.start:
            print("Error: End is lesser than Start")
            input()

    
    def do_job(self, generated_string):
        print(generated_string)

        
    def from_start_to_end(self):
        i=self.start
        while i<=self.end:
            self.string_gen(self.collection, i)
            i+=1

        
    def string_gen(self, coll, actlen, pos=0, string=''):
        if pos<actlen:
            for c in coll:
                self.string_gen(coll,actlen,pos+1,string+c)
                if pos== actlen-1:
                    self.do_job(string+c)

                    
    def run(self):
        self.from_start_to_end()

BruteForce().run()
