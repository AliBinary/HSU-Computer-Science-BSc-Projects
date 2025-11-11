using System;
using System.Collections.Generic;

public class Program
{
    public static void Main()
    {
        Console.WriteLine();

        // کاربر مدیر سامانه
        var systemAdmin = new UserWithRoles("SystemAdmin", new List<string> { "Admin", "User" });

        // کاربر عمومی سامانه
        var generalUser = new UserWithRoles("GeneralUser", new List<string> { "User" });

        // تست 1: تست دسترسی مدیر سامانه
        PrintTestHeader("Test 1: Role-based Authorization for System Admin");
        try
        {
            bool isAuthorized = RoleAuthorizationService.AuthorizeUser(systemAdmin, "Admin");
            PrintAuthorizationResult(systemAdmin.Username, "Admin", isAuthorized);
        }
        catch (UnauthorizedAccessException)
        {
            PrintAuthorizationResult(systemAdmin.Username, "Admin", false);
        }

        Console.WriteLine();

        // تست 2: تست دسترسی کاربر عمومی
        PrintTestHeader("Test 2: Role-based Authorization for General User");
        try
        {
            bool isAuthorized = RoleAuthorizationService.AuthorizeUser(generalUser, "Admin");
            PrintAuthorizationResult(generalUser.Username, "Admin", isAuthorized);
        }
        catch (UnauthorizedAccessException)
        {
            PrintAuthorizationResult(generalUser.Username, "Admin", false);
        }

        Console.WriteLine();
        Console.WriteLine(new string('=', 50));


        // کاربر مدیر محتوا
        var contentManager = new UserWithClaims("ContentManager", new List<UserClaim>
        {
            new UserClaim("PermissionLevel", "Manage"),
            new UserClaim("Department", "Content")
        });

        // کاربر مشاهده‌کننده محتوا
        var contentViewer = new UserWithClaims("ContentViewer", new List<UserClaim>
        {
            new UserClaim("PermissionLevel", "View"),
            new UserClaim("Department", "Content")
        });

        // تست 3: تست دسترسی مدیر محتوا
        PrintTestHeader("Test 3: Claim-based Authorization for Content Manager");
        try
        {
            bool isAuthorized = ClaimAuthorizationService.AuthorizeUser(contentManager, "PermissionLevel", "Manage");
            PrintAuthorizationResult(contentManager.Username, "PermissionLevel: Manage", isAuthorized);
        }
        catch (UnauthorizedAccessException)
        {
            PrintAuthorizationResult(contentManager.Username, "PermissionLevel: Manage", false);
        }

        Console.WriteLine();

        // تست 4: تست دسترسی کاربر مشاهده‌کننده محتوا
        PrintTestHeader("Test 4: Claim-based Authorization for Content Viewer");
        try
        {
            bool isAuthorized = ClaimAuthorizationService.AuthorizeUser(contentViewer, "PermissionLevel", "Manage");
            PrintAuthorizationResult(contentViewer.Username, "PermissionLevel: Manage", isAuthorized);
        }
        catch (UnauthorizedAccessException)
        {
            PrintAuthorizationResult(contentViewer.Username, "PermissionLevel: Manage", false);
        }

        Console.WriteLine();
        Console.WriteLine(new string('=', 50));

    }

    private static void PrintTestHeader(string header)
    {
        Console.ForegroundColor = ConsoleColor.Cyan; // تغییر رنک متن
        Console.WriteLine(header);
        Console.ResetColor(); // بازکرداندن رنک به حالت پیش‌فرض
        Console.WriteLine(new string('-', header.Length)); // خط افقی با طول عنوان
    }

    private static void PrintAuthorizationResult(string username, string roleOrClaim, bool isAuthorized)
    {
        Console.Write($"{username}: ");
        Console.ForegroundColor = isAuthorized ? ConsoleColor.Green : ConsoleColor.Red; // انتخاب رنک بر اساس نتیجه
        Console.WriteLine($"Authorization for '{roleOrClaim}' - {(isAuthorized ? "Access Granted" : "Access Denied")}");
        Console.ResetColor(); // بازکرداندن رنک به حالت پیش‌فرض
    }
}
