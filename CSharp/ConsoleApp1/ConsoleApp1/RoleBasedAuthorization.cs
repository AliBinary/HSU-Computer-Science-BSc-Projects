public class UserWithRoles
{
    public string Username { get; set; }
    public List<string> AssignedRoles { get; set; }

    public UserWithRoles(string username, List<string> assignedRoles)
    {
        Username = username;
        AssignedRoles = assignedRoles;
    }
}

public class RoleAuthorizationService
{
    public static bool AuthorizeUser(UserWithRoles user, string requiredRole)
    {
        if (user.AssignedRoles.Contains(requiredRole))
        {
            return true;
        }
        else
        {
            throw new UnauthorizedAccessException($"{user.Username} does not have permission for the role: {requiredRole}.");
        }
    }
}
