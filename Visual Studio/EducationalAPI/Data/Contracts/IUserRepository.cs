using EducationalAPI.Entities;

namespace EducationalAPI.Data.Contracts
{
    public interface IUserRepository
    {
        Task<IEnumerable<User>> GetAllUsersAsync();
        Task<User?> GetUserByIdAsync(int userId);
        Task<User> CreateUserAsync(User user);
        Task<bool> UpdateUserAsync(int userId, User updatedUser);
        Task<bool> DeleteUserAsync(int userId);
    }
}
