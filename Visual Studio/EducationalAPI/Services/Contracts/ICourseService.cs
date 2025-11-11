using EducationalAPI.Entities;

namespace EducationalAPI.Services.Contracts
{
    public interface ICourseService
    {
        Task<IEnumerable<Course>> GetAllCoursesAsync();
        Task<Course?> GetCourseByIdAsync(int courseId);
        Task<Course> CreateCourseAsync(Course course);
        Task<bool> UpdateCourseAsync(int courseId, Course updatedCourse);
        Task<bool> DeleteCourseAsync(int courseId);
        Task<bool> UpdateCourseAsync(Course course);
    }
}
