// نمایانکر یک ادعای کاربر
public class UserClaim
{
    public string ClaimType { get; set; } // نوع ادعا (مثلاً سطح دسترسی)
    public string ClaimValue { get; set; } // مقدار ادعا (مثلاً "Admin")

    public UserClaim(string claimType, string claimValue)
    {
        ClaimType = claimType;
        ClaimValue = claimValue;
    }
}

// نمایانکر یک کاربر که دارای ادعاهای خاص است
public class UserWithClaims
{
    public string Username { get; set; } // نام کاربر
    public List<UserClaim> Claims { get; set; } // لیست ادعاهای کاربر

    public UserWithClaims(string username, List<UserClaim> claims)
    {
        Username = username;
        Claims = claims;
    }
}

// سرویس مجوزدهی بر اساس ادعاها
public class ClaimAuthorizationService
{
    // بررسی می‌کند که آیا کاربر دارای ادعای مورد نظر است یا خیر
    public static bool AuthorizeUser(UserWithClaims user, string requiredClaimType, string requiredClaimValue)
    {
        foreach (var claim in user.Claims)
        {
            if (claim.ClaimType == requiredClaimType && claim.ClaimValue == requiredClaimValue)
            {
                return true; // دسترسی مجاز است
            }
        }
        throw new UnauthorizedAccessException($"{user.Username} does not have the required claim of type '{requiredClaimType}' with value '{requiredClaimValue}'.");
    }
}
