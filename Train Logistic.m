load('female 40x40');
dataFemale = female;
load('male 40x40');
dataMale = male;
fprintf('Data Loaded \n');
XNetM=dataMale(1:291,:);
XNetF=dataFemale(1:339,:);

yNetM=ones(291,1);
yNetF=zeros(339,1);

X1=XNetM(1:281,:);
X2=XNetF(1:329,:);
y1=yNetM(1:281,:);
y2=yNetF(1:329,:);

X=[X1;X2];
y=[y1;y2];

fprintf('X and y formed \n');
[m, n] = size(X);
X = [ones(m, 1) X];
initial_theta = zeros(n + 1, 1);
[cost, grad] = costFunction(initial_theta, X, y);

fprintf('Cost at initial theta (zeros): %f\n', cost);

fprintf('\nProgram paused. Press enter to continue.\n');
pause;

options = optimset('GradObj', 'on', 'MaxIter', 400);
[theta, cost] = fminunc(@(t)(costFunction(t, X, y)), initial_theta, options);

fprintf('Cost at theta found by fminunc: %f\n', cost);












