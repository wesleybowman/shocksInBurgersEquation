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
    
    userInput=raw_input('Pick a function: ')
    
    if userInput in "123" and len(userInput) == 1:
        if userInput=='1':
            print '\nYou chose the Gaussian! \n'
            x=np.linspace(-10, 10, 10000)
            u=np.exp(-x**2)
        elif userInput=='2':
            print 'You chose the tanh! \n'
            x=np.linspace(-20, 20, 10000)
            u=np.tanh(-x)
        elif userInput=='3':
            print 'You chose the sine wave! \n'
            x=np.linspace(-1,1+2*np.pi,10000)
            u=np.sin(x)
    else:
        print 'Invalid Input, using Gaussian function. \n'
        userInput='1'
        x=np.linspace(-10, 10, 10000)
        u=np.exp(-x**2)
    
    return u,x,userInput

def function(nt):
    '''Getting the function given different time values. '''

    t=nt*np.ones(len(u))
    k=u*t+x
    return x,k

def afterShock(nt,l,m):
    '''Find the shocks that occur after the first shock.
    This function also splits the function into its corresponding parts:
    a top, a middle, and a bottom. This is done so that integration
    later is more easily done.'''
        
    t=nt*np.ones(len(u))
    
    k=u*t+x
    
    #This finds the first point in the function where two points overlap
    kIndex=np.where(k > np.min(k[np.where(np.diff(k) < 0)[0][0]:]))[0][0]

    kx=k[kIndex:]
    ux=u[kIndex:]
    
    for index, k_value in enumerate(k[:-1]):
        if k_value > k[index+1]:
            l.append(index)
            break

    kTop=k[kIndex:l[0]]
    uTop=u[kIndex:l[0]]
    
    reversed_k = kx[::-1]
    
    for index, k_value in enumerate(reversed_k[:-1]):
        if k_value > reversed_k[index+1]:
            m.append(index)
            break

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
    
def beforePlot():
    '''Plotting that is after the first shock is found, but before all the 
    shocks are found.'''

    plt.figure(1)

    plt.subplot(211)
    
    plt.xlabel(r'$x$',fontsize=20)
    plt.ylabel(r'$u(x,t)$',fontsize=20)
    plt.plot(x,u) #Original data 

    plt.subplot(212)
    
    plt.xlabel(r'$x$',fontsize=20)
    plt.ylabel(r'$u(x,t)$',fontsize=20)
    
    plt.plot(k,u,'-g') #Data shifted by speed
    
    plt.grid(True)
    plt.show()
    
def afterPlot(u):
    '''Plotting that is done after all the shocks are found.
    This includes the original function and how much it has shifted,
     the integral that is done, and the characteristics with the
     shocks found plotted over top of those characteristics.'''
    
    x0x=[x0]*len(u)

    plt.figure(2)
    
    plt.subplot(221)
    
    plt.xlabel(r'$x$',fontsize=20)
    plt.ylabel(r'$u(x,t)$',fontsize=20)
    
    plt.plot(x,u) #Original data 
    plt.plot(k,u,'-g') #Data shifted by speed
    
    plt.subplot(222)
            
    plt.xlabel(r'$x$',fontsize=20)
    
    plt.plot(kx,ux)
    plt.plot(kTop,uTop)
    plt.plot(kMiddle,uMiddle,'-c')
    plt.plot(kBottom,uBottom,'-b')
    plt.plot(x0x,u)
    
    plt.subplot(212)
    
    '''Plots the characteristics of the initial condition
     with the shocks plotted as well.'''

    if userInput=='1':
        charx=np.linspace(-10, 10, 50)
        u=np.exp(-charx**2)
    if userInput=='2':
        charx=np.linspace(-20, 20, 50)
        u=np.tanh(-charx)
    if userInput=='3':
        charx=np.linspace(0, 2*np.pi, 50)
        u=np.sin(charx)
    
    yy=[]
    
    for i in range(len(charx)):
        
        if userInput=='1':
            uIndex=np.where(u==np.exp(-charx[i]**2))
        if userInput=='2':
            uIndex=np.where(u==np.tanh(-charx[i]))
        if userInput=='3':
            uIndex=np.where(u==np.sin(charx[i]))
        
        if u[uIndex[0][0]]==0:
            y=[0]*len(u)
        else:
            y=[(1/u[uIndex[0][-1]])]*len(u)
        yy.append(y)
        
    plt.xlabel(r'$x$',fontsize=20)
    plt.ylabel(r'$t$',fontsize=20)
    plt.ylim(0,3)
    
    for i in range(len(yy)):
        plt.plot(charx,yy[i]*(charx-charx[i]),'-b')

    plt.plot(x00,d[timeIndex[0][0]:],'-r')
            
    plt.grid(True)
    plt.show()
    
def char(userInput):
    '''Plots the characteristics of the initial condition
     with the shocks plotted as well.'''

    if userInput=='1':
        charx=np.linspace(-10, 10, 50)
        u=np.exp(-charx**2)
    if userInput=='2':
        charx=np.linspace(-20, 20, 50)
        u=np.tanh(-charx)
    if userInput=='3':
        charx=np.linspace(0, 2*np.pi, 50)
        u=np.sin(charx)
    
    yy=[]
    
    for i in range(len(charx)):
        
        if userInput=='1':
            uIndex=np.where(u==np.exp(-charx[i]**2))
        if userInput=='2':
            uIndex=np.where(u==np.tanh(-charx[i]))
        if userInput=='3':
            uIndex=np.where(u==np.sin(charx[i]))
        
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
    
    for i in range(len(yy)):
        ax.plot(charx,yy[i]*(charx-charx[i]),'-b')

    
    ax.plot(x00,d[timeIndex[0][0]:],'-r')
    
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
if __name__=='__main__':
    u,x,userInput=pickFunction()
    
#    t1=clock()
    
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
    
    print ('First shock occurs at: %.4f x at time %0.4f ') %(x0,dtime)
    
#    plot(x,k,u)
    '''Replaced the individual plot that had the function and the overlap with
    a plot that has two separate plots with subplotting.'''
    beforePlot()
    
    x00=[]
    for time in d[timeIndex[0][0]:]:
        k,kx,ux,kTop,uTop,kMiddle,uMiddle,kBottom,uBottom=afterShock(time,[],[])
        
        
        #Give an initial value of x0 to start out with. This is a 'guess.'
        x0=(kTop[-1]+kTop[0])/2
        
        a=[k[i+1]-k[i] for i in range(len(kTop))]
        b=[k[i+1]-k[i] for i in range(len(kMiddle))]
        c=[k[i+1]-k[i] for i in range(len(kBottom))]
           
        rightSide,leftSide=-1,1 #set values so the while loop isn't true.
        
        while rightSide!=leftSide:
            
            
            midPoint=np.where(k>=x0)  #find the rough midpoint 
            endPoint=np.where(kBottom>=kTop[-1])  #find where the edge of the top ends
            
            '''Changed the lines below so that we take the mean of the width vector,
            and not just use the very first value. Didn't seem to change anything,
            but I think this should be better. '''
            
            '''The lines below are just separating the top, middle, and bottom
            sections so that they are split down the middle. This is done so 
            that the equal area rule can be done. '''
            
            topLeft=u[midPoint[0][0]:]*np.mean(a)   
            intTopLeft=np.sum(topLeft)
            
            middleLeft=uMiddle[:midPoint[0][0]]*np.mean(b)
            intMidLeft=np.sum(middleLeft)
            
            try:
                bottomLeft=uBottom[midPoint[0][0]:endPoint[0][0]]*np.mean(c)
    
            except IndexError:
                '''Without this, if the top edge goes past the end of the x-value,
                then it will error out, and this only changes the values of the 
                integration by a little. '''
                bottomLeft=uBottom[midPoint[0][0]:]*np.mean(c)
            intBotLeft=np.sum(bottomLeft)
            
            leftSide=intTopLeft-intMidLeft
            
            '''Moving on from the left side to the right side.'''
            
            middleRight=uMiddle[midPoint[0][0]:]*np.mean(b)
            intMidRight=np.sum(middleRight)
            
            bottomRight=uBottom[:midPoint[0][0]]*np.mean(c)
            intBotRight=np.sum(bottomRight)
            
            rightSide=intMidRight-intBotRight
            
            '''Change the guess to get the areas as close as possible to one another. '''
            
            if np.abs(rightSide)-np.abs(leftSide)<0.005 or np.abs(leftSide)-np.abs(rightSide)<0.005:
                x00.append(x0)
                break
            
            if np.abs(rightSide)>np.abs(leftSide):
                x0+=np.abs(leftSide)/np.abs(rightSide)
    
            else:
                x0-=np.abs(rightSide)/np.abs(leftSide)
    
#    plot(x,k,u)
#    plotInt()
#    char(userInput)

    '''Replaced the three different plots above with one plot
    that plots them all with subplots. '''
    afterPlot(u)
    
    #Setting up for the animation
    
    if userInput=='1':
        x = np.linspace(-10, 10, 1000)
        u=np.exp(-x**2)
        fp=5  #frames for the animation
    if userInput=='2':
        x = np.linspace(-20, 20, 1000)
        u=np.tanh(-x)
        fp=5
    if userInput=='3':
        x=np.linspace(-1,1+2*np.pi,1000)
        u=np.sin(x)
        fp=5
    
    anim(u,x)
    
#    t2=clock()
#    dt=t2-t1
#    print 'Seconds: %d' %(dt)
    
