function exercise7()
    % y=x^2 +x
    y = [1 1 0];

    syms x
    ans = int(x^2+x,0,pi);
    disp(ans)
    
    p = polyint(y);
    x = 0:0.01:pi;
    plot(x,polyval(p,x));

