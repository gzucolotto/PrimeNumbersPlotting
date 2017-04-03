class IterationCounter(object):
    iterations_counter = {}

    def __init__(self, f):
        print "inside IterationCounter.__init__()"
        #TODO: include f into interations_counter. Need to distinguish function by each class
        self.f = f # Prove that function definition has completed
        self.iterations_counter[f] = 0

    def __call__(self):
        print "inside IterationCounter.__call__()"
        print "class name ", self.f.__class__.__name__
        #TODO: increment interation count for f
        self.f()
        self.iterations_counter[self.f] += 1

@IterationCounter
def aFunction():
    print "inside aFunction()"

print "Finished decorating aFunction()"

aFunction()
aFunction()