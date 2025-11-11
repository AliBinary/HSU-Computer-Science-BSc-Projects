namespace hakimApp.Entities.Dto.User
{
    public class SelectUserDto
    {
        public int Id { get; set; }
        public string FullName { get; set; }
        public string ContactNumber { get; set; }
        public string NationalID { get; set; }

        public DateTime DateOfBirth { get; set; }

        public string WorkEmail { get; set; }
        public string EmployeeCode { get; set; }
        public string SecurityCode { get; set; }
        public string LoginHash { get; set; }
        public string ResidentialAddress { get; set; }
        public bool IsEmployed { get; set; }
    }
}
