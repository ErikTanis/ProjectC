public class ItemGroup
{

    public int Id { get; set; }
    public required string Name { get; set; }
    public required string Description { get; set; }
    public required DateTime CreatedAt { get; set; } = DateTime.Now;
    public required DateTime UpdatedAt { get; set; } = DateTime.Now;

}