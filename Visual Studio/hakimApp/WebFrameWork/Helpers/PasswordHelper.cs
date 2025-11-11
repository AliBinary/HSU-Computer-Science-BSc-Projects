using Microsoft.AspNetCore.Cryptography.KeyDerivation;
using System.Security.Cryptography;

namespace hakimApp.WebFrameWork.Helpers
{
    public class PasswordHelper
    {
        public static byte[] GetSecureSalt()
        {
            byte[] byteRange = new byte[32];
            RandomNumberGenerator.Create().GetBytes(byteRange);
            return byteRange;
        }
        public static string HashUsingPBKDF2(string password, byte[] salt)
        {
            byte[] derieveKey = KeyDerivation.Pbkdf2(password, salt, KeyDerivationPrf.HMACSHA256, 100000, 32);
            return Convert.ToBase64String(derieveKey);
        }
    }
}
