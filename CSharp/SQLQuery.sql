USE [ShoppingDB]
GO
/** Object:  StoredProcedure [dbo].[UsP_InsertCustomer]    Script Date: 11/5/2024 7:09:50 PM **/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:  Alireza Shafiee Fard
-- Create date: 1403/07/18
-- Description: Insert customer
-- =============================================
CREATE PROCEDURE [dbo].[UsP_InsertCustomer]
 @FullName as nvarchar(150),
 @UserName as nvarchar(50),
 @PasswardHash as nvarchar(250),
 @PasswordSalt as nvarchar(250),
 @BirthDate as date=NULL,
 @PhoneNO as nvarchar(11)='',
 @Address as nvarchar(MAX)='',
 @NationalCode as nvarchar(10)='',
 @Email as nvarchar(100)='',
 @Stuse as bit=0,
 @Id as int out,
 @rCode as int out,
 @rMsg as nvarchar(max) out
AS
BEGIN
 -- SET NOCOUNT ON added to prevent extra result sets from
 -- interfering with SELECT statements.
 SET NOCOUNT ON;
if exists(SELECT 1 FROM [dbo].TB_Customer WHERE [UserName]=@UserName) 
BEGIN
SET @rCode=0
SET @rMsg=N'نام کاربری تکراری می باشد'
RETURN
END
if exists(SELECT 1 FROM [dbo].TB_Customer WHERE [PhoneNO]=@PhoneNO) 
BEGIN
SET @rCode=0
SET @rMsg=N'شماره تلفن تکراری می باشد'
RETURN
END
if exists(SELECT 1 FROM [dbo].TB_Customer WHERE [Email]=@Email) 
BEGIN
SET @rCode=0
SET @rMsg=N'پست الکترنیک تکراری می باشد'
RETURN
END
BEGIN TRY
INSERT INTO [dbo].TB_Customer
(
[Username],
[PasswordSalt],
[PasswardHash],
[FullName],
[BirthDate],
[PhoneNO],
[NationalCode],
[Address],
[Email],
[Stuse]
)
VALUES 
(
@UserName,
@PasswordSalt,
@PasswardHash,
@FullName,
@BirthDate,
@PhoneNO,
@NationalCode,
@Address,
@Email,
@Stuse
)
SET @Id=SCOPE_IDENTITY()
SET @rCode = 1
  SET @rMsg = N'عملیات با موفقیت ثبت شد'
 END TRY
 BEGIN CATCH
 END CATCH
END