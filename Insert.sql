USE Restaurant

INSERT INTO Dish (Name, Type, Weight, Price) VALUES 
('Caesar Salad', 'Appetizer', 150, 12.50),
('Fettuccine Alfredo', 'Main Course', 300, 24.90),
('Borscht', 'Soup', 250, 10.90),
('Steak', 'Main Course', 400, 32.00),
('Apple Pie', 'Dessert', 200, 9.50),
('Risotto', 'Main Course', 350, 17.90),
('Sushi', 'Appetizer', 150, 20.00),
('Tandoori Chicken', 'Main Course', 350, 19.90),
('Vegetable Ratatouille', 'Vegetarian', 300, 15.50),
('Cheesecake', 'Dessert', 180, 10.00);

INSERT INTO Recipe (Dish_ID, Time, Technology) VALUES 
(1, 15, 'Mixing ingredients'),
(2, 20, 'Boiling and frying'),
(3, 30, 'Boiling and steeping'),
(4, 25, 'Grilling'),
(5, 40, 'Baking'),
(6, 35, 'Boiling and sauting'),
(7, 20, 'Rolling and slicing'),
(8, 30, 'Marinating and baking'),
(9, 30, 'Boiling and baking'),
(10, 50, 'Baking');

INSERT INTO Cooking (Dish_ID, Amount, Date) VALUES 
(1, 10, '2024-11-01 10:00:00'),
(2, 5, '2024-11-02 11:30:00'),
(3, 8, '2024-11-03 12:15:00'),
(4, 12, '2024-11-04 14:45:00'),
(5, 6, '2024-11-05 09:30:00'),
(6, 11, '2024-11-06 16:00:00'),
(7, 7, '2024-11-07 08:20:00'),
(8, 4, '2024-11-08 17:10:00'),
(9, 9, '2024-11-09 15:00:00'),
(10, 3, '2024-11-10 13:25:00');

SELECT * FROM Dish
SELECT * FROM Recipe
SELECT * FROM Cooking