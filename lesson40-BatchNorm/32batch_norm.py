######################batch_norm######################33####1.解释#不在有效的空间,会出现梯度消失#batch_norm有效地变化#2.feature缩放###Image Noramlization####                                         R,   G ,  B####normalize=transforms.Normalize(mean=[0.485,0.456,0.406],#                                   std=[0.229,0.224,0.225])#######(xR-0.485)/0.229,(xG-0.456)/224,(xB-0.406)/0.225 ~N(0,1)###Batch Noramalization#3.Batch Norm##batch norm,####[N,C,H*W]->[C],ch0mean,...ch(C-1)mean######layer norm,####[N]##instance norm,####[N, C]##Group norm(何凯明),#####4.Batch normalizationimport torchimport torch.nn as nn# x=torch.rand(100,16,784)# layer=nn.BatchNorm1d(16)#channel# out=layer(x)# print(layer.running_mean)# print(layer.running_var)#5.pipline##详见ppt#5.nn.BatchNorm2dx=torch.rand(1,16,7,7)layer=nn.BatchNorm2d(16)out=layer(x)print(out.shape)print(layer.weight)print(layer.weight.shape)print(layer.bias.shape)#6.class variableprint(vars(layer))#affine=true-自动学习，trianning=true#7.testlayer.eval()nn.BatchNorm1d(16,eps=1e-05, momentum=0.1, track_running_stats=True)out=layer(x)#8.好处#收敛的更快#性能更好#更加鲁棒性###稳定###大的lr（对超参变化不敏感）