import math
#"""printing parameters to be given by user"""
print('Design Inputs' )
delta_Energy=float(input("Fluctuation of energy=")) #flucation of energy
rpm=float(input("Mean Speed=")) #mean speed
coffient_speed=float(input("coeffient of speed Fluctuation=")) #coffient of speed
print("If space limitation is not given 'enter zero (0)' ")
space=float(input("Space Limitation=")) #sapce limitaion
#"""calucating mean dia"""
v=20.0
if space>0:
    d=0.85*space*1000 #mm
else:
    v=20
    d=v*60/(3.1415*rpm)
    d=d*1000 #to change it into millimeter
    d=int(d)
v=3.1415*d*rpm/60000 #correct velocity of flywheel with given rpm and diameter calucated

if v>25: #check for exess velocity
    d-=5
    v=3.1415*d*rpm/60000 #m/s
#caculating mass
while 1:
    mass=delta_Energy/(coffient_speed*v*v)
    density=7100.0 #kg/m**3
    if d<=300:
        b=mass/((3.14/4)*density*(d/1000)*(d/1000))
        b=b*1000 #meter to millimeter
        b= (int((b-0.5)/5+1))*5
        code=1
    else:
        mass_r=0.9*mass
        bh=mass_r/(3.14*(d/1000)*density)
        if space==0:
            h=math.sqrt(bh/1.5)*1000

            h=math.ceil(h)
            b=1.5*h
            b=math.ceil(b)
            code=2
        else:
            temp=1.7 #bbyh
            while temp>=1.2:
                h=math.sqrt(bh//temp)
                h=1000*h
                h=math.ceil(h)
                if (d+h)<space:
                    temp-=0.05
            b=math.ceil(temp*h)
    if d>600:
        code=3
    if code==1:
        possion_ratio=0.211
        omega=2*3.14*rpm/60
        sigmax=(3+possion_ratio)/8*density*omega*omega*d*d/4
    if code==2:
        sigmax=density*v*v/(10**6)
    if code==3:
        if d<=750:
            n=4
        else:
            if d<=2000:
                n=6
            else:
                n=8
     #stress in unstrained rim
        sigma1=density*v*v/1000000
        #stress in restrained rim
        sigma2=sigma1*(2*(3.145**2)*(d/2000)*((h*n**2)/1000))
        sigma_r=.75*sigma1+0.25*sigma2
        if sigma_r>40:
            v=v-0.5
            d=v*60000/(3.14*rpm)
        else:
            break
    if code==1 or code==2:
        break


print('\n\n\n'+"DESIGN REPORT")
if code==1:
    print("Flywheel=Solid Disc")
    print("diameter of Flywheel",d,"mm")
    print("width of Flywheel",b,"mm")
else:
    if code == 2:
        print("Flywheel=Web type")
        print("Web thickness=",math.ceil(b/20),"mm")
    else:
        print("Flywheel Type= Arms Type")
        print("Number of Arms=",n)
    print("mean Flywheel diameter=",d,"mm")
    print("Outside Diameter= ",d+h,"mm")
    print("Rim Width",b,"mm")
    print("Rim Thickness",h,"mm")












