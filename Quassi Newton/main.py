import sympy as sp
import numpy as np

#define symoblic variable
x_1,x_2,S,α,β,ϴ = sp.symbols('x_1 x_2 S α β ϴ')

#define the function
f = (x_1)**2+3*(x_2)**2+(x_1)*(x_2)+(x_1)+(x_2)

#calculate derivative for x1 and x2
df_dx1=sp.diff(f,x_1)
df_dx2=sp.diff(f,x_2)

#define inital values
x_1_value=0
x_2_value=0
X_0= np.array([[x_1_value, x_2_value]])
X_0_transpose=X_0.transpose()
h_0 = np.array([[1/2, 0],
                [0, 1/6]])
q_0_Uvalue = df_dx1.subs({x_1: x_1_value, x_2: x_2_value})
q_0_Avalue = df_dx2.subs({x_1: x_1_value, x_2: x_2_value})
q_0 = np.array([[q_0_Uvalue, q_0_Avalue]])## Q0 MATRİS
q_0_transpose = q_0.transpose()

#Find p_0
p_0 = np.dot(h_0, q_0.transpose())*-1
p_0_transpose=p_0.transpose()
#find X_1
X_1=X_0_transpose+S*p_0

#take X_1 and put the gradient for q_1
q_1_Uvalue = df_dx1.subs({x_1: X_1[0, 0], x_2: X_1[1, 0]})
q_1_Avalue = df_dx2.subs({x_1: X_1[0, 0], x_2: X_1[1, 0]})
q_1 = np.array([[q_1_Uvalue, q_1_Avalue]])
#q_1 transpose
q_1_transpose=q_1.transpose()

# Multiplication Operation
result_sum = np.dot(p_0_transpose, q_1_transpose).sum()

## Find S
if result_sum != 0:
    S_solve = sp.solve(result_sum, S)

## X_1  (Without S)
reel_X_1 = X_0_transpose+ S_solve*p_0
reel_X_1_transpose=reel_X_1.transpose()
reel_X_1_Uvalue = reel_X_1_transpose[0,0]
reel_X_1_Avalue = reel_X_1_transpose[0,1]

## Q_1 in sayısal hali (without S)
reel_q_1_Uvalue =df_dx1.subs({x_1: reel_X_1_Uvalue, x_2: reel_X_1_Avalue})
reel_q_1_Avalue =df_dx2.subs({x_1: reel_X_1_Uvalue, x_2: reel_X_1_Avalue})
reel_q_1=np.array([[reel_q_1_Uvalue,reel_q_1_Avalue]])

#q1 transpose
reel_q_1_transpose = np.transpose(reel_q_1)

ϴ = reel_q_1_transpose - q_0_transpose
α = reel_X_1 - X_0_transpose
β = np.divide(α, ϴ)
print(f"β = {β}")
