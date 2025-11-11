using EducationalAPI.Data.Contracts;
using EducationalAPI.Entities;
using EducationalAPI.Services.Contracts;

namespace EducationalAPI.Services.Implementations
{
    public class UserService : IUserService
    {
        private readonly IUserRepository _userRepository;

        public UserService(IUserRepository userRepository)
        {
            _userRepository = userRepository;
        }

        public async Task<IEnumerable<User>> GetAllUsersAsync()
        {
            return await _userRepository.GetAllUsersAsync();
        }

        public async Task<User?> GetUserByIdAsync(int userId)
        {
            return await _userRepository.GetUserByIdAsync(userId);
        }

        public async Task<User> CreateUserAsync(User user)
        {
            return await _userRepository.CreateUserAsync(user);
        }


        public async Task<bool> UpdateUserAsync(int userId, User updatedUser)
        {
            return await _userRepository.UpdateUserAsync(userId, updatedUser);
        }

        public async Task<bool> DeleteUserAsync(int userId)
        {
            return await _userRepository.DeleteUserAsync(userId);
        }

        public Task<bool> UpdateUserAsync(User user)
        {
            throw new NotImplementedException();
        }
    }
}
