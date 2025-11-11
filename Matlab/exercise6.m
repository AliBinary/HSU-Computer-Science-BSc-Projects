function exercise6()
    % y=2x^4 -6x^3 +5x^2 -x +3
    y = [2 -6 5 -1 3];

    p = polyder(y);

    exercise5(p);
end

function exercise5(y)
    ans = roots(y);
    x = min(ans)-1:0.01:max(ans)+1;
    
    t1 = polyval(y,x);
    t2 = polyval(y,ans);
    
    plot(x,t1,'k',ans, t2, 'ro');
end