USE ShoppingDB;

ALTER TABLE [dbo].[TB_EmployeesOrders] NOCHECK CONSTRAINT ALL;
ALTER TABLE [dbo].[TB_RefreshToken] NOCHECK CONSTRAINT ALL;
ALTER TABLE [dbo].[TB_Goods] NOCHECK CONSTRAINT ALL;

DELETE FROM [dbo].[TB_EmployeesOrders];
DELETE FROM [dbo].[TB_RefreshToken];
DELETE FROM [dbo].[TB_Goods]; 
DELETE FROM [dbo].[TB_Employee];

DBCC CHECKIDENT ('[dbo].[TB_Employee]', RESEED, 0);
DBCC CHECKIDENT ('[dbo].[TB_EmployeesOrders]', RESEED, 0);
DBCC CHECKIDENT ('[dbo].[TB_Goods]', RESEED, 1);
DBCC CHECKIDENT ('[dbo].[TB_RefreshToken]', RESEED, 0);


ALTER TABLE [dbo].[TB_EmployeesOrders] CHECK CONSTRAINT ALL;
ALTER TABLE [dbo].[TB_RefreshToken] CHECK CONSTRAINT ALL;
ALTER TABLE [dbo].[TB_Goods] CHECK CONSTRAINT ALL;

DBCC CHECKIDENT ('[dbo].[TB_Goods]', RESEED, 0);
DBCC CHECKIDENT ('[dbo].[TB_RefreshToken]', RESEED, 0);

ALTER TABLE [dbo].[TB_EmployeesOrders] CHECK CONSTRAINT ALL;
ALTER TABLE [dbo].[TB_RefreshToken] CHECK CONSTRAINT ALL;
