'''
    shocksInBurgersEquation lets the user choose an initial function and find 
    the shocks of that function using the equal area rule. 
    Copyright (C) 2013 Wesley A. Bowman

    This program is free software; you can redistribute it and/or modify 
    it under the terms of the GNU General Public License as published by 
    the Free Software Foundation; either version 2 of the License, or 
    (at your option) any later version.

    This program is distributed in the hope that it will be useful, 
    but WITHOUT ANY WARRANTY; without even the implied warranty of 
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License 
    along with this program; if not, write to the 
    Free Software Foundation, Inc., 59 Temple Place, 
    Suite 330, Boston, MA 02111-1307 USA

'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
#from time import clock

def pickFunction():
    print 'Pick a function from the following:'
    print '1: Gaussian'
    print '2: Hyperbolic Tangent'
    print '3: Sine'
    
    
    try:
        userInput=raw_input('Pick a function: ')
        print ""
        if userInput=='1':
            print 'You chose the Gaussian! \n'
            x=np.linspace(-10, 10, 10000)
            u=np.exp(-x**2)
        if userInput=='2':
            print 'You chose the tanh! \n'
            x=np.linspace(-10, 10, 10000)
            u=1+np.tanh(-x)
        if userInput=='3':
            print 'You chose the sine wave! \n'
            x=np.linspace(0,2*np.pi,10000)
            u=1+np.sin(x)
        if userInput!='1' and userInput!='2' and userInput!='3':
            raise Exception
    except Exception:
        userInput='1'
        x=np.linspace(-10, 10, 10000)
        u=np.exp(-x**2)
        print 'Invalid Input, using Gaussian function. \n'
    
    return u,x,userInput

def function(nt):
    '''Getting the function given different time values. '''
    t=np.linspace(0,nt,10000)
    k=u*t+x
    return x,k

def afterShock(nt,l,m):
    '''Find the shocks that occur after the first shock.
    This function also splits the function into its corresponding parts:
    a top, a middle, and a bottom. This is done so that integration
    later is more easily done.'''
        
    t=np.linspace(0,nt,10000)
    
    k=u*t+x
    
    kIndex=np.where(k > np.min(k[np.where(np.diff(k) < 0)[0][0]:]))[0][0]

    kx=k[kIndex:]
    ux=u[kIndex:]
    
    
    
    try:
        for i in range(len(k)):
                try:
                    if k[i]>k[i+1]:
                        l.append(i)
                except IndexError:
                    break
                length=len(l)
                if length>=1:
                    raise Exception
    except Exception:
        pass
    
    
    kTop=k[kIndex:l[0]]
    uTop=u[kIndex:l[0]]
        
    reversed_k = kx[::-1]
        
    try:
        for i in range(len(reversed_k)):
                try:
                    if reversed_k[i]<reversed_k[i+1]:
                        m.append(i)
                except IndexError:
                    break
                length=len(m)
                if length>=1:
#                    print length
                    raise Exception
    except Exception:
        pass

 
    bottomValue=reversed_k[m[-1]]
    bottomIndex=np.where(k==bottomValue)

    kMiddle=k[l[0]:bottomIndex[0][0]]
    uMiddle=u[l[0]:bottomIndex[0][0]]
    
    kBottom=k[bottomIndex[0][0]:]
    uBottom=u[bottomIndex[0][0]:]
    
    return k,kx,ux,kTop,uTop,kMiddle,uMiddle,kBottom,uBottom
    
def plot(x,k,u):
    '''Figure stuff from here on'''
    
    fig=plt.figure()
    ax = fig.add_subplot(111)
    
    ax.set_xlabel(r'$x$',fontsize=20)
    ax.set_ylabel(r'$u(x,t)$',fontsize=20)
    ax.autoscale()
    
    ax.plot(x,u) #Original data 
    ax.plot(k,u) #Data shifted by speed
    
    plt.grid(True)
    plt.show()

def plotInt():
    '''Plot the integral that is being done. '''
    
    x0x=[x0]*len(u)

    fig=plt.figure()
    ax = fig.add_subplot(111)
            
    ax.set_xlabel(r'$x$',fontsize=20)
    ax.set_ylabel(r'$u(x,t)$',fontsize=20)
    ax.autoscale()
    
    ax.plot(kx,ux)
    ax.plot(kTop,uTop)
    ax.plot(kMiddle,uMiddle,'-c')
    ax.plot(kBottom,uBottom,'-b')
    ax.plot(x0x,u)
            
    plt.grid(True)
    plt.show()

def char(userInput):
    '''Plots the characteristics of the initial condition
     with the shocks plotted as well.'''

    if userInput=='1':
        charx=np.linspace(-10, 10, 50)
        u=np.exp(-charx**2)
    if userInput=='2':
        charx=np.linspace(-10, 10, 50)
        print 'tanh'
        u=1+np.tanh(-charx)
    if userInput=='3':
        charx=np.linspace(0, 2*np.pi, 50)
        print 'sin'
        u=1+np.sin(charx)
    
    yy=[]
    
    for i in range(len(charx)):
        
        if userInput=='1':
            uIndex=np.where(u==np.exp(-charx[i]**2))
        if userInput=='2':
            uIndex=np.where(u==1+np.tanh(-charx[i]))
        if userInput=='3':
            uIndex=np.where(u==1+np.sin(charx[i]))
        
        if u[uIndex[0][0]]==0:
            y=[0]*len(u)
        else:
            y=[(1/u[uIndex[0][-1]])]*len(u)
        yy.append(y)
    
    fig=plt.figure()
    ax = fig.add_subplot(111)
            
    ax.set_xlabel(r'$x$',fontsize=20)
    ax.set_ylabel(r'$t$',fontsize=20)
    ax.axis([-10,10,0,3])
    #ax.autoscale
    
    for i in range(len(yy)):
        ax.plot(charx,yy[i]*(charx-charx[i]),'-b')

    
    ax.plot(x00,d[timeIndex[0][0]:]-1.1,'-r')
    
    plt.grid(True)
    plt.show()

def anim(u,x,fp=5):
    '''Animating the function to see it move based on its speed '''
    fig = plt.figure()
    ax = plt.axes(xlim=(-10, 10), ylim=(-3, 3))
    
    line, = ax.plot([], [])
    
    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        return line,
    
    # animation function.  This is called sequentially
    def animate(i):

        k=u*i+x
        line.set_data(k, u)
        return line,
    
    anim = animation.FuncAnimation(fig, animate, init_func=init,frames=fp, interval=500, blit=True)
    
    plt.show()

''' Start of the main program '''

u,x,userInput=pickFunction()

#t1=clock()

d=np.linspace(0, 10, 1000)

for dtime in d:

    x,k=function(dtime)

    try:
        kIndex=np.where(k > np.min(k[np.where(np.diff(k) < 0)[0][0]:]))[0][0]
        break
    except IndexError:
        pass
    
timeIndex=np.where(d==dtime) #get the index of where we left off in the time array. 


kx=k[kIndex:]
ux=u[kIndex:]
x0=k[kIndex]
#x00.append(x0)   #Append the first shock, but not needed.


#print ('First shock occurs at: %.4f x at time %0.4f ') %(x0,dtime)

plot(x,k,u)

x00=[]
for time in d[timeIndex[0][0]:]:
    k,kx,ux,kTop,uTop,kMiddle,uMiddle,kBottom,uBottom=afterShock(time,[],[])
    
    
    #Give an initial value of x0 to start out with. This is a 'guess.'
    x0=(kTop[-1]+kTop[0])/2
    
    a=[k[i+1]-k[i] for i in range(len(kTop))]
    b=[k[i+1]-k[i] for i in range(len(kMiddle))]
    c=[k[i+1]-k[i] for i in range(len(kBottom))]
    
#    a=[]
#    b=[]
#    c=[]
#    
#    for i in range(len(kTop)):
#        a.append(k[i+1]-k[i])
#
#    for i in range(len(kMiddle)):
#        b.append(k[i+1]-k[i])
#    
#    for i in range(len(kBottom)):
#        c.append(k[i+1]-k[i])
    
    rightSide,leftSide,current=-1,1,0 #set values so the while loop isn't true.
    
    while rightSide!=leftSide:
        
        midPoint=np.where(kTop>=x0)  #find the rough midpoint 
        endPoint=np.where(kBottom>=kTop[-1])  #find where the edge of the top ends
        
        '''Changed the lines below so that we take the mean of the width vector,
        and not just use the very first value. Didn't seem to change anything,
        but I think this should be better. '''
        
        '''The lines below are just separating the top, middle, and bottom
        sections so that they are split down the middle. This is done so 
        that the equal area rule can be done. '''
        
        topLeft=uTop[midPoint[0][0]:]*a[0]
#        topLeft=uTop[midPoint[0][0]:]*np.mean(a)   
        intTopLeft=np.sum(topLeft)
        
        middleLeft=uMiddle[:midPoint[0][0]]*b[0]
#        middleLeft=uMiddle[:midPoint[0][0]]*np.mean(b)
        intMidLeft=np.sum(middleLeft)
        
        try:
            bottomLeft=uBottom[midPoint[0][0]:endPoint[0][0]]*c[0]
#            bottomLeft=uBottom[midPoint[0][0]:endPoint[0][0]]*np.mean(c)

        except IndexError:
            '''Without this, if the top edge goes past the end of the x-value,
            then it will error out, and this only changes the values of the 
            integration by a little. '''
            bottomLeft=uBottom[midPoint[0][0]:]*c[0]
#            bottomLeft=uBottom[midPoint[0][0]:]*np.mean(c)
        intBotLeft=np.sum(bottomLeft)
        
        leftSide=intTopLeft-intMidLeft-intBotLeft
        
        '''Moving on from the left side to the right side.'''
        
        middleRight=uMiddle[midPoint[0][0]:]*b[0]
#        middleRight=uMiddle[midPoint[0][0]:]*np.mean(b)
        intMidRight=np.sum(middleRight)
        
        bottomRight=uBottom[:midPoint[0][0]]*c[0]
#        bottomRight=uBottom[:midPoint[0][0]]*np.mean(c)
        intBotRight=np.sum(bottomRight)
        
        rightSide=intMidRight-intBotRight
        
        '''print statements for testing''' 
        
#        print intTopLeft
#        print intMidLeft
#        print intBotLeft
#        print "Left Side"
#        print leftSide
#        print '\n'
#        print intMidRight
#        print intBotRight
#        print 'Right Side'
#        print rightSide
#        print '\n'
        
        '''Change the guess to get the areas as close as possible to one another. '''
        
        if np.abs(rightSide)>np.abs(leftSide):
            x0+=0.01

        else:
            x0-=0.01
       
        if np.abs(rightSide)-np.abs(leftSide)<0.5 or np.abs(leftSide)-np.abs(rightSide)>0.5:
#            print x0
            x00.append(x0)
            break
        
print x00

plot(x,k,u)

plotInt()
char(userInput)

#Setting up for the animation

if userInput=='1':
    x = np.linspace(-10, 10, 1000)
    u=np.exp(-x**2)
    fp=5  #frames for the animation
if userInput=='2':
    x = np.linspace(-10, 10, 1000)
    u=1+np.tanh(-x)
    fp=5
if userInput=='3':
    x=np.linspace(0,2*np.pi,1000)
    u=1+np.sin(x)
    fp=5

anim(u,x)

#t2=clock()
#dt=t2-t1
#print 'Seconds: %d' %(dt)

