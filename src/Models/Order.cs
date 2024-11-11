using Microsoft.AspNetCore.Http.Features;

public class Order
{

    public required int Id { get; set; }
    public required int SourceId { get; set; }
    public required DateTime OrderDate { get; set; }
    public required DateTime RequestDate { get; set; }
    public required string Reference { get; set; }
    public required string ReferenceExtra { get; set; }
    public required string OrderStatus { get; set; }
    public required string Notes { get; set; }
    public required string ShippingNotes { get; set; }
    public required string PickingNotes { get; set; }
    public required int WarehouseId { get; set; }
    public required string ShipTo { get; set; }
    public required string BillTo { get; set; }
    public required string ShipmentId { get; set; }
    public required float TotalAmount { get; set; }
    public required float TotalDiscount { get; set; }
    public required float TotalTax { get; set; }
    public required float TotalSurcharge { get; set; }
    public required DateTime CreatedAt { get; set; }
    public required DateTime UpdatedAt { get; set; }
    public required List<Item> Items { get; set; }

}