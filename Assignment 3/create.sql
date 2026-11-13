USE sandwich_maker;

CREATE TABLE sandwiches (
    sandwich_size varchar(50),
    price decimal(5, 2)
);

CREATE TABLE resources (
    Item varchar(50),
    amount int
);

CREATE TABLE recipes (
    sandwich_size varchar(50),
    Item varchar(50),
    amount int
);