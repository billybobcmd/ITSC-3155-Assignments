USE sandwich_maker;

INSERT INTO resources (Item, amount) VALUES
("bread", 12),
("ham", 18),
("cheese", 24);

INSERT INTO sandwiches (sandwich_size, price) VALUES
("small", 1.75),
("medium", 3.25),
("large", 5.5);

INSERT INTO recipes (sandwich_size, Item, amount) VALUES
("small", "bread", 2),
("small", "ham", 4),
("small", "cheese", 4),
("medium", "bread", 4),
("medium", "ham", 6),
("medium", "cheese", 8),
("large", "bread", 6),
("large", "ham", 8),
("large", "cheese", 12);