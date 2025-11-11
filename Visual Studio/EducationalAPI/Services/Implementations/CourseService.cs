using EducationalAPI.Data.Contracts;
using EducationalAPI.Entities;
using EducationalAPI.Services.Contracts;

namespace EducationalAPI.Services.Implementations
{
    public class CourseService : ICourseService
    {
        private readonly ICourseRepository _courseRepository;

        public CourseService(ICourseRepository courseRepository)
        {
            _courseRepository = courseRepository;
        }

        public async Task<IEnumerable<Course>> GetAllCoursesAsync()
        {
            return await _courseRepository.GetAllCoursesAsync();
        }

        public async Task<Course?> GetCourseByIdAsync(int courseId)
        {
            return await _courseRepository.GetCourseByIdAsync(courseId);
        }

        public async Task<Course> CreateCourseAsync(Course course)
        {
            return await _courseRepository.CreateCourseAsync(course);
        }


        public async Task<bool> UpdateCourseAsync(int courseId, Course updatedCourse)
        {
            return await _courseRepository.UpdateCourseAsync(courseId, updatedCourse);
        }

        public async Task<bool> DeleteCourseAsync(int courseId)
        {
            return await _courseRepository.DeleteCourseAsync(courseId);
        }

        public Task<bool> UpdateCourseAsync(Course course)
        {
            throw new NotImplementedException();
        }
    }
}
