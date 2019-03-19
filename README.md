# phonydatamaker
Makes phony data

That's what it does.

Basically just some phony banking data  with account number, credit score, debt to income ratio, total balances of deposits,
total balances of loans, and 100 weeks of product uptake. Not super realistic but kind of close. Deposits, loans, and debt to income 
are skewed as I've seen in real life.

Credit score is centered around US mean credit score.
Debt to income and the two balances combined with credit score do not add up btw. An account could have a few mil on deposit
and a bunch borrowed, a low debt to income and a terrible credit score. Its all pseudo random with attempts only made to
match skewedness that I've seen irl.

Products are labelled with number 1 to 100. 0's represent no product. There are 100 instances representing a single week each.
So, each element is a week and if a product was taken out that week it was labelled. If it is a 0 then no product that week.
