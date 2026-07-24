from fractions import Fraction as F


def H(n):
    s=F(0)
    for j in range(1,n+1): s += F(1,j)
    return s

min_prod=(None,None)
for d in range(3,121):
    gam=F(1,12*d**3)
    eps=F(2,12*d**3-1)
    alpha=(1-gam)/d
    assert eps*(1-gam)/2==gam
    assert alpha*alpha>4*gam
    assert alpha-F(1,d+1)-3*gam/(2*alpha)>0
    assert (d+1)**2*gam<alpha
    assert d*eps<F(1,50)
    assert eps<F(13,2000)
    for m in range(2,d+1):
        B=1+(m-1)*eps
        A=(1+(F(5*m,3)-1)*eps)/(1-m*eps)
        delta=A-1
        assert m*eps<F(1,50)
        assert A<F(6,5)
        assert delta<3*d*eps
        assert gam*B/((m-1)*(1-eps))<eps
        assert A-B>m*eps
        for t in range(2,m+1):
            z=delta*H(t-2)
            assert z<1
            Flow=(1-2*m*eps)*(1-eps)**2*(1-z)**2
            assert Flow>F(m,m+1)
            # c_t=t-1 equality branch: only t>=4, t<=m-1, r=m-t+1
            if 4<=t<=m-1:
                r=m-t+1
                R=F((t-1)*r*(m-1)**2, m*(r+t-2)**2)
                assert R>=F(m+1,m)
                P=Flow*R
                if min_prod[0] is None or P<min_prod[0]: min_prod=(P,(d,m,t,r,t-1,'eq'))
            # c_t>=t branch, t<m; check every r
            if t<m:
                for r in range(1,m-t+2):
                    R=F(t*r*(m-1)**2,m*(r+t-2)**2)
                    assert R>=F(m+1,m)
                    P=Flow*R
                    if min_prod[0] is None or P<min_prod[0]: min_prod=(P,(d,m,t,r,t,'ge'))
            else:
                # t=m: nonendpoint c_t>=m+1
                r=1
                R=F((m+1)*r*(m-1)**2,m*(r+t-2)**2)
                assert R==F(m+1,m)
                P=Flow*R
                if min_prod[0] is None or P<min_prod[0]: min_prod=(P,(d,m,t,r,m+1,'endpoint-excluded'))
print('all independent exact checks passed through d=120')
print('minimum FR=', float(min_prod[0]), 'at', min_prod[1])
print('exact=', min_prod[0])
