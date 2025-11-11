using System.Security.Cryptography;
using System.Text;

namespace EducationalAPI.Utilities
{
    public static class PasswordHasher
    {
        public static string HashPassword(string password, string salt)
        {
            using var sha256 = SHA256.Create();
            var combined = Encoding.UTF8.GetBytes(password + salt);
            return Convert.ToBase64String(sha256.ComputeHash(combined));
        }

        public static string GenerateSalt()
        {
            var saltBytes = new byte[16];
            using var rng = RandomNumberGenerator.Create();
            rng.GetBytes(saltBytes);
            return Convert.ToBase64String(saltBytes);
        }

        public static bool VerifyPassword(string password, string salt, string hash)
        {
            var computedHash = HashPassword(password, salt);
            return computedHash == hash;
        }
    }
}
