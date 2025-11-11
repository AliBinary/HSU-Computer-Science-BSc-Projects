using EducationalAPI.Entities;

namespace EducationalAPI.Data.Contracts
{
    public interface ICourseRepository
    {
        Task<IEnumerable<Course>> GetAllCoursesAsync();
        Task<Course?> GetCourseByIdAsync(int courseId);
        Task<Course> CreateCourseAsync(Course course); // نوع بازگشتی Task<Course>
        Task<bool> UpdateCourseAsync(int courseId, Course updatedCourse);
        Task<bool> DeleteCourseAsync(int courseId);
    }
}
