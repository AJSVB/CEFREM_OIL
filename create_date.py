import numpy as np
import math as Math
Math.PI = Math.pi
def measure(lon1, lat1, lon2, lat2):#  // generally used geo measurement function
    R = 6378.137; 
    dLat = lat2 * Math.PI / 180 - lat1 * Math.PI / 180;
    dLon =  lon2 * Math.PI / 180 - lon1 * Math.PI / 180;
    a = Math.sin(dLat/2) * Math.sin(dLat/2) +\
    Math.cos(lat1 * Math.pi / 180) * Math.cos(lat2 * Math.pi / 180) *\
    Math.sin(dLon/2) * Math.sin(dLon/2);
    c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
    d = R * c;
    return d * 1000; 
first_group=np.array([
"028779_034271_670E",
"027729_03213D_8BBA",
"028254_03310D_2CBF",
"017008_01FFFA_2E03",
"028079_032BC4_CD6E",
"017183_02051B_23A0",
"017358_020A41_209E",
"017708_02150F_A538",
"016658_01F5A2_5CAE",
"016833_01FAD0_8D68",
                      
                     ])

second_group=np.array([
"028604_033C4E_98EB",
"027554_031BF8_7B59",
"027729_03213D_A1D8",
"028254_03310D_6290",
"017008_01FFFA_C60A",
"028079_032BC4_87EA",
"017358_020A41_D491",
"017708_02150F_E0EC",
"016658_01F5A2_350C",
"016833_01FAD0_BA57",
])
third_group=np.array([
"028101_032C77_1CCF",
"027926_032729_DEE9",
"028801_034342_51B4",
"017730_0215BB_2364",
"017030_02009E_F92F",
"016855_01FB70_AB59",
"016505_01F10F_FAA2",
"016680_01F645_FD3F",
"017205_0205B9_3E58",
"017380_020AEB_E6E8",
])

forth_group=np.array([
"028626_033D1F_B4CC",
"027576_031CA9_F5D7",
"028101_032C77_9739",
"028801_034342_D9A6",
"017030_02009E_89B6",
"016855_01FB70_D844",
"016505_01F10F_CE84",
"016680_01F645_F4EA",
"017205_0205B9_FC6E",
"017380_020AEB_BFE2",
])

fifth_group=np.array([
"017103_0202E0_ED2A",
"016753_01F88A_4864",
"017628_0212A4_55BC",
"017803_021813_3EE0",
"028699_033FA1_D891",
"027824_03241B_074F",
"027999_03296C_8743",
"028349_03340F_99EC",
"028174_032EB2_883E",
"027649_031EE7_4717",
])
sixth_group=np.array([
"027904_032677_7DC6",
"027729_03213D_0519",
"028254_03310D_936A",
"017008_01FFFA_F527",
"028079_032BC4_7648",
"017183_02051B_01C1",
"017358_020A41_D598",
"017708_02150F_4A19",
"016658_01F5A2_EFC7",
"016833_01FAD0_D849",
])

seventh_group=np.array([
"017278_0207F5_CEC4",
"017103_0202E0_A9AF",
"016753_01F88A_D43A",
"017628_0212A4_8289",
"028699_033FA1_69F2",
"027824_03241B_5DED",
"027999_03296C_F3EE",
"028349_03340F_184D",
"028174_032EB2_0654",
"027649_031EE7_99E7",
])

eighth_group=np.array([
"028028_032A54_1326",
"028203_032F9A_8D65",
"027503_031A7A_15BF",
"027678_031FC6_FF41",
"017307_0208BF_966A",
"016607_01F41E_780A",
"016782_01F955_C3BB",
"017132_0203A9_7C6F",
"016957_01FE80_992C",
"017657_02137D_4CB9",
])

nineth_group=np.array([
"027605_031D91_1F38",
"027780_0322C6_7D07",
"028130_032D5B_A82B",
"027955_03280F_DEA4",
"017059_020187_B2C6",
"017759_0216AE_0302",
"017234_02069A_FA82",
"016709_01F72A_140B",
"016884_01FC52_ECF0",
"016534_01F1F5_DCBA",
])

tenth_group=np.array([
"028181_032EEB_28C4",
"028356_033445_2871",
"028006_0329A5_63CF",
"027831_032454_6468",
"027656_031F1B_3F13",
"027481_0319CB_6187",
"027481_0319CB_6187",
"028706_033FE4_B6E6",
"028706_033FE4_B6E6",
"028706_033FE4_B6E6",
])

eleventh_group=np.array([
"027481_0319CB_0EB7",
"028181_032EEB_4893",
"028706_033FE4_2FFD",
"028356_033445_2A73",
"028006_0329A5_273D",
"027831_032454_5DEC",
"027656_031F1B_4DB1",
"028706_033FE4_2FFD",
"028181_032EEB_4893",
"028181_032EEB_4893",
])

twelveth_group=np.array([
"017285_020823_CC8F",
"017285_020823_CC8F",
"017810_02184A_6A9D",
"017810_02184A_6A9D",
"017110_02030F_5E87",
"017635_0212D5_0F87",
"016935_01FDE7_0A5C",
"016935_01FDE7_0A5C",
"016760_01F8BE_D7F3",
"017810_02184A_6A9D",
])

thirteenth_group=np.array([
"028283_0331F4_7541",
"027583_031CDB_C720",
"027758_032215_7AB6",
"028108_032CA6_0773",
"027933_03275A_96C5",
"027933_03275A_96C5",
"028108_032CA6_0773",
"028633_033D57_CEAB",
"028633_033D57_CEAB",
"028633_033D57_CEAB",
])


import json
from collections import Counter
with open('data_in/images_informations_preprocessed.json') as json_file:
    data = json.load(json_file)
    #for p in data:
        #print(p)
    l1= {}
    l3= {}
    l5= {}
    l7= {}
    l9= {}
    l11= {}
    l13= {}
    l15= {}
    l17= {}
    l19= {}
    l21= {}
    l23= {}
    l25= {}

    x=1000000000
    for p in data:
        if (first_group == p).any():
            l1[str(p)] = [int(data[p]['coord_upperleft'][0]*x) / x,int(data[p]['coord_upperleft'][1]*x) /x,
                          int(data[p]['coord_lowerright'][0]*x) /x,
                          int(data[p]['coord_lowerright'][1]*x) /x
                         ]
            
        if (second_group == p).any():
            l3[str(p)] = [int(data[p]['coord_upperleft'][0]*x) / x,int(data[p]['coord_upperleft'][1]*x) /x,
                          int(data[p]['coord_lowerright'][0]*x) /x,
                          int(data[p]['coord_lowerright'][1]*x) /x
                         ]
        if (third_group == p).any():
            l5[str(p)] = [int(data[p]['coord_upperleft'][0]*x) / x,int(data[p]['coord_upperleft'][1]*x) /x,
                          int(data[p]['coord_lowerright'][0]*x) /x,
                          int(data[p]['coord_lowerright'][1]*x) /x
                         ]
            
        if (forth_group == p).any():
            l7[str(p)] = [int(data[p]['coord_upperleft'][0]*x) / x,int(data[p]['coord_upperleft'][1]*x) /x,
                          int(data[p]['coord_lowerright'][0]*x) /x,
                          int(data[p]['coord_lowerright'][1]*x) /x
                         ]
            
        if (fifth_group == p).any():
            l9[str(p)] = [int(data[p]['coord_upperleft'][0]*x) / x,int(data[p]['coord_upperleft'][1]*x) /x,
                          int(data[p]['coord_lowerright'][0]*x) /x,
                          int(data[p]['coord_lowerright'][1]*x) /x
                         ]
        if (sixth_group == p).any():
            l11[str(p)] = [int(data[p]['coord_upperleft'][0]*x) / x,int(data[p]['coord_upperleft'][1]*x) /x,
                          int(data[p]['coord_lowerright'][0]*x) /x,
                          int(data[p]['coord_lowerright'][1]*x) /x
                         ]
            
        if (seventh_group == p).any():
            l13[str(p)] = [int(data[p]['coord_upperleft'][0]*x) / x,int(data[p]['coord_upperleft'][1]*x) /x,
                          int(data[p]['coord_lowerright'][0]*x) /x,
                          int(data[p]['coord_lowerright'][1]*x) /x
                         ]
        if (eighth_group == p).any():
            l15[str(p)] = [int(data[p]['coord_upperleft'][0]*x) / x,int(data[p]['coord_upperleft'][1]*x) /x,
                          int(data[p]['coord_lowerright'][0]*x) /x,
                          int(data[p]['coord_lowerright'][1]*x) /x
                         ]
        if (nineth_group == p).any():
            l17[str(p)] = [int(data[p]['coord_upperleft'][0]*x) / x,int(data[p]['coord_upperleft'][1]*x) /x,
                          int(data[p]['coord_lowerright'][0]*x) /x,
                          int(data[p]['coord_lowerright'][1]*x) /x
                         ]
            
        if (tenth_group == p).any():
            l19[str(p)] = [int(data[p]['coord_upperleft'][0]*x) / x,int(data[p]['coord_upperleft'][1]*x) /x,
                          int(data[p]['coord_lowerright'][0]*x) /x,
                          int(data[p]['coord_lowerright'][1]*x) /x
                         ]
            
        if (eleventh_group == p).any():
            l21[str(p)] = [int(data[p]['coord_upperleft'][0]*x) / x,int(data[p]['coord_upperleft'][1]*x) /x,
                          int(data[p]['coord_lowerright'][0]*x) /x,
                          int(data[p]['coord_lowerright'][1]*x) /x
                         ]
        if (twelveth_group == p).any():
            l23[str(p)] = [int(data[p]['coord_upperleft'][0]*x) / x,int(data[p]['coord_upperleft'][1]*x) /x,
                          int(data[p]['coord_lowerright'][0]*x) /x,
                          int(data[p]['coord_lowerright'][1]*x) /x
                         ]
            
        if (thirteenth_group == p).any():
            l25[str(p)] = [int(data[p]['coord_upperleft'][0]*x) / x,int(data[p]['coord_upperleft'][1]*x) /x,
                          int(data[p]['coord_lowerright'][0]*x) /x,
                          int(data[p]['coord_lowerright'][1]*x) /x
                         ]

       # print(data[p]['coord_upperleft'])
        #print(data[p]['coord_lowerright'])
        #print()
   # print(l1)
    #print(l2)
#    a=Counter(l1)
#    b=Counter(l2)
#    c=Counter(l3)
#    d=Counter(l4)
    
print(np.array(list(l1.values())))
leftmax1 = np.array(list(l1.values()))[:,0]
uppermin1 = np.array(list(l1.values()))[:,1]
print(leftmax1)
print(uppermin1)
print(np.max(leftmax1))
print(np.min(uppermin1))
leftmaxv1=np.max(leftmax1)
upperminv1=np.min(uppermin1)

print(np.array(list(l3.values())))
leftmax3 = np.array(list(l3.values()))[:,0]
uppermin3 = np.array(list(l3.values()))[:,1]
print(leftmax3)
print(uppermin3)
print(np.max(leftmax3))
print(np.min(uppermin3))
leftmaxv3=np.max(leftmax3)
upperminv3=np.min(uppermin3)

print(np.array(list(l5.values())))
leftmax5 = np.array(list(l5.values()))[:,0]
uppermin5 = np.array(list(l5.values()))[:,1]
print(leftmax5)
print(uppermin5)
print(np.max(leftmax5))
print(np.min(uppermin5))
leftmaxv5=np.max(leftmax5)
upperminv5=np.min(uppermin5)

print(np.array(list(l7.values())))
leftmax7 = np.array(list(l7.values()))[:,0]
uppermin7 = np.array(list(l7.values()))[:,1]
print(leftmax7)
print(uppermin7)
print(np.max(leftmax7))
print(np.min(uppermin7))
leftmaxv7=np.max(leftmax7)
upperminv7=np.min(uppermin7)

print(np.array(list(l9.values())))
leftmax9 = np.array(list(l9.values()))[:,0]
uppermin9 = np.array(list(l9.values()))[:,1]
print(leftmax9)
print(uppermin9)
print(np.max(leftmax9))
print(np.min(uppermin9))
leftmaxv9=np.max(leftmax9)
upperminv9=np.min(uppermin9)

print(np.array(list(l11.values())))
leftmax11 = np.array(list(l11.values()))[:,0]
uppermin11 = np.array(list(l11.values()))[:,1]
print(leftmax11)
print(uppermin11)
print(np.max(leftmax11))
print(np.min(uppermin11))
leftmaxv11=np.max(leftmax11)
upperminv11=np.min(uppermin11)

print(np.array(list(l13.values())))
leftmax13 = np.array(list(l13.values()))[:,0]
uppermin13 = np.array(list(l13.values()))[:,1]
print(leftmax13)
print(uppermin13)
print(np.max(leftmax13))
print(np.min(uppermin13))
leftmaxv13=np.max(leftmax13)
upperminv13=np.min(uppermin13)

print(np.array(list(l15.values())))
leftmax15 = np.array(list(l15.values()))[:,0]
uppermin15 = np.array(list(l15.values()))[:,1]
print(leftmax15)
print(uppermin15)
print(np.max(leftmax15))
print(np.min(uppermin15))
leftmaxv15=np.max(leftmax15)
upperminv15=np.min(uppermin15)

print(np.array(list(l17.values())))
leftmax17 = np.array(list(l17.values()))[:,0]
uppermin17 = np.array(list(l17.values()))[:,1]
print(leftmax17)
print(uppermin17)
print(np.max(leftmax17))
print(np.min(uppermin17))
leftmaxv17=np.max(leftmax17)
upperminv17=np.min(uppermin17)

print(np.array(list(l19.values())))
leftmax19 = np.array(list(l19.values()))[:,0]
uppermin19 = np.array(list(l19.values()))[:,1]
print(leftmax19)
print(uppermin19)
print(np.max(leftmax19))
print(np.min(uppermin19))
leftmaxv19=np.max(leftmax19)
upperminv19=np.min(uppermin19)

print(np.array(list(l21.values())))
leftmax21 = np.array(list(l21.values()))[:,0]
uppermin21 = np.array(list(l21.values()))[:,1]
print(leftmax21)
print(uppermin21)
print(np.max(leftmax21))
print(np.min(uppermin21))
leftmaxv21=np.max(leftmax21)
upperminv21=np.min(uppermin21)

print(np.array(list(l23.values())))
leftmax23 = np.array(list(l23.values()))[:,0]
uppermin23 = np.array(list(l23.values()))[:,1]
print(leftmax23)
print(uppermin23)
print(np.max(leftmax23))
print(np.min(uppermin23))
leftmaxv23=np.max(leftmax23)
upperminv23=np.min(uppermin23)

print(np.array(list(l25.values())))
leftmax25 = np.array(list(l25.values()))[:,0]
uppermin25 = np.array(list(l25.values()))[:,1]
print(leftmax25)
print(uppermin25)
print(np.max(leftmax25))
print(np.min(uppermin25))
leftmaxv25=np.max(leftmax25)
upperminv25=np.min(uppermin25)

l2 = {}
l4 = {}
l6 = {}
l8 = {}
l10 = {}
l12 = {}
l14 = {}
l16 = {}
l18 = {}
l20 = {}
l22 = {}
l24 = {}
l26 = {}

def wow(l1,l2,upperminv,leftmaxv,x,y):
    for k in l1:
        v=l1[k]
        print(v)
        l2[k] =  [int(measure(v[0],upperminv,leftmaxv,upperminv)/y),int(measure(leftmaxv,v[1],leftmaxv,upperminv)/x)]
        

    

wow(l1,l2,upperminv1,leftmaxv1,27.06052348, 11.49417818)
print()
wow(l3,l4,upperminv3,leftmaxv3,26.92563584, 11.7892986)
print("Lui")
wow(l5,l6,upperminv5,leftmaxv5,27.19040644, 11.18661894)
print()
wow(l7,l8,upperminv7,leftmaxv7,27.24637143, 11.40972705)
21.535343308
39.918591556
print()

wow(l9,l10,upperminv9,leftmaxv9,27.29277991, 11.3347548)
print()

wow(l11,l12,upperminv11,leftmaxv11,26.97047807, 11.28243305)
print()

wow(l13,l14,upperminv13,leftmaxv13,27.1187434,  11.86561356)
print()
wow(l15,l16,upperminv15,leftmaxv15,27.29791944, 11.79595231)
print("Lui")
wow(l17,l18,upperminv17,leftmaxv17,27.45173665, 11.19293078)
print()
wow(l19,l20,upperminv19,leftmaxv19,26.77823651 ,11.39256797)
21.535343308
39.918591556
print()

wow(l21,l22,upperminv21,leftmaxv21,26.75344831 ,11.30063966)
print()

wow(l23,l24,upperminv23,leftmaxv23,26.6025474  ,11.25265844)
print()

wow(l25,l26,upperminv25,leftmaxv25,26.74274096 ,11.77327846)

[]
[]
[]
[]
[]
[]

import h5py
import matplotlib.pyplot as plt
import numpy as np
import cv2
hf_im=h5py.File('data_in/images_preprocessed.hdf5','r')
hf_an=h5py.File('data_in/annotations_labels_preprocessed.hdf5','r')
def reduce_bit(x):
    return (x+80)*2 #cv2.normalize(x, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)


def wowo(first_group,l2,input_array,output_array,miy,mix):
    maxx = np.max(np.array(list(l2.values())),axis=0)
   # print(maxx)
    for e,image_key in enumerate(first_group):
        temp = np.array(hf_im[image_key])
        #print(temp.shape)
        
        temp = temp[l2[image_key][1]:miy+l2[image_key][1]-maxx[1],l2[image_key][0]:-maxx[0]+mix+l2[image_key][0]]
        tempan = np.array(hf_an[image_key])
        tempan = tempan[l2[image_key][1]:miy+l2[image_key][1]-maxx[1],l2[image_key][0]:-maxx[0]+mix+l2[image_key][0]]

        #input_array.append((temp,temp,temp))
        input_array.append(reduce_bit(temp))
        output_array.append(tempan) #todo attention

#        output_array.append((tempan==1)*256.) #todo attention
        
        print(temp.shape)
        


  #  fig1=plt.figure(1)

    tempsum = np.sum(te[4000:4100,4500:4600] for te in input_array) 

  #  plt.imshow(tempsum)
  #  plt.colorbar()
  #  plt.show()



    #hf_seg.close()
#def reduce_bit(x):
#    return x*256
scale = 1
def saver(input_array,output_array,string, ext = False):
        iag = input_array[0]

        shap = iag.shape
        s1=shap[1]
        s0=shap[0]
        for x in np.arange(0,s1,256*scale):
            for y in np.arange(0,s0,256*scale):

                temp = np.array(input_array[:,y:y+256*scale:,x:x+256*scale:])

                tempan = np.array(output_array[:,y:y+256*scale:,x:x+256*scale:])
                mask1= (tempan==1)*1.
                mask2= (tempan==2)*1.

                #print(tempan.shape)
                a = np.max(np.max(tempan,axis = -1),axis=-1)
                #print(a.shape)
                b = np.sort(a)
                #print(b)
                #print(b[-3])
                if(np.sum(temp==160)>130):
            #    print("nop")
                    continue
                if b[-2-2*ext] != 1 and b[-1] != 2: 
                #if(np.sum(tempan!=0)<1):
                #    continue
                    #if(len(input_array)==len(nothing_array)):
                    #    continue
                    #else:
                    import random
                    if random.random() < .99:
                       # nothing_array.append(reduce_bit(temp))
                        continue

                import matplotlib
                #print(temp)
                #print(tempan)
                tempan = np.amax((tempan),axis=0)
                #print(tempan)
                #break
                #print(tempan)
              #  print(input_image[i].shape)
               # print(b[-1])
                a='6X/'+str(string)+str(x)+str(y)+'.jpg'
                b='6Y/'+str(string)+str(x)+str(y)+'.jpg'
                c=temp
                d=tempan

                #plt.imshow(tempan)
                #plt.colorbar()

               # plt.show()
                #np.to_csv(a,c)
                #np.to_csv(b,d)
                #c.tofile(a,sep=',')
                #d.tofile(b,sep=',')
                with open(a, 'wb') as f:
                    np.save(f, c )
                with open(b, 'wb') as f:
                    np.save(f, d )
                #print(d)
              #  input_array.append(reduce_bit(temp))
             #   annotation_array.append(tempan)

              #  print(temp.shape)

input_array1=[]
output_array1 = []
input_array2=[]
output_array2 = []
input_array3=[]
output_array3 = []
input_array4=[]
output_array4 = []
input_array5=[]
output_array5 = []
input_array6=[]
output_array6 = []
input_array7=[]
output_array7 = []
input_array8=[]
output_array8 = []
input_array9=[]
output_array9 = []
input_array10=[]
output_array10 = []
input_array11=[]
output_array11 = []
input_array12=[]
output_array12 = []
input_array13=[]
output_array13 = []

wowo(first_group,l2,input_array1,output_array1, 10608, 18441)
input_array = np.array(input_array1)
output_array = np.array(output_array1)
del input_array1
del output_array1
saver(input_array,output_array,'first')

wowo(second_group,l4,input_array2,output_array2,10119, 17719)
input_array = np.array(input_array2)
output_array = np.array(output_array2)
del input_array2
del output_array2
saver(input_array,output_array,'second')

wowo(third_group,l6,input_array3,output_array3,10634, 19011)
input_array = np.array(input_array3)
output_array = np.array(output_array3)
del input_array3
del output_array3
saver(input_array,output_array,'third')

wowo(forth_group,l8,input_array4,output_array4,10638, 18649)
input_array = np.array(input_array4)
output_array = np.array(output_array4)
del input_array4
del output_array4
saver(input_array,output_array,'forth')

wowo(fifth_group,l10,input_array5,output_array5,10632, 18663)
input_array = np.array(input_array5)
output_array = np.array(output_array5)
del input_array5
del output_array5
saver(input_array,output_array,'fifth')

wowo(sixth_group,l12,input_array6,output_array6,10607, 18784)
input_array = np.array(input_array6)
output_array = np.array(output_array6)
del input_array6
del output_array6
saver(input_array,output_array,'sixth')

wowo(seventh_group,l14,input_array7,output_array7,10666, 17872)
input_array = np.array(input_array7)
output_array = np.array(output_array7)
del input_array7
del output_array7
saver(input_array,output_array,'seventh')

wowo(eighth_group,l16,input_array8,output_array8,10637, 19153)
input_array = np.array(input_array8)
output_array = np.array(output_array8)
del input_array8
del output_array8
saver(input_array,output_array,'eighth')

wowo(nineth_group,l18,input_array9,output_array9,10620, 19143)
input_array = np.array(input_array9)
output_array = np.array(output_array9)
del input_array9
del output_array9
saver(input_array,output_array,'nineth')

wowo(tenth_group,l20,input_array10,output_array10,10623, 17705)
input_array = np.array(input_array10)
output_array = np.array(output_array10)
del input_array10
del output_array10
saver(input_array,output_array,'tenth')

wowo(eleventh_group,l22,input_array11,output_array11,10599, 18439)
input_array = np.array(input_array11)
output_array = np.array(output_array11)
del input_array11
del output_array11
saver(input_array,output_array,'eleventh')

wowo(twelveth_group,l24,input_array12,output_array12,10582, 18115)
input_array = np.array(input_array12)
output_array = np.array(output_array12)
del input_array12
del output_array12
saver(input_array,output_array,'twelveth')

wowo(thirteenth_group,l26,input_array13,output_array13,10582, 18825)
input_array = np.array(input_array13)
output_array = np.array(output_array13)
del input_array13
del output_array13
saver(input_array,output_array,'thirteenth',ext=True)


hf_im.close()
hf_an.close()



