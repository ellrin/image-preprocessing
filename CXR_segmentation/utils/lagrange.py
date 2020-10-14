def lagrange(xpred, X, Y):
    
    ypred = 0

    for i in range(len(X)):

        xa = list(X[0:i])
        xb = list(X[i+1:])

        xa.extend(xb) 
        fn = Y[i]
        for j in range(len(xa)):
            
            fn *= (xpred-xa[j])/(X[i]-xa[j])
            
        ypred += fn
        
    return ypred      