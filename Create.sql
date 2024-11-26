Create database Restaurant

USE Restaurant

-- Dish
CREATE TABLE Dish (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Type VARCHAR(255) NOT NULL,
    Weight FLOAT CHECK (Weight > 0),
    Price MONEY CHECK (Price > 0)
);

-- Recipe
CREATE TABLE Recipe (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Dish_ID INT NOT NULL,
    Time FLOAT CHECK (Time > 0),
    Technology VARCHAR(255) NOT NULL,
    CONSTRAINT FK_Recipe_Dish FOREIGN KEY (Dish_ID) REFERENCES Dish(ID) ON DELETE CASCADE,
    CONSTRAINT UC_Recipe_Dish UNIQUE (Dish_ID)
);

-- Cooking
CREATE TABLE Cooking (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Dish_ID INT NOT NULL,
    Amount INT CHECK (Amount > 0),
    Date DATETIME NOT NULL,
    CONSTRAINT FK_Cooking_Dish FOREIGN KEY (Dish_ID) REFERENCES Dish(ID) ON DELETE CASCADE
);