package utilities

class MyUtilities {
    static void addMyFeature(def job) {
        job.with {
            description('Arbitrary feature')
        }
    }
}



import utilities.MyUtilities

def myJob = job('example')
MyUtilities.addMyFeature(myJob)