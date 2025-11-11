function exercise5(y)
    ans = roots(y);
    x = min(ans)-2:0.01:max(ans)+2;
    
    t1 = polyval(y,x);
    t2 = polyval(y,ans);
    
    plot(x,t1,'k',ans, t2, 'ro');