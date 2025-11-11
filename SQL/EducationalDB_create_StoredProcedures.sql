-- استورپروسیجر برای ایجاد کاربر جدید
CREATE PROCEDURE sp_CreateUser
    @Username NVARCHAR(50),
    @Email NVARCHAR(100),
    @PasswordHash NVARCHAR(128)
AS
BEGIN
    INSERT INTO Users (Username, Email, PasswordHash, CreatedAt, IsDeleted)
    VALUES (@Username, @Email, @PasswordHash, GETDATE(), 0);
END;
GO

-- استورپروسیجر برای به‌روزرسانی اطلاعات کاربر
CREATE PROCEDURE sp_UpdateUser
    @UserID INT,
    @Username NVARCHAR(50),
    @Email NVARCHAR(100),
    @PasswordHash NVARCHAR(128)
AS
BEGIN
    UPDATE Users
    SET Username = @Username,
        Email = @Email,
        PasswordHash = @PasswordHash
    WHERE UserID = @UserID AND IsDeleted = 0;
END;
GO

-- استورپروسیجر برای حذف نرم کاربر
CREATE PROCEDURE sp_DeleteUser
    @UserID INT
AS
BEGIN
    UPDATE Users
    SET IsDeleted = 1
    WHERE UserID = @UserID;
END;
GO

-- استورپروسیجر برای ایجاد دوره جدید
CREATE PROCEDURE sp_CreateCourse
    @Title NVARCHAR(100),
    @Description NVARCHAR(MAX),
    @Price DECIMAL(10, 2)
AS
BEGIN
    INSERT INTO Courses (Title, Description, Price, CreatedAt, IsDeleted)
    VALUES (@Title, @Description, @Price, GETDATE(), 0);
END;
GO

-- استورپروسیجر برای به‌روزرسانی اطلاعات دوره
CREATE PROCEDURE sp_UpdateCourse
    @CourseID INT,
    @Title NVARCHAR(100),
    @Description NVARCHAR(MAX),
    @Price DECIMAL(10, 2)
AS
BEGIN
    UPDATE Courses
    SET Title = @Title,
        Description = @Description,
        Price = @Price
    WHERE CourseID = @CourseID AND IsDeleted = 0;
END;
GO

-- استورپروسیجر برای حذف نرم دوره
CREATE PROCEDURE sp_DeleteCourse
    @CourseID INT
AS
BEGIN
    UPDATE Courses
    SET IsDeleted = 1
    WHERE CourseID = @CourseID;
END;
GO

-- استورپروسیجر برای ثبت خرید جدید
CREATE PROCEDURE sp_CreatePurchase
    @UserID INT,
    @CourseID INT,
    @AmountPaid DECIMAL(10, 2)
AS
BEGIN
    INSERT INTO Purchases (UserID, CourseID, PurchaseDate, AmountPaid)
    VALUES (@UserID, @CourseID, GETDATE(), @AmountPaid);
END;
GO

-- استورپروسیجر برای دریافت خریدهای یک کاربر
CREATE PROCEDURE sp_GetUserPurchases
    @UserID INT
AS
BEGIN
    SELECT P.PurchaseID, P.CourseID, C.Title, P.PurchaseDate, P.AmountPaid
    FROM Purchases P
    INNER JOIN Courses C ON P.CourseID = C.CourseID
    WHERE P.UserID = @UserID;
END;
GO
