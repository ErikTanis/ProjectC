public class Shipment
{
    public required int Id { get; set; }
    public required int OrderId { get; set; }
    public required int SourceId { get; set; }
    public required DateTime OrderDate { get; set; }
    public required DateTime RequestDate { get; set; }
    public required DateTime ShipmentDate { get; set; }
    public required string ShipmentType { get; set; }
    public required string ShipmentStatus { get; set; }
    public required string Notes { get; set; }
    public required string CarrierCode { get; set; }
    public required string CarrierDescription { get; set; }
    public required string ServiceCode { get; set; }
    public required string PaymentType { get; set; }
    public required string TransferMode { get; set; }
    public required int TotalPackageCount { get; set; }
    public required double TotalPackageWeight { get; set; }
    public required List<ItemInfo> Items { get; set; }
    public required DateTime CreatedAt { get; set; } = DateTime.Now;
    public required DateTime UpdatedAt { get; set; } = DateTime.Now;
}