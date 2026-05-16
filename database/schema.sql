CREATE DATABASE FarmManagementSystem;
GO

USE FarmManagementSystem;
GO


CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY IDENTITY(1,1),
    SupplierName NVARCHAR(100),
    ContactNumber NVARCHAR(20),
    Address NVARCHAR(255)
);


CREATE TABLE FeedTypes (
    FeedID INT PRIMARY KEY IDENTITY(1,1),
    FeedName NVARCHAR(100),
    Unit NVARCHAR(20)
);


CREATE TABLE FinanceCategories (
    CategoryID INT PRIMARY KEY IDENTITY(1,1),
    CategoryName NVARCHAR(100)
);



CREATE TABLE Staging_DailyOperations (
    OpDate DATE,
    SupplierName NVARCHAR(100),
    FeedName NVARCHAR(100),
    CategoryName NVARCHAR(100),
    Quantity DECIMAL(10,2),
    UnitPrice DECIMAL(18,2),
    Notes NVARCHAR(MAX)
);







CREATE TABLE DailyOperations (
    OperationID INT PRIMARY KEY IDENTITY(1,1),

    OpDate DATE,

    SupplierID INT,
    FeedID INT,
    CategoryID INT,

    Quantity DECIMAL(10,2),

    UnitPrice DECIMAL(18,2),

    TotalAmount AS (Quantity * UnitPrice) PERSISTED,

    Notes NVARCHAR(MAX),

    FOREIGN KEY (SupplierID)
    REFERENCES Suppliers(SupplierID),

    FOREIGN KEY (FeedID)
    REFERENCES FeedTypes(FeedID),

    FOREIGN KEY (CategoryID)
    REFERENCES FinanceCategories(CategoryID)
);



INSERT INTO Suppliers (SupplierName)

SELECT DISTINCT SupplierName
FROM Staging_DailyOperations;





INSERT INTO FeedTypes (FeedName)

SELECT DISTINCT FeedName
FROM Staging_DailyOperations;




INSERT INTO FinanceCategories (CategoryName)

SELECT DISTINCT CategoryName
FROM Staging_DailyOperations;





INSERT INTO DailyOperations
(
    OpDate,
    SupplierID,
    FeedID,
    CategoryID,
    Quantity,
    UnitPrice,
    Notes
)

SELECT

    s.OpDate,

    sup.SupplierID,

    f.FeedID,

    c.CategoryID,

    s.Quantity,

    s.UnitPrice,

    s.Notes

FROM Staging_DailyOperations s

LEFT JOIN Suppliers sup
ON s.SupplierName = sup.SupplierName

LEFT JOIN FeedTypes f
ON s.FeedName = f.FeedName

LEFT JOIN FinanceCategories c
ON s.CategoryName = c.CategoryName;



SELECT * FROM DailyOperations;

USE FarmManagementSystem;
GO

SELECT * FROM dbo.Staging_FarmData;

-- Database schema will be added here
