using EducationalAPI.Entities;

namespace EducationalAPI.Services.Contracts
{
    public interface IUserService
    {
        Task<IEnumerable<User>> GetAllUsersAsync();
        Task<User?> GetUserByIdAsync(int userId);
        Task<User> CreateUserAsync(User user);
        Task<bool> UpdateUserAsync(int userId, User updatedUser);
        Task<bool> DeleteUserAsync(int userId);
        Task<bool> UpdateUserAsync(User user);
    }
}
