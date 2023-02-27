import numpy as np
import sys
import matplotlib.pyplot as plt
import math

sys.path.append(".")
from Random import Random

if __name__ == "__main__":

	#set default number of samples
	Nsample = 100

	# read the user-provided seed from the command line (if there)
	if '-Nsample' in sys.argv:
		p = sys.argv.index('-Nsample')
		Nsample = int(sys.argv[p+1])
	if '-h' in sys.argv or '--help' in sys.argv:
		print ("Usage: %s -Nsample [number]" % sys.argv[0])
		print
		sys.exit(1) 

	nAccept = 0
	nTotal = 0
	
	# accepted values
	Xaccept = []
	Yaccept = []

	# reject values
	Xreject = []
	Yreject = []

	# sample number
	isample = []
	# calculated values of Pi (per sample)
	calcSin = []

	Yhist = []

	random = Random()

	idraw = max(1,int(Nsample)/100000)
	for i in range(0,Nsample):
		X = random.rand()
		Y = 2.0
		while Y >1.0:
			Y = random.Exponential(5)


		nTotal += 1
		if( Y <= math.sin(X*math.pi)): #accept if inside
			nAccept += 1
			if(i % idraw == 0):
				Xaccept.append(X)
				Yaccept.append(Y)
		else: # reject if outside
			if(i % idraw == 0):
				Xreject.append(X)
				Yreject.append(Y)
		if(i % idraw == 0):
			isample.append(nTotal)
			calcSin.append((nAccept/nTotal))
			###multiply nAccept/nTotal by the mass of the box, which is,
			
		
	
	#plot calculated pi vs sample number
	fig1 = plt.figure()
	plt.plot(isample,calcSin)
	plt.ylabel(r'Approximate Integral')
	plt.xlabel("Sample number")
	plt.xlim(0,isample[len(isample)-1])
	ax = plt.gca()
	ax.axhline(0.6366,color='green',label=r'True Integral')
	plt.title(r'Approximation of the integral as a function of number of samples')
	plt.legend()

	fig1.savefig("calculatedSin.pdf")


	#plot accept/reject points
	fig2 = plt.figure()
	plt.plot(Xaccept,Yaccept,marker='o',linestyle='',color='green',label='accept')
	plt.plot(Xreject,Yreject,marker='o',linestyle='',color='red',label='reject')
	plt.ylabel("Y")
	plt.xlabel("X")
	plt.legend()


	# x_circle = np.arange(min(min(Xaccept),min(Xreject)),max(max(Xaccept),max(Xreject)),0.001)
	# y_circle = [np.sqrt(i*i) for i in x_circle]

	x_circle = np.arange(min(min(Xaccept),min(Xreject)),max(max(Xaccept),max(Xreject)),0.001)
	y_circle = [(math.sin(i*math.pi)) for i in x_circle]
	plt.plot(x_circle,y_circle,color='blue',label=r'$y = sin(pi*x)$')
	plt.legend()
	plt.title('Sampled points')
	fig2.savefig("SinQuadPy.pdf")
	
	fig3 = plt.figure()
	plt.hist((Yaccept+Yreject))
	fig3.savefig('Ydistr.pdf')
	
# print(calcSin)





