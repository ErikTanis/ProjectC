public class Client
{

    public required int Id { get; set; }
    public required string Name { get; set; }
    public required string Address { get; set; }
    public required string City { get; set; }
    public required string ZipCode { get; set; }
    public required string Province { get; set; }
    public required string Country { get; set; }
    public required string ContactName { get; set; }
    public required string ContactPhone { get; set; }
    public required string ContactEmail { get; set; }
    public required DateTime CreatedAt { get; set; } = DateTime.Now;
    public required DateTime UpdatedAt { get; set; } = DateTime.Now;

}