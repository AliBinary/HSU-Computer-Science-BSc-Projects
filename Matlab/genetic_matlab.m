% Define the fitness function (objectives)
function y = multiobjective(x)
    y(1) = 0.225*x(1) + 2.2*x(2) + 0.8*x(3) + 0.1*x(4) + 0.05*x(5) + 0.26*x(6);
    y(2) = 10*x(1) + 20*x(2) + 120*x(3);
    y(3) = 24*x(1) + 27*x(2) + 15*x(4) + 1.1*x(5) + 52*x(6);
end

% Define the nonlinear inequality constraints (g_i(x))
function [c, ceq] = nonlinear_constraints(x)
    c = [
        720*x(1) + 107*x(2) + 7080*x(3) + 134*x(5) + 1000*x(6) - 5000;
        0.2*x(1) + 10.1*x(2) + 13.2*x(3) + 0.75*x(4) + 0.15*x(5) + 1.2*x(6) - 12.5;
        344*x(1) + 460*x(2) + 1040*x(3) + 75*x(4) + 17.4*x(5) + 240*x(6) - 2500;
        18*x(1) + 151*x(2) + 78*x(3) + 2.5*x(4) + 0.2*x(5) + 4*x(6) - 63;
        x(1) - 6.0;
        x(2) - 1.0;
        x(3) - 0.25;
        x(4) - 10.0;
        x(5) - 10.0;
        x(6) - 4.0
    ];
    ceq = []; % No equality constraints
end

% Set optimization options
options = optimoptions('gamultiobj', 'MaxGenerations', 100);

% Solve the multi-objective optimization problem
numberOfVariables = 6;
[x, fval] = gamultiobj(@multiobjective, numberOfVariables, [], [], [], [], zeros(1, numberOfVariables), [], @nonlinear_constraints, options);

% Display results
disp('Optimal solutions (Pareto front):');
disp(x);
disp('Objective function values at the Pareto front:');
disp(fval);
