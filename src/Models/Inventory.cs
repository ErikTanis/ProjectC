public class Inventory
{
    public required int Id { get; set; }
    public required string ItemId { get; set; }
    public required string Description { get; set; }
    public required string ItemReference { get; set; }
    public required List<int> Locations { get; set; }
    public required int TotalOnHand { get; set; }
    public required int TotalExpected { get; set; }
    public required int TotalOrdered { get; set; }
    public required int TotalAllocated { get; set; }
    public required int TotalAvailable { get; set; }
    public required DateTime CreatedAt { get; set; } = DateTime.Now;
    public required DateTime UpdatedAt { get; set; } = DateTime.Now;

}