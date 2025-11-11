namespace hakimApp.Entities.Dto.User
{
    public class CustomerDto
    {
        public string EmployeeCode { get; set; }
        public string FullName { get; set; }
        public string ContactNumber { get; set; }
        public string NationalID { get; set; }
        public string WorkEmail { get; set; }
        public string Password { get; set; }
        public string ResidentialAddress { get; set; }
        public bool IsEmployed { get; set; }
    }
}
