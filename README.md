# Restaurant Database

## Deploy

http://84.201.167.162:8200/

## Description

The **Restaurant** database is designed to manage information about dishes, their recipes, and the cooking process. It consists of three tables: **Dish**, **Recipe**, and **Cooking**.

## Database Structure

### 1. Table: Dish

- **Purpose**: Stores information about dishes.
- **Fields**:
  - `ID` (INT, PRIMARY KEY) — unique identifier for each dish.
  - `Name` (VARCHAR(255), NOT NULL) — name of the dish.
  - `Type` (VARCHAR(255), NOT NULL) — type of dish (e.g., appetizer, main course, dessert).
  - `Weight` (FLOAT, CHECK (Weight > 0)) — weight of the dish in grams.
  - `Price` (MONEY, CHECK (Price > 0)) — price of the dish.

### 2. Table: Recipe

- **Purpose**: Contains recipes for each dish.
- **Fields**:
  - `ID` (INT, PRIMARY KEY) — unique identifier for each recipe.
  - `Dish_ID` (INT, NOT NULL) — identifier for the associated dish (foreign key).
  - `Time` (FLOAT, CHECK (Time > 0)) — preparation time in minutes.
  - `Technology` (VARCHAR(255), NOT NULL) — cooking technology used (e.g., baking, boiling, frying).
- **Constraints**:
  - `FK_Recipe_Dish` — foreign key referencing `Dish(ID)`.
  - `UC_Recipe_Dish` — unique constraint on `Dish_ID`.

### 3. Table: Cooking

- **Purpose**: Records the cooking process for dishes.
- **Fields**:
  - `ID` (INT, PRIMARY KEY) — unique identifier for each cooking record.
  - `Dish_ID` (INT, NOT NULL) — identifier for the dish being cooked (foreign key).
  - `Amount` (INT, CHECK (Amount > 0)) — number of portions prepared.
  - `Date` (DATETIME, NOT NULL) — date and time of cooking.
- **Constraints**:
  - `FK_Cooking_Dish` — foreign key referencing `Dish(ID)`.
