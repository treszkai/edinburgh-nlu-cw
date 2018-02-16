from rnn import *
import numpy as np
# this will test the implementation of predict, acc_deltas, and acc_deltas_bptt in rnn.py, for a simple 3x2 RNN

y_exp = np.array([[ 0.39411072,  0.32179748,  0.2840918 ], [ 0.4075143,   0.32013043,  0.27235527], [ 0.41091755,  0.31606385,  0.2730186 ], [ 0.41098376,  0.31825833,  0.27075792], [ 0.41118931,  0.31812307,  0.27068762], [ 0.41356637,  0.31280332,  0.27363031], [ 0.41157736,  0.31584609,  0.27257655]])
s_exp = np.array([[ 0.66818777,  0.64565631], [ 0.80500806,  0.80655686], [ 0.85442692,  0.79322425], [ 0.84599959,  0.8270955 ], [ 0.84852462,  0.82794442], [ 0.89340731,  0.7811953 ], [ 0.86164528,  0.79916155], [ 0., 0.]])
U_exp = np.array([[ 0.89990596,  0.79983619], [ 0.5000714,   0.30009787]])
V_exp = np.array([[ 0.69787081,  0.30129314,  0.39888647], [ 0.60201076,  0.89866058,  0.70149262]])
W_exp = np.array([[ 0.57779081,  0.47890397], [ 0.22552931,  0.62294835], [ 0.39667988 , 0.19814768]])

loss_expected = 8.19118156763
loss2_expected = 3.29724981191
loss3_expected = 6.01420605985
mean_loss_expected = 1.16684249596

deltaU_1_exp = np.array([[-0.11298744, -0.107331  ], [ 0.07341862, 0.06939134]])
deltaV_1_exp = np.array([[-0.06851441, -0.05931481, -0.05336094], [ 0.06079254,  0.0035937,   0.04875759]])
deltaW_1_exp = np.array([[-2.36320453, -2.24145091], [ 3.13861959,  2.93420307], [-0.77541506, -0.69275216]])

deltaU_3_exp = np.array([[-0.12007034, -0.1141893 ], [ 0.06377434, 0.06003115]])
deltaV_3_exp = np.array([[-0.07524721, -0.06495432, -0.05560471], [ 0.05465826, -0.00306904, 0.04567927]])
deltaW_3_exp = np.array([[-2.36320453, -2.24145091], [ 3.13861959,  2.93420307], [-0.77541506, -0.69275216]])

vocabsize = 3
hdim = 2
# RNN with vocab size 3 and 2 hidden layers
r = RNN(vocabsize,hdim)
r.V[0][0]=0.7
r.V[0][1]=0.3
r.V[0][2]=0.4
r.V[1][0]=0.6
r.V[1][1]=0.9
r.V[1][2]=0.7

r.W[0][0]=0.6
r.W[0][1]=0.5
r.W[1][0]=0.2
r.W[1][1]=0.6
r.W[2][0]=0.4
r.W[2][1]=0.2

r.U[0][0]=0.9
r.U[0][1]=0.8
r.U[1][0]=0.5
r.U[1][1]=0.3

x = np.array([0,1,2,1,1,0,2])
d = np.array([1,2,1,1,1,1,1])
x2 = np.array([1,1,0])
d2 = np.array([1,0,2])
x3 = np.array([1,1,2,1,2])
d3 = np.array([1,2,1,2,1])

print("### predicting y")
y,s = r.predict(x)
if not np.isclose(y_exp, y, rtol=1e-08, atol=1e-08).all():
	print("y expected\n{0}".format(y_exp))
	print("y received\n{0}".format(y))
else:
	print("y passed")
if not np.isclose(s_exp, s, rtol=1e-08, atol=1e-08).all():
	print("\ns expected\n{0}".format(s_exp))
	print("s received\n{0}".format(s))
else:
	print("s passed")

print("\n### computing loss and mean loss")
loss = r.compute_loss(x,d)
loss2 = r.compute_loss(x2,d2)
loss3 = r.compute_loss(x3,d3)
mean_loss = r.compute_mean_loss([x,x2,x3],[d,d2,d3])
if not np.isclose(loss_expected, loss, rtol=1e-08, atol=1e-08) or not np.isclose(loss2_expected, loss2, rtol=1e-08, atol=1e-08) or not np.isclose(loss3_expected, loss3, rtol=1e-08, atol=1e-08):
	print("loss expected: {0}".format(loss_expected))
	print("loss received: {0}".format(loss))
	print("loss2 expected: {0}".format(loss2_expected))
	print("loss2 received: {0}".format(loss2))
	print("loss3 expected: {0}".format(loss3_expected))
	print("loss3 received: {0}".format(loss3))
else:
	print("loss passed")
if not np.isclose(mean_loss_expected, mean_loss, rtol=1e-08, atol=1e-08):
	print("mean loss expected: {0}".format(mean_loss_expected))
	print("mean loss received: {0}".format(mean_loss))
else:
	print("mean loss passed")

print("\n### standard BP")
r.acc_deltas(x,d,y,s)
if not np.isclose(deltaU_1_exp, r.deltaU).all():
	print("\ndeltaU expected\n{0}".format(deltaU_1_exp))
	print("deltaU received\n{0}".format(r.deltaU))
else:
	print("deltaU passed")
if not np.isclose(deltaV_1_exp, r.deltaV).all():
	print("\ndeltaV expected\n{0}".format(deltaV_1_exp))
	print("deltaV received\n{0}".format(r.deltaV))
else:
	print("deltaV passed")
if not np.isclose(deltaW_1_exp, r.deltaW).all():
	print("\ndeltaW expected\n{0}".format(deltaW_1_exp))
	print("deltaW received\n{0}".format(r.deltaW))
else:
	print("deltaW passed")

print("\n### BPTT with 3 steps")
r.deltaU.fill(0)
r.deltaV.fill(0)
r.deltaW.fill(0)

r.acc_deltas_bptt(x,d,y,s,3)
if not np.isclose(deltaU_3_exp, r.deltaU).all():
	print("\ndeltaU expected\n{0}".format(deltaU_3_exp))
	print("deltaU received\n{0}".format(r.deltaU))
else:
	print("deltaU passed")
if not np.isclose(deltaV_3_exp, r.deltaV).all():
	print("\ndeltaV expected\n{0}".format(deltaV_3_exp))
	print("deltaV received\n{0}".format(r.deltaV))
else:
	print("deltaV passed")
if not np.isclose(deltaW_3_exp, r.deltaW).all():
	print("\ndeltaW expected\n{0}".format(deltaW_3_exp))
	print("deltaW received\n{0}".format(r.deltaW))
else:
	print("deltaW passed")
