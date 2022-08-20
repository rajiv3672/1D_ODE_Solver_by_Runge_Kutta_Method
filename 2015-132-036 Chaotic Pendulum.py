'''
RAJIV DAS
2015-132-036



For NON LINEAR DAMPED DRIVEN OSCILLATION the equation of motion is given by,
d/dt(dθ/dt)=-γ(dθ/dt)-(ω0^2)sinθ (F0/m)cos(ωd*t).
Here (dθ/dt) symbolized as y2 and θ symbolized as y1.Also γ,ω0,ωd symbolized as d,w0,wd for coding purpose and explained
later what means which.

We are only concerned about CHAOTIC behaviour.

The theory and empirical values were taken from "Waves and Oscillations by Walter Fox Smith,Oxford Press"
(Chapter 4,section 4.8)

SOME BASICS:
*Taylor series for sinθ= θ -(θ^3)/6 + (θ^5)/120 - . . . || For our case The restoring force Fr=Ksinθ, this gives a
centrosymetric potential(U=-dFr/dθ). That ensures there are 1st harmonic resonance,3rd harmonic resonance and so on.
So choosing ωd=(2/3)*ω0 results strong 1st and 3rd harmonic resonance and the motion becomes more CHAOTIC(at least
increases chances).
*γ refers to damping parameter , less γ means less damping. Less damping gives more freedom to oscillation thus more
uncertainty which leads to CHAOS. Also less γ gives sharp response at resonance frequencies.

To have fun you should change the values of constants and see if those results in chaos.
'''
import matplotlib.pyplot as plt
from numpy import sin,cos,pi
h=10**-4#Increment
d=.05#damping parameter||Less it is ,more chaotic pendulum is.
w0=1#Natural frequeency||Basically g/l , held to 1 for making calculations easy.
W=w0*w0
D=.9#Driving forces amplitude
wd=2/3#Diriving frequency|| Some special values can lead to chaos,.
def f(y2,y1,t):#function for angular acceleration ,i.e,d/dt(dθ/dt)
    return -d*y2 - W*sin(y1) + D*cos(wd*t)
y20=0#initial angular velocity
y10=pi/4#initial angular displacement
t=0#initial value of time
y2=y20
y1=y10
Y2=[y2]#list for angular velocity
Y1=[y1]#list for angular displacement
T=[wd*t]#list for time
te=100#Stop time
c=0#counter||we will need it later

print("This may take time and RAM, so please wait :(")
print("It will show 3 plots")

while t<te+h:#Loop for solution
    Yii=y2+(h/6)*(f(y2,y1,t)+4*f(y2+.5*h,y1+.5*h,t+.5*h)+f(y2+h,y1+h,t+h))#4th order R-K method||calculating angular velocity
    Y2.append(Yii)
    Yi=y1+h*y2#calculating angular displacement
    Y1.append(Yi)
    t=t+h
    T.append(wd*t)
    y2=Yii
    y1=Yi
    c=c+1

Q1=[]#list for locus
Q2=[]#list for locus
i=0
X55=[]#A REPLICA OF Y1 LIST FOR NOT ALTERING Y1 VALUES
V66=[]#A REPLICA OF Y2 LIST FOR NOT ALTERING Y2 VALUES
while i<c:#loop for locus
    q1=1*sin(Y1[i])
    Q1.append(q1)
    q2=1-1*cos(Y1[i])
    Q2.append(q2)
    i=i+1
    X55.append(Y1[i])
    V66.append(Y2[i])

i=0
n=1#For making Poincaré Map we need to range Y1 as (-π≤Y1≤π)
P=[]#list for phase space
Pd=[]#list for phase space
while n<13:# loop for phase space||
    while i < c:
        if X55[i] > n * pi and X55[i]<(n+1)*pi:
            X55[i] = X55[i] - 2 * pi * n
            P.append(X55[i])
            Pd.append(V66[i])
        if X55[i] < -n * pi and X55[i]>-(n+1)*pi:
            X55[i] = X55[i] + 2 * pi * n
            P.append(X55[i])
            Pd.append(V66[i])
        elif X55[i] <= pi and X55[i] >= -pi:
            P.append(X55[i])
            Pd.append(V66[i])
        i = i + 1
        #USING X55 AND V66 LIST WE DID NOT ALTER Y1 AND Y2.IF WE DIDN'T DO THAT FIRST PLOT WOULD BE FAULTY
    n=n+1
plt.figure(1)#plot for θ and dθ/dt
plt.axvline(linewidth=1.1,color='b',linestyle='-')
plt.axhline(linewidth=1.1,color='b',linestyle='-')
plt.grid(color='y', linestyle='--', linewidth=.4)
plt.title("C H A O S\nMagenta θ vs t\nRed dθ/dt vs t")
plt.ylabel("dθ/dt & θ →→→",fontsize=20)
plt.xlabel("ωd*t→→→",fontsize=20)
plt.plot(T,Y1,color='m',linewidth='.7')
plt.plot(T,Y2,color='r',linewidth='.7')

plt.figure(2)#plot for locus
plt.axvline(linewidth=1.1,color='b',linestyle='-')
plt.axhline(linewidth=1.1,color='b',linestyle='-')
plt.grid(color='y', linestyle='--', linewidth=.4)
plt.title("LOCUS OF PENDULUM")
plt.ylabel("Y→→→",fontsize=20)
plt.xlabel("X→→→",fontsize=20)
plt.plot(Q1,Q2,color='g',linestyle=':', linewidth=.2)

plt.figure(3)#plot for phase spase
plt.axvline(linewidth=1.1,color='b',linestyle='-')
plt.axhline(linewidth=1.1,color='b',linestyle='-')
plt.grid(color='y', linestyle='--', linewidth=.4)
plt.title("~P H A S E   S P A C E~\nPoincaré Map")
plt.ylabel("dθ/dt→→→",fontsize=20)
plt.xlabel("θ→→→",fontsize=20)
plt.plot(P,Pd,'r*',markersize=.2)

plt.show()