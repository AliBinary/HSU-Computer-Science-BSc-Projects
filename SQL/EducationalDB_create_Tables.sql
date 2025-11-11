-- ایجاد جدول Users
CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50) NOT NULL UNIQUE,
    Email NVARCHAR(100) NOT NULL UNIQUE,
    PasswordHash NVARCHAR(128) NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    IsDeleted BIT DEFAULT 0
);

-- ایجاد جدول Courses
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY IDENTITY(1,1),
    Title NVARCHAR(100) NOT NULL,
    Description NVARCHAR(MAX),
    Price DECIMAL(10,2) NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    IsDeleted BIT DEFAULT 0
);

-- ایجاد جدول Purchases
CREATE TABLE Purchases (
    PurchaseID INT PRIMARY KEY IDENTITY(1,1),
    UserID INT NOT NULL,
    CourseID INT NOT NULL,
    PurchaseDate DATETIME DEFAULT GETDATE(),
    AmountPaid DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
