# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 07:54:54 2021

@author: Aya Arbiat
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#img to grey scale
img_file = Image.open("bilo112.jpg")
img_grey = img_file.convert('L') 
c = np.array(img_grey)

# width, height = img_file.size
pixels=c.size
yx_coords = np.flip(np.column_stack(np.where(c >= 0)),axis=1)
cxy=np.zeros([pixels,3])
cxy[:,0]=yx_coords[:,0]
cxy[:,1]=-1*yx_coords[:,1]
cxy[:,2]=[x for sets in c for x in sets]
cxy_og=cxy

cxy_mini=cxy[cxy[:,2] <= 245]
cxy_sorted = cxy_mini[cxy_mini[:, 0].argsort()]
# np.savetxt("bilo.csv", cxy_mini, delimiter='\t', fmt='%4d')

# plt.plot(cxy_mini[:,0],cxy_mini[:,1],'.')
# plot1 = plt. figure(1)


#B
###########################################
B=cxy_sorted[7:12394,:]
# plot1 = plt. figure(2)
# plt.plot(B[:,0],B[:,1],'.')
bx=218-4+1

#deleting some points 
#####################
B=np.delete(B, 1271, 0)

Bdel=np.delete(B, 2, 1)
p=[15,-7]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[180,-8]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[199,-12]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[204,-18]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[211,-25]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[214,-26]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[180,-8]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[193,-11]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[10,-221]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[20,-225]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[206,-223]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[209,-219]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

#B_outer
########
btop= np.zeros((bx,3))
bbottom= np.zeros((bx,3))

for j in range(bx):    
    bmid=B[B[:,0] == 4+j]
    for l in range(len(bmid)):
        if bmid[l,1]==max(bmid[:,1]):
            btop[j,:]=bmid[l,:]
        if bmid[l,1]==min(bmid[:,1]):
            bbottom[j,:]=bmid[l,:]

btop=np.delete(btop,np.s_[14:173], 0)
bbottom=np.delete(bbottom,np.s_[29:180], 0)


plot1 = plt. figure(4)
plt.plot(btop[:,0],btop[:,1],'.')   
plt.plot(bbottom[:,0],bbottom[:,1],'.')

np.savetxt("btop.csv", btop, delimiter='\t', fmt='%4d')
np.savetxt("bbottom.csv", bbottom, delimiter='\t', fmt='%4d')

#B_corner1

#deleting some points 
#####################
Bdel=np.delete(B, 2, 1)
p=[206,-118]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[211,-118]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[212,-115]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bc1_temp=B[B[:,0] >= 200]
Bc1=Bc1_temp[Bc1_temp[:,0] <= 218]
Bc1_sortedy = Bc1[Bc1[:, 1].argsort()]
Bc1_temp=Bc1_sortedy[Bc1_sortedy[:,1] >= -120]
Bc1=Bc1_temp[Bc1_temp[:,1] <= -101]
Bc1= Bc1[Bc1[:, 0].argsort()]
# plt.plot(Bc1[:,0],Bc1[:,1],'.')

bc1=218-200+1
btop_c1= np.zeros((bc1,3))
bbottom_c1= np.zeros((bc1,3))

for j in range(bc1):    
    bmid_c1=Bc1[Bc1[:,0] == 200+j]
    for l in range(len(bmid_c1)):
        if bmid_c1[l,1]==min(bmid_c1[:,1]):
            bbottom_c1[j,:]=bmid_c1[l,:]
               
plt.plot(bbottom_c1[:,0],bbottom_c1[:,1],'.')

np.savetxt("bbottom_c1.csv", bbottom_c1, delimiter='\t', fmt='%4d')


#B_corner2
Bc2_temp=B[B[:,0] >= 200]
Bc2=Bc2_temp[Bc2_temp[:,0] <= 218]
Bc2_sortedy = Bc2[Bc2[:, 1].argsort()]
Bc2_temp=Bc2_sortedy[Bc2_sortedy[:,1] >= -139]
Bc2=Bc2_temp[Bc2_temp[:,1] <= -120]
Bc2= Bc2[Bc2[:, 0].argsort()]
# plt.plot(Bc2[:,0],Bc2[:,1],'.')

bc2=218-200+1
btop_c2= np.zeros((bc2,3))
bbottom_c2= np.zeros((bc2,3))

for j in range(bc2):    
    bmid_c2=Bc2[Bc2[:,0] == 200+j]
    for l in range(len(bmid_c2)):
        if bmid_c2[l,1]==max(bmid_c2[:,1]):
            btop_c2[j,:]=bmid_c2[l,:]
            
plt.plot(btop_c2[:,0],btop_c2[:,1],'.')   
np.savetxt("btop_c2.csv", btop_c2, delimiter='\t', fmt='%4d')

#B_inner
#########
#deleting some points 
#####################
Bdel=np.delete(B, 2, 1)
p=[88,-101]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[133,-101]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[139,-96]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

Bdel=np.delete(B, 2, 1)
p=[79,-58]
i=np.where(np.all(Bdel==p,axis=1))
B=np.delete(B, i, 0)

B_temp=B[B[:,0] >= 78]
B_inner=B_temp[B_temp[:,0] <= 144]
B_inner_sortedy = B_inner[B_inner[:, 1].argsort()]
B_temp=B_inner_sortedy[B_inner_sortedy[:,1] >= -187]
B_inner=B_temp[B_temp[:,1] <= -57]
B_inner=np.delete(B_inner, 1795, 0)

plt.plot(B_inner[:,0],B_inner[:,1],'.')

#B_mid
Binin_temp=B_inner[B_inner[:,1] >= -153]
Binin_y=Binin_temp[Binin_temp[:,1] <= -88]
B_inner_sortedx = Binin_y[Binin_y[:, 0].argsort()]
Binin_temp=B_inner_sortedx[B_inner_sortedx[:,0] >= 87]
B_inin=Binin_temp[Binin_temp[:,0] <= 144]
B_inin=np.delete(B_inin, 22, 0)
B_inin=np.delete(B_inin, 1250, 0)
# plt.plot(B_inin[:,0],B_inin[:,1],'.')

bxx=144-87+1
btop_inin= np.zeros((bxx,3))
bbottom_inin= np.zeros((bxx,3))

for j in range(bxx):    
    bmid_inin=B_inin[B_inin[:,0] == 87+j]
    for l in range(len(bmid_inin)):
        if bmid_inin[l,1]==max(bmid_inin[:,1]):
            btop_inin[j,:]=bmid_inin[l,:]
        if bmid_inin[l,1]==min(bmid_inin[:,1]):
            bbottom_inin[j,:]=bmid_inin[l,:]

# plt.plot(btop_inin[:,0],btop_inin[:,1],'.')   
# plt.plot(bbottom_inin[:,0],bbottom_inin[:,1],'.')

np.savetxt("btop_inin.csv", btop_inin, delimiter='\t', fmt='%4d')
np.savetxt("bbottom_inin.csv", bbottom_inin, delimiter='\t', fmt='%4d')

#B_border1
Bb1_temp=B[B[:,1] >= -71]
Bb1_y=Bb1_temp[Bb1_temp[:,1] <= -57]
Bb1_sortedx = Bb1_y[Bb1_y[:, 0].argsort()]
Bb1_temp=Bb1_sortedx[Bb1_sortedx[:,0] >= 79]
Bb1=Bb1_temp[Bb1_temp[:,0] <= 144]
# plt.plot(Bb1[:,0],Bb1[:,1],'.')

bxxx1=144-79+1
btop_b1= np.zeros((bxxx1,3))
bbottom_b1= np.zeros((bxxx1,3))

for j in range(bxxx1):    
    bmid_b1=Bb1[Bb1[:,0] == 79+j]
    for l in range(len(bmid_b1)):
        # if bmid_b1[l,1]==max(bmid_b1[:,1]):
        #     btop_b1[j,:]=bmid_b1[l,:]
        if bmid_b1[l,1]==min(bmid_b1[:,1]):
            bbottom_b1[j,:]=bmid_b1[l,:]

bbottom_b1=np.vstack([[78,-57,0],bbottom_b1])

bbottom_b1=np.delete(bbottom_b1,np.s_[1:51], 0)            
plt.plot(bbottom_b1[:,0],bbottom_b1[:,1],'.')

np.savetxt("bbottom_b1.csv", bbottom_b1, delimiter='\t', fmt='%4d')


#B_border2
Bb2_temp=B[B[:,1] >= -187]
Bb2_y=Bb2_temp[Bb2_temp[:,1] <= -174]
Bb2_sortedx = Bb2_y[Bb2_y[:, 0].argsort()]
Bb2_temp=Bb2_sortedx[Bb2_sortedx[:,0] >= 79]
Bb2=Bb2_temp[Bb2_temp[:,0] <= 144]
# plt.plot(Bb2[:,0],Bb2[:,1],'.')

bxxx2=144-79+1
btop_b2= np.zeros((bxxx2,3))
bbottom_b2= np.zeros((bxxx2,3))

for j in range(bxxx2):    
    bmid_b2=Bb2[Bb2[:,0] == 79+j]
    for l in range(len(bmid_b2)):
        if bmid_b2[l,1]==max(bmid_b2[:,1]):
            btop_b2[j,:]=bmid_b2[l,:]

btop_b2=np.vstack([[78,-187,0],btop_b2])

btop_b2=np.delete(btop_b2,np.s_[1:53], 0)
plt.plot(btop_b2[:,0],btop_b2[:,1],'.')   

np.savetxt("btop_b2.csv", btop_b2, delimiter='\t', fmt='%4d')

#I
###########################################
I=cxy_sorted[12396:18158,:]
# plot1 = plt. figure(3)
# plt.plot(I[:,0],I[:,1],'.')
ix=339-256+1

Idel=np.delete(I, 2, 1)
p=[257,-211]
i=np.where(np.all(Idel==p,axis=1))
I=np.delete(I, i, 0)
Idel=np.delete(I, 2, 1)
p=[257,-210]
i=np.where(np.all(Idel==p,axis=1))
I=np.delete(I, i, 0)
Idel=np.delete(I, 2, 1)
p=[334,-25]
i=np.where(np.all(Idel==p,axis=1))
I=np.delete(I, i, 0)

itop= np.zeros((ix,3))
ibottom= np.zeros((ix,3))

for j in range(ix):    
    imid=I[I[:,0] == 256+j]
    for l in range(len(imid)):
        if imid[l,1]==max(imid[:,1]):
            itop[j,:]=imid[l,:]
        if imid[l,1]==min(imid[:,1]):
            ibottom[j,:]=imid[l,:]
   
plt.plot(itop[:,0],itop[:,1],'.')   
plt.plot(ibottom[:,0],ibottom[:,1],'.')   

np.savetxt("itop.csv", itop, delimiter='\t', fmt='%4d')
np.savetxt("ibottom.csv", ibottom, delimiter='\t', fmt='%4d')

#leaf
###########################################
leaf=cxy_sorted[18159:25038,:]
# plot1 = plt. figure(4)
plt.plot(leaf[:,0],leaf[:,1],'.')

#deleting some points 
#####################
leafdel=np.delete(leaf, 2, 1)
p=[494,-153]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[500,-147]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[501,-150]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[502,-151]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[502,-148]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[507,-137]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[525,-111]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[534,-79]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[534,-75]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[368,-187]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[417,-166]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[394,-167]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)



leafdel=np.delete(leaf, 2, 1)
p=[433,-58]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[420,-66]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[419,-68]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[419,-65]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[413,-74]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)

leafdel=np.delete(leaf, 2, 1)
p=[412,-75]
i=np.where(np.all(leafdel==p,axis=1))
leaf=np.delete(leaf, i, 0)
            
           
gx=534-369+1
gtop= np.zeros((gx,3))
gbottom= np.zeros((gx,3))

for j in range(gx):    
    gmid=leaf[leaf[:,0] == 369+j]
    for l in range(len(gmid)):
        if gmid[l,1]==max(gmid[:,1]):
            gtop[j,:]=gmid[l,:]
        if gmid[l,1]==min(gmid[:,1]):
            gbottom[j,:]=gmid[l,:]

# plot1 = plt. figure(4)
plt.plot(gtop[:,0],gtop[:,1],'.')   
plt.plot(gbottom[:,0],gbottom[:,1],'.') 

np.savetxt("gtop.csv", gtop, delimiter='\t', fmt='%4d')
np.savetxt("gbottom.csv", gbottom, delimiter='\t', fmt='%4d')

#L
###########################################
L=cxy_sorted[25043:30905,:]
# plot1 = plt. figure(5)
# plt.plot(L[:,0],L[:,1],'.')

Ldel=np.delete(L, 2, 1)
p=[654,-181]
i=np.where(np.all(Ldel==p,axis=1))
L=np.delete(L, i, 0)
Ldel=np.delete(L, 2, 1)
p=[572,-214]
i=np.where(np.all(Ldel==p,axis=1))
L=np.delete(L, i, 0)

lx=712-568+1
ltop= np.zeros((lx,3))
lbottom= np.zeros((lx,3))

for j in range(lx):    
    lmid=L[L[:,0] == 568+j]
    for l in range(len(lmid)):
        if lmid[l,1]==max(lmid[:,1]):
            ltop[j,:]=lmid[l,:]
        if lmid[l,1]==min(lmid[:,1]):
            lbottom[j,:]=lmid[l,:]

plt.plot(ltop[:,0],ltop[:,1],'.')   
plt.plot(lbottom[:,0],lbottom[:,1],'.')

np.savetxt("ltop.csv", ltop, delimiter='\t', fmt='%4d')
np.savetxt("lbottom.csv", lbottom, delimiter='\t', fmt='%4d')

#O
###########################################
O=cxy_sorted[30906:pixels,:]
# plot1 = plt. figure(6)
# plt.plot(O[:,0],O[:,1],'.')

#some points to delete
Odel=np.delete(O, 2, 1)
p=[739,-223]
i=np.where(np.all(Odel==p,axis=1))
O=np.delete(O, i, 0)
#del for Oin
Odel=np.delete(O, 2, 1)
p=[856,-62]
i=np.where(np.all(Odel==p,axis=1))
O=np.delete(O, i, 0)
Odel=np.delete(O, 2, 1)
p=[811,-182]
i=np.where(np.all(Odel==p,axis=1))
O=np.delete(O, i, 0)

ox=940-731+1
otop= np.zeros((ox,3))
obottom= np.zeros((ox,3))

#O_outer
#########
for j in range(ox):    
    omid=O[O[:,0] == 731+j]
    for l in range(len(omid)):
        if omid[l,1]==max(omid[:,1]):
            otop[j,:]=omid[l,:]
        if omid[l,1]==min(omid[:,1]):
            obottom[j,:]=omid[l,:]

otop=np.delete(otop,np.s_[43:167], 0)
obottom=np.delete(obottom,np.s_[32:174], 0)

plt.plot(otop[:,0],otop[:,1],'.')   
plt.plot(obottom[:,0],obottom[:,1],'.')

np.savetxt("otop.csv", otop, delimiter='\t', fmt='%4d')
np.savetxt("obottom.csv", obottom, delimiter='\t', fmt='%4d')

#O_inner
#########
Oin_temp=O[O[:,0] >= 794]
Oin=Oin_temp[Oin_temp[:,0] <= 875]
Oin_sortedy = Oin[Oin[:, 1].argsort()]
Oin_temp=Oin_sortedy[Oin_sortedy[:,1] >= -188]
Oin=Oin_temp[Oin_temp[:,1] <= -48]
Oin= Oin[Oin[:, 0].argsort()]
# plt.plot(Oin[:,0],Oin[:,1],'.')



#O_top
Oo1_temp=Oin[Oin[:,0] >= 802]
Oo1=Oo1_temp[Oo1_temp[:,0] <= 868]
Oo1_sortedy = Oo1[Oo1[:, 1].argsort()]
Oo1_temp=Oo1_sortedy[Oo1_sortedy[:,1] >= -70]
Oo1=Oo1_temp[Oo1_temp[:,1] <= -48]
Oo1= Oo1[Oo1[:, 0].argsort()]
# plt.plot(Oo1[:,0],Oo1[:,1],'.')

ox1=868-802+1
Otop_o1= np.zeros((ox1,3))
Obottom_o1= np.zeros((ox1,3))


for j in range(ox1):    
    omid_o1=Oo1[Oo1[:,0] == 802+j]
    for l in range(len(omid_o1)):
        if omid_o1[l,1]==min(omid_o1[:,1]):
            Obottom_o1[j,:]=omid_o1[l,:]

# Obottom_o1=np.delete(O, 46, 0)
plt.plot(Obottom_o1[:,0],Obottom_o1[:,1],'.')

np.savetxt("Obottom_o1.csv", Obottom_o1, delimiter='\t', fmt='%4d')

#O_bottom
Oo2_temp=Oin[Oin[:,0] >= 802]
Oo2=Oo2_temp[Oo2_temp[:,0] <= 868]
Oo2_sortedy = Oo2[Oo2[:, 1].argsort()]
Oo2_temp=Oo2_sortedy[Oo2_sortedy[:,1] >= -188]
Oo2=Oo2_temp[Oo2_temp[:,1] <= -168]
Oo2= Oo2[Oo2[:, 0].argsort()]
# plt.plot(Oo2[:,0],Oo2[:,1],'.')

ox2=868-802+1
Otop_o2= np.zeros((ox2,3))
Obottom_o2= np.zeros((ox2,3))


for j in range(ox2):    
    omid_o2=Oo2[Oo2[:,0] == 802+j]
    for l in range(len(omid_o2)):
        if omid_o2[l,1]==max(omid_o2[:,1]):
            Otop_o2[j,:]=omid_o2[l,:]

plt.plot(Otop_o2[:,0],Otop_o2[:,1],'.')   

np.savetxt("Otop_o1.csv", Otop_o2, delimiter='\t', fmt='%4d')      
            
